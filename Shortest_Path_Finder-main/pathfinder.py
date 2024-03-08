#All the Imports
import turtle as tl
import tkinter.messagebox as tmsg
import numpy as np
import random


class BFS:
	def __init__(self,a,b):
		self.x = a
		self.y = b
		self.n = self.x*self.y 
		self.matrix = np.zeros((self.n, self.n))
	
	def adjacency(self, prohibited):
		for i in range(self.n):
			if i not in prohibited:
				for j in range(self.n):
					if j==i+self.x or j==i-self.x:
						self.matrix[i][j] = 1
					if i%self.x==0:
						if j==i+1:
							self.matrix[i][j] = 1
					elif (i+1)%self.x==0:
						if j==i-1:
							self.matrix[i][j] = 1			
					else:
						if j==i+1 or j==i-1:
							self.matrix[i][j] = 1	
	def calculate_distance(self ,m, n):
		self.visited = np.zeros(self.n)
		self.parent = np.zeros(self.n)
		self.visited[m] =1
		self.queue =[]
		self.queue.append(m)
		while len(self.queue)>0:
			a = self.queue[0]
			self.queue.remove(a)
			for i in range(self.n):
				#If the condition is true, a becomes the parent of node i , and node i is marked as visited, and it is added to queue.
				if self.matrix[a][i]==1 and self.visited[i]==0:
					self.parent[i]= a
					self.visited[i]= 1
					self.queue.append(i)
					if i==n:
						self.queue=[]
						break
		if i!=n:    #If the current node i is the destination node n, then queue is cleared, and the loop is terminated.
			return				
		self.traversed =[]
		p=int(self.parent[n])
		self.traversed.append(p)
		while(p!=m):   #Once the destination node n is found, then code starts moving backward,checking each node's parent until it reaches the starting node m 
			p = int(self.parent[p])
			if p==m:
				break
			self.traversed.append(p)

		
