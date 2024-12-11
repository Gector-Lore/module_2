my_list = [0, 42, 69, 322, 13, 99, -5, 9, 8, 7, -6, 5]
i = 1
while i < len(my_list):
    print(my_list[i])
    i += 1
    if my_list[i] < 0:
        break