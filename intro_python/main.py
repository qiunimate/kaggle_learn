import utils

def add_three(input):
    output = input + 3
    return output

def append_inplace(input_list, input_value):
    input_list.append(input_value)

def add_multiple(in1, in2):
    output = in1 + in2
    return output

def arithmetic_func(in1, in2, func='add'):
    assert func in ['add', 'sub', 'mul', 'div'] # 'func must be one of add, sub, mul, div'
    if func == 'add':
        return in1 + in2
    elif func == 'sub':
        return in1 - in2
    elif func == 'mul':
        return in1 * in2
    elif func == 'div':
        return in1 / in2

def find_in_list(input_list, input_value):
    """e.g. used for find elemetn in list"""
    for i in input_list:
        if i == input_value:
            return
    print("not found")

if __name__ == '__main__':
    input1 = 3
    input2 = 4
    list_num = [1, 2, 3, 4, 5]

    print("input1: {}".format(input1))
    print("input2: {}".format(input2))
    print('='*20)

    print("return value of add_three(input1): {}".format(add_three(input1)))
    print("input1 after add_three(input1): {}".format(input1))
    print('='*20)

    print("list_num: {}".format(list_num))
    print("return value of append_inplace(list_num, input1): {}".format(append_inplace(list_num, input1)))
    print("list_num after append_inplace(list_num, input1): {}".format(list_num))
    print('='*20)

    print("return value of add_multiple(input1, input2): {}".format(add_multiple(input1, input2)))
    print("return value of arithmetic_func(input1, input2, func='add'): {}".format(arithmetic_func(input1, input2, func='add')))
    print("return value of arithmetic_func(input1, input2, func='sub'): {}".format(arithmetic_func(input1, input2, func='sub')))
    print("return value of arithmetic_func(input1, input2, func='mul'): {}".format(arithmetic_func(input1, input2, func='mul')))
    print("return value of arithmetic_func(input1, input2, func='div'): {}".format(arithmetic_func(input1, input2, func='div')))

