class zmiana:
    def znajdz (text):
        s= list(text)
        tab=[['a','b','c'],['d','e','f'],['g','h','i']]
        for i in range(2):
            p=text.find(tab[i-1][0])
            s[p]= tab[i+1][0]
            p=text.find(tab[i-1][1])
            s[p]= tab[i+1][1]
            p=text.find(tab[i-1][2])
            s[p]= tab[i+1][2]
            p=text.find(tab[i][0])
            s[p]= tab[i+1][0]
            p=text.find(tab[i][1])
            s[p]= tab[i+1][1]
            p=text.find(tab[i][2])
            s[p]= tab[i+1][2]
        print(s)


