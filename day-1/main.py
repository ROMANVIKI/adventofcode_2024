def histerian_hysteria():
    total = 0
    left_lis = []
    right_lis = []
    while True:
        data_inp = input('Provide "done" after providing the input values!')
        if data_inp.lower() == "done":
            break
        try:
            lis_char_1, lis_char_2 = map(int, data_inp.split())
            left_lis.append(lis_char_1)
            right_lis.append(lis_char_2)

        except ValueError:
            print("Invalid input. Please enter two numbers seperated by a space.")

    sorted_lef_lis = sorted(left_lis)
    sorted_right_lis = sorted(right_lis)

    for i in range(len(sorted_lef_lis)):
        total += abs(sorted_lef_lis[i] - sorted_right_lis[i])
    return total


sol = histerian_hysteria()

print(sol)
