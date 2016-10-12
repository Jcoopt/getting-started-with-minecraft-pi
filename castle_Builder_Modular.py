import explorerhat as eh
#import RPi.GPIO as GPIO
from mcpi import minecraft
import casMod as cm
mc = minecraft.Minecraft.create()
stone=1


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
pressed=0
while True:
    
    x, y, z = mc.player.getPos()
    eh.touch.pressed(buttonPress)
    if pressed== 1:
        cm.clearSpace(x,y,z)
        cm.towers(x,y,z,block)
        cm.walls(x,y,z,block)
        cm.floor(x,y,z,block)
        cm.door(x,y,z)
        pressed=0
