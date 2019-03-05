from tkinter import *
import tkinter.messagebox
import random
import time

tk = Tk()
tk.title("Bounce!")

#This is used so that the window cannot be resized and the frame is fix
tk.resizable(0, 0)

#it places the window in front of the other windows
tk.wm_attributes("-topmost",1)

#Initializing the Canvas with no border and no highlightthickness
canvas = Canvas(tk, width = 500, height = 500,  bd = 0, highlightthickness = 0) 

canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)
        start = [-3, -2, -1, 0, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.hit_bottom = False
        
 #here the self.y is -1 so that the ball will go upwards and the user will have the time to react
        self.y = -1
        self.canvas.height = self.canvas.winfo_height()
        self.canvas.width =  self.canvas.winfo_width()
#Initially the ball will move in direction in y= -1 but when the ball moves, the value of the 
#self.id y coordinates changes and to control when it goes out of window we change the direction
#of the ball from y=-1 to y=+1

# This is the reason why we are using pos 
#In the draw we are creating constraints and make sure that the ball does not move out of the window
 
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        
        #the first if statement checks whether the ball is in the column of the paddle
        #in the second if statement we are checking whether the ball touched the paddle or not
        #the first statement doesn't check whether the ball touches the paddle or not.
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False
               
#this will move the ball upwards so we are
#using -1 for y axis(0,0) is the initial location of the ball
# and it will in the directior of given x and y coordinates    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        #the .coords returns an array with x1,y1,x2,y2
        #x1 and y1 are the initial coordinates and x2 and y2 are the final coordinates 
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas.height:
            self.hit_bottom = True
            canvas.create_text(245,100,text = 'Game Over')
            tkinter.messagebox.showinfo("Oops!", "Game Over.")
        if pos[0] <= 0:
            self.x =3
        if pos[2] >= self.canvas.width:
            self.x = -3
        if self.hit_paddle(pos) == True:
            self.y = -3

class  Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 200, 400)

#We are using self.x = -1 so. initially the paddle will move in negative x direction        
        self.x = 0
        self.canvas.width = self.canvas.winfo_width()
        
#the bind_all is used to use the keys to move the paddle        
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas.width:
            self.x = 0
    
    def turn_left(self,evt):
        self.x = -2
        
    def turn_right(self,evt):
        self.x = 2

paddle = Paddle(canvas, 'green')    
ball = Ball(canvas, paddle, 'red')
#It will redraw the screen again and again as the ball moves.
while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)       #the smaller the is, the faster the speed of ball is

    else:
        break 

#Always remember to write tk.mainloop() at the end of tkinter program otherwise the window will not be visible
tk.mainloop()