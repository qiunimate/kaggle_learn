from utils import sep

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

# 3
def type_class():
    print("type of int_num: {}".format(type(1)))
    # 3.1
    sep(3.1)
    print("cast 3.14 to int: {}".format(int(3.14)))
    print("cast 3.99 to int: {}".format(int(3.99)))
    print("cast 1 to float: {}".format(float(1)))
    print("cast 1 to bool: {}".format(bool(1)))
    # 3.2
    sep(3.2)
    print("cast 3.14 to bool: {}".format(bool(3.14)))
    print("cast -99 to bool: {}".format(bool(-99)))
    print("cast 0 to bool: {}".format(bool(0)))
    # 3.3
    sep(3.3)
    print("cast '' to bool: {}".format(bool('')))
    print("cast ' ' to bool: {}".format(bool(' ')))
    print("cast 'hello' to bool: {}".format(bool('hello')))
    # 3.4
    sep(3.4)
    str_num = '123'
    print("str_num: {}".format(str_num))
    print("type of str_num: {}".format(type(str_num)))
    print("length of str: {}".format(len(str_num)))
    for char in str_num:
        print("char: {}".format(char))
    # 3.5
    sep(3.5)
    print("cast 'A' to int: {}".format(ord("A")))
    print("cast 65 to char: {}".format(chr(65)))

# 4
def condition_class():
    sep(4.1)
    a = True
    print("a: {}".format(a))
    print("not a: {}".format(not a))
    if not a:   # when the statement after if is True, the next block(before else, you can tell be indent) is executed
        print("a is False")
    else:
        print("a is True")

    sep(4.2)
    i = 1
    while i < 6:
        print(i)
        i += 1
    
    
    for i in range(1, 6):
        print(i)

# 5
def list_class():
    flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold",
                     "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]
    
    # 5.1 indexing
    sep(5.1)
    print("flowers_list 0 (first): {}".format(flowers_list[0]))
    print("flowers_list 1 (second): {}".format(flowers_list[1]))
    print("flowers_list -1 (last): {}".format(flowers_list[-1]))

    # 5.2 slicing
    sep(5.2)
    my_fav_flowers = [*flowers_list[2:5], flowers_list[7]] # * is unpacking operator, to take out elements from list instead of list itself
    my_fav_flowers = flowers_list[2:5] + [flowers_list[7]]
    print("my_fav_flowers: {}".format(my_fav_flowers))

    your_fav_flowers = flowers_list[2:5:2] # the third number stands for the step size
    your_fav_flowers_invert = flowers_list[4:1:-2]
    print("your_fav_flowers: {}".format(your_fav_flowers))
    print("your_fav_flowers_invert: {}".format(your_fav_flowers_invert))

    # 5.3 append
    sep(5.3)
    flowers_list.append("rose") # append to the end of list
    new_flowers_list =  flowers_list.append("lily") # return None because append is inplace
    new_flowers_list = flowers_list + ["lily"] # solution
    




if __name__ == '__main__': 
    # input1 = 3
    # input2 = 4
    # list_num = [1, 2, 3, 4, 5]

    # print("input1: {}".format(input1))
    # print("input2: {}".format(input2))
    # print('='*20)

    # print("return value of add_three(input1): {}".format(add_three(input1)))
    # print("input1 after add_three(input1): {}".format(input1))
    # print('='*20)

    # print("list_num: {}".format(list_num))
    # print("return value of append_inplace(list_num, input1): {}".format(append_inplace(list_num, input1)))
    # print("list_num after append_inplace(list_num, input1): {}".format(list_num))
    # print('='*20)

    # print("return value of add_multiple(input1, input2): {}".format(add_multiple(input1, input2)))
    # print("return value of arithmetic_func(input1, input2, func='add'): {}".format(arithmetic_func(input1, input2, func='add')))
    # print("return value of arithmetic_func(input1, input2, func='sub'): {}".format(arithmetic_func(input1, input2, func='sub')))
    # print("return value of arithmetic_func(input1, input2, func='mul'): {}".format(arithmetic_func(input1, input2, func='mul')))
    # print("return value of arithmetic_func(input1, input2, func='div'): {}".format(arithmetic_func(input1, input2, func='div')))


    # everything is done in functions so that one may choose which function to run
    # type_class()
    # condition_class()
    list_class()
