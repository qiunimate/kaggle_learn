# import utils

def add_three(input):
    output = input + 3
    return output

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

    # res1 = add_multiple(input1, input2)
    # res2 = arithmetic_func(input1, input2, func='asfdsv')
    res3 = find_in_list(list_num, 3)
    print(res3)