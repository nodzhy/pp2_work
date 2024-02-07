#__func 1___
#task 1
"""
def change():
    ounce=gramm/28.349
    print(ounce)
gramm=int(input())
change()
"""
#task 2
"""
def cel():
    c=(5/9)*(F-32)
    print(c)
F=int(input())
cel()
"""
#task 3
"""
def solve(head, leg):
    rab_num=0
    chick_num=0
    rab_num=(leg-(2*head))/2
    chick_num=head-rab_num
    print("number of the rabbits ", rab_num, "and number of chicken ", chick_num) 
solve(35, 94)
"""
#task 5
"""
def permutations(s):
    def generate(current, remaining):
        if len(remaining) == 1:
            print(current + remaining[0])
        else:
            for i in range(len(remaining)):
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i+1:]
                generate(new_current, new_remaining)
    generate("", s)
s = input()
permutations(s)
"""
#task 6
"""
def flip():
    word =s.split()
    rev_string=word[::-1]
    string=' '.join(rev_string)
    print(string)
s= input()
flip()
"""
#task 7
"""
def has_33(nums):
    for i in range(len(nums) - 1 ):
      if nums[i] == 3 and nums[i + 1] == 3:
          return True
      elif nums[i] == 3 and nums[i + 1] != 3:
          return False
print(has_33([3, 3, 1]))
print(has_33([1, 1, 3, 3]))
print(has_33([1, 3, 1]))
"""
#task 8
"""
def spy_game(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==0 and nums[i+2]==7:
            return True
        elif nums[i]==3 and nums[i+1]!=0:
            return False
        elif nums[i]==3 and nums[i+1]==0 and nums[i+2]!=7:
            return False

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0]))
"""
#task 9
"""
def cycle():
    V=4/3*(3.14)*R*R*R 
    print(V)
R=int(input())
cycle()
"""
#task 10
"""
def unique_elements(l):
    new_list = []
    i = 0
    while i < len(l):
        t_or_f = True
        j = 0
        while j < i:
            if l[i] == l[j]:
                t_or_f = False
            j += 1
        if t_or_f:
            new_list.append(l[i])
        i += 1
    return new_list

l = input('Enter elements: ')
elements = l.split()
new_list = unique_elements(elements)
print(new_list)
"""
#task 11
"""
def pal():
    new_word=word[::-1]
    if new_word==word:
        print("yes")
    else:
        print("no")
word=str(input())
pal()
"""
#task 12
"""
def histogram():
    numbers = input().split()
    numbers = [int(num) for num in numbers]
    for num in numbers:
        print('*' * num)
histogram()
"""
#task 13
"""
import random
def find_num_random(rand_num, count):
    count += 1
    num = int(input('Take a guess.\n'))
    if num == rand_num:
        print(f'Good job, ', name,'! You guessed my number in {count} guesses!')
        return
    print('\nYour guess is too low.')
    return find_num_random(rand_num, count)

name = input('Hello! What is your name?\n')
number = random.randint(1, 20)
count = 0
print(f'Well, {name}, I am thinking of a number between 1 and 20.\n')
find_num_random(number, count)
"""
