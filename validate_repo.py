from __future__ import annotations

from pathlib import Path
import py_compile
import re
import sys

ROOT = Path(__file__).resolve().parent

MODULES = [
    "Pertemuan-01-Dasar-Sistem-Kontrol-dan-PID",
    "Pertemuan-02-Dasar-MATLAB",
    "Pertemuan-03-Transfer-Function-Plant",
    "Pertemuan-04-PID-MATLAB-dan-Blok-Manual",
    "Pertemuan-05-Autonics-Pemanas-Air-Manual",
    "Pertemuan-06-Autonics-DAQMaster-MATLAB",
    "Pertemuan-07-MATLAB-Arduino-LED-ADC",
    "Pertemuan-08-Responsi-P01-P07-dan-Checkpoint-PCB",
    "Pertemuan-09-MATLAB-Arduino-Kontrol-Suhu-PID",
    "Pertemuan-10-MATLAB-Arduino-Baca-RPM-dan-Posisi",
    "Pertemuan-11-MATLAB-Arduino-PID-Kecepatan",
    "Pertemuan-12-MATLAB-Arduino-PID-Posisi",
    "Pertemuan-13-PlatformIO-ADC-RPM-Posisi-dengan-AI",
    "Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI",
    "Pertemuan-15-PlatformIO-Kontrol-Motor-GUI-AI",
    "Pertemuan-16-Responsi-P09-P15",
]

PROJECT = {8, 12, 16}
errors: list[str] = []

# These thresholds are intentionally modest. Their purpose is to catch an
# accidentally truncated/placeholder teaching document, not to enforce style.
MIN_MATERI = 1200
MIN_JOBSHEET = 600
MIN_ASSESSMENT = 250

for i, name in enumerate(MODULES, 1):
    p = ROOT / name
    if not p.is_dir():
        errors.append(f"P{i:02}: missing directory {name}")
        continue

    docs = {
        "Materi.md": MIN_MATERI,
        "Jobsheet.md": MIN_JOBSHEET,
    }
    expected = "Project.md" if i in PROJECT else "TugasVideo.md"
    docs[expected] = MIN_ASSESSMENT

    for required, min_chars in docs.items():
        f = p / required
        if not f.is_file():
            errors.append(f"P{i:02}: missing {required}")
            continue
        text = f.read_text(encoding="utf-8", errors="ignore").strip()
        if len(text) < min_chars:
            errors.append(
                f"P{i:02}: {required} looks truncated ({len(text)} chars < {min_chars})"
            )

    if i in PROJECT and (p / "TugasVideo.md").exists():
        errors.append(f"P{i:02}: TugasVideo.md must be replaced by Project.md")

required_paths = [
    "README.md",
    "INSTALLATION.md",
    "HARDWARE_PCB_SPEC.md",
    "WIRING.md",
    "SAFETY.md",
    "TESTING.md",
    "RUN_CHECKLIST.md",
    "SIMULINK_MODELS.md",
    "build_all_slx.m",
    "shared/python/response_metrics.py",
    "shared/python/test_response_metrics.py",
    "shared/arduino/PIDCore.h",
    "shared/matlab/response_metrics.m",
    "shared/protocol/SERIAL_PROTOCOL.md",
    "Pertemuan-03-Transfer-Function-Plant/examples/build_three_plants_simulink.m",
    "Pertemuan-04-PID-MATLAB-dan-Blok-Manual/examples/build_pid_manual_simulink.m",
    "Pertemuan-09-MATLAB-Arduino-Kontrol-Suhu-PID/examples/matlab_temp_pid_host.m",
    "Pertemuan-09-MATLAB-Arduino-Kontrol-Suhu-PID/examples/analyze_temp_pid_log.m",
    "Pertemuan-09-MATLAB-Arduino-Kontrol-Suhu-PID/examples/build_temp_pid_simulink.m",
    "Pertemuan-10-MATLAB-Arduino-Baca-RPM-dan-Posisi/examples/arduino_encoder_stream/arduino_encoder_stream.ino",
    "Pertemuan-10-MATLAB-Arduino-Baca-RPM-dan-Posisi/examples/quadrature_state_test.py",
    "Pertemuan-10-MATLAB-Arduino-Baca-RPM-dan-Posisi/examples/analyze_encoder_log.m",
    "Pertemuan-11-MATLAB-Arduino-PID-Kecepatan/examples/arduino_speed_pid/arduino_speed_pid.ino",
    "Pertemuan-11-MATLAB-Arduino-PID-Kecepatan/examples/matlab_speed_pid_experiment.m",
    "Pertemuan-11-MATLAB-Arduino-PID-Kecepatan/examples/analyze_speed_pid_log.m",
    "Pertemuan-11-MATLAB-Arduino-PID-Kecepatan/examples/speed_pid_simulation.m",
    "Pertemuan-11-MATLAB-Arduino-PID-Kecepatan/examples/build_motor_speed_pid_simulink.m",
    "Pertemuan-12-MATLAB-Arduino-PID-Posisi/WORKSHEET_ANALISIS.md",
    "Pertemuan-12-MATLAB-Arduino-PID-Posisi/examples/arduino_position_pid/arduino_position_pid.ino",
    "Pertemuan-12-MATLAB-Arduino-PID-Posisi/examples/matlab_position_pid_experiment.m",
    "Pertemuan-12-MATLAB-Arduino-PID-Posisi/examples/position_pid_offline.m",
    "Pertemuan-12-MATLAB-Arduino-PID-Posisi/examples/analyze_position_pid_log.m",
    "Pertemuan-12-MATLAB-Arduino-PID-Posisi/examples/build_motor_position_pid_simulink.m",
    "Pertemuan-13-PlatformIO-ADC-RPM-Posisi-dengan-AI/PROMPT_AI_CONTOH.md",
    "Pertemuan-13-PlatformIO-ADC-RPM-Posisi-dengan-AI/examples/mega_io_monitor/platformio.ini",
    "Pertemuan-13-PlatformIO-ADC-RPM-Posisi-dengan-AI/examples/mega_io_monitor/src/main.cpp",
    "Pertemuan-13-PlatformIO-ADC-RPM-Posisi-dengan-AI/examples/python_serial_plotter/plot_serial.py",
    "Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/PROMPT_AI_CONTOH.md",
    "Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/examples/mega_temp_pid/platformio.ini",
    "Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/examples/mega_temp_pid/src/main.cpp",
    "Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/examples/mega_temp_pid/lib/PIDCore/PIDCore.h",
    "Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/examples/gui/app.py",
    "Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/examples/gui/response_metrics.py",
    "Pertemuan-15-PlatformIO-Kontrol-Motor-GUI-AI/PROMPT_AI_CONTOH.md",
    "Pertemuan-15-PlatformIO-Kontrol-Motor-GUI-AI/examples/mega_motor_pid/platformio.ini",
    "Pertemuan-15-PlatformIO-Kontrol-Motor-GUI-AI/examples/mega_motor_pid/src/main.cpp",
    "Pertemuan-15-PlatformIO-Kontrol-Motor-GUI-AI/examples/gui/app.py",
    "Pertemuan-15-PlatformIO-Kontrol-Motor-GUI-AI/examples/analyze_saved_run.py",
    "Pertemuan-16-Responsi-P09-P15/examples/final_smoke_test.py",
    "Pertemuan-16-Responsi-P09-P15/examples/node_serial_logger/index.js",
    "Pertemuan-16-Responsi-P09-P15/examples/node_serial_logger/package.json",
]

