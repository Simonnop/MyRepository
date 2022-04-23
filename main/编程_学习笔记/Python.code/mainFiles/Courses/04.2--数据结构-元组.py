# 3.11 元组

'''
    元组 tuple

    元组与列表很像,但是元组不能被修改

    定义:
        元组名=(元素1,元素2,...)
        元组名=元素1,元素2,...

    索引与列表相同: 元组名[位置]

    元素的提取也与列表相同
'''

tuple1=(1,3,5)
tuple2=2,4,6

tuple1
tuple2

x,y,z=tuple1
y

'''
    元组是函数返回多重值的便捷方法
'''

def print_Sum(a=1,b=2):
    return a+b,a*b

a=print_Sum()

type(a),a

'''
    多重赋值 (python风格的变量互换)
'''

x=1
y=2

x,y=y,x

x,y

'''
    元组可以与列表相互嵌套
'''

t=((1,2,3),[2,4,6])

type(t[1])