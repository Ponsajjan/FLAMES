from tkinter import *
window=Tk()
window.title('FLAMES')
window.geometry('450x300')
window.resizable(0,0)
l1=Label(window,text='FLAMES',font=('Arial Bold',50))
l1.grid(column=0,row=0)
l2=Label(window,text='Enter name1',font=('Arial',14))
l2.grid(column=0,row=1)
txt1=Entry(window,width=25)
txt1.grid(column=1,row=1)
l3=Label(window,text='Enter name2',font=('Arial',14))
l3.grid(column=0,row=2)
txt2=Entry(window,width=25)
txt2.grid(column=1,row=2)    

from tkinter import messagebox
def clicked():
    
    name1=str(txt1.get())
    name2=str(txt2.get())
    name1=name1.replace(' ','')
    name2=name2.replace(' ','')
    for j in name2:
        for i in name1:
            if i==j:
                name1=name1.replace(i,'')
                name2=name2.replace(i,'')
                break
    count=len(name1+name2)
    if count>0:
        
        list1=['Friends','Lovers','Affaction','Marriage','Enemy','Sibling']
        while len(list1)>1:
            c=count%len(list1)
            sindex=c-1
            if sindex>=0:
                left=list1[:sindex]
                right=list1[sindex+1:]
                list1=right+left
            else:
                list1=list1[:len(list1)-1]
        
        messagebox.showinfo('Relation ship is',list1[0])
    else:
        messagebox.showinfo('PlZz...','Enter different namess..')
    
bt=Button(window,text='check flames',command=clicked)
bt.grid(column=1,row=3)
window.mainloop()

