#4. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 

#Original list: [1, 1, 2, 3, 4, 4, 5, 1] Length of the first part of the list:3 Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1]) 
def split_list(lst, first_part_len):
    first_part = lst[:first_part_len]
    second_part = lst[first_part_len:]
    return first_part, second_part
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
split_length = 3
part1, part2 = split_list(original_list, split_length)
print("Splitted the list into two parts:", (part1, part2))
