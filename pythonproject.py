import io
import requests
import webbrowser
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image





class New_App:
    def __init__(self):
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=68ec3a8eb3c4423cbd3cab47ecbe3f1f').json()

        print(self.data)
        self.load_gui()
        self.load_news_item(0)


    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.title('My News')
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def load_news_item(self, index):
        self.clear()

        #image
        try: 
         url_img = self.data['articles'][index]['urlToImage']
         raw_data = urlopen(url_img).read()
         im = Image.open(io.BytesIO(raw_data)).resize((350,250))
         photo = ImageTk.PhotoImage(im)

        except : 
         img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
         raw_data = urlopen(img_url).read()
         im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
         photo = ImageTk.PhotoImage(im)

        label = Label(self.root,image = photo)
        label.pack()

        heading = Label(self.root,text = self.data['articles'][index]['title'], bg='black',fg='white',wraplength=350, justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))


        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350,justify='center')
        details.pack(pady=(2,20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root, bg ='black')
        frame.pack(expand=True,fill=BOTH)
        
        if index != 0 :
         prev = Button(frame, text='Prev', width=16, height=3,command= lambda : self.load_news_item(index-1))
         prev.pack(side=LEFT)

        read = Button(frame, text ='ReadMore',width=16,height=3, command= lambda : self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles']) -1 :
         next = Button(frame, text='Next', width=16, height=3, command= lambda: self.load_news_item(index+1))
         next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(sel, url) :
        webbrowser.open(url)    

        




obj = New_App()
