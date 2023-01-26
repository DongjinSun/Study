## 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
## 대소문자 구분을 하지 않음
## 구두점 무시.

import collections
import re
import doctest
def Sol(s:str,b:list):
    """
    >>> Sol("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"])
    'ball'
    """
    s = s.lower()
    s = re.sub("[^a-z ]","",s)
    s = [_ for _ in s.split() if _ not in b]
    c = collections.Counter(s)
    return max(c,key=c.get)


if __name__ == "__main__":
    doctest.testmod()
