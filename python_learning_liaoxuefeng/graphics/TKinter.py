from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidegts()

    def createWidegts(self):
        # self.helloLabel = Label(self, text='hello,world')
        # self.helloLabel.pack()
        # self.quitButton = Button(self, text='Quite', command=self.quit)
        # self.quitButton.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Mseeage', 'hello, %s' % name)


app = Application()
# 设置窗口标题
app.master.title('hello world')
# 主消息循环
app.mainloop()
