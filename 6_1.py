## 입력 : "A man, a plan, a canal: Panama"
## 출력 : True
## 입력 : "race a car"
## 출력 : false
## 대소문자 구분 X , 영문자와 숫자만을 대상
## leetcode 125

## 문자열이나 리스트를 처리할 경우 슬라이싱을 활용하여 처리하는 것이 제일 빠름 (C 내부 코드 사용)
## 정규식을 사용하는 것이 list comprehension 보다 빠름


import doctest
import collections
import re

def Sol(s : str): #45ms
    """
    >>> Sol("A man, a plan, a canal: Panama")
    True
    >>> Sol("race a car")
    False
    >>> Sol("")
    True
    >>> Sol("a")
    True
    """
    # s = [i.lower() for i in s if i.isalnum()] ## 529ms
    s = s.lower()  
    s = re.sub('[^a-z0-9]',"",s)
    for i in range(len(s)//2):
        if s[i] != s[~i]:
            return False
    return True

def Sol_(s : str): ## 54ms
    """
    >>> Sol("A man, a plan, a canal: Panama")
    True
    >>> Sol("race a car")
    False
    >>> Sol("")
    True
    >>> Sol("a")
    True
    """
    s = [i.lower() for i in s if i.isalnum()] ## 529ms
    # s = s.lower()  
    # s = re.sub('[^a-z0-9]',"",s)
    for i in range(len(s)//2):
        if s[i] != s[~i]:
            return False
    return True


def Sol2(s : str): ##47ms
    """
    >>> Sol2("A man, a plan, a canal: Panama")
    True
    >>> Sol2("race a car")
    False
    >>> Sol2("")
    True
    >>> Sol2("a")
    True
    """
    d = collections.deque()
    for i in s:
        if i.isalnum():
            d.append(i.lower())
    while len(d)>1:
        if d.popleft() != d.pop():
            return False
    return True

def Sol3(s:str):
    # s = s.lower()  
    # s = re.sub('[^a-z0-9]',"",s)
    s = [i.lower() for i in s if i.isalnum()]
    return s==s[::-1]

def Sol3_(s:str): ##40ms
    s = s.lower()  
    s = re.sub('[^a-z0-9]',"",s)
    # s = [i.lower() for i in s if i.isalnum()]
    return s==s[::-1]

def time_check(f,s): 
    import time
    start = time.process_time()
    for i in range(100000):
        f(s)
    end = time.process_time()
    print(f"Function {f} time = {(end-start)*1000:.3f}ms")
    



if __name__ == "__main__":
    doctest.testmod()
    time_check(Sol,"A man, a plan, a canal: Panama")
    time_check(Sol_,"A man, a plan, a canal: Panama")
    time_check(Sol2,"A man, a plan, a canal: Panama")
    time_check(Sol3,"A man, a plan, a canal: Panama")
    time_check(Sol3_,"A man, a plan, a canal: Panama")
