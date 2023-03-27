import time 
def timer_decor(input_func):
    def output_func(*args):
        start = time.time()
        input_func(*args)
        print(time.time() - start)
    return output_func

@timer_decor
def summ(x,y)-> None:
    return print(x+y)
@timer_decor
def txt_summ()-> None:
    input = open('Задача 5\input.txt','r').read().split(', ')
    output = open('Задача 5\output.txt','w')
    output.write(str(float(input[0]) + float(input[1])))
    pass

summ(100, 20)
txt_summ()