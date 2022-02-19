from tkinter import *
import random
root=Tk()
root.title("generate password")
root.geometry("400x400")
label=Label(root)

array_3d=[[['1','2','3','4','5','6'],["head","tail"],["A","B","C","D","E","F","G","H","I","J","K"]]]
print(array_3d[0][2][1])

def passwordgenerate():
    random_no1=random.randint(0,5)
    random_no2=random.randint(0,1)
    random_no3=random.randint(0,10)
    
    letter_1=str(array_3d[0][0][random_no1])
    letter_2=(array_3d[0][1][random_no2])
    letter_3=(array_3d[0][2][random_no3])
    
    label["text"]=letter_1+""+letter_2+""+letter_3
    
    

btn=Button(root,text="password generate",command=passwordgenerate,bg="green",fg="yellow")
label.place(relx=0.5,rely=0.6,anchor=CENTER)
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()

