def findPal(string):
    def findOdd(string):
        max = 1
        for Middle in range(len(string)):
            leftBorder = Middle - 1
            rightBorder = Middle + 1
            while (leftBorder >= 0 and rightBorder < len(string) and string[leftBorder] == string[rightBorder]):
                new_str = string[leftBorder:rightBorder + 1]
                if len(new_str) > max:
                    max = len(new_str)
                    if len(palindromes[0]) < len(new_str):
                        palindromes[0] = new_str
                leftBorder -= 1
                rightBorder += 1
        return max

    def findEven(string):
        max = 1
        for Middle in range(len(string)):
            leftBorder = Middle
            rightBorder = Middle + 1
            while (leftBorder >= 0 and rightBorder < len(string) and string[leftBorder] == string[rightBorder]):
                new_str = string[leftBorder:rightBorder + 1]
                if len(new_str) > max:
                    max = len(new_str)
                    if len(palindromes[0]) < len(new_str):
                        palindromes[0] = new_str
                leftBorder -= 1
                rightBorder += 1
        return max

    return max([findOdd(string), findEven(string)])


string = input()
global palindromes
palindromes = list()
palindromes.append('')
findPal(string)
if palindromes[0] != '':
    print(palindromes[0])
else:
    print(string[0])