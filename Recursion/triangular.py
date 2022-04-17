def triangle(n):
    if n == 1:
        return 1
    else:
        return n + triangle(n-1)

def trianglePrint(n, nMax):
    borderExtra = nMax - n
    line = (borderExtra * '-') + ((('-' + '\u25b2') * n) + '-') + (borderExtra * '-')
    print(line)
    if n == 1:
        return 1
    else:
        return n + trianglePrint(n-1, nMax)
            

def main():
    print("This program will allow the user to request the nth triangle number...")
    max = int(input("Provide a positive whole number: "))
    triNum = triangle(max)
    print("The " + str(max) + "th triangle number is " + str(triNum) + ".")
    print()
    for n in range(1, max + 1):    
        border = ('=' * ((n * 2) + 1))
        print(border)
        print("Triangle_" + str(n) + " = " + str(triNum))
        print(border)
        triNum = trianglePrint(n, n)
        print(border)
        print()
        
    print()

main()