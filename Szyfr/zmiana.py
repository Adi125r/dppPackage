def znajdz (text):
    s= list(text)
    tab=[['a','b','c'],['d','e','f'],['g','h','i']]
    p=text.find(tab[0][0])
    s[p]= tab[2][0]
    print(s)

znajdz('asdr')
