import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "sympy"],
    "include_files": []
}

base = None

# Se fosse Windows GUI:
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Fatora - 1",
    version="1.0",
    description="Software para fatorar polinomios",
    options={"build_exe": build_exe_options},
    executables=[Executable("fatorador_polinomios.py", base=base)]
)