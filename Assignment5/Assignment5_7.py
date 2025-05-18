def CalArea(leng, width):
    area = leng * width
    return area

def CalPer(leng, width):   
    perimeter = 2 * (leng + width)
    return perimeter

def main():
        length = int(input("Enter the length of the rectangle: "))
        wid = int(input("Enter the width of the rectangle: "))

        ret1 = CalArea(length, wid)
        ret2 = CalPer(length, wid)

        print("Area of rectangle is ", ret1)
        print("Perimeter of reactangle is ", ret2)

if __name__ == "__main__":
    main()
