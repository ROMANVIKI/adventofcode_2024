

def mul(x, y):
    return x * y


def mullItOver():
    patterns = []
    total = 0
    while True:
        data_input = input('Enter data or put "enter" to exit:')
        current_index = 0
        if data_input == 'enter':
            break

        while current_index < len(data_input):
            if data_input[current_index: current_index + 4] == 'mul(':
                start = current_index + 4
                comma_index = data_input.find(',', start)
                end_index = data_input.find(')', comma_index)


                if comma_index != -1 and end_index != -1:
                    try:
                        x = int(data_input[start:comma_index].strip())
                        y = int(data_input[comma_index + 1: end_index].strip())


                        result = mul(x, y)
                        total += result

                        current_index = end_index + 1 

                    except ValueError:
                        current_index += 4
                        continue
                else:
                    current_index += 1
            else:
                current_index += 1
    return total



sol = mullItOver()
print(sol)
