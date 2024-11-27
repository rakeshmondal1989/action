
a = [[2,3,5],[1,2,4,6]]
new_list1 = []
for i in a:
    for j in i:
        new_list1.append(j)
print(new_list1)

a = [[2,3,5],[1,2,4,6],[2,5,7,[12,13]]]
new_list = []
for i in a:
    for j in i:
        new_list.append(j)
        if type(j)==list:
            new_list.remove(j)
            for k in j:
                new_list.append(k)
                
print(new_list)
                   
