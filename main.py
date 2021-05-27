from tkinter import *

window = Tk()
window.title('youtube_video_downloader')
window.geometry('640x480')
window.resizable(False, False)

def addVideo():
    pass

def extraction():
    pass

linkFrmae = LabelFrame(window, text='링크')
linkFrmae.pack(fill='x', padx=5, pady=5, ipady=5)

linkEntry = Entry(linkFrmae).pack(side='left', fill='x', expand=True, padx=5, pady=5, ipady=5)

addVideoBtn = Button(linkFrmae, text='링크 추가', width=10, command=addVideo)
addVideoBtn.pack(side='right', padx=5, pady=5)

listFrame = Frame(window)
listFrame.pack(fill='both', padx=5, pady=5)

scrollbar = Scrollbar(listFrame)
scrollbar.pack(side='right', fill='y')

linkList = Listbox(listFrame, selectmode='extended', height=10, yscrollcommand=scrollbar.set)
linkList.pack(side='left', fill='both', expand=True)
scrollbar.config(command=linkList.yview)

formatFrame = LabelFrame(window, text='파일 형식')
formatFrame.pack(side='left', padx=5, pady=5)

formatVar = IntVar()
MP3_Rad = Radiobutton(formatFrame, text='MP3', value=3, variable=formatVar)
MP4_Rad = Radiobutton(formatFrame, text='MP4', value=4, variable=formatVar)
MP3_Rad.select()
MP3_Rad.pack(side='left')
MP4_Rad.pack(side='left')

extractionBtn = Button(window, text='추출', width=12, padx=5, pady=5, command=extraction)
extractionBtn.pack(side='right', padx=5, pady=5)

window.mainloop()