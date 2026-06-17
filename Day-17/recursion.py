'''
def display(s,ind):
    if ind == len(s):
        return
    print(s[:ind+1])
    display(s,ind+1)

display("python",0)


p
py
pyt
pyth
pytho
python




##Print Reverse String Pattern
#abcdef,3-> abc,bcd,cde,def
#abcdef,4->abcd,bcde,cdef



def display(s, ind, l):
    if ind == len(s) - l + 1:
        return
    print(s[ind:ind+l])
    display(s, ind + 1, l)

display("python Programming", 0, 7)


python 
ython P
thon Pr
hon Pro
on Prog
n Progr
 Progra
Program
rogramm
ogrammi
grammin
ramming


def display(l, ind):
    if ind == len(l):
        return 0
    return l[ind] + display(l, ind + 1)

l = [1, 2, 4, 5, 7, 3, 5, 6]
print(display(l, 0))

33

'''
def display(s, i):
    if i == len(s):
        return 0

    if s[i] in 'aeiouAEIOU':
        return 1 + display(s, i + 1)
    else:
        return display(s, i + 1)

s = "python programming"
print(display(s, 0))

4

'''
