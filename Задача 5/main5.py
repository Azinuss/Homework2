import time 
def timerdecor(input_func):
    def output_func(*args):
        start = time.time()
        input_func(*args)
        print(time.time() - start)
    return output_func

@timerdecor
def summ(x,y):
    return print(x+y)
@timerdecor
def txtsumm():
    input = open('Задача 5\input.txt','r').read().split(', ')
    output = open('Задача 5\output.txt','w')
    output.write(str(float(input[0]) + float(input[1])))
    pass

summ(100, 20)
txtsumm()