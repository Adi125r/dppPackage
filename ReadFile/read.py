from Meal import product, dish


def readFromFile(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def splitContentOnDishList(content):
    dishList=[]
    d=dish.dish()
    for i in range(0,len(content),2):
        p = product.product()
        if content[i+1]!='-1':
           p.name=content[i]
           if content[i+1].find(' gram')!=-1:
               s=content[i + 1].replace(' gram', '')
               p.weightInGram=s
           else:
               s=content[i + 1].replace(' amount', '')
               p.amount=s
           d.productList.append(p)
        else:
            d.name=content[i]
            dishList.append(d)
            d=dish.dish()
    return dishList

def printSomething():
    print("Library")

printSomething()
