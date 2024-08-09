def asciiGrid(L: list):
    
    def maxlenL(L: list) -> int:
        longest = 0
        for line in L:
            for elem in line:
                if longest < len(elem):
                    longest = len(elem) + 2
        return longest
    
    def maxlenlineL(L: list):
        longest = 0
        for line in L:
            if len(line) > longest:
                longest = len(line)
        return longest

    def printSep(line: list, gwidth: int):
        [print("+" + "-"*(widthp), end="") for i in range(gwidth)]
        print("+")

    def printP(line: list):
        [print("| " + line[i] + " "*(widthp - 1 - len(line[i])), end="") for i in range(len(line))]
        print("|")

    if not L:
        return 1
    
    gwidth = maxlenlineL(L)
    widthp = maxlenL(L)
    printSep([i for i in range(len(L[0]))], gwidth)
    for line in L[:-1]:
        printP(line)
        printSep(line, gwidth)
    printP(L[-1])
    printSep(L[-1], len(L[-1]))
    return 0
