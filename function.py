#!/usr/bin/python2
# -*- coding: utf-8 -*- 

def f1():
    print '&2', ;print id(2)
    x=2
    print '&x', ;print id(x)
    y='hello'
    print '&hello', ;print id("hello")
    print '&y', ;print id(y)
def f2():
    x=2
    print '&2', ;print id(2)
    print '&x', ;print id(x)
    x=3
    print '&3', ;print id(3)
    print '&x', ;print id(x)
    L=[1,2,3]
    M=L
    print '&L', ;print id(L)
    print '&M', ;print id(M)
    print '&L[2]', ;print id(L[2])
    L[0]=2
    print '&L', ;print id(L)
    print M
def modify1(m,K):
    m=2
    K=[4,5,6]
    return 
    
def modify2(m,K):
    m=2
    K[0]=0
    return
def f3():
    n=100
    L=[1,2,3]
    modify1(n,L)
    print n
    print L
    modify2(n,L)
    print n
    print L
def f4():
    x=2
    count=2
    while count>0:
        x=3
        print x
        count=count-1
x=2
def fun1():
    print x
def fun2():
    global x
    x=3
    print x
def f5():
    fun1()
    fun2()
    print x

# def display(a,b):
#     print a
#     print b
# display('hello','world')

def display(a='hello',b='wolrd'):
    print a+b
def f6():
    display()
    display(b='world')
    display(a='hello')
    display('world')

def insert(a,L=[]):
    L.append(a)
    print L
def f7():
    insert('hello')
    insert('world')
def storename(name,*nickName):
    print 'real name is %s' %name
    for nickname in nickName:
        print nickname
def f8():
    storename('jack')
    storename(u'詹姆斯',u'小皇帝')
    storename(u'奥尼尔',u'大鲨鱼',u'三不沾')
f8()
def printvalue(a,**d):
    print 'a=%d' %a
    for x in d:
        print x+'=%d' %d[x]
def f9():
    printvalue(1,b=2,c=3)
def function():
    x=2
    y=[3,4]
    return x,y
def f10():
    print function()











