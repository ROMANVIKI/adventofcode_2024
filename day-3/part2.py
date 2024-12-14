
# def mul(x, y):
#     return x * y
#
#
# def mullItOverPartTwo():
#     total = 0
#     while True:
#         data_input = input('Enter the test cases, to quit enter "exit": ')
#
#         if data_input.lower() == 'exit':
#             break
#
#         current_index = 0
#         mul_func = True
#         while current_index < len(data_input):
#             try:
#                 if data_input[current_index: current_index + 7] == "don't()":
#                     mul_func = False
#                     current_index += 7  # Move past "don't()"
#                     continue
#
#                 if data_input[current_index: current_index + 4] == 'do()':
#                     mul_func = True
#                     current_index += 4  # Move past "do()"
#                     continue
#
#                 if data_input[current_index: current_index + 4] == 'mul(' and mul_func:
#                     start = current_index + 4
#
#                     comma_index = data_input.find(',', start)
#                     end_index = data_input.find(')', comma_index)
#
#                     if comma_index != -1 and end_index != -1:
#                         try:
#                             x = int(data_input[start: comma_index].strip())
#                             y = int(data_input[comma_index + 1:end_index].strip())
#                             result = mul(x, y)
#                             total += result
#
#                             current_index = end_index + 1
#                         except ValueError:
#                             current_index += 4
#                             continue
#                     else:
#                         current_index += 1
#                 else:
#                     current_index += 1
#             except IndexError:
#                 break
#
#     return total
#
#
# # Run the function
# sol = mullItOverPartTwo()
# print(sol)
#
#
#


def mul(x, y):
    return x * y


def mull_it_over_part_two(file_path):
    total = 0

    try:
        with open(file_path, 'r') as file:
            for data_input in file:
                data_input = data_input.strip()  # Remove extra whitespace or newlines

                current_index = 0
                mul_func = True
                while current_index < len(data_input):
                    try:
                        if data_input[current_index: current_index + 7] == "don't()":
                            mul_func = False
                            current_index += 7  # Move past "don't()"
                            continue

                        if data_input[current_index: current_index + 4] == 'do()':
                            mul_func = True
                            current_index += 4  # Move past "do()"
                            continue

                        if data_input[current_index: current_index + 4] == 'mul(' and mul_func:
                            start = current_index + 4

                            comma_index = data_input.find(',', start)
                            end_index = data_input.find(')', comma_index)

                            if comma_index != -1 and end_index != -1:
                                try:
                                    x = int(data_input[start: comma_index].strip())
                                    y = int(data_input[comma_index + 1:end_index].strip())
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
                    except IndexError:
                        break

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return total


# Provide the path to your input text file
file_path = 'input.txt'
sol = mull_it_over_part_two(file_path)
print(sol)

