from mcpi import minecraft

mc = minecraft.Minecraft.create()

stone=1
def clearSpace(x,y,z):
    mc.setBlocks(x+9,y-2,z+5,x-9,y+10,z+30,0)
def towers(x,y,z,block):
    #Closest tower on the right
    mc.setBlocks(x+5, y-1, z+10, x+9, y+8, z+14, block)
    mc.setBlocks(x+6, y-1, z+11, x+8, y+8, z+13, 0)
    
    #Closest tower on the left
    mc.setBlocks(x-5, y-1, z+10, x-9, y+8, z+14, block)
    mc.setBlocks(x-6, y-1, z+11, x-8, y+8, z+13, 0)
    
    #Furthest tower on the right
    mc.setBlocks(x+5, y-1, z+24, x+9, y+8, z+28, block)
    mc.setBlocks(x+6, y-1, z+25, x+8, y+8, z+27, 0)
    
    #Furthest tower on the left
    mc.setBlocks(x-5, y-1, z+24, x-9, y+8, z+28, block)
    mc.setBlocks(x-6, y-1, z+25, x-8, y+8, z+27, 0)
def walls(x,y,z,block):
    #Front wall
    mc.setBlocks(x+4, y-1, z+12, x-4, y+4, z+12, block)
    #Left wall
    mc.setBlocks(x+7, y-1, z+15, x+7, y+4, z+23, block)
    #Right wall
    mc.setBlocks(x-7, y-1, z+15, x-7, y+4, z+23, block)
    #Back wall
    mc.setBlocks(x+4, y-1, z+26, x-4, y+4, z+26, block)
def door(x,y,z):
    mc.setBlocks(x+1, y, z+12, x-1, y+2, z+12, 0)
def floor(x,y,z,block):
    mc.setBlocks(x-9, y-1, z+10, x+9, y-1, z+28, block)
