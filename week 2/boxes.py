import math

itemCount = int(input('Enter the number of items:'))
boxSize = int(input('Enter the  number of items per box'))
boxCount = math.ceil(itemCount / boxSize)

print (f"With {itemCount} items, packing {boxSize} items in each box, you will need {boxCount} boxes.  ")