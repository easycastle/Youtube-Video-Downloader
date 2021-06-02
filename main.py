import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog

import youtube_dl
import os

window = Tk()
window.title('youtube_video_downloader')
window.geometry('640x480')
window.resizable(False, False)

def addVideo():
    link = linkEntry.get()

    if link == '':
        msgbox.showwarning('경고', '링크를 작성하지 않았습니다.')
    elif 'https://www.youtube.com/watch?v=' in link and link != 'https://www.youtube.com/watch?v=':
        if link in linkList.get(0, END):
            msgbox.showwarning('경고', '이미 대기 중인 링크입니다.')
        else:
            linkList.insert(END, link)
    else:
        msgbox.showwarning('경고', '올바른 링크가 아닙니다.')

    linkEntry.delete(0, END)

def EnterAddVideo(event):
    addVideo()

def deleteSelectedLink():
    if len(linkList.curselection()) == 0:
        msgbox.showwarning('경고', '선택한 링크가 없습니다.')
    else:
        for index in reversed(linkList.curselection()):
            linkList.delete(index)

def BackSpaceDeleteSelectedLink(event):
    deleteSelectedLink()

def deleteAllLink():
    if linkList.size() == 0:
        msgbox.showwarning('경고', '링크를 입력하세요.')
    else:
        response = msgbox.askyesno('경고', '정말로 전체 삭제를 하시겠습니까?')

        if response == 1:
            linkList.delete(0, END)

def browsePath():
    folder_selected = filedialog.askdirectory()
    
    if folder_selected == '':
        return

    pathEntry.delete(0, END)
    pathEntry.insert(0, folder_selected)

def extract():
    if linkList.size() == 0:
        msgbox.showwarning('경고', '링크를 입력하세요.')
    elif pathEntry.get() == '':
        msgbox.showwarning('경고', '저장 위치를 입력하세요.')
    else:
        ytdlOption = {
            'outtmpl' : os.path.join(pathEntry.get(), '%(title)s.%(ext)s'), 
            'format' : formatCmb.get()
        }

        size = linkList.size()
        downloadCnt = 0

        for video in linkList.get(0, END):
            with youtube_dl.YoutubeDL(ytdlOption) as ytdl:
                ytdl.download([video])

            linkList.delete(0)
            downloadCnt += 1

            progress = (downloadCnt + 1) / size * 100
            progressVar.set(progress)
            progressBar.update()

        msgbox.showinfo('알림', '모든 영상을 추출했습니다.')
        progressVar.set(0)
        progressBar.update()



linkFrmae = LabelFrame(window, text='링크')
linkFrmae.pack(fill='x', padx=5, pady=4)

linkEntry = Entry(linkFrmae)
linkEntry.pack(side='left', fill='x', expand=True, padx=5, pady=5, ipady=3)
linkEntry.bind('<Return>', EnterAddVideo)
linkEntry.focus()

addVideoBtn = Button(linkFrmae, text='링크 추가', width=10, command=addVideo)
addVideoBtn.pack(side='right', padx=5, pady=5)



linkOperationFrame = Frame(window)
linkOperationFrame.pack(fill='both', padx=5, pady=4)

listFrame = Frame(linkOperationFrame)
listFrame.pack(side='left', fill='both', expand=True)

xScrollbar = Scrollbar(listFrame, orient=HORIZONTAL)
yScrollbar = Scrollbar(listFrame)
xScrollbar.pack(side='bottom', fill='x')
yScrollbar.pack(side='right', fill='y')

linkList = Listbox(listFrame, selectmode='extended', height=10, xscrollcommand=xScrollbar.set, yscrollcommand=yScrollbar.set)
linkList.pack(side='left', fill='x', expand=True)
linkList.bind('<BackSpace>', BackSpaceDeleteSelectedLink)
xScrollbar.config(command=linkList.xview)
yScrollbar.config(command=linkList.yview)


deleteBtnFrame = Frame(linkOperationFrame)
deleteBtnFrame.pack(side='right')

deleteSelectionBtn = Button(deleteBtnFrame, text='선택 삭제', width=10, command=deleteSelectedLink)
deleteSelectionBtn.pack(padx=5, pady=18)
deleteAllBtn = Button(deleteBtnFrame, text='전체 삭제', width=10, command=deleteAllLink)
deleteAllBtn.pack(padx=5, pady=18)



pathFrame = LabelFrame(window, text='저장경로')
pathFrame.pack(fill='x', padx=5, pady=4)

pathEntry = Entry(pathFrame)
pathEntry.pack(side='left', fill='x', expand=True, padx=5, pady=5, ipady=3)

pathBtn = Button(pathFrame, text='찾아보기', width=10, command=browsePath)
pathBtn.pack(side='right', padx=5, pady=5)



optionFrame = LabelFrame(window, text='옵션 설정')
optionFrame.pack(side='top', fill='x', padx=5, pady=4)

formatLabel = Label(optionFrame, text='포맷')
formatLabel.pack(side='left', padx=5, pady=5)

formatOption = ['mp4', 'm4a', 'webm', 'best', 'worst', 'bestvideo', 'worstvideo', 'bestaudio', 'worstaudio']
formatCmb = ttk.Combobox(optionFrame, state='readonly', values=formatOption, width=10)
formatCmb.current(0)
formatCmb.pack(fill='x', padx=5, pady=5)


progressFrame = LabelFrame(text='진행 상황')
progressFrame.pack(side='top', fill='x', padx=5, pady=4)

progressVar = DoubleVar()
progressBar = ttk.Progressbar(progressFrame, maximum=100, variable=progressVar)
progressBar.pack(fill='x', padx=5, pady=5)



runFrame = Frame(window)
runFrame.pack(side='right')

startBtn = Button(runFrame, text='닫기', width=12, padx=5, pady=5, command=window.quit)
startBtn.pack(side='right', padx=5, pady=5)

extractionBtn = Button(runFrame, text='추출', width=12, padx=5, pady=5, command=extract)
extractionBtn.pack(side='right', padx=5, pady=5)

window.mainloop()