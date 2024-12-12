def histerian_hysteria():
    total = 0
    left_list = []
    right_list = []
    while True:
        data_inp = input()
        # I just added an extra if block so that if the data were given provide "done"
        # so that the while look will know when to stop.
        if data_inp.lower() == "done":
            break

        # Here we use map to seperate the integers and append those integers to their respective lists
        try:
            lis_char_1, lis_char_2 = map(int, data_inp.split())
            left_list.append(lis_char_1)
            right_list.append(lis_char_2)

        except ValueError:
            print("Invalid input. Please enter two numbers seperated by a space.")

    # According to the problem we have to sort the list so we use sorted in-build function here
    sorted_lef_lis = sorted(left_list)
    sorted_right_list = sorted(right_list)

    # used a for loop so loop thorugh the integers in two arr
    for i in range(len(sorted_lef_lis)):
        total += abs(sorted_lef_lis[i] - sorted_right_list[i])
    return total


sol = histerian_hysteria()

print(sol)
