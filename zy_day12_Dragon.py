# coding utf-8
# author: Dragon
# 第一题
# class Student(object):
#     def __new__(cls, *args, **kwargs):
#         print('如果没有调用父类我是不会执行的！~~')
#         return super().__new__(cls)
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return '我的名字是：%s,我的年龄是:%d' % (self.name, self.age)
#
#     def __del__(self):
#         print('程序退出之后我会执行')
#
#     def __call__(self, *args, **kwargs):
#         def work():
#             print('Hello,Can I help you???')
#
#         return work
#
#
# students = Student('dragon', 18)
# students()()
# print(students)

# 第二题
# class Person(object):
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print('外星人在吃东西！~~')
#     def run(self):
#         print('外星人在跑步')
#
# class Student(Person):
#     def __init__(self,name,age,id):
#         self.name = name
#         self.age = age
#         self.id = id
#     def eat(self):
#         print('学生在东西')
#     def study(self):
#         print('学生在学习')
#
# def get_name(person):
#     person.eat()
#     person.run()
#
# p = Person('man')
# s = Student('dragon',18,16210128)
# get_name(p)
# get_name(s)

# 第三题 多态
# class Animal(object):
#     def eat(self):
#         print('动物在吃饭')
#     def drink(self):
#         print('动物在喝牛奶')
#
# class Dog(Animal):
#     def run(self):
#         print('狗在跑')
# a = Animal()
# d = Dog()
#
# def fun(animal):
#     animal.eat()
#     animal.drink()
#     animal.run()
# fun(d)

# 鸭子形态:
class Animal(object):
    def run(self):
        print('动物在跑步')

class Person(object):
    def run(self):
        print('人在跑步')

def fun(object):
    object.run()

a = Animal()
p = Person()

fun(a)
fun(p)