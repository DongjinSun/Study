## 가장 긴 팰린드롬 부분 문자열
## 입력 "babad"
## 출력 "bab"
## 입력 "cbbd"
## 출력 "bb"

from pprint import pprint

#Dynamic programing
def Sol(s:str):
    n = len(s)
    # b = [[0]*n for _ in range(n)]
    # for i in range(n):
    #     b[i][i] = 1
    if len(s)<2 or s == s[::-1]:
        return s
    b = [0]*n
    m = 0
    maxij = [0,0]
    # for i in range(n): ## 마지막
    #     for j in range(i): ## 처음
    #         if s[i]==s[j]:
    #             if j+1<i-1:
    #                 b[i][j] = b[i-1][j+1]
    #             else:
    #                 b[i][j] = 1
    #             if b[i][j] and m < i-j+1:
    #                 m = i-j+1
    #                 maxij = [j,i]
    for i in range(n): ## 마지막
        for j in range(i+1): ## 처음
            if s[i]==s[j]:
                if j+1<i-1:
                    b[j] = b[j+1]
                else:
                    b[j] = 1
                if b[j] and m < i-j+1:
                    m = i-j+1
                    maxij = [j,i]
            else:
                b[j]=0
            print(b)
    return s[maxij[0]:maxij[1]+1]
                    
def example(s:str):
    def expand(left: int, right: int) ->str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    if len(s) <2 or s==s[::-1]:
        return s
    result = ""
    for i in range(len(s)-1):
        result = max(result,expand(i,i+1),expand(i,i+2),key=len)
    return result


def time_check(f,s): 
    import time
    start = time.process_time()
    for i in range(100000):
        f(s)
    end = time.process_time()
    print(f"Function {f} time = {(end-start)*1000:.3f}ms")

if __name__ == "__main__":
    print(Sol("abdka"))
    # time_check(Sol,"babad")
    # time_check(example,"babad")