class Body:
	def __init__(self):
		#These lines set the width and height of the window or screen to 1000 pixels and 700 pixels, respectively.
		self.width = 1000   
		self.height = 700
  
		#creates a turtle graphics screen object using the Screen()
		self.screen =tl.Screen()
  
		#sets dimensions of screen using previously defined width and height.
		self.screen.setup(self.width, self.height)
		self.screen.title("Finding the shortest path between two points.")
		self.screen.bgcolor("white")
  
		#current position of the turtle or object on the screen.
		self.x=0
		self.y=0
  
		# controls whether the main loop of the program should continue running.
		self.run =True
	
		#self.dx and self.dy represent the change in position (delta x and delta y) for each step taken by the turtle.
		self.dx = 48  #48 units horizontally
		self.dy =20	  #20 units vertically
		self.step = 20 #distance the turtle will move in each step.
		
  		#By setting self.cx to -470 and self.cy to 110, the turtle's starting position is adjusted to a specific location on the screen.
		self.cy = 110
		self.cx = -470

		#List to store points that are prohibited or restricted from traversing 
		self.prohibited=[]
  
		#List to store the shortest path found between two points
		self.rs =[]
		self.write() #used to write information on screen
		self.grid()	 #to create grid
		self.allow = True
		#self.main()
		self.hs =[]
  
		# to store the index of the starting point & end point in the program.
		self.start_pt = 0
		self.end_pt = 959

		#to indicate whether the starting point has been set or not
		self.start = True
		self.end =False
  
		#to indicate whether hurdles or obstacles are present or not
		self.hurdles =False		
		self.listen_mouse_clicks()
		
  		# to keep the program running and responsive, allowing it to handle user interactions and update the screen as necessary.
		self.screen.mainloop()	
		

	def main(self):
		b= BFS(self.dx,self.dy)
		b.adjacency(self.prohibited)
		try:
			b.calculate_distance(self.start_pt,self.end_pt)
			for i in self.rs:
				i.goto(1000,1000)
			self.rs.clear()
			for i in b.traversed:
				self.draw_point(i)
		except:
			tmsg.showinfo("Not Found","No path found between between the start and the end points")		

		
	def draw_point(self ,n):
		#creates a new turtle object named self.block
		self.block = tl.Turtle()
		#pen up from the drawing surface, so no drawing will occur 
		self.block.penup()
		self.block.shape("circle")#square to change shape (It is shape of drawing points during traversal)
		self.block.color("black") # The color of points is set to the black.
		self.block.speed(0)       #speed is set to 0 to move turtle instantly
		self.block.goto(self.cx+20*(n%self.dx),self.cy-20*(n//self.dx))	
		self.rs.append(self.block) #stores references to all the turtle objects representing points drawn on the screen.

	#To initialize start point
	#After starting the drawing we cannot add end point and hurdles in program during ongoing pathfinding process hence end & hurdles set to false 
	def draw_start(self):
		self.start=True  #flag to indicate that user is expected to select a starting point
		self.end = False  
		self.hurdles=False 

	#To initialize the end point.
	def draw_end(self):
		self.start=False
		self.end = True #flag to indicate that user is expected to select a ending point
		self.hurdles=False

	#Used to Draw hurdles.
	def draw_hurdles(self):
		self.start=False
		self.end = False
		self.hurdles=True#flag to indicate that user is expected to select a hurdles
  
  #instructions are displayed in an organized way by making them easy for the user to read and follow.
	def write(self):
		self.pen = tl.Turtle()
		self.pen.penup()
		self.pen.hideturtle()
		self.pen.speed(0)
		self.pen.color("black")
		self.pen.goto(-480,300)
		self.pen.write("Shortest Path Finder",False,align="left",font=("arial",20,"bold"))	#False indicates text should not be underlined
		self.pen.goto(-480,270)
		self.pen.write("Instructions:",False,align="left",font=("arial",15,"bold"))	
		self.pen.goto(-480,250)
		self.pen.write("a) Press 's' in the keyboard and click anywhere on grid to place the starting point.(color: green)",False,align="left",font=("arial",10,"bold"))	
		self.pen.goto(-480,230)
		self.pen.write("b) Press 'e' in the keyboard and click anywhere on grid to place the ending point.(color:blue)",False,align="left",font=("arial",10,"bold"))	
		self.pen.goto(-480,210)
		self.pen.write("c) Press 'h' in the keyboard and click anywhere on grid to place the hurdles.(color: red)",False,align="left",font=("arial",10,"bold"))
		self.pen.goto(-480,190)
		self.pen.write("d) Press 'r' in the keyboard to place some random hurdles on the grid.",False,align="left",font=("arial",10,"bold"))
		self.pen.goto(-480,170)
		self.pen.write("e) Press 'space bar' in the keyboard to see the shortest path(colored in black)",False,align="left",font=("arial",10,"bold"))
		self.pen.goto(-480,150)
		self.pen.write("f) Press 'o' in the keyboard to clear the grid.",False,align="left",font=("arial",10,"bold"))

		#draw_squares takes the mouse click coordinates (x and y) and finds the corresponding grid cell coordinates (xcor and ycor).
		def draw_squares(self,x,y):
			xcor =None
			ycor =None

			#loops over the possible x-coordinates on the grid and checks if the mouse click falls within a specific range or not
			for i in range(self.dx):
				if x<(self.cx+20*i)+10 and x>(self.cx+20*i)-10:
					xcor= self.cx+20*i  #If the mouse click is within the range, it sets the xcor to the center of that grid cell
					break
					
			#loops over the possible y-coordinates on the grid and checks if the mouse click falls within a specific range 
			for j in range(self.dy):
				if y<(self.cy-20*j)+10 and y>(self.cy-20*j)-10:
					ycor= self.cy-20*j #If the mouse click is within the range, it sets the ycor to the center of that grid cell
					break
 
			#If the self.hurdles flag is set and valid grid coordinates are found:
			if self.hurdles:		
				if xcor and ycor:	
					loc =j*self.dx + i   #calculates location of obstacle. 
					self.prohibited.append(loc)	 #Adds the obstacle location to the list of prohibited locations
					self.t = tl.Turtle()
					self.t.penup()
					self.t.shape("circle")
					self.t.color("pink")
					self.t.speed(-1)  #slowest speed 
					self.t.goto(xcor,ycor)
					self.hs.append(self.t)
     
			#If the self.start flag is set and valid grid coordinates are found
			if self.start:
				if xcor and ycor:	
					self.start_pt =j*self.dx + i   # calculates the location of the starting point 
					try:
						self.st.goto(xcor,ycor)
					
     				#If no turtle object exists, it creates one, sets its appearance to green square
					except:	
						self.st = tl.Turtle()
						self.st.penup()
						self.st.shape("square")
						self.st.color("green")
						self.st.speed(-1)
						self.st.goto(xcor,ycor)
      
			#If the self.end flag is set and valid grid coordinates are found:
			if self.end:
				if xcor and ycor:	
					self.end_pt = j*self.dx + i   #calculates the location of the ending point
					try:
						self.et.goto(xcor,ycor)
      
					#If no turtle object exists, it creates one, sets it to blue square.
					except:	
						self.et = tl.Turtle()
						self.et.penup()
						self.et.shape("square")
						self.et.color("blue")
						self.et.speed(-1)
						self.et.goto(xcor,ycor)	
	
 	
	def erase_all(self):
		try:
			#These lines move the turtle objects starting point (self.st) and the ending point (self.et) to coordinates (1000, 1000)
			self.st.goto(1000,1000)
			self.et.goto(1000,1000)
			
   			#self.hs, which presumably contains obstacles or hurdles.
			for i in self.hs:
				i.goto(1000,1000)
			self.hs = []
			self.prohibited=[]	
			for i in self.rs:
				i.goto(1000,1000)
			self.rs = []			
		except:
			pass

	
	def random_hurdles(self):
		if self.allow:    						#used to ensure that obstacles are generated only when allowed
			for i in range(100):   				#This loop iterates 100 times, generating 100 random obstacles.
				loc = random.randint(0,959)		#random locations
				self.prohibited.append(loc)	    #This adds the randomly generated location to the list prohibited
				self.t = tl.Turtle()
				self.t.penup()
				self.t.shape("square")
				self.t.color("red")
				self.t.speed(-1)
				self.t.goto(self.cx+20*(loc%self.dx),self.cy-20*(loc//self.dx))	
				self.hs.append(self.t)	
				self.allow =False				
		self.allow =True	

		
	def listen_mouse_clicks(self):
		#Without this line, the screen would not respond to any user input.
		self.screen.listen()
  
		#When the screen detects a mouse click, it calls the draw_squares method, which handles drawing objects at particular cell
		self.screen.onclick(self.draw_squares)
  
		self.screen.onkeypress(self.main,"space")
		self.screen.onkeypress(self.draw_start,"s")
		self.screen.onkeypress(self.draw_end,"e")  # when e is pressed calls draw_end method
		self.screen.onkeypress(self.draw_hurdles,"h")
		self.screen.onkeypress(self.erase_all,"o")
		self.screen.onkeypress(self.random_hurdles,"r")

		

	def grid(self):
		#creates self.g object with black colour 
		self.g = tl.Turtle()
		self.g.color("black") 
		self.g.hideturtle()
		self.g.speed(-1)
		for i in range(21): #Grid contains 21 horizontal lines
			self.g.penup()
			self.g.goto(-480,+120-(20*i))
			self.g.pendown()
			self.g.forward(480*2)	
		for i in range(49): #Grid contains 49 vertical lines.
			self.g.penup()
			self.g.setheading(-90)
			self.g.goto(-480+20*i,+120)
			self.g.pendown()
			self.g.forward(400)		
		

if __name__=="__main__":
	b =Body()
