def checking_current_list(current_list):
    is_increasing = None
    for i in range(len(current_list) - 1):
        diff = current_list[i] - current_list[i + 1]

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if diff > 0:
            if is_increasing is None:
                is_increasing = True
            elif not is_increasing:
                return False
        if diff < 0:
            if is_increasing is None:
                is_increasing = False
            elif is_increasing:
                return False
    return True


def red_nosed_reports():
    total_safe_reports = 0
    while True:
        report_input = input()
        if report_input == "done":
            break
        try:
            current_list = list(map(int, report_input.split()))
            if checking_current_list(current_list):
                total_safe_reports += 1
        except ValueError:
            print("Please provide number values seperated by a space.")

    return total_safe_reports


sol = red_nosed_reports()
print(sol)
