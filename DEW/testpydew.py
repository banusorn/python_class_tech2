#รับ imputเฉพาะ123 -Yes
#สร้าง if elif ให้เลือกเฉพาะ 123 -Yes
#รับมาประมวลผล วงกลม สามเหลี่ยม สี่เหลี่ยม -Yes
#รับค่าOutputไปลง Text -Yes


import os
from lib2to3.pgen2.token import OP
while 1:
    input_string = input(" --Area-- \n# 1. Circle\n# 2. Triangle\n# 3. Rectangle\n  \n(Press Enter 1,2,3):")

    Circle = '1'
    for c in input_string:
        if Circle == c:
            PI = 3.14
            radius = float(input(' Please Enter the radius of a circle: '))
            area = PI * radius * radius
            circumference = 2 * PI * radius
            f = open("D:/Calculation_Area_20220707080000.txt", "w")
            f.write("Type = Circle (1) ")
            f.close

            f = open("D:/Calculation_Area_20220707080000.txt", "a")
            f.write("\n---------------")
            f.close

            f = open("D:/Calculation_Area_20220707080000.txt", "a")
            f.write("\nArea Of a Circle")
            f.close

            new_text = (" %.2f " %area)
            f.write(new_text)
            f.close()
            
            f = open("D:/Calculation_Area_20220707080000.txt", "a")
            f.write("\nCircumference Of a Circle =")
            f.close

            new_text = (" %.2f " %circumference)
            f.write(new_text)
            f.close()

            print(" Area Of a Circle = %.2f" %area)
            print(" Circumference Of a Circle = %.2f" %circumference)


    Triangle = '2'
    for t in input_string:
        if Triangle == t:
            base = float(input('Please enter base : '))
            height = float(input('Please enter height : '))
            total = ((1/2) * (base * height))
            f = open("D:/Calculation_Area_20220707080000.txt", "w")
            f.write("Type = Triangle (2)")
            f.close

            f = open("D:/Calculation_Area_20220707080000.txt", "a")
            f.write("\n---------------")
            f.close

            f = open("D:/Calculation_Area_20220707080000.txt", "a")
            f.write("\nTriangle area =")
            f.close

            new_text = (" %.2f " %total)
            f.write(new_text)
            f.close()

            print( 'Triangle area = %.2f' %total )


    Rectangle = '3'
    for r in input_string:
        if Rectangle == r:
            width = float(input('Please enter width : '))
            height = float(input('Please enter height : '))
            total = width * height

            f = open("D:/Calculation_Area_20220707080000.txt", "w")
            f.write("Type = Rectangle (3)")
            f.close

            f = open("D:/Calculation_Area_20220707080000.txt", "a")
            f.write("\n---------------")
            f.close

            f = open("D:/Calculation_Area_20220707080000.txt", "a")
            f.write("\nRectangle area =")
            f.close

            new_text = (" %.2f " %total)
            f.write(new_text)
            f.close()

            print( 'Rectangle = %.2f ' %total )
