nunu = input()
arr = list(map(int,input().split())) 
l = len(arr)  
i = 0  
max = 1  
start = 0 
end = 0  
beststart = 0  
bestend = 0 
while i<l:
    if i+1 < l and arr[i+1]>=arr[i]:
        end = end + 1 
        if (end-start+1) > max:
            max = (end - start + 1)  
            beststart = start  
            bestend = end  
    else:
        start = i+1  
        end = i+1 
 
    i = i + 1
 
print (len(arr[beststart:bestend+1]))  