import random

operatorList = ['+','-']

for l in range(100):
    result=-1
    i=0
    while result == -1:
        a = random.randint(1,100)
        b = random.randint(1,100)
        c = random.randint(1,100)
        operaterFirstPick = random.randint(0,1)
        operaterSecondPick = random.randint(0,1)
        #print("This is the ",i,"'s try.")
        if operaterFirstPick == 0:
            if operaterSecondPick == 0:
                result = a+b+c
            else:
                result = a+b-c
                if a+b < c:
                    result = -1;
        else:
            if operaterSecondPick == 0:
                result = a-(b+c)
                if a < b+c :
                    result = -1;
            else:
                result = a-(b-c)
                if b<c:
                    result = -1;
                elif a<b-c:
                    result = -1;
        i+=1
        #print(result)

    print(str(a)+operatorList[operaterFirstPick]+" ("+str(b)+ operatorList[operaterSecondPick] +str(c)+") =")#+str(result))
        