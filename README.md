# Conway's Game Of Life
Demo Video: <https://www.youtube.com/watch?v=t30rUXlpwZA>


Conway's game of life is a cellular automaton invented by John Horton Conway. Its premise is simple. There are cells on a grid that are affected by rules that decide whether the cells live or die. Now, despite the rules being quite simple, Conway’s Game of life is famed for the complex patterns it can produce, and is seen as one of the more interesting mathematical and logical experiments invented. I have coded a rendition of Conway’s game of life, and will be detailing it in the coming paragraphs.


# The rules of life


Before I begin to talk about my actual code, I will skim over the rules of Conway’s game of life. Conway's game of life has four very simple rules.
 
**Rule #1** - if there are less than two living cells around (around being a direct neighbor to any given cell) that cell will die.

**Rule #2** - If there are two living cells around any given cell, and that cell is currently living, it survives.

**Rule #3** - If there are three living cells around any given cell, regardless of the state, it survives. This means a dead cell becomes a living one, and a living one stays alive.

**Rule #4** - If there are more than 3 living cells around any cell it dies.


 For each “step” in the simulator, the rules are applied to all cells, and the patterns the cells form update and evolve because of that. Due to the simplicity of the rules, they aren't all that challenging to port into code. In my **cgol.py** file, I have a function called **conwayslife**. Below are its contents:


```python

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
As you can see, this code is fairly simple, and is the innermost workings of my program. For context, **dim** is the grid side dimension, considering its a square. What's truly fascinating, however, is the degree of complexity that can be derived from these simple rules. There is one [video](https://youtu.be/xP5-iIeKXE8?si=sDXKXkCrovsNnCv_) by Philip Bradbury on Youtube that I think perfectly shows this. 



# My code and how it works


## The inner workings 


In this section, we will be looking at the more technical part of the code, contained within **cgol.py**. The two most important classes of this code is **Grid** that deals with the world, and **View**, which deals with the users view onto it.

One of the major design choices I made early on was whether to use a dictionary or nested list to store my cells. I started out with a nested list, but changed to using a dictionary later on. It let me have far looser boundaries for the grid, and would only store live cells, saving space. To put it fairly simply, it's just more flexible, easier to manipulate, and uses less memory. Below is the grid I use. It takes (x,y) coordinates, and a 0 or 1 value to represent if the cell is alive or dead.

```python
self.gridata = {}
```

Another interesting feature in **cgol.py** is the **View** class. The view and grid are separate entities, with the **Grid** being the entire simulation space and the view being the observable simulation space. The **View** supports things like zooming in and out and panning across the grid.

```python
class View:

    """
    The View class handles the view regarding zoom and pan
    """
    def __init__(self, view_size, x, y):
        self.view_size = view_size
        self.x = x
        self.y = y
```
I paid special attention to unit tests when developing **View** to make sure that it worked completely as intended.


## The ui


The file responsible for the user interface is **cgol_ui.py**. I chose pygame for the user interface due to my prior experience making games with it. The main class of **cgol_ui.py** is Simulator, it keeps track of the grid and view. While the code in **cgol.py** is the actual functionality of the simulation, there isnt any explicit visual component. Now, that's where **cgol_ui.py** comes in. It gives a clear and concise visual representation of the output of **cgol.py**, whilst also giving the user the ability to visually manipulate it.


A few of the stand out features in **cgol_ui.py** are the commands. Especially zoom, pan, and copy. Zoom and pan are actually what utilise **View** in **cgol.py**, and were probably the trickiest commands to code. One of the bugs I ran into while coding them was that the sides of the grid elongated and the proportions were all off. I eventually found it was due to rounding error in the **View** class.


```python
self.view_size = math.round(max(min(self.view_size * f, grid_size), 1))
```


The bug was due to the fact that when I was rounding, I would marginally throw the proportion off, and that would result in a cascade where my entire grid would be out of proportion. The fix, however, was simple.


```python
self.view_size = math.ceil(max(min(self.view_size * f, grid_size), 1))
```


With that small change, the zooming worked properly. 


## Plaintext


Lets now turn to the copy command in **cgol_ui.py**. It works by reading a file representing a pattern in the unimaginatively named [**plaintext**](https://conwaylife.com/wiki/plaintext) serialisation format. This is the standard way to represent Conway's game of life patterns in text. Heres an example:



```

!Name: Glider
!
.0.
..0
000

```


As you can see here, zeroes are used to depict live cells and full stops to depict dead cells. The **plaintext.py** file is what interprets the normal **plaintext** files, and puts the patterns on screen. 


Now, the nice thing about having a piece of code that can read these serialised files is that it's really not all that tricky to just copy paste more patterns in. While at this point, one would have to delve into the code a little bit to change what files are being printed, one of the features that are high up on my TODO list is a patterns library, where you can just select a pattern and it prints to screen. 


### A guide to using my program


There are a few commands to edit the board, the guide for said commands being accessible by left clicking the question mark icon.


**Left click on cell** - Turns cell on/off depending on prior state

**Right click** - Copies pattern to screen. Currently only gosper glider gun - better pattern copying will be implemented later

**Space bar** - Pause/Unpause simulation

**E** - Move single step in simulation

**F** - Clear grid entirely

**R** - Randomise grid entirely

**WASD** - Move up, left, down, and right respectively

**CZ** - Zoom in and out respectively


# IMPORTANT INFO


This project relies on pygame to run.


Run the following command to run the code: python3 ./cgol_ui.py
