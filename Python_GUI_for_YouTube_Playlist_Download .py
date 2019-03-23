import os
from tkinter import filedialog
from pytube import *
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import re
from tkinter import *

#with chosen path

#'/home/shivam/Music/downloadedVideo'
master = Tk()

currdir = os.getcwd()
tempdir = filedialog.askdirectory(parent=master, initialdir=currdir, title='Please select a directory')
def start_download():
    Playlistpl = Playlist(e1.get())
    Playlistpl.download_all(tempdir)
master.title('Download Utube Playlist')
Label(master, text="Enter Playlist URL here ->").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=2)

Button(master,text="QUIT",
                   fg="red",
                   command=quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master,text="Start Download",
                   fg="green",
                   command=start_download).grid(row=3, column=2, sticky=W, pady=4)

mainloop()