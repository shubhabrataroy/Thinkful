def bubble_sort(list_of_numbers):
    lengthOfList = len(list_of_numbers)
    for i in range(lengthOfList): 
        for j in range(1, lengthOfList-i): 
            if list_of_numbers[j] < list_of_numbers[j - 1 ]:
                list_of_numbers[j], list_of_numbers[j-1] = list_of_numbers[j - 1], list_of_numbers[j]
    return list_of_numbers

#Do not change code below this line
unsorted_list = [20, 31, 5, 1, 591, 1351, 693]
print(unsorted_list)
print(bubble_sort(unsorted_list))
