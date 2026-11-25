"""راه‌انداز: پروژه از داخل فایل zip کنار همین فایل باز می‌شه و اجرا می‌شه.
(برای وقتی که آپلود پوشه‌ها روی GitHub ممکن نیست.)"""
import glob
import os
import runpy
import shutil
import sys
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))

zips = sorted(glob.glob(os.path.join(ROOT, "*.zip")))
if not zips:
    sys.exit("START ERROR: no .zip file found next to start.py")

target = os.path.join(ROOT, "_project")
shutil.rmtree(target, ignore_errors=True)
with zipfile.ZipFile(zips[0]) as z:
    z.extractall(target)

project = None
for dirpath, _dirs, _files in os.walk(target):
    if os.path.isfile(os.path.join(dirpath, "app", "main.py")):
        project = dirpath
        break
if project is None:
    sys.exit("START ERROR: app/main.py not found inside the zip")

print(f"starting from {zips[0]} -> {project}", flush=True)
os.chdir(project)
sys.path.insert(0, project)
runpy.run_module("app.main", run_name="__main__")
