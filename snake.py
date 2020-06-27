# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 11:41:18 2020

@author: Saurabh
"""
from tkinter import *
import random

size=300
black_box="000000"

class mov_tiles():
    def __init__(self):
        self.window = Tk()
        self.window.title("Snake")
        self.canvas = Canvas(self.window , width = size , height= size)
        self.snake = self.canvas.create_rectangle(0, 0 ,15, 15, fill='Black')
        self.coordinates= []
        #self.coord = [i*15 for i in range(0,len(20))]
        self.apple =self.canvas.create_rectangle(self.apple_coordinates(0, 285, 2) , fill ='Red')
        self.canvas.pack()
        #self.window.resizable(0,0)
        self.x = 0
        self.y = 0
        self.count = 0
        self.my_rectangles=[]
        self.my_variables=[self.canvas.coords(self.snake)]
        self.flag = 10
        
        self.window.bind('<KeyPress-Left>' ,  self.left)
        self.window.bind('<KeyPress-Right>' , self.right)
        self.window.bind('<KeyPress-Up>' ,  self.up)
        self.window.bind('<KeyPress-Down>' , self.down)
        
        self.initialize_grid()
        
        play = Button(self.window, text="Play", command=self.initialize_game)
        play.pack()
        
    def mainloop(self):
        self.window.mainloop()
        
    # ---------------------------------------    
    # Initialization Functions
    # ---------------------------------------
        
    def initialize_grid(self):
        for i in range(0, 19):
            self.canvas.create_line((i+1)*15, 0, (i+1)*15, 300)
        
        for i in range(0, 19):
            self.canvas.create_line(0, (i+1)*15, 300, (i+1)*15)
        
    def apple_coordinates(self, start, end, step):
        for i in range(step):
            self.coordinates.append((random.randint(start,end)//15)*15)
        
        self.coordinates.extend((self.coordinates[0] + 15, self.coordinates[1] + 15))
        return self.coordinates
        
    
    # ---------------------------------------
    # Game Play Function
    #----------------------------------------
    #get apple coordinates if encountered change coordinates of snake

    def initialize_game(self):
        a, b, c, d = self.canvas.coords(self.snake)
        self.update_snake()
        if ((a < 300 and c > 0) and (b < 300 and d > 0)):
            #print("in this")
            self.canvas.move(self.snake, self.x, self.y)
            if self.count > 0:
                if self.canvas.coords(self.snake) in self.my_variables:
                    self.end_game()
                else :
                    self.my_variables.clear()
                    self.my_variables.append([a, b, c ,d])
                    for i in range(self.count):
                        self.move_rect(i)
            self.canvas.after(50, self.initialize_game)
        else :
            self.end_game()
        #self.check_intersection()
        
    def update_snake(self):
        if  ( self.canvas.coords(self.snake) == self.coordinates):
            self.coordinates.clear()
            self.count += 1
            self.my_rectangles.append(self.canvas.create_rectangle(0, 0, 0, 0,fill='Black'))
            #for i in range(len(self.snake_body)):
            #    self.canvas.coords(self.temp_rect)
            self.canvas.coords(self.apple, self.apple_coordinates(0, 285, 2))
            
    def move_rect(self, i):
        self.my_variables.append(self.canvas.coords(self.my_rectangles[i]))
        self.canvas.coords(self.my_rectangles[i], self.my_variables[i])
        
    def end_game(self):
        label = Label(self.canvas, text="GAME OVER")
        label.pack()
    
    def left(self,event):
        if not self.flag == 0 :
            self.x=-15
            self.y= 0
            self.flag = 0

    def right(self,event):
        if not self.flag == 0:
            self.x = 15
            self.y = 0
            self.flag = 0
        
    def up(self,event):
        if not self.flag == 1:
            self.x= 0
            self.y=-15
            self.flag = 1
        
    def down(self,event):
        if not self.flag == 1:
            self.x=0
            self.y=15
            self.flag = 1
            
game=mov_tiles()
game.mainloop()