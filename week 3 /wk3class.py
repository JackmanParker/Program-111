from itertools import count


def computeArea(width, height):
    area = width * height
    return area

def rectangleCount(count):
    for i in count:
        width =int(input(f"What is the length of Rectangle {1+count}"))
        height =int(input(f"What is the  of Rectangle {1+count}"))
        print(computeArea(width, height))
        totalArea =+ (computeArea(width, height))
    print(totalArea)
    
   
def main():
    count = int(input("How many rectangles do you need solved: "))
    rectangleCount(count)
    
    

main()

