lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_only (any_lst):
    new_lst = []
    for element in any_lst:
        if element % 2 == 0:
            new_lst.append(element)
            
    return new_lst
    
print(even_only (lst))
