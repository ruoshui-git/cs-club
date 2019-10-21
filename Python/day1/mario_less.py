height = int(input('Height: '))

while height > 8 or height < 0:
    height = int(input('Height: '))

for row in range(height):
    print((height - (row + 1)) * ' ','#' * (row + 1), sep='')