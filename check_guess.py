import random
random_num = random.randint(1,100)
def check_guess():
    n = 0
    while True:
        guess_num = int(input('请输入猜测的数字(1-100):'))
        n = n + 1
        if guess_num <1 or guess_num > 100 :
            print('输入错误,请输入(1-100)中的数字')
            continue
        elif guess_num == random_num:
            print(f'恭喜你,猜对了,你一共猜了{n}次')
            break
        elif guess_num > random_num:
            print('真可惜,猜大了')
        else :
            print('真可惜,猜小了')
check_guess()