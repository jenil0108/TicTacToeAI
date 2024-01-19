import tkinter as tk
from tkinter import ttk
import random 
import sys
global okVar
def minimax(ar,d,alpha,beta,ismax):
    ch=check(ar)
    if ch!=-100:
        return ch
    if ismax:
        best=-100
        for ci in range(3):
            for j in range(3):
                if ar[ci][j]=='':
                    ar[ci][j]='X'
                    score=minimax(ar,d+1,alpha,beta,False)
                    ar[ci][j]=''
                    best=max(best,score)
                    alpha=max(score,alpha)
                    if beta<=alpha:
                        break
        return best
    else:
        best=100
        for ci in range(3):
            for j in range(3):
                if ar[ci][j]=='':
                    ar[ci][j]='O'
                    score=minimax(ar,d+1,alpha,beta,True)
                    ar[ci][j]=''
                    best=min(best,score)
                    beta=min(beta,score)
                    if beta<=alpha:
                        break
        return best

def pmove(ar):
    global okVar
    okVar=tk.IntVar()    
    c.wait_variable(okVar)
    ar[a][w]='O'


def cmove(ar):
    best=-100
    global player_title
    move=[-1,-1]
    for ci in range(3):
        for cj in range (3):
            if ar[ci][cj]=='':
                ar[ci][cj]='X'
                score=minimax(ar,0,-100,100,False)
                ar[ci][cj]=''
                if (score>best):
                    move=[ci,cj]
                    best=score
    ci=move[0]
    cj=move[1]
    ar[ci][cj]='X'
    return ci*3+cj

def check(ar):
    global correct
    for k in range(3):
        for j in range (3):
            if (j==0):
                if (ar[k][j]==ar[k][j+1] and ar[k][j+1]==ar[k][j+2] and ar[k][j]!=''):
                    correct=[[j,k],[k,j+1],[j+2,k]]
                    winner=ar[k][j]
                    if winner=='X':
                        return 1
                    else:
                        return -1
            if (k==0):
                if (ar[k][j]==ar[k+1][j] and ar[k+1][j]==ar[k+2][j] and ar[k][j]!=''):
                    correct=[[j,k],[j,k+1],[j,k+2]]
                    winner=ar[k][j]
                    if winner=='X':
                        return 1
                    else:
                        return -1
    if (ar[0][0]==ar[1][1] and ar[1][1]==ar[2][2] and ar[0][0]!=''):
        correct=[[0,0],[1,1],[2,2]]
        winner=ar[0][0]
        if winner=='X':
            return 1
        else:
            return -1
    if (ar[0][2]==ar[1][1] and ar[1][1]==ar[2][0] and ar[0][2]!=''):
        correct=[[2,0],[1,1],[0,2]]
        winner=ar[0][2]
        if winner=='X':
            return 1
        else:
            return -1
    if (ar[0][0]!='' and ar[0][1]!='' and ar[0][2]!='' and ar[1][0]!='' and ar[1][1]!='' and ar[1][2]!='' and ar[2][0]!='' and ar[2][1]!='' and ar[2][2]!=''):
        return 0
    correct=[]
    return -100
    

def board(ar,c):  
    for k in range (3):
        for j in range (3):
            ycentre=k*100+50
            xcentre=j*100+50
            if (ar[k][j]=="X"):
                line=c.create_line(xcentre-25,ycentre-25,xcentre+25,ycentre+25,fill="white")
                line=c.create_line(xcentre-25,ycentre+25,xcentre+25,ycentre-25,fill="white")
            elif (ar[k][j]=="O"):
                circle=c.create_oval(xcentre-25,ycentre-25,xcentre+25,ycentre+25,outline="white")

def change(z,y,q):
    global a,w,okVar,i
    a=z
    okVar.set(1)
    w=y
    i=q


def decide(x):
    global player_title
    player_title=x
    okVar.set(1)


memo={}
corrrect=[]
move=''
ar=[['','',''],['','',''],['','','']]
root=tk.Tk()
root.title("TicTacToe")
c=tk.Canvas(root,bg="black", height = 320, width =300)
c.pack()
player_title='O'
comp_title='X'
b1=tk.Button(c,text="You Start", command= lambda x=1:decide(x), height=6, width=20, background="White")
b1.place(x=75,y=50)
b2=tk.Button(c,text="Computer Starts", command=lambda x=2:decide(x), height=6, width=20, background="White")
b2.place(x=75,y=170)
okVar=tk.IntVar()
c.wait_variable(okVar)
b1.destroy()
b2.destroy()
print(player_title)
a=-1
w=-1
i=-1
line=c.create_line(0,100,300,100,fill="white")
line=c.create_line(0,200,300,200,fill="white")
line=c.create_line(100,0,100,300,fill="white")
line=c.create_line(200,0,200,300,fill="white")
b=['','','','','','','','','']
b[0]=tk.Button(c, command=lambda x=0, y=0, z=0:change(x,y,z), height=6, width=13, background="black")
b[1]=tk.Button(c, command=lambda x=0, y=1, z=1:change(x,y,z), height=6, width=13, background="black")
b[2]=tk.Button(c, command=lambda x=0, y=2, z=2:change(x,y,z), height=6, width=13, background="black")
b[3]=tk.Button(c, command=lambda x=1, y=0, z=3:change(x,y,z), height=6, width=13, background="black")
b[4]=tk.Button(c, command=lambda x=1, y=1, z=4:change(x,y,z), height=6, width=13, background="black")
b[5]=tk.Button(c, command=lambda x=1, y=2, z=5:change(x,y,z), height=6, width=13, background="black")
b[6]=tk.Button(c, command=lambda x=2, y=0, z=6:change(x,y,z), height=6, width=13, background="black")
b[7]=tk.Button(c, command=lambda x=2, y=1, z=7:change(x,y,z), height=6, width=13, background="black")
b[8]=tk.Button(c, command=lambda x=2, y=2, z=8:change(x,y,z), height=6, width=13, background="black")
b[0].place(x=0,y=0)
b[1].place(x=100,y=0)    
b[2].place(x=200,y=0)
b[3].place(x=0,y=100)
b[4].place(x=100,y=100)
b[5].place(x=200,y=100)
b[6].place(x=0,y=200)
b[7].place(x=100,y=200)
b[8].place(x=200,y=200)
f=player_title
while(True):
    if f==2:
        cm=cmove(ar)
        b[cm].destroy()
        board(ar,c)
        ch=check(ar)
        if ch==0:
            r="Tie"
            break
        elif ch==1:
            r="You lose"
            
            line=c.create_line(correct[0][0]*100+50,correct[0][1]*100+50,correct[2][0]*100+50,correct[2][1]*100+50,fill="red")
            break
            

    pmove(ar)
    
    b[i].destroy()    
    board(ar,c)
    ch=check(ar)
    if ch==0:
        r="Tie"
        break   
    elif ch==-1:
        r="You Win"
        line=c.create_line(correct[0][0]*100+50,correct[0][1]*100+50,correct[2][0]*100+50,correct[2][1]*100+50,fill="red")
        break
    f=2

label=tk.Label(c, text=r,height=1,width=10,bg="White")
label.place(x=0,y=300) 
c.pack()   
tk.mainloop()
