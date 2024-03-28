first_tuple = (1, 2, 3, 4, 5)
second_tuple = (2, 3, 6, 4, 7)
third_tuple = (2, 8, 3, 4, 9)

result = []

for first_element in first_tuple:
    for second_element in second_tuple:
        for third_element in third_tuple:
            if first_element == second_element == third_element:
                result.append(first_element)