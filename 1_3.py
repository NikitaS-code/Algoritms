list = [1,1,2,3,3]
secondlist = []
for item in list:
    if item not in secondlist:
        secondlist.append(item)
print(secondlist)  