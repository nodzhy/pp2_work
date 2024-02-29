import re

#task 1
pattern1 = re.compile(r"ab*")
# task 2
pattern2 = re.compile(r"ab{2,3}")
# task 3
pattern3 = re.compile(r"[a-z]+\_")
# task 4
pattern4 = re.compile(r"[A-Z]{1}[a-z]+")
# task 5
pattern5 = re.compile(r"a.+b\Z")
# task 6
pattern6 = re.compile(r"[ ,.]")
# task 7
def snakeToCamel(text):
    camelCase=""
    pattern = re.compile(r"[_]")
    words=pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            camelCase+=word.capitalize()
        else: 
            camelCase += word
    return camelCase
# task 8
def modify(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:  
            res += " " + word
        else:
            res += word
    return res
# task 9
def spaces(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += " " + word
        else:
            res += word
    return res
# task 10
def camel_to_snake(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i == 0:
            res += word.casefold()
        else:
            res += "_" + word.casefold()
    return res
def main():
    print("Task 1")
    print("write words:")
    task1=input()
    print(pattern1.search(task1))

    print("Task 2")
    print("write words:")
    task2=input()
    print(pattern2.search(task2))

    print("Task 3")
    print("write words:")
    task3=input()
    print(pattern3.findall(task3))

    print("Task 4")
    print("write words:")
    task4=input()
    print(pattern4.findall(task4))

    print("Task 5")
    print("write words:")
    task5=input()
    print(pattern5.search(task5))

    print("Task 6")
    text = "gfdjf,fhdsjh..fdskjf fjhgerj,. fds"
    print(pattern6.sub(":", text))

    print("Task 7")
    print("write words:")
    task7=input()
    print(snakeToCamel(task7))

    print("Task 8")
    print("write words:")
    task8=input()
    print(modify(task8))
    
    print("Task 9")
    print("write words:")
    task9=input()
    print(spaces(task9))

    print("Task 10")
    print("write words:")
    task10=input()
    print(camel_to_snake(task10))

if __name__ == "__main__":
    main()