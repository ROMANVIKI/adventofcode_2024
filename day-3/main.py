# import re
#
# def mul(x, y):
#     return x * y
#
# def mullItOver():
#     patterns = []
#     total = 0
#     while True:
#         data_input = input("Enter a string (or 'exit' to stop): ")
#
#         if data_input.lower() == 'exit':
#             break
#
#         # Use regex to find all valid `mul(x,y)` patterns
#         matches = re.findall(r'mul\((\d+),(\d+)\)', data_input)
#
#         for match in matches:
#             x, y = map(int, match)  # Convert strings to integers
#             result = mul(x, y)
#             total += result
#             patterns.append((x, y, result))  # Store details of the operation
#
#     return patterns, total
#
# # Run the program
# patterns, total = mullItOver()
# print("Patterns:", patterns)
# print("Total:", total)



def mul(x, y):
    return x * y

def mullItOver():
    patterns = []
    total = 0
    while True:
        data_input = input("Enter a string (or 'exit' to stop): ")
        
        if data_input.lower() == 'exit':
            break
        
        current_index = 0
        while current_index < len(data_input):
            # Check for 'mul(' at the current index
            if data_input[current_index: current_index + 4] == 'mul(':
                start = current_index + 4  # Move index to start of the first number
                comma_index = data_input.find(',', start)  # Find the comma separating the two numbers
                close_index = data_input.find(')', comma_index)  # Find the closing parenthesis

                # Ensure indices are valid and the format is correct
                if comma_index != -1 and close_index != -1:
                    try:
                        # Extract and convert the numbers
                        x = int(data_input[start:comma_index].strip())
                        y = int(data_input[comma_index + 1:close_index].strip())
                        
                        # Perform the multiplication and store results
                        result = mul(x, y)
                        total += result
                        patterns.append((x, y, result))
                        
                        # Move index past the current 'mul(x,y)' pattern
                        current_index = close_index + 1
                    except ValueError:
                        # If conversion fails, move past this 'mul' to avoid an infinite loop
                        current_index += 4
                        continue
                else:
                    # If no valid comma or closing parenthesis, move index forward
                    current_index += 1
            else:
                # Move to the next character if no 'mul(' is found
                current_index += 1
    
    return patterns, total

# Run the program
patterns, total = mullItOver()
print("Patterns:", patterns)
print("Total:", total)

