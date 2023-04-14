def positive_numbers(lst):
    positive_lst=[]
    for number in lst:
        if number > 0:
            positive_lst.append(number)
    return positive_lst

list1=[12,-7,5,64,-14]
positive_list1 = positive_numbers(list1)
print(positive_list1)

list2=[12,14,-95,3]
positive_list2 = positive_numbers(list2)
print(positive_list2)
