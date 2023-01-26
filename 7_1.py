## 두 수의 합
## nums = [2,7,11,15], target = 9
## 출력 : [0,1]

import doctest

def Sol(nums:list,target:int)-> list:
    """
    >>> Sol([2,7,11,15],9)
    [0, 1]
    """

    for i,k in enumerate(nums):
        n = target - k
        if n in nums:
            return [i,nums.index(n)]
    return []

def Sol2(nums:list,target:int)-> list:
    """
    >>> Sol2([2,7,11,15],9)
    [0, 1]
    """
    nums_d= dict(zip(nums,range(len(nums))))
    for i,k in enumerate(nums):
        n = target - k
        if n in nums_d and nums_d[n]!=i:
            return [i,nums_d[n]]
    return []

def Brute_Force(nums:list,target:int)->list:
    """
    >>> Brute_Force([2,7,11,15],9)
    [0, 1]
    """
    for i,k in enumerate(nums):
        for j,q in enumerate(nums[i+1:]):
            if k+q == target:
                return [i,j]

def time_check(f,nums,target): 
    import time
    start = time.process_time()
    for i in range(100000):
        f(nums,target)
    end = time.process_time()
    print(f"Function {f} time = {(end-start)*1000:.3f}ms")



if __name__ == "__main__":
    # time_check(Sol,[2,7,11,15],9)
    # time_check(Sol2,[2,7,11,15],9)
    # time_check(Brute_Force,[2,7,11,15],9)
    # doctest.testmod()
    # time_check(example,"babad")
    print(Sol2([3,3],6))