from tkinter import*
from PIL import ImageTk,Image
import instaloader
window=Tk()
window.title("Instadownloader")
window.geometry("600x400")
frame=Frame(window,width=300, height=400)
frame.pack()
frame.place(anchor='center',relx=0.5,rely=0.5)
img=ImageTk.PhotoImage(Image.open("2019_2$largeimg18_Monday_2019_071625041.jpg"))
lb1=Label(window,text="Enter username")
lb1.pack()
label=Label(frame,image=img)
label.pack()
box=Entry(window)
box.pack()
def download():
   test=instaloader.Instaloader()
   acc=box.get()
   test.download_profile(acc,profile_pic_only=True)
   
bt1=Button(window,text="Click here to download",command=download)
bt1.pack()
window.mainloop()
