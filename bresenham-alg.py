from PIL import Image
import random
import math
import time

img = Image.new('RGB', (320, 320))
def main():
    choice = input("Enter 1 to generate N number of lines OR 2 to test the specific test cases:\n")
    if(int(choice) == 1): 
        #randomly generate
        N = input("Give number of lines:\n")
        bre_start1 = time.time()
        print("start: ", bre_start1)
        for i in range(int(N)):
            #randomly generate a number 0-200
            #source:https://docs.python.org/3/library/random.html
            x0 = random.randint(0,255)
            y0 = random.randint(0,255)
            x1 = random.randint(0,255)
            y1 = random.randint(0,255)
            brensenham(x0, x1, y0, y1)
        bre_stop1 = time.time()
        print("stop: ", bre_stop1) 
        bre_time1 = (bre_stop1 - bre_start1)*1000
        print("Time taken in milliseconds for all lines =", bre_time1)
    if(int(choice) == 2):
        #Testing specific cases
        brensenham(0, 200, 80, 200) #hor
        brensenham(80, 20, 80, 200) #vert
        brensenham(0, 0, 200, 200) #diagonal positive
        brensenham(0, 150, 150, 0) #diagonal negitive
        brensenham(0, 0, 150, 80) #class example
        brensenham(0, 0, 20, 150) #positive slope
        brensenham(0, 100, 150, 80) #negative slope
        brensenham(0, 200, 15, 100) #negative slope
        # brensenham(18, 206, 154, 70)
        # brensenham(0, 0, 13, 212)
        #brensenham(0, 0, 200, 40)
        #brensenham(0, 10, 60, 20)
        # brensenham(0, 200, 40, 40)
        # brensenham(0, 240, 40, 140)
    else:
        print("restart program")
    img2 = img.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    img2.show()

def brensenham(x0, y0, x1, y1):
    bre_start = time.time()
    print("start: ", bre_start)
    #values
    print("x0 = ")
    print(x0)
    print("y0 = ")
    print(y0)
    print("x1 = ")
    print(x1)
    print("y1 = ")
    print(y1)

    #if the line is a dot
    if((x0 == x1) and (y0 == y1)):
        #All test cases contain following code from rosetta code to display a single pixel
        #source: https://rosettacode.org/wiki/Draw_a_pixel#Python
        pixels = img.load()
        pixels[x0,y0] = (255,0,0)
        print("dot")
    #if the line is vertical
    elif (x0 == x1):
        if (y1 > y0):
            dy = y1 - y0
            for i in range(dy):
                x = x0
                y = i + y0
                pixels = img.load()
                pixels[x,y] = (255,0,0)
        elif (y0 > y1):
            dy = y0 - y1
            for i in range(dy):
                x = x0
                y = i + y1
                pixels = img.load()
                pixels[x,y] = (255,0,0)
        print("vert")
    #if the line is horizontal
    elif(y0 == y1):
        if(x1 > x0):
            dx = x1 - x0
            for i in range(dx):
                x = i + x0
                y = y0
                pixels = img.load()
                pixels[x,y] = (255,0,0)
        elif(x0 > x1):
            dx = x0 - x1
            for i in range(dx):
                x = i + x0
                y = y0
                pixels = img.load()
                pixels[x,y] = (255,0,0)
        print("hor")

    else:
        #test cases found with help from Denbigh Strakey lecture pdf
        #https://www.cs.montana.edu/courses/spring2009/425/dslectures/Bresenham.pdf  
        #Algorthim psuedo form Open Genius IQ website
        #https://iq.opengenus.org/bresenham-line-drawining-algorithm/  
        dy = y1-y0
        dx = x1-x0
        absdy = abs(dy)
        absdx = abs(dx) 
        x = x0
        y = y0
        #slope < 1
        if(absdx > absdy):
            E = 2*absdy - absdx
            for i in range(absdx):
                if(dx < 0):
                    x = x - 1
                else:
                    x = x + 1
                if(E < 0):
                    E = E + 2*absdy
                else:
                    if(dy < 0):
                        y = y - 1
                    else:
                        y = y + 1
                    E = E + (2*absdy - 2*absdx)
                pixels = img.load()
                pixels[x,y] = (255,0,0)
            # slope is >= 1
        else:
            E = 2*absdx - absdy
            for i in range(absdy):
                if(dy < 0):
                    y = y - 1
                else:
                    y = y + 1
                if(E < 0):
                    E = E + 2*absdx
                else:
                    if(dx < 0):
                        x = x - 1
                    else:
                        x = x + 1
                    E = E + (2*absdx) - (2*absdy)
                pixels = img.load()
                pixels[x,y] = (255,0,0)
    bre_stop = time.time()
    print("stop: ", bre_stop) 
    bre_time = (bre_stop - bre_start)*1000
    print("Time taken in milliseconds =", bre_time)
main()