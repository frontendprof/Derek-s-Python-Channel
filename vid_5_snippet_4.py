
# B_R_R
#M_S_A_W

import math

print("""We can calculate

                rectangles

                circles

                triangles

                rhombus

                parallelograms

                trapezoids 


with their parameters you specify

""")

def get_area(shape):
  shape=shape.lower()

  if shape=="rectangle":
    rectangle_area()

  elif shape=="circle":
    circle_area()

  elif shape=="rhombus":
    rhombus_area()

  elif shape=="triangle":
    triangle_area()

  elif shape=="parallelogram":
    parallelogram_area()

  elif shape=="trapezoid":
    trapezoid_area()
  
  else:
    print("Please inquire above mentioned shapes only ")

def rectangle_area():
  length=float(input("What is the length? "))
  width=float(input("What is the width? "))
  area=length * width
  print("The area of your rectangular is {:.2f} ".format(area))

def circle_area():
  radius=float(input("What is the radius: "))
  area=math.pi*(math.pow(radius,2))
  print("The area of your circle is {:.2f}".format(area))

def rhombus_area():
  first_diagonal=float(input("What is the first diagonal length? "))
  second_diagonal=float(input("What is the second diagonal length? "))
  area=first_diagonal * second_diagonal
  print("The area of your rhombus is {:.2f} ".format(area))

def triangle_area():
  height=float(input("What is the height: "))
  base=float(input("What is the base: "))
  area=(height*base)/2
  print("The area of your triangle is {:.2f}".format(area))

def parallelogram_area():
  height=float(input("What is the height: "))
  base=float(input("What is the base: "))
  area=(height*base)/2
  print("The area of your parallelogram is {:.2f}".format(area))

def trapezoid_area():
  height=float(input("What is the height: "))
  base_1=float(input("What is the first base: "))
  base_2=float(input("What is the second base: "))
  area=((base_1+base_2)/2)*height
  print("The area of your trapezoid is {:.2f}".format(area))


def main():
  get_a=input("""
  ***********

  What is your shape that you want its area of: 

  ***********
  """)
  get_area(get_a)

main()
