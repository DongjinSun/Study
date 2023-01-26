## 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라
## 입력 : [-1,0,1,2,-1,4]
## 출력 : [[-1,0,1],[-1,-1,2]]


def Sol(nums:list)->list:
    n=len(nums)
    res = []
    temp = set()
    for i in range(n):
        d = set()
        temp2 = set()
        if nums[i] in temp:
            continue
        for j in range(i+1,n):
            if nums[j] in temp or nums[j] in temp2:
                continue
            if -(nums[i]+nums[j]) in d:
                res.append([nums[i],nums[j],-(nums[i]+nums[j])])
                temp2.add(nums[j])
                temp2.add(-(nums[j]+nums[i]))
            d.add(nums[j])
        temp.add(nums[i])
                
    return res


def Sol2(nums:list)->list:
    n=len(nums)
    nums=sorted(nums)
    res = []
    temp = set()
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        target = nums[i]
        j=i+1
        k=n-1
        while j<k:
            if nums[i]+nums[j]+nums[k]>0:
                while k>j+1 and nums[k]==nums[k-1]:
                    k-=1
                k-=1
            elif nums[i]+nums[j]+nums[k]<0:
                while j<k-1 and nums[j]==nums[j+1]:
                    j+=1
                j+=1
            else:
                res.append([nums[i],nums[j],nums[k]])
                while j<k-1 and nums[j]==nums[j+1]:
                    j+=1
                j+=1
                while k>j+1 and nums[k]==nums[k-1]:
                    k-=1
                k-=1
    return res

import collections
def Sol3(nums:list)->list:
    neg = collections.defaultdict(int)
    pos = collections.defaultdict(int)
    res = []
    zero = 0
    for i in nums:
        if i > 0:
            pos[i]+=1
        elif i < 0:
            neg[i]+=1
        else:
            zero+=1
    if zero>2:
        res.append([0,0,0])
        
    for i,p in enumerate(neg.keys()):
        if zero and neg[p]>0:
            if -p in pos:
                res.append([p,0,-p])
        if neg[p]>1:
            if -p*2 in pos:
                res.append([p,p,-p*2])
        for q in list(neg.keys())[i+1:]:
            if -(p+q) in pos:
                res.append([p,q,-(p+q)])
    
    for i,p in enumerate(pos.keys()):
        if pos[p]>1:
            if -p*2 in neg:
                res.append([p,p,-p*2])
        for q in list(pos.keys())[i+1:]:
            if -(p+q) in neg:
                res.append([p,q,-(p+q)])
        
    return res


if __name__ =="__main__":
    print(Sol3([-1,0,1,2,-1,-4]))            
        