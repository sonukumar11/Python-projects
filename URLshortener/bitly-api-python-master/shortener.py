#Install the bitly_api module by entering the command into the terminal: python setup.py install
import bitly_api
import tkinter as tk

#Get Your Access Token from the bitly official OAuth Page
bitlyAcessToken = '4c65d45b1b01ea02c20337b04b887fc88aabfaae'
#Establishing Connection..
connect = bitly_api.Connection(access_token = bitlyAcessToken)
#Creating an Instance of Tkinter Class
root= tk.Tk()
#creating a canvas of size 400x300
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

#Creating a Styled label
label1 = tk.Label(root, text='URL Shortener',fg = "red",font = "Times")
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

#creating Another Label
label2 = tk.Label(root, text='Type your URL here:',fg = "magenta",font = "Times")
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

#creating an entry box for user Input
entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def UrlShorten():
    url = entry1.get()
    label1 = 0
    try:
        newUrl = connect.shorten(url)
        label1 = tk.Label(root, text= newUrl['url'],fg = "cyan",font = "Times")
        canvas1.create_window(200, 230, window=label1)
    except:
        label1 = tk.Label(root, text= "Please Enter a Valid URL.")
        canvas1.create_window(200, 230, window=label1)
    print(newUrl)
    print(newUrl['url'])

button1 = tk.Button(text='Shorten URL', command=UrlShorten, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()


