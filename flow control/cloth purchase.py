clotyp = int(input("select cloth type press 1)silk 2)linen 3)cotton"))
puchrat = int(input("enter purchase rate"))
if(clotyp==1):
    if(puchrat>5000):
        print(puchrat)
    elif(puchrat>4000) and(puchrat<5000):
        res=puchrat-((puchrat*10)/100)
        print(res)
    elif(puchrat>3000) and (puchrat<4000):
        res=puchrat-((puchrat*8)/100)
        print(res)
    elif(puchrat>2000) and (puchrat<3000):
        res=puchrat-((puchrat*7)/100)
        print(res)
    else:
        res=puchrat-((puchrat*5)/100)
        print(res)
elif(clotyp==2):
    if (puchrat > 5000):
        res = puchrat-((puchrat * 20)/100)
        print(res)
    elif (puchrat > 4000) and (puchrat < 5000):
        res = puchrat - ((puchrat * 10) / 100)
        print(res)
    elif (puchrat > 3000) and (puchrat < 4000):
        res = puchrat - ((puchrat * 9) / 100)
        print(res)
    elif (puchrat > 2000) and (puchrat < 3000):
        res = puchrat - ((puchrat * 7) / 100)
        print(res)
    else:
        res = puchrat - ((puchrat * 5 )/ 100)
        print(res)

elif(clotyp==3):
        if (puchrat > 5000):
            res = puchrat - ((puchrat * 20)/100)
            print(res)
        elif (puchrat > 4000) and (puchrat < 5000):
            res = puchrat - ((puchrat * 10) / 100)
            print(res)
        elif (puchrat > 3000) and (puchrat < 4000):
            res = puchrat - ((puchrat * 9) / 100)
            print(res)
        elif (puchrat > 2000) and (puchrat < 3000):
            res = puchrat - ((puchrat * 7) / 100)
            print(res)
        else:
            res = puchrat - ((puchrat * 5) / 100)
            print(res)
else:
        print("cannot purchase")