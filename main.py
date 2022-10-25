from PIL import Image
import numpy as np
import math
import sys
#import datatlines.txt
#global my_matrix
#my_matrix = []

length = 0
# img = Image.new('RGB', (320, 320))
def Inputlines ( datalines ):
    text_file = open("datalines.txt", "r")
    lines = text_file.read()
    num = 0
    lines_list = lines.split(", ")
    length = len(lines_list)
    num_rows = length/4
    # I used this website to help me make a list into a matrix
    # https://note.nkmk.me/en/python-list-ndarray-1d-to-2d/
    #matrix = []
    global my_matrix
    my_matrix = np.array(lines_list).reshape(-1, 4).tolist()


#{ Reads ‘datalines’ from an external file (name of file is provided by the user).
# On return `num' will contain the number of lines read from the file. }
def ApplyTransformation (matrix):
    global my_matrix
    new_matrix = []
    for x in my_matrix:
        x0 = int(x[0])
        y0 = int(x[1])
        x1 = int(x[2])
        y1 = int(x[3])
        start = [x0, y0, 1]
        end = [x1, y1, 1]
        #I used this website help me find a way to multply multiple matrices
        #https://www.geeksforgeeks.org/numpy-dot-python/ 
        startp = np.dot(start, matrix)
        endp = np.dot(end, matrix)
        line = [int(startp[0]), int(startp[1]), int(endp[0]), int(endp[1])]
        print(line)
        new_matrix.append(line)

    my_matrix = np.array(new_matrix).reshape(-1, 4).tolist()
    return my_matrix
#{applies the transformation matrix to the lines that appear in “datalines”}

def brensenham(x0, y0, x1, y1):
    global img
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
                x = i + x1
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

def Displaypixels (datalines ):
    global img
    img = Image.new('RGB', (320, 320))
    # print(my_matrix)

    # I used this website to help me understand the shape method
    # https://stackoverflow.com/questions/18688948/numpy-how-do-i-find-total-rows-in-a-2d-array-and-total-column-in-a-1d-array
    a = np.array(my_matrix)
    num_rows = np.shape(a)[0]
    for i in range(int(num_rows)):
        brensenham(int(my_matrix[i][0]), int(my_matrix[i][1]), int(my_matrix[i][2]), int(my_matrix[i][3]))
    img2 = img.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    img2.show()
#{ Displays (i.e., scan-converts) ‘datalines’ containing `num' lines }

def Outputlines ( datalines ):
    num_rows = len(my_matrix)
    text_file = open("output.txt", "w")
    for x in my_matrix:
        x2 = str(x)
        text_file.write(x2)
    text_file.close()
    final_file = open("output.txt", "r")
    lines = final_file.read()
    lines = lines.rstrip()
    lines = lines.rstrip(lines[1])
    lines = lines.rstrip(lines[-1])
    lines = lines.replace("][", ", ")
    lines = lines.replace("[", "")
    lines = lines.replace("'", "")
    final_file.close()
    text_file = open("output.txt", "w")
    text_file.write(lines)
    text_file.close()
#{ Outputs ‘datalines’ containing `num' lines to an external file (name of file is provided by the user). }

def BasicTranslate ( Tx , Ty ):
    A = [[1, 0, 0],
    [0, 1, 0],
    [int(Tx), int(Ty), 1]]
    return A
#{ Translation - `Tx' is the horizontal and `Ty' is the vertical displacements. }

def BasicScale ( Sx, Sy ):
    A = [[int(Sx), 0, 0],
    [0, int(Sy), 0],
    [0, 0, 1]]
    return A
#{ Scale - `Sx' and `Sy' are the horizontal and vertical scaling factors;
#center of scale is at the origin of the Coordinate System. }

def BasicRotate ( angle ):
    angle = int(angle)
    angle = angle * (3.1415/180)
    A = [[round(math.cos(angle), 2), -round(math.sin(angle), 2), 0],
    [round(math.sin(angle), 2), round(math.cos(angle), 2), 0],
    [0, 0, 1]]
    return A
#{ Rotation - angle of rotation is `angle' degrees (clockwise);
#  Center of rotation is at the origin of the Coordinate System. }

def Scale ( Sx, Sy, Cx, Cy):
    Sx = int(Sx)
    Sy = int(Sy)
    Cx = int(Cx)
    Cy = int(Cy)
    NCx = 0 - int(Cx)
    NCy = 0 - int(Cy)
    mat = BasicTranslate(NCx, NCy)
    mat2 = BasicScale(Sx, Sy)
    mat3 = BasicTranslate(Cx, Cy)
    A = np.dot(mat, mat2)
    A = np.dot(A, mat3)
    return A
#{ Scale - `Sx' and `Sy' are the horizontal and vertical scaling factors;
# center of scale is at Cx, Cy. }

def Rotate ( angle, Cx, Cy ):
    angle = int(angle)
    Cx = int(Cx)
    Cy = int(Cy)
    NCx = 0 - int(Cx)
    NCy = 0 - int(Cy)
    mat = BasicTranslate(NCx, NCy)
    mat2 = BasicRotate(angle)
    mat3 = BasicTranslate(Cx, Cy)
    A = np.dot(mat, mat2)
    A = np.dot(A, mat3)
    return A
#{ Rotation - angle of rotation is `angle' degrees (clockwise);
# Center of rotation is at Cx, Cy. }


def main():
    global A
    while True:
        print("Hello please enter the number for your option")
        num = input(
            """
            1 - Inputlines
            2 - Apply Transformation (again)
            3 - Displaypixels
            4 - Outputlines
            5 - BasicTranslate
            6 - BasicScale
            7 - BasicRotate
            8 - Scale
            9 - Rotate
            10 - esc

            """
        )
        datalines = ""

        if num == "1":
            datalines = input("Please enter name of file you wish to read datalines form. (ex. datalines.txt): ")
            Inputlines ( datalines )
            print("1")
            print(datalines)
        elif num == "2":
            ApplyTransformation ( A )
        elif num == "3":
            Displaypixels( datalines )
        elif num == "4":
            Outputlines ( datalines )
        elif num == "5":
            num1, num2 = input("Please enter the x and y values by which you wish to translate. (ex. 10 10): ").split()
            A = BasicTranslate ( num1 , num2 )
            ApplyTransformation ( A )
        elif num == "6":
            num1, num2 = input("Please enter the values by which you wish to scale. (ex. 2 1): ").split()
            A = BasicScale ( num1 , num2 )
            ApplyTransformation ( A )
        elif num == "7":
            num1 = input("Please enter the value by which you wish to rotate. (ex. 90): ")
            A = BasicRotate ( num1 )
            ApplyTransformation ( A )
        elif num == "8":
            num1, num2, num3, num4 = input("Please enter the values by which you wish to scale and then the x and y you wish it to be centered on. (ex. 2 2 30 30): ").split()
            A = Scale ( num1 , num2, num3, num4 )
            ApplyTransformation ( A )
        elif num == "9":
            num1, num2, num3 = input("Please enter the value by which you wish to rotate and then the x and y you wish it to be centered on. (ex. 45 30 30): ").split()
            A = Rotate ( num1 , num2, num3 )
            ApplyTransformation ( A )
        elif num == "10":
            sys.exit()


if __name__ == "__main__":
    main()
