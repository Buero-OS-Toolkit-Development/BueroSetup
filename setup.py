import os, zipfile, shutil
from tkinter.filedialog import *
import tkinter.messagebox as tm

tm.showinfo("BüroSetup 17", "Vielen Dank, dass Sie sich für Büro entschieden haben.\nSie starten BüroSetup Version 17!")

pfad1 = askopenfilename(title="Zip-Datei mit Büro auswählen", filetypes=[("ZIP comprimized folder", "*.zip")])
pfad2 = askopenfilename(title="Zip-Datei mit System auswählen", filetypes=[("ZIP comprimized folder", "*.zip")])
pfad3 = askopenfilename(title="Zip-Datei mit Hintergrundsystem auswählen", filetypes=[("ZIP comprimized folder", "*.zip")])

for i in ["pycols", "pyautogui", "naturalsize", "requests"]:
    os.system("py -m pip install --upgrade "+i)

for i in ["./images", "./programdata", "./programdata/ads", "./programdata/update", "./programdata/buero", "./programdata/buero/debug",\
          "./programdata/achievements", "./programdata/lkims", "./music", "./programdata/win", "./programdata/run"]:
    os.mkdir(i)

for i in [pfad1, pfad2, pfad3]:
    with zipfile.ZipFile(i, "r") as zip_ref:
        zip_ref.extractall("./programdata/update")

for i in ["büro.py", "bueroUtils.py", "systemupdate.py", "update.py", "fehleranalyse.py"]:
    shutil.move("./programdata/update/"+i, "./"+i)
shutil.move("./programdata/update/tipps.txt", "./programdata/buero/tipps.txt")

with open("./programdata/buero/agb.txt", "x") as f:
    f.write(str(tm.askokcancel("AGB", "Wollen Sie unseren AGB jetzt zustimmen?")))
with open("./programdata/buero/color.txt", "x") as f:
    f.write("WHITE#*#WHITE#*#WHITE#*#WHITE#*#WHITE#*#")
with open("./programdata/buero/log.txt", "x") as f:
    f.write("False")
with open("./programdata/buero/notizen.txt", "x") as f:
    f.write("Fügen Sie eine Notiz hinzu")
with open("./programdata/buero/versioninfo.txt", "x") as f:
    pfad1_ = pfad1.split("/")[-1]
    f.write(pfad1_[pfad1_.find("büro")+4:-1].rstrip(".zip"))
with open("./programdata/buero/versioninfo_System.txt", "x") as f:
    f.write(pfad2[pfad2.find("system")+5:-1].rstrip(".zip"))
with open("./programdata/buero/PIN_opt.txt", "x") as f:
    f.write("False")
with open("./programdata/buero/PIN_l.txt", "x") as f:
    f.write("4")
with open("./programdata/buero/menu.txt", "x") as f:
    f.write("")
with open("./programdata/buero/achievements.txt", "x", encoding="utf-8") as f:
    f.write("0#*#")
with open("./programdata/buero/devid.txt", "x", encoding="utf-8") as f:
    f.write("noDevIDGivenYet")
with open("./programdata/buero/deviceidstatic.txt", "x", encoding="utf-8") as f:
    f.write("False")
for i in os.listdir("./programdata/update"):
    if ".lkim" in i:
        if "Special" in i:
            shutil.move("./programdata/update/"+i, "./programdata/lkims/"+i)
        else:
            shutil.move("./programdata/update/"+i, "./programdata/achievements/"+i)
    elif "z!" in i:
        shutil.move("./programdata/update/"+i, "./programdata/win/"+i)
    else:
        shutil.move("./programdata/update/"+i, "./programdata/ads/"+i)

if tm.askokcancel("Büro", "Soll versucht werden, Büro zu öffnen?"):
    os.system("py ./büro.py")
    if tm.askokcancel("Fehlerbehebung", "Falls Fehler aufgetreten sind:\nSoll die Fehleranalyse gestartet werden?"):
        os.system("pyt ./fehleranalyse.py")
