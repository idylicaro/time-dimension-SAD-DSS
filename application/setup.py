import sys

import cx_Freeze
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "pyodbc"]}

base = None
executables = [cx_Freeze.Executable('main.py')]
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "time-dimension-SAD-DSS",
    version = "1.0",
    description = "My 'Sad' Dss application!",
    options = {"build_exe": build_exe_options},
    executables = executables
)