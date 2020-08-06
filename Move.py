from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_Source):
                src = os.path.join(folder_Source,filename)
                new_destination = os.path.join(folder_Destination,filename)
                os.rename(src,new_destination)


folder_Source = "" # Main Folder where the files will be
folder_Destination = "" # Folder where you want to move the files
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_Source, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
        observer.stop()
observer.join()

