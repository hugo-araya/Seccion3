from tkinter import * 
from PIL import Image, ImageTk

def salir():
    print(nombre_str.get())
    nombre_str.set('hjshjdhsj')

root = Tk() 
root.title('Formulario 1') 
root.geometry("400x600+100+200")

nombre_label = Label(root,text="Nombre :") 
nombre_label.grid(row=0,column=0) 
nombre_str = StringVar() 
nombre_entry = Entry(root,textvariable=nombre_str) 
nombre_entry.grid(row=0,column=1) 

last_label= Label(root,text="Apellido : ") 
last_label.grid(row=1,column=0) 
last_str = StringVar() 
last_entry = Entry(root,textvariable=last_str) 
last_entry.grid(row=1,column=1) 

mail_label = Label(root,text="Email : ") 
mail_label.grid(row=2,column=0) 
mail_str = StringVar() 
mail_entry = Entry(root,textvariable=mail_str) 
mail_entry.grid(row=2,column=1) 

finish = Button(root,text="finalizar",relief=FLAT, command = salir) 
finish.grid(row=3,column=1) 

im = Image.open('Campeon.png')
ph = ImageTk.PhotoImage(im,size=0.5)
imagen_label= Label(root,image=ph,text='Campeon') 
imagen_label.grid(row=4,column=1) 
root.mainloop() 