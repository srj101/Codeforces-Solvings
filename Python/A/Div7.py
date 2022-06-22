def convert(list):
      
    # Converting integer list to string list
    s = [str(i) for i in list]
      
    # Join list items using join()
    res = int("".join(s))
      
    return(res)
    
for cases in range(int(input())):
    number = int(input())
    finalNumber = int(str(number).lstrip('0'))
    if finalNumber%7 == 0:
        print(finalNumber)
    else:
        
        c = 0
        ok = 0
        for j in list(str(finalNumber)):
            if ok ==1:
                break
            for i in range(1,10):
                if ok == 1:
                    break
                no = list(str(finalNumber))
                no[c] = str(i)
                finalNumber = convert(no)  
                if finalNumber %7 ==0:
                    print(finalNumber)
                    ok = 1
            c+=1