for rel in required_paths:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required program/document: {rel}")

# Check source-file references written inside backticks in mandatory module
# documentation. Generated .slx/output artifacts are deliberately excluded.
source_suffixes = {".py", ".m", ".ino", ".cpp", ".h", ".ini", ".md", ".ipynb", ".js", ".json", ".txt"}
ref_pattern = re.compile(r"`((?:examples|models)/[^`\s]+)")
for i, name in enumerate(MODULES, 1):
    module = ROOT / name
    assessment = "Project.md" if i in PROJECT else "TugasVideo.md"
    for doc_name in ("Materi.md", "Jobsheet.md", assessment):
        doc = module / doc_name
        if not doc.is_file():
            continue
        text = doc.read_text(encoding="utf-8", errors="ignore")
        for match in ref_pattern.findall(text):
            ref = match.rstrip(".,;:)")
            if "<" in ref or ">" in ref:
                continue
            candidate = module / ref
            if candidate.suffix.lower() == ".slx":
                continue
            if candidate.suffix.lower() in source_suffixes and not candidate.is_file():
                errors.append(f"P{i:02}: broken source reference in {doc_name}: {ref}")

# Guard the protocol/state fixes that are easy to regress accidentally.
source_requirements = {
    "Pertemuan-13-PlatformIO-ADC-RPM-Posisi-dengan-AI/examples/mega_io_monitor/src/main.cpp": [
        "#PROTO,IO_MONITOR,2", "resetEncoderEstimator", "lastCount=0"
    ],
    "Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/examples/mega_temp_pid/src/main.cpp": [
        "#PROTO,TEMP_PID,2", "HEARTBEAT_TIMEOUT_MS", "heaterOff"
    ],
    "Pertemuan-15-PlatformIO-Kontrol-Motor-GUI-AI/examples/mega_motor_pid/src/main.cpp": [
        "#PROTO,MOTOR_PID,3", "clearSpeedEstimator", "lastCount"
    ],
    "Pertemuan-16-Responsi-P09-P15/examples/final_smoke_test.py": [
        "RUN,0", "field_counts", "telemetry_lines"
    ],
}
for rel, tokens in source_requirements.items():
    p = ROOT / rel
    if not p.is_file():
        continue
    text = p.read_text(encoding="utf-8", errors="ignore")
    for token in tokens:
        if token not in text:
            errors.append(f"readiness marker missing in {rel}: {token}")

# Compile every Python file. py_compile checks syntax without requiring GUI or
# hardware dependencies to be importable in this CI stage.
for py in ROOT.rglob("*.py"):
    if ".venv" in py.parts:
        continue
    try:
        py_compile.compile(str(py), doraise=True)
    except Exception as exc:
        errors.append(f"python compile: {py.relative_to(ROOT)}: {exc}")

# Detect explicit incomplete markers in teaching material and source.
for pattern in ("*.md", "*.py", "*.cpp", "*.ino", "*.m"):
    for p in ROOT.rglob(pattern):
        if p.name == "validate_repo.py":
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if "TODO_MANDATORY" in text or "PLACEHOLDER_MANDATORY" in text:
            errors.append(f"incomplete marker in {p.relative_to(ROOT)}")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("VALIDATION PASS")
print(f"Modules checked: {len(MODULES)}")
print(f"Required paths checked: {len(required_paths)}")
print("Documentation/reference/protocol checks: PASS")
