#task 1
"""
first_list=[]
print("количество элементов листа")
n=int(input())

print("напишите ваши элементы")

for i in range(n):
    number=int(input())
    first_list.append(number)

print("напиши на сколько умножить элементы")
times=int(input())
new_list=list(map(lambda x : x * times, first_list))

print(new_list)
"""
#task 2
"""
first_list=[]
print("количество слов")
number=int(input())
print("напишите слова")

for i in range(number):
   word=input()
   first_list.append(word)

def count(x):
    cnt = 0
    for letter in x:
       if letter.isupper():
            cnt +=1
    return cnt

def count2(x):
    cnt=0
    for letter in x:
        if letter.islower():
            cnt+=1
    return cnt

new_list=list(map(count, first_list))
print("количество заглавных букв: ", new_list)
new2_list=list(map(count2, first_list))
print("количество прописных букв: ", new2_list)
"""
#task 3
"""
print("напишите слово")
word=input()
reversed_word= ''.join(reversed(word))
if word==reversed_word:
    print("true")
else:
    print("false")
"""
#task 4
"""
import math
from time import sleep
number=int(input())
speed_mls=int(input())
speed_sec=float(speed_mls/1000)
sqr=float(math.sqrt(number))
sleep(speed_sec)
print("Square root of ", number, " after ", speed_mls, " miliseconds is ", sqr)
"""
#task 5
"""
mytup = (True, True, False)
mytup2 = (True, True, True)
print(all(mytup))
print(all(mytup2))
"""