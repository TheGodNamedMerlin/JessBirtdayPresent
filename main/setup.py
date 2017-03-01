import sys
from cx_Freeze import setup, Executable

setup(
    name = "Chapter01",
    version = "1.0",
    description = "A game developed for jess' birthday",
    executables = [Executable("Main.py", base = "Win32GUI")])
