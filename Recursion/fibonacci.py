def main():
    print("This program will provide the user with the nth number i the fibonacci sequence, and all number preceding it....")
    fibNum = int(input("Provide a number: "))
    fibNumVal = fibonacci(fibNum)
    print("The " + str(fibNum) + "th number in the fibonacci sequence is " + str(fibNumVal))
    fibNums = []
    for n in range (0, fibNum + 1):
        fibNumVal = fibonacci(n)
        print("The " + str(n) + "th number is " + str(fibNumVal))
        fibNums.append(fibNumVal)
    print("Fibonacci sequence: " + str(fibNums))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1    
    else:
        nMinOne = fibonacci(n-1)
        if nMinOne <= 0:
            nMinTwo = 0
        else:
            nMinTwo = fibonacci(n-2)
        nVal = nMinOne + nMinTwo
    return nVal

main()