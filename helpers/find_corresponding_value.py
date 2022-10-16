import itertools
from numpy import array


def closest_value(myArr, myNumber):
    myArr = array(myArr)
    return myArr[myArr == myNumber] or myArr[myArr > myNumber].min()


def initial_set_formatting(init_set: list) -> list:
    set_dict = {val: init_set.count(val) for val in init_set}
    updated_set_dict = set_dict.copy()
    for key, value in set_dict.items():
        if value > 5:
            updated_set_dict[key] = 5
    updated_init_set = []
    for key, value in updated_set_dict.items():
        updated_init_set.extend(key for _ in range(value))

    return updated_init_set


def check_for_initial_equals(vals, comb_num, target):
    for a in itertools.combinations(vals, comb_num):
        if sum(a) == target:
            return list(a)


# checking every possible comb of missing nums
def exact_equals(vals, target, comb_amount):
    if comb_amount in [2, 3, 4, 5]:
        return check_for_initial_equals(vals, comb_amount, target)
    return [a for a in vals if a == target]


def get_min_of_new_equals(results_list, target):
    sum_res = [sum(i) for i in results_list]
    min_res = closest_value(sum_res, target)
    return [i for i in results_list if sum(i) == min_res][0]


def new_equals_comb_count(vals, comb_count, target):
    new_min = 0
    min_diff_comb = 0
    print(f'looking for a {comb_count}  way comb..')
    for a in itertools.combinations(vals, comb_count):
        if sum(a) > target:
            if not new_min:
                new_min = sum(a)
            if new_min >= sum(a):
                new_min = sum(a)
                min_diff_comb = list(a)
            else:
                continue
    return min_diff_comb


# new equals combination check
def new_equals_comb(vals, target, comb_amount):
    if comb_amount in [2, 3, 4, 5]:
        return new_equals_comb_count(vals, comb_amount, target)
    return
