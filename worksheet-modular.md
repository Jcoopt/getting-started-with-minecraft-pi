# Getting Started with Minecraft Pi

Minecraft is a popular sandbox open-world building game. A free version of Minecraft is available for the Raspberry Pi; it also comes with a programming interface. This means you can write commands and scripts in Python code to build things in the game automatically. It's a great way to learn Python!

![Minecraft Pi banner](images/minecraft-pi-banner.png)

## Run Minecraft

To run Minecraft, double click the desktop icon or enter `minecraft-pi` in the terminal.

![](images/mcpi-start.png)

When Minecraft Pi has loaded, click on **Start Game**, followed by **Create new**. You'll notice that the containing window is offset slightly. This means to drag the window around you have to grab the title bar behind the Minecraft window.

![](images/mcpi-game.png)

You are now in a game of Minecraft! Go walk around, hack things, and build things!

Use the mouse to look around and use the following keys on the keyboard:

| Key          | Action               |
| :---:        | :-----:              |
| W            | Forward              |
| A            | Left                 |
| S            | Backward             |
| D            | Right                |
| E            | Inventory            |
| Space        | Jump                 |
| Double Space | Fly / Fall           |
| Esc          | Pause / Game menu    |
| Tab          | Release mouse cursor |

You can select an item from the quick draw panel with the mouse's scroll wheel (or use the numbers on your keyboard), or press `E` and select something from the inventory.

![](images/mcpi-inventory.png)

You can also double tap the space bar to fly into the air. You'll stop flying when you release the space bar, and if you double tap it again you'll fall back to the ground.

![](images/mcpi-flying.png)

With the sword in your hand, you can click on blocks in front of you to remove them (or to dig). With a block in your hand, you can use right click to place that block in front of you, or left click to remove a block.


## Building castles with Python and Minecraft
![Before](images/before.png)
![After](images/after.png)
Now is time to start building something! We could build a house, but that's a bit boring. What if we build an entire castle every time you place a wool block?

### Getting started

Bring your focus away from the Minecraft by pressing the `Tab` key, which will free your mouse. Open Python 3 (or IDLE3) and open a new window (`File > New window`) and save it as Castle-builder.py (`File > Save`)

Then type the following in the python window:
```python
import explorerhat as eh
import casMod as cas
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
```
This imports the Minecraft library and creates a connection to the Minecraft game so we can change it. It is required at the start of every Minecraft pi program. It also imports two modules (these will be explained later)

We're now going to write a small program using the minecraft library and one of the modules we imported earlier. Modules are another python file that contains a bunch of code written earlier (possibly by another person) that you can bring into your program.

With all the setup finished, we now need to write a way for the computer to know when and where to build our castle. We are going to use the player's position using `mc.player.getPos()` and what block they are standing on with `mc.getBlock()` which gives the type of block at a given position.   
We also need to assign which block we are going to use by assigning the `block` variable to 1, which is stone.   
We will need to add a simple loop to our program. In this case, an indefinite while loop (loops until its told to stop) to check where the player is standing.   
```python
block=1
while True:
    x, y, z = mc.player.getPos()
    blockBelow=mc.getBlock(x, y-1, z)

```
For this program we are going to check using an `if` statement if the user is standing on orange wool (which has a block ID of 35).   

If they are, we use the casMod module we imported earlier to call some functions. Functions allow you to separate up your code into smaller chunks and make it reusable. Most functions are defined and called a little bit like this (DON'T put this in your program!):

```python
def functionName(parameter1,parameter2):   
    doSomethingWith(Variable2)
functionName(variable1,variable2)
```   
If you were open up the casMod.py file you would see a handful of functions like this.

We can "pass" the function a variable each time we use it. To build the castle we will give our functions the players position so it can always know where they are.

To add the functions we need o extend the while loop:
```python
while True:
    x, y, z = mc.player.getPos()
    blockBelow=mc.getBlock(x, y-1, z)
    if blockBelow == 35:
        cas.clearSpace(x,y,z)
        cas.towers(x,y,z,block)
        cas.walls(x,y,z,block)
        cas.floor(x,y,z,block)
        cas.door(x,y,z)
        mc.setBlock(x, y-1, z,block)
```
You're done! Save and run the program and change to Minecraft. Place an orange wool block on the floor and then step on it. BOOM! Instant castle.

What if we could link real life with minecraft? What if we could press a button and have the castle built for us? OR press another button and build another castle made out of LAVA? Let's find out!   

## Building castles with the Explorer HAT
![Explorer HAT](images/explorer-hat.png)

The Explorer is a very nice general purpose add-on board for the Raspberry Pi, also known as a HAT (Hardware Attachment on Top).   
The explorer hat comes with four capacitive touch buttons which work the same way a smartphone's screen does. We are going to assign each button a block, so that every time we press the button a castle made of that block will be built.    
First, create a new python file  (`File > New window`) and save it as Castle-explorer.py (`File > Save`)

```python
 from mcpi import minecraft
import casMod as cas
import explorerhat as eh
pressed=0

mc = Minecraft.create()
```
This allows us to use the explorer hat's library, and declares a variable for if a button is being pressed. We now need a function to handle what happens if a button is pressed:

```python
def buttonPress(channel, event):
    block1=1
    block2=3
    block3=5
    block4=20
    global block
    global pressed
    if channel > 4:
        return
    if event =='press':
        pressed=1
        if channel==1:
            block=block1           
        if channel==2:
            block=block2   
        if channel==3:
            block=block3
        if channel==4:
            block=block4
```
This function changes the block type that our castle will be made of, depending on which button has been pressed. The 'channel' variable is the button, and the event is whether it has been pressed or not. The block variables are what block the house will be made from. You can change them to be anything else, but for now we'll leave them as 1, 3, 5 and 20 which will build the castle out of stone, dirt, wood planks or glass.
The last thing we need to do is add a While loop.
```python
while True:

    x, y, z = mc.player.getPos()
    eh.touch.pressed(buttonPress)
    if pressed== 1:
        cas.clearSpace(x,y,z)
        cas.towers(x,y,z,block)
        cas.walls(x,y,z,block)
        cas.floor(x,y,z,block)
        cas.door(x,y,z)
        pressed=0

```
This tells our function from earlier if a button has been pressed, and which one. The `if` statement checks if a button has been pressed and it has runs our castle building code. The last thing we need to do is set our pressed variable to 0 otherwise the program will continue to build castles forever. 

And we're done! Jump back into Minecraft and every time you press one of the explorer HAT's buttons, a castle will appear!   

## Challenges
- Try changing the block IDs, see if you can build a castle out of other blocks like TNT. What happens if you build it out of sand?   
- Can you make a bigger castle? Perhaps thicker walls or taller towers?   
- What about perhaps playing with the Explorer HAT build in LEDs. To use them, use ```eh.light.yellow.on()```. You can try using different colours.
