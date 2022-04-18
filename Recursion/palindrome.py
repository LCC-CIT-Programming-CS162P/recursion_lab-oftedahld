def main():
    print("This program will allow a user to provide a string and determine if it's a palindrome...")
    orgTestString = str(input("Provide a string to test: "))
    #testString = "Teet"
    testString = scrubber(orgTestString)
    isPalindrome = palindrome(testString)
    if isPalindrome == True:
        print('String "' + (orgTestString) + '" ' + 'IS a palindrome!')
    else:
        print('String "' + (orgTestString) + '" ' + 'IS NOT a palindrome!')

def palindrome(testString):
    stringLength = int(len(testString))
    if stringLength >= 2:
        if testString[0] == testString[stringLength - 1]:
            testString = testString[1:stringLength-1]
            return palindrome(testString)
        else:
            return False
    else:
        return True

def scrubber(string):
    string = string.lower()
    stringList = list(string)
    modStringList = ""
    for i in stringList:
        if i.isalnum():
            modStringList += i
    return modStringList

main()