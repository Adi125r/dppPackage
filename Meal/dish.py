from Meal import person

class dish:

    def __init__(self):
        self.name=''
        self.productList=[]

    @staticmethod
    def calculateProductDemand(nDish,nMen,nWomen,nChildren):
        caluclatedProducList=[]
        for val in nDish.productList:
            if val.weightInGram!=-1:
                print(val.weightInGram)
                ilosc=float(val.weightInGram)*nWomen * person.Person.kobieta.value + float(val.weightInGram)*nMen * person.Person.mezczyzna.value + float(val.weightInGram)*nChildren * person.Person.dziecko.value
                str='%s %.2f gram'%(val.name,float(ilosc))
                #print(str)
                caluclatedProducList.append(str)
            else:
                print(val.amount)
                ilosc = float(val.amount) * nWomen * person.Person.kobieta.value + float(
                    val.amount) * nMen * person.Person.mezczyzna.value + float(
                    val.amount) * nChildren * person.Person.dziecko.value
                str = '%s %.2f szt' % (val.name, float(ilosc))
                #print(str)
                caluclatedProducList.append(str)
        return caluclatedProducList