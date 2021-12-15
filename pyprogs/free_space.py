import os

os.chdir("./PNG/")
li = os.listdir()
for _ in li:
    os.remove(f"./{_}")
os.chdir("./../SVG/")
li = os.listdir()
for _ in li:
    os.remove(f"./{_}")