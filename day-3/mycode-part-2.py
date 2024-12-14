import re
class MullItOverPartTwo:
    def __init__(self):
        self.text_input = ''
        with open('input.txt', 'r') as f:
            for line in f.readlines():
                self.text_input += line
        
        self.find_valid_instructions()
        self.part2 = 0
    

    def find_valid_instructions(self):
        self.valid_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", self.text_input)
    

    def process_multiplications(self):
        is_mul = True
        for instr in self.valid_instructions:
            print(instr)
            if instr == 'do()':
                is_mul = True
            elif instr == 'don\'t()':
                is_mul = False
            elif is_mul:
                nums = re.findall(r'\d{1,3}', instr)
                self.part2 += int(nums[0]) * int(nums[1])

if __name__ == '__main__':
    sol = MullItOverPartTwo()
    sol.process_multiplications()
    print(sol.part2)
