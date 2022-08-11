import os
import shutil
from win10toast import ToastNotifier
from time import sleep



folder = os.path.join(os.environ["HOMEPATH"],
                      "OneDrive\Desktop\AUTOMATE FILES")

folder2 = os.getcwd()
app_icon_fold = folder2 + "\\Elegantthemes-Beautiful-Flat-Document.ico"
app_icon_fold = app_icon_fold.replace("\\", "\\\\")


print(app_icon_fold)
os.chdir(folder)
image_formats = ["jpg", "png", "jpeg", "gif", "webp", "tiff"]
excel_formats = ["xlsx", "xls", ".csv"]
audio_formats = ["mp3", "wav"]
video_formats = ["mp4", "avi", "webm", "m4v"]
Text_formats = ["ai", "ait", "txt", "rtf"]
Pdf_format = ["pdf"]
Doc_formats = ["doc", "docx"]
PPT_formats = ["ppt", "pptx"]
Python_format = ["py"]
Java_format = ["java"]
C_Cpp_format = ["c", "cpp"]
Exe_format = ["exe"]


def init():
        if not os.path.isdir(os.path.join(folder, "Images")):
            os.mkdir(os.path.join(folder, "Images"))
        if not os.path.isdir(os.path.join(folder, "Excel")):
            os.mkdir(os.path.join(folder, "Excel"))
        if not os.path.isdir(os.path.join(folder, "Audio")):
            os.mkdir(os.path.join(folder, "Audio"))
        if not os.path.isdir(os.path.join(folder, "Videos")):
            os.mkdir(os.path.join(folder, "Videos"))
        if not os.path.isdir(os.path.join(folder, "Texts")):
            os.mkdir(os.path.join(folder, "Texts"))
        if not os.path.isdir(os.path.join(folder, "PDFs")):
            os.mkdir(os.path.join(folder, "PDFs"))
        if not os.path.isdir(os.path.join(folder, "PPTs")):
            os.mkdir(os.path.join(folder, "PPTs"))
        if not os.path.isdir(os.path.join(folder, "Docs")):
            os.mkdir(os.path.join(folder, "Docs"))
        if not os.path.isdir(os.path.join(folder, "Python")):
            os.mkdir(os.path.join(folder, "Python"))
        if not os.path.isdir(os.path.join(folder, "Java")):
            os.mkdir(os.path.join(folder, "Java"))
        if not os.path.isdir(os.path.join(folder, "C_CPP")):
            os.mkdir(os.path.join(folder, "C_CPP"))
        if not os.path.isdir(os.path.join(folder, "EXE")):
            os.mkdir(os.path.join(folder, "EXE"))
        if not os.path.isdir(os.path.join(folder, "Others")):
            os.mkdir(os.path.join(folder, "Others"))

toast=ToastNotifier()
toast.show_toast(
    "Arrange !", "The process has been started", icon_path=app_icon_fold, duration=10)


init()

while True:
    try:
        files = os.listdir(folder)
        
        for file in files:
            if os.path.isfile(file) and file != "arrange.py" and file != "Elegantthemes-Beautiful-Flat-Document.ico" :
                ext = (file.split(".")[-1]).lower()

                if ext in image_formats:
                    shutil.move(file, "Images/"+file)
                elif ext in audio_formats:
                    shutil.move(file, "Audio/"+file)
                elif ext in video_formats:
                    shutil.move(file, "Videos/"+file)
                elif ext in Text_formats:
                    shutil.move(file, "Texts/"+file)
                elif ext in Pdf_format:
                    shutil.move(file, "PDFs/"+file)
                elif ext in Doc_formats:
                    shutil.move(file, "Docs/"+file)
                elif ext in PPT_formats:
                    shutil.move(file, "PPTs/"+file)
                elif ext in Python_format:
                    shutil.move(file, "Python/"+file)
                elif ext in Java_format:
                    shutil.move(file, "Java/"+file)
                elif ext in C_Cpp_format:
                    shutil.move(file, "C_CPP/"+file)
                elif ext in Exe_format:
                    shutil.move(file, "EXE/"+file)

                elif ext in excel_formats:
                    shutil.move(file,'Excel/'+file)
                else:
                    shutil.move(file,'Others/'+file) 
    except:
        continue

    sleep(1)

    
    
#  #if program is using too much memory we can increae the value of sleep function 