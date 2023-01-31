import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#the directory from which the event is going to take place
from_dir = "C:/Users/Dell/Downloads" 




# Event Handler Class

class FileMovementHandler(FileSystemEventHandler):

    #display message on deleting a file
    def on_deleted(self, event):
        print(f"Oops someone deleted the file {event.src_path} !...")

       
# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt: #press ctrl+C

    print("stopped")
    observer.stop()
