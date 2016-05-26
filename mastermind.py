# -*- coding: Latin-1 -*- 
from tkinter import*
import tkinter.messagebox
from math import *
from random import randrange


def play():
    "Launch a new game"	
    global NGood_pos, NBad_pos,CMP   
    NGood_pos,NBad_pos=0,0                                           
    combinaison()

def combinaison():
    "Function to generate a combinaison"
    global combin	
    combin=[randrange(1,nb_colors) for i in range(0,lengh_combi)] 

def mouseDown( event):
    "Mouse click function"
    global SelectObject,X,Y,color,color_chosen,click,figure,prop,propo
    canv.currObject=None  
    X,Y=event.x,event.y                                      
    click=1 

#pick a color 
    xCcol,yCcol=30,[130+50*i for i in range(0,nb_colors)]
    D=[hypot(X-xCcol,Y-yCcol[i]) for i in range(0,nb_colors)]
    for i in range(0,nb_colors): 
        if D[i]<r:
            SelectObject=Ccol[i]
            color=colors[i]
            figure=figures[i]
            canv.itemconfig(SelectObject,width=4)
            color_chosen=True

#display this color on the gaming zone
    xCgam,yCgam=[250+50*i for i in range(0,lengh_combi)],[130+50*j for j in range(0,max_propositions)]
    D2=[hypot(X-xCgam[i],Y-yCgam[j])for j in range(0,max_propositions)for i in range(0,lengh_combi)]
    for j in range(0,max_propositions):
        for i in range(0,lengh_combi):
            if D2[i+lengh_combi*j]<15: 
                SelectObject=Cgam[i+lengh_combi*j]
                if color_chosen==False :
                    SelectObject=None 
                if color_chosen==True :
                    canv.itemconfig(SelectObject,fill=color,width=4)
                    propo[i]=figure
                    p=propo.count(0)
                    if p==0:
                        prop=propo
                        canv.itemconfig(Arrow[j],fill="black")
                        if j<max_propositions-1: canv.itemconfig(Arrow[j+1],fill="white")
                        proposition()


def set_game():
    "Setting game"
    global Ccol,Cgam,Arrow,S,Trep,colors,click,figures,prop,propo,C1,C2
    global xCcol,yCcol,xCgam,yCgam,xTrep,yTrep,xS,yS

    click=0
    Reset.configure(state=NORMAL) 
    Play.configure(state=DISABLED)
    prop=[0]*lengh_combi
    propo=[0]*lengh_combi 
    canv.delete(ALL)
    canv.create_text(30,80,text='Colors',fill="white")
    canv.create_text(300,80,text='Gaming Zone',fill="white")
    canv.create_text(600,80,text='Answer Zone',fill="white")
    canv.create_text(300,690,text='Solution',fill="white")

    #Set up color zone
    canv.create_rectangle(10,100,50,150+50*(nb_colors-1),width=2,fill="white")

    #display colors
    colors=["yellow","red","green","blue","orange"]
    figures=[0]*len(colors)
    for i in range(0,len(colors)):figures[i]=colors.index(colors[i])+1
    xCcol,yCcol=30,[130+50*i for i in range(0,nb_colors)]
    Ccol=[canv.create_oval(xCcol-r,yCcol[i]-r,xCcol+r,yCcol[i]+r,width=2,fill=colors[i])for i in range(0,nb_colors)]

    #display gaming zone
    canv.create_rectangle(220,100,280+50*(lengh_combi-1),150+50*(max_propositions-1),width=2,fill="white")
    xCgam,yCgam=[250+50*i for i in range(0,lengh_combi)],[130+50*j for j in range(0,max_propositions)]
    Cgam=[canv.create_oval(xCgam[i]-r,yCgam[j]-r,xCgam[i]+r,yCgam[j]+r,width=2,fill="grey")for j in range(0,max_propositions)for i in range(0,lengh_combi)]
    Arrow=[canv.create_polygon(120,yCgam[j]-r/8,180,yCgam[j]-r/8,180,yCgam[j]-r/2,190,yCgam[j],180,yCgam[j]+r/2,180,yCgam[j]+r/8,120,yCgam[j]+r/8,width=0,fill="black")for j in range(0,max_propositions)]
    canv.itemconfig(Arrow[0],fill="white")

    #display answer zone
    canv.create_rectangle(550,100,575+20*(lengh_combi-1),150+50*(max_propositions-1),width=2,fill="white")
    xTrep,yTrep=[560+20*i for i in range(0,lengh_combi)],[130+50*j for j in range(0,max_propositions)]
    Trep=[canv.create_rectangle(xTrep[i],yTrep[j]-r,xTrep[i]+5,yTrep[j]+r,width=1,fill="grey",outline="black")for j in range(0,max_propositions)for i in range(0,lengh_combi)] 

    #display solution zone
    canv.create_rectangle(220,625,280+50*(lengh_combi-1),675,width=2,fill="white")
    xS,yS=[250+50*i for i in range(0,lengh_combi)],650
    S=[canv.create_oval(xS[i]-r,yS-r,xS[i]+r,yS+r,width=2,fill="grey")for i in range(0,lengh_combi)]

    information.config(text=text2)
    play()

