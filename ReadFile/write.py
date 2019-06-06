def writeFile(filename, dishList):
    with open(filename, 'w') as f:
        for val in dishList:
            for pr in val.productList:
                f.write(pr.name+"\n")
                if pr.amount != -1:
                    f.write(pr.amount+" amount\n")
                if pr.weightInGram != -1:
                    f.write(pr.weightInGram+" gram\n")
            f.write(val.name + "\n")
            f.write("-1\n")
    print("cos")
def printSomething():
    print("cos")

writeFile()
