'''
i = 0
j = 0

for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print()
'''
list = []

for i in range(7):
    list.append([])
    for j in range(7):
        if i == j:
            list[i].append("*")
            list[7-(i+1)].append("*")
        else:
            list[i].append(" ")


print(list)
        
    
    