from tkinter import *
import random 
import time
import tkinter.messagebox
 
score_1 = 0
score_2 = 0

tk = Tk()
tk.title("Pong!")
tk.resizable(0, 0)
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0 ,highlightthickness = 0)
canvas.pack()

#To change the background color
canvas.config( bg='black')
tk.update()

#here we are creating al line in the center 
# we are writing x1 y1 x2 y2 
#the line should go from x1 y1 to x2 y2
canvas.create_line(250, 0, 250, 400, fill = 'blue')

class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):
        self.canvas = canvas

#for creating the two paddles
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        
#creating the canvas        
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 233, 190)

#initializing the initial direction of the ball
        startx = [-3, -2, -1, 1, 2, 3]
        starty = [-3, -2, -1, 1, 2, 3]
        
#Initializing the hit bottom part
        self.hit_bottom1 = False
        self.hit_bottom2 = False
        
        random.shuffle(startx)
        random.shuffle(starty)
        
#It will decide the initial drirection of the movement of the ball        
        self.x = startx[0]
        self.y = starty[0]
        
        self.canvas.height = self.canvas.winfo_height()
        self.canvas.width = self.canvas.winfo_width()
               
#Initializing when the ball hit the paddle 1 it should return back         
    def hit_paddle1(self, pos):
        paddle1_pos = self.canvas.coords(self.paddle1.id)
        if pos[1] >=  paddle1_pos[1] and pos[1] <= paddle1_pos[3]:
            if pos[0] >= paddle1_pos[0] and pos[0] <=  paddle1_pos[2]:
                return True
            return False
        
#Initializing when the ball hit the paddle 2 the ball should return back        
    def hit_paddle2(self, pos):
        paddle2_pos = self.canvas.coords(self.paddle2.id)
        if pos[1] <=  paddle2_pos[3] and pos[3] >= paddle2_pos[1]:
            if pos[0] <= paddle2_pos[2] and pos[2] >=  paddle2_pos[0]:
                return True
            return False
        
#the main function to check what to do when the ball misses the paddle or strike the paddle        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas.height:
            self.y = -3 
        if pos[0] <=0:
            self.x = 3
            self.score(False)
            self.hit_bottom1 = True
        if pos[2] >=self.canvas.width:
            self.x = -3
            self.score(True)
            self.hit_bottom1 = True
            
 #while using the functions defined in a class 
 # ans when you are using them use self.func_name()  (most important)
            
        if self.hit_paddle1(pos) == True:
            self.x = 3 
        if self.hit_paddle2(pos) == True:
            self.x= -3
     
#Keeping track of the score and checking when the score of the first player increases and when the second player scores        
    def score(self, val):
        global score_1 
        global score_2
        if val == True:
                a = self.canvas.create_text(125, 40, text = score_1, font = ('Arial', 60), fill = 'white')
                canvas.itemconfig(a, fill = 'black')
                score_1 += 1
                a = self.canvas.create_text(125, 40, text = score_1, font = ('Arial', 60), fill = 'white')
             
        if val == False:
                a = self.canvas.create_text(325, 40, text = score_2, font = ('Arial', 60), fill = 'white')
                canvas.itemconfig(a, fill = 'black')
                score_2 += 1
                a = self.canvas.create_text(325, 40, text = score_2, font = ('Arial', 60), fill = 'white')   
 
class Paddle1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 10, 80, fill = color)
        self.canvas.move(self.id, 5, 150)
    
    #Initally self.y = 0 so that the paddle doesn't move right now        
        self.y = 0
        
        self.canvas.height = self.canvas.winfo_height()
        self.canvas.width = self.canvas.winfo_width()

     #bind_all is used to bind the keys with their actions           
        self.canvas.bind_all('w', self.turn_up)
        self.canvas.bind_all('s', self.turn_down)
    
    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas.height:
            self.y = -3

    def turn_up(self, evt):
        self.y = -3
    def turn_down(self, evt):
        self.y = 3


class Paddle2:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 10, 80, fill = color)
        self.canvas.move(self.id, 485, 150)
        
    #Initally self.y = 0 so that the paddle doesn't move right now    
        self.y = 0
       
        self.canvas.height = self.canvas.winfo_height()
        self.canvas.width = self.canvas.winfo_width()
     
     #bind_all is used to bind the keys with their actions   
        self.canvas.bind_all('5', self.turn_up)
        self.canvas.bind_all('2', self.turn_down)
    
    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas.height:
            self.y = -3
        
    #trun_up and turn_down are for controlling thr direction of the ball using the keys    
    def turn_up(self, evt):
        self.y = -3
    def turn_down(self, evt):
        self.y = 3        
        
        
#Creating the objects Ball, Paddle1 and Paddle 2        
paddle1 = Paddle1(canvas, 'white')
paddle2 = Paddle2(canvas, 'grey')
ball =  Ball(canvas, paddle1, paddle2, 'orange')

#This loop will take care that the game never ends
while 1:
    ball.draw()
    paddle1.draw()
    paddle2.draw()
    
    if score_1 == 10:
        ball.x = 0
        ball.y = 0
        paddle1.y = 0
        paddle2.y = 0
        canvas.create_text(250, 200, text = "Congrats White Player!, You win", font = 32, fill = 'red' )
        canvas.create_text(250, 215, text = "Score: " + str(score_1) + ' - ' + str(score_2), font = 32, fill = 'red') 
        tkinter.messagebox.showinfo("Gamer over", "White Wins!!")
    
    if score_2 == 10:
        ball.x = 0
        ball.y = 0
        paddle1.y = 0
        paddle2.y = 0
        canvas.create_text(250, 200, text = "Congrats Grey Player!, You win", font = 32, fill = 'red' )
        canvas.create_text(250, 215, text = "Score: " + str(score_1) + ' - ' + str(score_2), font = 32, fill = 'red') 
        tkinter.messagebox.showinfo("Gamer over", "Grey Wins!!")
        
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)   
    
    if score_1 == 10 or score_2 == 10:
        time.sleep(10000)

tk.mainloop()
