#!/usr/bin/python
from tkinter import *
root=Tk()

def chance(player):
  
    ch=Label(root,text=player)
    ch.grid(row=0,column=3)
    
def played(r,c):
    global player,go
    if player =='X' and go :
            original[r][c].configure(text='x')
            player='O'
            chance(player)
            new[r][c]='x'
    elif player == 'O' and go  :
        original[r][c].configure(text='o')
        player='X'
        chance(player)
        new[r][c]='o'
    for i in range(0,3):
        if new[i][1]==new[i][0]==new[i][2] =='x' or new[i][1]==new[i][0]==new[i][2] =='o' :
            original[i][0].config(bg='red')
            original[i][1].config(bg='red')
            original[i][2].config(bg='red')
            go=FALSE
           # Label1=Label(root,text=player,font='50')
            #Label1.grid(row=3,column=3)
            if  player == 'O':
                player ='X'
                Label1=Label(root,text='X',font='50')
                Label1.grid(row=3,column=3)
            elif  player=='X':
                player ='O'
                Label1=Label(root,text=player,font='50')
                Label1.grid(row=3,column=3)
                break

    for k in range(0,3):
        if new[1][k]==new[0][k]==new[2][k] =='x' or new[1][k]==new[0][k]==new[2][k] =='o' :
            original[1][k].config(bg='red')
            original[2][k].config(bg='red')
            original[0][k].config(bg='red')
            go=FALSE
            if player =='O':
                
                Label1=Label(root,text='X',font='50')
                Label1.grid(row=3,column=3)
            elif  player =='X':
                player ='O'
                Label1=Label(root,text=player,font='50')
                Label1.grid(row=3,column=3)
                break


original=[[0,0,0],[0,0,0],[0,0,0]]
new=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        original[i][j]=Button(root,command = lambda r=i,c=j: played(r,c))
        original[i][j].grid(row=i,column=j)

lable1=Label(root)
lable1.grid(row=3,column=3)
player = 'X'
go=TRUE
mainloop()