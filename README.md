# Conway's Game Of Life
Demo Video: <https://www.youtube.com/watch?v=t30rUXlpwZA>


Conway's game of life is a cellular automata invented by John Horton Conway. Its premise is fairly simple. There are cells on a grid that are affected by rules that decide whether it lives or dies, those two states being its only. Now, despite it seeming quite simple, Conway’s Game of life is famed for its complexity, and is seen as one of the more interesting mathematical and logical experiments invented. I have coded a rendition of Conway’s game of life, and will be detailing it in the coming paragraphs.


# The maths behind it


Before I begin to talk about my actual code, I will go in depth with the actual math of Conway’s game of life. Conway's game of life has four very simple rules.
 
Rule #1 - if there are less than two living cells around (around being a direct neighbor to any given cell, that cell will die.
Rule #2 - If there are two living cells around any given cell, and that cell is currently living, it survives.
Rule #3 - If there are three living cells around any given cell, regardless of the state it survives. This means a dead cell becomes a living one, and a living one stays alive.
Rule #4 - If there are more than 3 living cells around any cell it dies.


Now, mathematically, these rules are fairly basic. For each “step” in the simulator, the rules are applied to all cells, and they update and evolve because of that. Due to the simplicity of the rules, they aren't all that challenging to port into code. In my cgol.py file, I have a function called conwayslife. Below are its contents


```
for x in range(dim):
        for y in range(dim):
            count = g.count_neighbours(x, y, dim)
            if count < 2:
                newgrid.set(x, y, 0)
            if count == 2 and g.get(x, y) == 1:
                newgrid.set(x, y, 1)
            if count == 3:
                newgrid.set(x, y, 1)
            if count > 3:
                newgrid.set(x, y, 0)
```
As you can see, this code is fairly simple, and is the innermost workings of my program. For context, dim is the grid side dimension, considering its a square. What's truly fascinating, however, is the degree of complexity that can be derived from these simple rules. There is one video by Philip Bradbury on Youtube that I think perfectly shows this. 
https://youtu.be/xP5-iIeKXE8?si=sDXKXkCrovsNnCv_


# My code and how it works


### The inner workings 


In this section, we will be looking at the more technical part of the code, contained within cgol.py. For the most part, this code relates to the grid and manipulation of it, but in some cases it thinks less of the grid, and more of the user's view of it.


One of the major design choices I made early on was whether to use a dictionary or list to store my cells. I started out with a list, but changed to using a dict later on due to it generally making more sense. It let me have far looser boundaries for the grid, and would only store live cells, dead cells not being worth storing. To put it fairly simply, it's just more flexible, easier to manipulate, and uses less memory. Inside cgol.py is where I manage all things related to the grid. Insertion of cells, deletion of cells, randomising and clearing cells

Another interesting feature in cgol.py is the view class. The view and grid are separate entities, with the grid being the entire simulation space and the view being the observable simulation space. The view supports things like zooming in and out and panning the view across the grid. 


### The ui


The file responsible for the actual user interface is called cgol_ui.py. In the next few paragraphs, I will be detailing its code as well as a few UI choices I made while writing it. While cgol_ui.py is longer, its focus is mainly on the display of the program and making it look nice. There are a few interesting concepts implemented, one of which I will get to momentarily, but the majority of it is just pygame code. I will briefly go through what cgol_ui does.


The visuals of the code are run by cgol_ui.py, with it actually making the visual representation for the grid. While the code in cgol is the actual functionality of the simulation, it's only really maths. Now, that's where cgol_ui comes in. It gives a clear and concise visual representation of the output of cgol, whilst also giving the user to visually manipulate it.


The code in cgol_ui could best be considered a front page of the code, with just about everything leading into it, and being used in it. A few of the stand out features of it, however, are the commands. Especially zoom, pan, and copy. Zoom and pan are actually what utilise view in cgol, and were probably the trickiest commands to code. One of the bugs I ran into while coding them was that the sides of the grid elongated and the proportions were all off. I eventually found it was due to one line of code.


```
self.view_size = math.round(max(min(self.view_size * f, grid_size), 1))
```


The bug was due to the fact that when I was rounding, I would marginally throw the proportion off, and that would result in a butterfly effect where my entire grid would be out of proportion. The fix, however, was simple.


```
self.view_size = math.ceil(max(min(self.view_size * f, grid_size), 1))
```


With that small change, the zooming worked properly. 


### Plaintext


Now I will go into a brief side tangent on the copy command in cgol_ui. It works by reading a file with a pattern depicted on it via the serialisation format. This is the standard way to represent conway's game of life patterns represented with text. For further reading: https://conwaylife.com/wiki/plaintext. While this is a fairly short article, it explains the format well enough. The formula for such files are as such:


!Name: Glider
!
.0.
..0
000


As you can see here, zeroes are used to depict live cells and full stops to depict dead. 


The plaintext.py file is what interprets the normal plaintext files, and puts them on screen as actual cells. How it does this is that it iterates over each line, ignoring it if it starts with “!”, and interpreting it if it doesn't. It takes the line, adds a live cell if the character is 0, and just ignores anything else.


Now, the nice thing about having a piece of code that can read these serialised files is that it's really not all that tricky to just copy paste more patterns in. While at this point, one would have to delve into the code a little bit to change what files are being printed, one of the features that are higher up on my TODO list is a patterns library, where you can just select a pattern and it prints to screen. 


The final piece of code we will look at is guide.py. Simply put, this just handles the text of the menu and the box menu goes in.


### A guide to using my program


There are a few commands to edit the board, the guide for said commands being accessible by left clicking the question mark icon.


Left click on cell - Turns cell on/off depending on prior state
Right click - Copies pattern to screen. Currently only gosper glider gun - better pattern copying will be implemented later
Space bar - Pause/Unpause simulation
E - Move single step in simulation
F - Clear grid entirely
R - Randomise grid entirely
WASD - Move up, left, down, and right respectively
CZ - Zoom in and out respectively


# IMPORTANT INFO


This project relies on pygame to run.


Run the following command to run the code: python3 ./cgol_ui.py
