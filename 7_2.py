## 비가 온후 얼마나 많은 물이 쌓일 수 있는지
## 입력 [0,1,0,2,1,0,1,3,2,1,2,1]
## 출력 6

import collections

def Sol(s:list)->int:
    d = list()
    counter = 0
    for i,k in enumerate(s):
        if k>0:
            if not len(d):
                d.append([k,i])
            else:
                pre = 0 
                while len(d):
                    if d[-1][0]<=k:
                        cur = d.pop()
                        counter +=(i-cur[1]-1)*(cur[0]-pre)
                        pre = cur[0]
                    else:
                        cur = d[-1]
                        counter +=(i-cur[1]-1)*(k-pre)
                        break
                d.append([k,i])
    return counter




if __name__ == "__main__":
    print(Sol([4,2,0,3,2,5]))
    
        
    