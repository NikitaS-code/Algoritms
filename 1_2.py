def mergeTwoarray(list1, list2):
    for nums in list1:
        list2.append(nums)
    new_list = sorted(list2)
    return new_list

list1 = [1,2,4]
list2 = [1,3,4]
result = mergeTwoarray(list1, list2)
print(result)