from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import os
import requests
import json
import time
import datetime
import logging
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import threading
import download_module
from utils import Utils

root = Tk()
currdir = os.getcwd()

"""
TODO:
[ ] Change to phantomJS for headless browser -- not that much necessary but better to do it not to see browser opening
[ ] Error handling
[ ] Change to local time
[ ] Include all the availbale APIs, only basic extraction is done until now
[ ] Parsing and timeline analysis?
[ ] Save to DataBase
"""

def browse_path():
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    save_path_entry.config(state='enabled')
    save_path_entry.delete(0,END)
    save_path_entry.insert(0,tempdir)

def browse_file():
    fname = filedialog.askopenfilename(filetypes = (("All files", "*"), ("Database files", "*.db")))
    cookie_path_entry.config(state='enabled')
    cookie_path_entry.delete(0,END)
    cookie_path_entry.insert(0,fname)

def enable_disable_login(enable):
    if enable == 1:
        username_entry.config(state='enabled')
        password_entry.config(state='enabled')
    else:
        username_entry.config(state='disabled')
        password_entry.config(state='disabled')

def Initiate_download(location, credential):
    directory = save_path_entry.get()
    if directory == '':
        Utils.showMessage('Error', 'Path not correct ,please enter the path')
        return
    # download from Amazon, OnHub, or Mother sense
    if location == 'Amazon':
        if credential == 'login':
            #login api
            url_login = 'https://www.amazon.com/ap/signin?showRmrMe=1&openid.return_to=https%3A%2F%2Falexa.amazon.com%2F&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_dp_project_dee&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&'

            #common api
            global_api = 'https://pitangui.amazon.com/api/'

            #instantiate the browser
            browser = webdriver.Firefox()

            #get the login page
            browser.get(url_login)

            logging.debug("logging-in!")
            print("logging-in.......")

            #Locate the username and password elements of the amazon website
            username = browser.find_element_by_id("ap_email")
            password = browser.find_element_by_id("ap_password")

            username_name = username_entry.get()
            password_pass = password_entry.get()

            #Enter username and password in their perspective fields
            username.send_keys(username_name)
            password.send_keys(password_pass)

            #Simulate the click event by finding the sign in button, find by id
            browser.find_element_by_id("signInSubmit").click()

            print("logged-in!!")

            # get the cookies from the current session
            all_cookies = browser.get_cookies()

            #save the cookies so that request library can use it
            cookies = {}
            for s_cookie in all_cookies:
                cookies[s_cookie['name']] = s_cookie['value']
            #close the browser 
            browser.close()

            #download the files using the cookie that we got from the login browser
            download_module.download_files(cookies, directory, CheckCalling.get(), CheckAudio.get())
            Utils.showMessage('Information', 'The download finished successfully!')

        elif credential == 'cookie':
            db_file = cookie_path_entry.get()
            if db_file == '':
                Utils.showMessage('Error', 'Path should not be empty, please provide cookie file')
                return
            download_module.main(db_file, directory, CheckCalling.get(), CheckAudio.get())
        else:
            Utils.showMessage('Error', 'Incorrect parameter, Please select credential type.')

#User Interface code
root.title("Download files from Cloud")
root.config(height = 480, width = 1000)
root.resizable(False, False)

icon = PhotoImage(file=os.path.join(currdir, 'icon.gif'))
root.tk.call('wm', 'iconphoto', root._w, icon)

gui_style = ttk.Style()
gui_style.configure('My.TFrame', background='#334353')

username = StringVar()
save_to = StringVar()
password = StringVar()
count = StringVar()
cloud_rVal = StringVar()
cloud_rVal.set('Amazon')
cred = StringVar()
cred.set('none')
cookie_path = StringVar()
CheckCalling = IntVar()
CheckAudio = IntVar()