def mouseUp( event):
    "Mouse click function 2"
    global SelectObject,click
    if click==1:
        canv.itemconfig(SelectObject,width=2)
    if click==0:
        SelectObject=None

def proposition():
    "Function to make a proposition"
    global CMP
    CMP=CMP+1
    VerifPos()


def VerifPos(): 
    "Function to verifie the combinaison"
    global Bad_pos,Good_pos,NGood_pos, NBad_pos,NG,CMP,C1,C2,s 
    for i in range(1,nb_colors+1):
            Bad_pos,Good_pos=0,0 
            for j in range(0,lengh_combi): 
                if prop[j]==i and combin[j]==i:
                    Bad_pos=Bad_pos+1
            NGood_pos=NGood_pos+Bad_pos
            if combin.count(i)>=prop.count(i):
                Good_pos=prop.count(i)-Bad_pos 
            else: 
                Good_pos=combin.count(i)-Bad_pos 	
            NBad_pos=NBad_pos+Good_pos
            for k in  range(0,NGood_pos):canv.itemconfig(Trep[k+lengh_combi*(CMP-1)],fill="green")
            for k in  range(0,NBad_pos):canv.itemconfig(Trep[k+NGood_pos+lengh_combi*(CMP-1)],fill="orange")
            for k in  range(0,lengh_combi-NGood_pos-NBad_pos):canv.itemconfig(Trep[k+NGood_pos+NBad_pos+lengh_combi*(CMP-1)],fill="red")
    if NGood_pos==lengh_combi:
            information.config(text=text3)
            Replay.configure(state=NORMAL)
            Reset.configure(state=DISABLED)
            canv.itemconfig(Arrow[CMP],fill="black")
            s=s+CMP 
            CMP=0
    else:
            information.config(text=text4)
            for j in range(0,lengh_combi): prop[j]=0
            NGood_pos,NBad_pos=0,0
            if CMP==max_propositions: 
                information.config(text=text5)
                Replay.configure(state=NORMAL)
                Reset.configure(state=DISABLED)
                s=s+CMP
                NGood_pos,NBad_pos=0,0
                CMP=0
              


def quit(): 
    " Leave the game " 
    ans=tkinter.messagebox.askokcancel('MASTERMIND',"Do you really want to quit ?") 
    if ans:root.quit()


def Replay():
    "Start a new game"
    global RA,RB,RC,RD,FF,CMP,NG,s
    Replay.configure(state=DISABLED)
    Reset.configure(state=DISABLED)
    Play.configure(state=NORMAL)
    information.config(text=text1)
    s=0
    CMP,NG=0,0
    C1[0],C1[1],C2=0,0,0
    RPG.config(text='%s'%C1[0]);RPP.config(text='%s'%C1[1])
    color_chosen=False
    canv.delete(ALL)
    RA.set(nb_colors);RB.set(lengh_combi);RC.set(max_propositions);RD.set(total_games)
    show_hide_choice.set(level[0]) 


def Reset():
    "Reset game" 
    global CMP
    Reset.configure(state=NORMAL)
    Play.configure(state=DISABLED)
    information.config(text=text2)
    CMP=0
    for j in range(0,max_propositions):
        for i in range(0,lengh_combi):
            canv.itemconfig(Cgam[i+lengh_combi*j],fill="grey")
            canv.itemconfig(Trep[i+lengh_combi*j],fill="grey")
    for i in range(0,lengh_combi):
        canv.itemconfig(S[i],fill="grey")
    color_chosen=False
    show_hide_choice.set(level[0]) 
    play()
    set_game()



