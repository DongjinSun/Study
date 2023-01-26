# 로그의 가장 앞부분은 식별자다.
# 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순으로 한다.
# 숫자로그는 입력순서대로 한다.
# 입력 : [ 'dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']
# 출력 : [ 'let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']

import doctest
import time
import collections
import heapq

class log_:
    def __init__(self,l):
        self.l = l
        l = l.split()
        self.i = l[0]
        self.log = " ".join(l[1:])
    
    def __lt__(self, other):
        if self.log[0].isnumeric():
            return False
        if self.log < other.log:
            return True
        elif self.log == other.log:
            if self.i < other.i:
                return True
            else:
                return False
        else:
            return False
    def __call__(self,l):
        return l

def Sol(s:list):
    """
    >>> Sol([ 'dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero'])
    ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
    """
    n = len(s)
    s_w=[]
    s_n=[]
    s_res = []
    for k in s:
        if k.split()[1].isalpha():
            heapq.heappush(s_w,log_(k))
        else:
            heapq.heappush(s_n,log_(k))
    for _ in range(len(s_w)):
        i = heapq.heappop(s_w)
        s_res.append(i.l)

    for _ in range(len(s_n)):
        i = heapq.heappop(s_n)
        s_res.append(i.l)
    return s_res

def Sol2(s:list): ## 43ms
    """
    >>> Sol2([ 'dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero'])
    ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
    """
    return sorted(s,key=lambda x : ((0,x.split()[1:],x.split()[0]) if x.split()[1].isalpha() else (1,)))
    

def example(s:list): ## 38ms
    """
    >>> example([ 'dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero'])
    ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
    """
    letters, digits = [],[]
    for log in s:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x: (x.split()[1:],x.split()[0]))
    return letters + digits

def time_check(f,s): 
    import time
    start = time.perf_counter()
    for i in range(100000):
        f(s)
    end = time.perf_counter()
    print(f"Function {f} time = {(end-start)*1000:.3f}ms")

if __name__ == "__main__":
    doctest.testmod()
    time_check(Sol,[ 'dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero'])
    time_check(Sol2,[ 'dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero'])
    time_check(example,[ 'dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero'])
        
    