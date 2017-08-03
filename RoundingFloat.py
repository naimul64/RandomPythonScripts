import random
import datetime


def round_float_to_decimal_place(decimal_place, floating_no):
    floating_no_backup = floating_no

    if type(floating_no) == type(9):
        floating_no = float(str(floating_no) + '.0')

    if floating_no >= 1:
        divby2 = 100
        while divby2 != 0:
            divby2 = floating_no / 2
            divby2 = int(divby2)
            if divby2 >= 1:
                floating_no -= divby2
        floating_no -= 1

    back_to_fraction = rounding_fraction(floating_no, decimal_place)

    rounded_float = float(int(floating_no_backup))
    rounded_float += back_to_fraction

    return rounded_float

def rounding_fraction(floating_no, decimal_place):
    for i in range(decimal_place + 1):
        floating_no *= 10
    fractionIntoInt = int(floating_no)
    if fractionIntoInt % 10 > 4:
        fractionIntoInt = int(fractionIntoInt / 10)
        fractionIntoInt += 1
    else:
        fractionIntoInt = int(fractionIntoInt / 10)
    back_to_fraction = float(fractionIntoInt)
    for i in range(decimal_place):
        back_to_fraction /= 10

    return back_to_fraction


def generate_test_case(test_case_size):
    test_case_list = []

    for i in range(test_case_size):
        test_case_list.append(random.uniform(0.0, 100.0))

    return test_case_list

def run_test(test_case_list):
    for flt in test_case_list:
        round_float_to_decimal_place(decimal_place=2, floating_no=flt)

def run_test_by_python_build_in(test_case_list):
    for flt in test_case_list:
        round(flt, 2)


def Main():

    start_time = datetime.datetime.now()
    test_case_list = generate_test_case(15000000)
    end_time = datetime.datetime.now()
    print "Time taken to generate test case: " + str(end_time - start_time) + " sec."

    start_time = datetime.datetime.now()
    run_test(test_case_list=test_case_list)
    end_time = datetime.datetime.now()
    print "Time taken by my rounding function: " + str(end_time - start_time) + " sec."

    start_time = datetime.datetime.now()
    run_test_by_python_build_in(test_case_list=test_case_list)
    end_time = datetime.datetime.now()
    print "Time taken my python's rounding function: " + str(end_time - start_time) + " sec."

Main()