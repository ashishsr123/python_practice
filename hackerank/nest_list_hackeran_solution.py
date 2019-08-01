marksheet=[]
scorelist=[]
if __name__ == '__main__':
    #The python interpreter stores the last expression value to the special variable called _.
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet+=[[name,score]]
                scorelist+=[score]
        b=sorted(list(set(scorelist)))[1] 
        dict_l = dict.fromkeys(scorelist)
        b2 = sorted(list(dict_l))

        for a,c in sorted(marksheet):
             if c==b:
                    print(a)