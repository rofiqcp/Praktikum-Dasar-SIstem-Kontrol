import csv
import sys
from pathlib import Path

import pandas as pd
import pyqtgraph as pg
import serial
import serial.tools.list_ports
from PyQt5 import QtCore, QtWidgets

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "common"))
try:
    from response_metrics import response_metrics
except Exception:
    response_metrics = None

FIELDS = [
    "time_ms", "setpoint", "position", "raw_speed", "ma_speed", "lpf_speed",
    "feedback", "error", "p", "i", "d", "output", "mode"
]


class MotorPIDGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ser = None
        self.rows = []
        self.setWindowTitle("PID Motor DC — Arduino Mega 2560")
        self.resize(1380, 820)
        self._build_ui()
        self.refresh_ports()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.poll_serial)
        self.timer.start(20)

    def _spin(self, lo, hi, value, step, decimals=3):
        w = QtWidgets.QDoubleSpinBox()
        w.setRange(lo, hi); w.setValue(value); w.setSingleStep(step); w.setDecimals(decimals)
        return w

    def _build_ui(self):
        grid = QtWidgets.QGridLayout(self)
        self.port = QtWidgets.QComboBox()
        self.refresh_btn = QtWidgets.QPushButton("Refresh")
        self.connect_btn = QtWidgets.QPushButton("Connect")
        self.mode = QtWidgets.QComboBox(); self.mode.addItems(["Speed", "Position"])
        self.sp = self._spin(-1000, 1000, 0, 10, 2)
        self.kp = self._spin(0, 3, 1, 0.05)
        self.ki = self._spin(0, 3, 0, 0.05)
        self.kd = self._spin(0, 3, 0, 0.01)
        self.alpha = self._spin(0, 1, 0.3, 0.05)
        self.ts = QtWidgets.QSpinBox(); self.ts.setRange(10, 300); self.ts.setValue(50)
        self.start_btn = QtWidgets.QPushButton("START")
        self.stop_btn = QtWidgets.QPushButton("STOP")
        self.zero_btn = QtWidgets.QPushButton("ZERO POSITION")
        self.clear_btn = QtWidgets.QPushButton("Clear Data")
        self.csv_btn = QtWidgets.QPushButton("Save CSV")
        self.xlsx_btn = QtWidgets.QPushButton("Save Excel")
        self.png_btn = QtWidgets.QPushButton("Save PNG")
        self.metrics = QtWidgets.QPlainTextEdit(); self.metrics.setReadOnly(True); self.metrics.setMaximumHeight(180)

        controls = [
            ("Port", self.port), ("", self.refresh_btn), ("", self.connect_btn),
            ("Mode", self.mode), ("Setpoint", self.sp), ("Kp", self.kp), ("Ki", self.ki),
            ("Kd", self.kd), ("LPF alpha", self.alpha), ("Sampling ms", self.ts),
            ("", self.start_btn), ("", self.stop_btn), ("", self.zero_btn),
            ("", self.clear_btn), ("", self.csv_btn), ("", self.xlsx_btn), ("", self.png_btn),
        ]
        for r, (label, widget) in enumerate(controls):
            if label: grid.addWidget(QtWidgets.QLabel(label), r, 0)
            grid.addWidget(widget, r, 1)

        self.plot_response = pg.PlotWidget(title="Setpoint & Feedback")
        self.plot_response.addLegend(); self.plot_response.showGrid(x=True, y=True)
        self.curve_sp = self.plot_response.plot(name="SP")
        self.curve_fb = self.plot_response.plot(name="Feedback")
        self.plot_pid = pg.PlotWidget(title="P, I, D & Output")
        self.plot_pid.addLegend(); self.plot_pid.showGrid(x=True, y=True)
        self.curve_p = self.plot_pid.plot(name="P")
        self.curve_i = self.plot_pid.plot(name="I")
        self.curve_d = self.plot_pid.plot(name="D")
        self.curve_u = self.plot_pid.plot(name="Output")
        grid.addWidget(self.plot_response, 0, 2, 9, 1)
        grid.addWidget(self.plot_pid, 9, 2, 9, 1)
        grid.addWidget(QtWidgets.QLabel("Response metrics"), 17, 0)
        grid.addWidget(self.metrics, 18, 0, 1, 3)

        self.refresh_btn.clicked.connect(self.refresh_ports)
        self.connect_btn.clicked.connect(self.toggle_connection)
        self.mode.currentIndexChanged.connect(lambda i: self.send(f"MODE={i}"))
        self.sp.valueChanged.connect(lambda v: self.send(f"SP={v}"))
        self.kp.valueChanged.connect(lambda v: self.send(f"KP={v}"))
        self.ki.valueChanged.connect(lambda v: self.send(f"KI={v}"))
        self.kd.valueChanged.connect(lambda v: self.send(f"KD={v}"))
        self.alpha.valueChanged.connect(lambda v: self.send(f"ALPHA={v}"))
        self.ts.valueChanged.connect(lambda v: self.send(f"TS={v}"))
        self.start_btn.clicked.connect(lambda: self.send("START"))
        self.stop_btn.clicked.connect(lambda: self.send("STOP"))
        self.zero_btn.clicked.connect(lambda: self.send("ZERO"))
        self.clear_btn.clicked.connect(self.clear_data)
        self.csv_btn.clicked.connect(self.save_csv)
        self.xlsx_btn.clicked.connect(self.save_excel)
        self.png_btn.clicked.connect(self.save_png)

    def refresh_ports(self):
        current = self.port.currentText()
        self.port.clear(); self.port.addItems([p.device for p in serial.tools.list_ports.comports()])
        if current:
            idx = self.port.findText(current)
            if idx >= 0: self.port.setCurrentIndex(idx)

    def toggle_connection(self):
        if self.ser:
            self.ser.close(); self.ser = None; self.connect_btn.setText("Connect"); return
        if not self.port.currentText():
            QtWidgets.QMessageBox.warning(self, "Serial", "Port belum dipilih."); return
        self.ser = serial.Serial(self.port.currentText(), 115200, timeout=0)
        self.connect_btn.setText("Disconnect")
        # Synchronize all GUI parameters after connecting.
        self.send(f"MODE={self.mode.currentIndex()}")
        for key, widget in [("SP",self.sp),("KP",self.kp),("KI",self.ki),("KD",self.kd),("ALPHA",self.alpha),("TS",self.ts)]:
            self.send(f"{key}={widget.value()}")

    def send(self, text):
        if self.ser and self.ser.is_open:
            self.ser.write((text + "\n").encode())

    def poll_serial(self):
        if not self.ser: return
        try:
            while self.ser.in_waiting:
                line = self.ser.readline().decode(errors="ignore").strip()
                if not line or line.startswith("#"): continue
                parts = line.split(",")
                if len(parts) != len(FIELDS): continue
                row = dict(zip(FIELDS, map(float, parts)))
                self.rows.append(row)
            if self.rows: self.update_plots()
        except (serial.SerialException, ValueError) as exc:
            self.metrics.setPlainText(f"Serial error: {exc}")

    def update_plots(self):
        data = self.rows[-1500:]
        t = [r["time_ms"] / 1000.0 for r in data]
        self.curve_sp.setData(t, [r["setpoint"] for r in data])
        self.curve_fb.setData(t, [r["feedback"] for r in data])
        self.curve_p.setData(t, [r["p"] for r in data])
        self.curve_i.setData(t, [r["i"] for r in data])
        self.curve_d.setData(t, [r["d"] for r in data])
        self.curve_u.setData(t, [r["output"] for r in data])
        if response_metrics and len(data) > 10:
            sp = data[-1]["setpoint"]
            m = response_metrics(t, [r["feedback"] for r in data], sp)
            self.metrics.setPlainText("\n".join(f"{k}: {v:.4g}" for k, v in m.items()))

    def clear_data(self):
        self.rows.clear(); self.metrics.clear()
        for c in [self.curve_sp,self.curve_fb,self.curve_p,self.curve_i,self.curve_d,self.curve_u]: c.setData([],[])

    def _choose(self, caption, ext):
        return QtWidgets.QFileDialog.getSaveFileName(self, caption, f"motor_pid.{ext}", f"*.{ext}")[0]

    def save_csv(self):
        if not self.rows: return
        path = self._choose("Save CSV", "csv")
        if path:
            with open(path, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(self.rows)

    def save_excel(self):
        if not self.rows: return
        path = self._choose("Save Excel", "xlsx")
        if path: pd.DataFrame(self.rows).to_excel(path, index=False)

    def save_png(self):
        path = self._choose("Save graph", "png")
        if path: self.plot_response.grab().save(path)

    def closeEvent(self, event):
        if self.ser: self.ser.close()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = MotorPIDGUI(); gui.show()
    sys.exit(app.exec_())
