'''
#recursive function: A recursive function calls itself in its body.
def func():
    if basecond1:
    return
    func()

def func(num):
    if num ==0:
        return

    print(num,end=" ")
    func(num-1)
    print(num,end=" ")

func(5)

5 4 3 2 1 1 2 3 4 5 



def func(num):
    if num == 0:
        return

    func(num - 1)
    print(num, end=" ")

func(5)

1 2 3 4 5 



def func(num):
    if num == 0:
        return

    print(num, end=" ")
    func(num - 1)

func(5)

5 4 3 2 1



def func(num):
    if num == 0:
        return

    print(num)
    func(num - 1)

func(5)

5
4
3
2
1


def func(num):
    if num == 0:
        return

    print(num, end=" ")
    func(num - 1)

func(15)

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1


# sum

def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(5))

15


# product
def sum(n):
    if n==1:
        return 1
    return n*sum(n-1)

print(sum(5))

120


#Factoral

def sum(n):
    if n == 1:
        return 1
    return n * sum(n - 1)

print(sum(5))


120



# Power

def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
print(power(2,4))

16

power(2,4)
= 2 * power(2,3)
= 2 * 2 * power(2,2)
= 2 * 2 * 2 * power(2,1)
= 2 * 2 * 2 * 2 * power(2,0)
= 2 * 2 * 2 * 2 * 1
= 16




def reverseofstr(s,ind):
    if ind ==0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)

l="Python Programming"
print(reverseofstr(l,len(l)-1))

gnimmargorP nohtyP

'''
def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("Python programming"))


gnimmargorp nohtyP









