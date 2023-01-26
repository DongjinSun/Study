import doctest

## inplace에 대해서 고민해보기
## 가변인자가 들어가면 주소값 그대로 들어감 --> 포인터랑 비슷


## 입력 ["h","e","l","l","o"]
## 출력 ["o","l","l","e","h"]
## 입력 ["H","a","n","n","a","h"]
## 출력 ["h","a","n","n","a","H"]

## leetcode 344

def Sol(s): ## 198
    # print(id(s))
    s[:]=s[::-1]
    # print(id(s))


def Sol2(s:str): #202
    s.reverse()

def time_check(f,s): 
    import time
    start = time.process_time()
    for i in range(100000):
        f(s)
    end = time.process_time()
    print(f"Function {f} time = {(end-start)*1000:.3f}ms")

def main(s):
    """
    >>> main(["h","e","l","l","o"])
    ['o', 'l', 'l', 'e', 'h']
    """
    Sol(s)
    return s
    



if __name__ == "__main__":
    doctest.testmod()
    time_check(Sol,"A man, a plan, a canal: Panama")
    # s = ["h","e","l","l","o"]
    # print(id(s))
    # Sol(s)
    # print(s)
