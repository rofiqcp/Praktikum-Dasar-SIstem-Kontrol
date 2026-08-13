from __future__ import annotations
from pathlib import Path
import py_compile
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

for i, name in enumerate(MODULES, 1):
    p = ROOT / name
    if not p.is_dir():
        errors.append(f"P{i:02}: missing directory {name}")
        continue
    for required in ("Materi.md", "Jobsheet.md"):
        if not (p / required).is_file():
            errors.append(f"P{i:02}: missing {required}")
    expected = "Project.md" if i in PROJECT else "TugasVideo.md"
    forbidden = "TugasVideo.md" if i in PROJECT else None
    if not (p / expected).is_file():
        errors.append(f"P{i:02}: missing {expected}")
    if forbidden and (p / forbidden).exists():
        errors.append(f"P{i:02}: {forbidden} must be replaced by Project.md")

required_paths = [
    "build_all_slx.m",
    "HARDWARE_PCB_SPEC.md",
    "WIRING.md",
    "SAFETY.md",
    "TESTING.md",
    "shared/python/response_metrics.py",
    "shared/arduino/PIDCore.h",
    "Pertemuan-03-Transfer-Function-Plant/examples/build_three_plants_simulink.m",
    "Pertemuan-04-PID-MATLAB-dan-Blok-Manual/examples/build_pid_manual_simulink.m",
    "Pertemuan-09-MATLAB-Arduino-Kontrol-Suhu-PID/examples/matlab_temp_pid.m",
    "Pertemuan-10-MATLAB-Arduino-Baca-RPM-dan-Posisi/examples/arduino_encoder_stream/arduino_encoder_stream.ino",
    "Pertemuan-11-MATLAB-Arduino-PID-Kecepatan/examples/arduino_speed_pid/arduino_speed_pid.ino",
    "Pertemuan-12-MATLAB-Arduino-PID-Posisi/examples/arduino_position_pid/arduino_position_pid.ino",
    "Pertemuan-13-PlatformIO-ADC-RPM-Posisi-dengan-AI/examples/mega_io_monitor/platformio.ini",
    "Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/examples/mega_temp_pid/platformio.ini",
    "Pertemuan-14-PlatformIO-Kontrol-Suhu-GUI-AI/examples/gui/app.py",
    "Pertemuan-15-PlatformIO-Kontrol-Motor-GUI-AI/examples/mega_motor_pid/platformio.ini",
    "Pertemuan-15-PlatformIO-Kontrol-Motor-GUI-AI/examples/gui/app.py",
]
for rel in required_paths:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required program: {rel}")

for py in ROOT.rglob("*.py"):
    if ".venv" in py.parts:
        continue
    try:
        py_compile.compile(str(py), doraise=True)
    except Exception as exc:
        errors.append(f"python compile: {py.relative_to(ROOT)}: {exc}")

# Detect common incomplete markers in mandatory documentation/programs.
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
