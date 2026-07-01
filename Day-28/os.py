
'''
import os

#os.mkdir('sample')
#os.makedirs('sample/demo')

path=os.path.join('sample/demo','demo.txt')
with open(path,'w+') as file:
    file.write("Hello world")
    file.seek(0)
    print(file.read())

#os.rmdir('sample/demo')

Hello world

'''


import os

import shutil

print(os.listdir('.'))

os.chdir('../')

print(os.listdir('.'))

print (os.path.abspath('main.py'))

print(os.path.exists('main.py'))

print(os.path.getsize('main.py'))




