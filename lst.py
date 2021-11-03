lst = [1, 2, 3, 4, 5]
another_lst = [7, 8, 9, 10]

print (lst[2])
print (lst[-3])

print(len(lst))

print("\n")

combined_lst = lst + another_lst
print(combined_lst)

temp = lst
lst = another_lst
another_lst = temp

print(lst)
print(another_lst)

lst[0] = 0
print(lst)

print(lst[:3])
print(lst[:2])
print(lst[:1])
print("\n")

print(another_lst[0:4:2])
print(another_lst[::2])
print(another_lst[::])
