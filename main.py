import contextlib
import datetime

from openpyxl.reader.excel import load_workbook

from helpers import path_to_file

from helpers.find_corresponding_value import exact_equals, new_equals_comb, initial_set_formatting

supposed_amount_cases = 5

flag = True
print('Greetings! Welcome to number counter v0.1!\nCurrently supported formats are - .xlsx, .xlsm, .xltx, .xltm\n')

while flag:
    new_equals = 0
    result_list = []
    user_input = input('Please type "Yes" to to find the target results.\n'
                       'Or "No" to exit the script.\n> ').lower().strip()
    if user_input in ['yes', 'y']:
        begin_time = datetime.datetime.now()
        path, file_name = path_to_file.check_for_datasheets()
        initial_set, initial_target, initial_results = path_to_file.get_dataset(path)
        # load excel file
        # open workbook
        workbook = load_workbook(filename=file_name)
        sheet = workbook.active

        if initial_results:
            for counter, _ in enumerate(initial_results, start=2):
                sheet[f"E{counter}"] = None

        initial_set = initial_set_formatting(initial_set)
        for i in range(supposed_amount_cases, 0, -1):
            print(f'Checking for {i} number target combination..')
            result_list = exact_equals(vals=initial_set, target=initial_target, comb_amount=i)
            if result_list:
                result_list = list(result_list)
                print(f'A {i} way target combination found!')
                break
            else:
                print(f'A {i} way target combination not found..\nChecking for another way.\n')

        if not result_list:
            print('No combinations to reach the target found.\nLooking for the closest, but greater than one.\n')
            with contextlib.suppress(ValueError):
                for i in range(supposed_amount_cases, 1, -1):
                    if new_equals_comb_list := new_equals_comb(vals=initial_set, target=initial_target, comb_amount=i):
                        result_list.append(new_equals_comb_list)
                new_equal_sum_list = [sum(res) for res in result_list]
                new_equals = min(new_equal_sum_list)

            result_list = [i for i in result_list if sum(i) == new_equals][0]
            initial_target = new_equals

        for counter, num in enumerate(result_list, start=2):
            sheet[f"E{counter}"] = num

        if new_equals:
            sheet["F2"] = new_equals
        workbook.save(filename=file_name)
        print('Done!\n')
        print(datetime.datetime.now() - begin_time)
    elif user_input in ['no', 'n']:
        print('See you next time!')
        flag = False
    else:
        print('Invalid input, please try again.')
