# dict_infor = {name:{age:sex},...}
dict_infor = {}
# 创建菜单
menu = '''
#############用户信息管理系统#############
#           1.添加/修改用户信息          #
#           2.查询用户信息              #
#           3.删除用户信息              #
#           4.退出系统                 #
#######################################
'''
print(menu)
# 用户操作

def add():
    try:
        name = input('请输入新的姓名').strip()
        age = int(input('请输入新的年龄'))
        sex = input('请输入新的性别')
        dict_infor[name] = {'年龄':age,'性别':sex}
        print('添加/修改成功')
    except ValueError:
        print('输入错误,请重新输入')

def check():
    name = input('请输入查询的用户姓名').strip()
    if name not in dict_infor:
        print('未查询到用户信息,请重新操作')
    else:
        check_infor = dict_infor[name]
        print(f'查询的用户姓名为{name},年龄{check_infor['年龄']},性别{check_infor['性别']}')

def del_():
    name = input('请输入要删除的用户姓名').strip()
    if name not in dict_infor:
        print('未查询到用户信息,请重新操作')
    else:
        del (dict_infor[name])
        print('删除成功')

while True:
    try:
        choice = int(input('请输入要使用的操作(1-4):'))
        if choice == 1:
            add()
        elif choice == 2:
            check()
        elif choice == 3:
            del_()
        elif choice == 4:
            print('退出系统,bye~')
            break
        else:
            print('输入错误,请输入1-4')
    except ValueError:
        print('输入错误,请输入数字')