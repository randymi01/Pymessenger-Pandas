import importlib
import subprocess

dependencies = ["pandas", "smtplib", "ssl", "os", "sys", "re"]

for package in dependencies:
    try:
        importlib.import_module(package)
    except ModuleNotFoundError:
        print('Module not installed: ',package)
        subprocess.call(['pip', 'install', package])