def rules(): 
    "Rules" 
    msg =Toplevel() 
    Message(msg, bg ="black", fg ="white", width =500,font ="Arial 10", 
        text='''What you have to do\n
        (Please follow instructions in blocks on the right side) \n
        1. Click on the button <Play> \n            
        2. Try a combinaison with colors proposed :
            - Computer generate a combinaison
            - Click on a color and then on a spot to place it
            - Place colors on the line selected by the white arrow
            - This one can be revealed with solution button \n
        3. Your combinaison get verified :
            - If a color is well placed, you get a green marker
            - If a color is not in the combinaison, you get a red marker
            - If a color is not on the good spot, you get an orange marker \n
        4. At the end of a game, you can start a new one by clicking on the
        <Replay> button''').pack(padx =10, pady =10) 

  

def makemenu(win):
    "Menu toolbar"
    top=Menu(win)
    win.config(menu=top)
    R=Menu(top)
    top.add_cascade(label='Rules',menu=R,underline=0)
    R.add_command(label='How to Play',command=rules,underline=0)
    Q=Menu(top)
    top.add_cascade(label='Quit',menu=Q,underline=0)
    Q.add_command(label='Quit the game',command=quit,underline=0)


def show_hide(): 
    " Show or Hide the solution" 
    global S,N
    if switch==1: 
        N=show_hide_choice.get()
        if N==1:
            for i in range(0,lengh_combi):
                canv.itemconfig(S[i],fill="grey")
            show_hide_choice.set(level[0]) 
        if N==2: 
            for i in range(0,lengh_combi):
                canv.itemconfig(S[i],fill=colors[ combin[i]-1]) 
            show_hide_choice.set(level[1]) 


 

##############################################################  MAIN PROGRAM  ####################################################################################### 

root=Tk()
root.title(' MASTERMIND ') 
makemenu(root)

#initialize game
click=0
total_games=1
max_propositions=10
lengh_combi=5
nb_colors=5
color_chosen=False
r=15
CMP=0 
Bad_pos,Good_pos=0,0                                                                                    
NGood_pos,NBad_pos=0,0                                                                                         
C1=[0,0] 
C2=0 
NG=0 
s=0 
switch=1 

# Canvas 1
canv=Canvas(root,height=750,width=820, bg='black') 
canv.grid(row=1,column=0)

# Canvas2
canv2=Canvas(root,height=810,width=200, bg='grey20') 
canv2.grid(row=1,column=1) 
SelectObject=canv2

# Mouse comands
root.bind("<Button-1>", mouseDown)
root.bind("<Button1-ButtonRelease>", mouseUp)

#Setting buttons
Reset=Button(canv2,text='Reset',height=1,width=35,relief=GROOVE,bg="white",command=Reset)
Reset.pack(padx=5,pady=2,side =BOTTOM,anchor=SW)
Reset.configure(state=DISABLED) 
Replay=Button(canv2,text='New Game',height=1,width=35,relief=GROOVE,bg="white",command=Replay)
Replay.pack(padx=5,pady=2,side =BOTTOM,anchor=SW)
Replay.configure(state=DISABLED) 
Play=Button(canv2,text='Play',height=1,width=35,relief=GROOVE,bg="white",command=set_game)
Play.pack(padx=5,pady=2,side =BOTTOM,anchor=SW)
Play.configure(state=NORMAL) 

#Instruction (on the right block)
text1="Thanks to play our MASTERMIND !\n\n Please click on the <Play> button\n to play a new game"
text2="The computer has generated a combinaison.\nFind the combinaison\n \n Please play on the line shown by the white \n arrow."
text3="Well played, you won the game ! \nClick on <New Game> \nto start a new one."
text4="Your combinaison does not fit !\nTry a new one\n(on the next line)"
text5="You have lost this game !\nClick on <New Game>\nto start a new one."
information=Label(canv2,text=text1,height=21,width=36,bg="grey20",fg="white",command=None)
information.pack(padx=5,pady=5,side=BOTTOM,anchor=SW)

# Show/Hide solution
Label(canv2,text='''Hide or Show the solution''',fg='white',bg='grey20').pack(padx=5,pady=1,side=BOTTOM) 
level=["1","2"] 
show_hide_choice=IntVar() 
show_hide_choice.set(level[0]) 
for i in range(0,2): 
    rad=Radiobutton(canv2,variable=show_hide_choice,value=level[i],command=show_hide) 
    rad.pack(padx=20,ipadx=20,pady=5,side=LEFT) 

root.config(bg="grey20") 
root.mainloop()
root.destroy() 