frame2 = ttk.Frame(root,padding="3 3 12 12", relief=GROOVE, borderwidth=2) #Row of buttons
frame2.grid(column=0, row=0,sticky=(N, W, E, S))
ttk.Button(frame2, text="Browse", command=browse_path).grid(column=3, row=0, sticky=(E, W))
save_path_entry = ttk.Entry(frame2, width=30, textvariable=save_to, state='readonly')
save_path_entry.grid(column=1, row=0, padx=3, columnspan=2, sticky=(W, E))
ttk.Label(frame2, text="Save To:").grid(column=0, row=0,padx=3, sticky=W)
ttk.Label(frame2, text="Download from:").grid(column=0, padx=3,row=1, sticky=W)

#radio buttons
Radiobutton(frame2, text="Amazon", variable=cloud_rVal, value='Amazon').grid(column=1, row=1, padx=3, sticky=W)
Radiobutton(frame2, text="IoT Device-2", variable=cloud_rVal, value='IoT2', state='disabled').grid(column=2, row=1, padx=3, sticky=W)
Radiobutton(frame2, text="IoT device-3", variable=cloud_rVal, value='IoT3',state='disabled').grid(column=3, row=1, padx=3, sticky=W)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=1, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#textboxes
username_entry = ttk.Entry(mainframe, width=30, textvariable=username, state='disabled')
username_entry.grid(column=1, row=4, columnspan=2, sticky=(W, E))
password_entry = ttk.Entry(mainframe, width=30, textvariable=password, show ='*',state='disabled')
password_entry.grid(column=1, row=5, columnspan=2, sticky=(W, E))
cookie_path_entry = ttk.Entry(mainframe, width=30, textvariable=cookie_path, state='readonly')
cookie_path_entry.grid(column=1, row=2, padx=3, columnspan=2, sticky=(W, E))

#Buttons
ttk.Button(mainframe, text="Download", command=lambda:Initiate_download(cloud_rVal.get(), cred.get())).grid(column=3, row=4,rowspan=2, sticky=(E, W, N, S))
ttk.Button(mainframe, text="Browse", command=browse_file).grid(column=3, row=2, sticky=(E, W))

#Radio buttons
Radiobutton(mainframe, text="None", variable=cred, value='none',command = lambda: enable_disable_login(0)).grid(column=1, row=1, padx=3, sticky=W)
Radiobutton(mainframe, text="Login", variable=cred, value='login',command = lambda: enable_disable_login(1)).grid(column=2, row=1, padx=3, sticky=W)
Radiobutton(mainframe, text="Cookies", variable=cred, value='cookie',command = lambda: enable_disable_login(0)).grid(column=3, row=1, padx=3, sticky=W)

ttk.Separator(mainframe,orient=HORIZONTAL).grid(row=3, columnspan=5, sticky=(E,W))

#labels
ttk.Label(mainframe,text='Credential:').grid(column=0,row=1,sticky=W)
ttk.Label(mainframe,text='Cookie file:').grid(column=0,row=2,sticky=W)
#ttk.Label(mainframe, text='Include').grid(column=1, row=6, sticky=(W,E))
ttk.Label(mainframe, text="Username:").grid(column=0, row=4, sticky=W)
ttk.Label(mainframe, text="Password:").grid(column=0, row=5, sticky=W)
ttk.Label(mainframe, text="Include:").grid(column=0, row=6, sticky=W)

#Options check 
C1 = Checkbutton(mainframe, text = "Calling and Messaging data", variable = CheckCalling, onvalue = 1, offvalue = 0)
C1.grid(column=1, row=6,columnspan=2, sticky=(W,E))
C2 = Checkbutton(mainframe, text = "Voice data", variable = CheckAudio, onvalue = 1, offvalue = 0)
C2.grid(column=3,row=6,sticky=(E,W))

#progress bar
#pr = ttk.Progressbar(mainframe, orient='horizontal', mode='indeterminate')
#pr.grid(column=3,row=6,sticky=(E,W))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

username_entry.focus()
root.bind('<Return>', Initiate_download)

root.mainloop()