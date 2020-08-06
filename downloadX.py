from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json

class MyHandler(FileSystemEventHandler):
    # i = 1
    def on_modified(self, event):
        setups_ext = (".exe",".msi")
        images_ext = (".png",".jpg",".jpeg",".bmp",".tiff",".gif")
        docs_ext = (".doc",".docx",".rtf",".ppt",".xlsx",".csv",".pptx",".xls",".file")
        videos_ext = (".web",".mp4",".avi",".webm",".flv",".mov",".wmv",".mkv")
        archive_ext = (".zip",".rar",".7z") 
        temp_ext = (".crdownload",".tmp")
        for filename in os.listdir(folder_Main):
            if filename.endswith(temp_ext):
                time.sleep(10)
                break    
            if filename.endswith(".txt"):
                print("Text File Found")
                src = os.path.join(folder_Main,filename)
                new_destination = os.path.join(folder_Text,filename)
                os.rename(src,new_destination)
            elif filename.endswith(".pdf"):
                print("PDF File Found")
                src = os.path.join(folder_Main,filename)
                new_destination = os.path.join(folder_PDF,filename)
                os.rename(src,new_destination)    
            elif filename.endswith(setups_ext):
                print("Setup File Found")
                src = os.path.join(folder_Main,filename)
                new_destination = os.path.join(folder_Setups,filename)
                os.rename(src,new_destination)
            elif filename.endswith(archive_ext):
                print("Archive File Found")
                src = os.path.join(folder_Main,filename)
                new_destination = os.path.join(folder_Archive,filename)
                os.rename(src,new_destination)
            elif filename.endswith(docs_ext):
                print("Doc File Found")
                src = os.path.join(folder_Main,filename)
                new_destination = os.path.join(folder_Docs,filename)
                os.rename(src,new_destination)
            elif filename.endswith(images_ext):
                print("Image File Found")
                src = os.path.join(folder_Main,filename)
                new_destination = os.path.join(folder_Images,filename)
                os.rename(src,new_destination)
            elif filename.endswith(videos_ext):
                print("Video File Found")
                src = os.path.join(folder_Main,filename)
                new_destination = os.path.join(folder_Videos,filename)
                os.rename(src,new_destination)
            else:
                print("Other File Found")
                src = os.path.join(folder_Main,filename)
                new_destination = os.path.join(folder_Others,filename)
                os.rename(src,new_destination)


folder_Main = "" # Main Folder where the files will be downloaded
folder_Text = "" # Text Folder
folder_PDF = "" # PDF Folder
folder_Setups = "" # Setups Folder
folder_Archive = "" # Archives Folder
folder_Docs = "" # Docs Fodler
folder_Images = "" # Images Folder
folder_Videos = "" # Videos Folder
folder_Others = "" # Other
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_Main, recursive=True)
observer.start()

try:
    while True:
        time.sleep(20)
        print("Out of sleep")
        observer.join()
except KeyboardInterrupt:
        observer.stop()
observer.join()

