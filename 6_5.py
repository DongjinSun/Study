# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
# 입력 : ['eat','tea', 'tan', 'ate', 'nat' ,'bat']
# 출력 : [['ate','eat','tea'],['nat','tan'],['bat']]
# collections.defualtdict() 를 통하면 
# 일반적으로 python에 내장 sort를 사용하는것이 가장 빠름.

import doctest
import collections

def Sol(s:list):
    i=0
    t = ""
    # d = dict()
    d = collections.defaultdict(list)
    for i in s:
        # try: 
        d["".join(sorted(i))] += [i] ## 딕셔너리의 키의 원소는 변형이 불가능한 값이어야 한다.

        # except:
        #     d["".join(sorted(i))]=[i] ## collections.defualtdict()를 사용하면 에러가 발생하지 않음

    return [_ for _ in d.values()]

if __name__ == "__main__":
    print(Sol(['eat','tea', 'tan', 'ate', 'nat' ,'bat']))

