first_tuple = (1, 4, 7, 11, 19, 23, 24, 29, 31)
second_tuple = (2, 4, 7, 11, 14, 24, 30, 31, 32)
third_tuple = (3, 4, 11, 24, 25, 30, 31, 35, 36)

for first_element in first_tuple:
    for second_element in second_tuple:
        for third_element in third_tuple:
            if first_element != second_element != third_element:

                print(first_element, second_element, third_element)