from tkinter import *
from tkinter.font import Font


top = Tk()
# Code to add widgets will go here...
top.state("zoomed")

ca = Canvas(top)
ca.pack()

backgroundImage = PhotoImage(file='E:\\PhotoChoser\\Pixabay\\design.png')
loginImg= PhotoImage(file='E:\\PhotoChoser\\Pixabay\\login.png')
signupImg= PhotoImage(file='E:\\PhotoChoser\\Pixabay\\sign.png')
background_label= Label(top, image=backgroundImage)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

frame=Frame(top)
frame.pack()

label= Label(top, bg='#ffffff')
label.place(relx=0.38,rely=0.075,relwidth=0.25,relheight=0.85)


font=Font(family='Andalus', size=12)

text_field= Entry(label,bg='#fff5ff',font=font)
text_field.place(relx=0.20,rely=0.38,relwidth=0.60,relheight=0.055)

font2=Font(family='Andalus', size=20)

text_field2= Entry(label, bg='#fff5ff',font=font2,show='*')
text_field2.place(relx=0.20,rely=0.52 , relwidth=0.60,relheight=0.055)

font3= Font(family="Montserrat", size="10",weight="bold")

label_name= Text(label,bg='#ffffff', bd=0,font= font3,pady=0,width=1)
label_name.insert(INSERT,"Name")
label_name.place(relx= 0.20 ,rely=0.35 ,relwidth=0.198 ,relheight=0.030)

label_pswd= Text(label,bg='#ffffff', bd=0,font= font3,pady=0,width=1)
label_pswd.insert(INSERT,"Password")
label_pswd.place(relx= 0.20 ,rely=0.49 ,relwidth=0.198 ,relheight=0.030)

font4= Font(family="Bodoni",size='18')

login= Button(label,bg='#ffffff',font=font4,width=1,image=loginImg,bd=0)
login.place(relx=0.37, rely=0.64 ,relwidth=0.30 ,relheight=0.055)

sign_up=Button(label,bg='#ffffff',font=font4,width=1,image=signupImg,bd=0)
sign_up.place(relx=0.37, rely=0.74 ,relwidth=0.30 ,relheight=0.055)

top.mainloop()