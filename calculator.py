try:
    num1 = float(input('请输入第一个数字:'))
    num2 = float(input('请输入第二个数字:'))
    yunsuanfu = input('请输入运算符:')
    match yunsuanfu:
        case '+':
            print(num1 + num2)
        case '-':
            print(num1 - num2)
        case '*':
            print(num1 * num2)
    if yunsuanfu == '/' and num2 != 0 :
        print(num1 / num2)
    elif yunsuanfu == '/' and num2 == 0 :
        print('输入错误,除数不能为0')
except:
    print('输入错误,请输入数字')