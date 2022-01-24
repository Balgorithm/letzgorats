import sys
input = sys.stdin.readline
from itertools import combinations  # 조합 라이브러리 사용

n = int(input())  # n 입력받기
coin_list = list(map(int,input().split()))  # coin_list

all_case = [] # all_case 라는 빈 리스트 생성 : all_case는 만들 수 있는 모든 금액을 저장하는 리스트
 
for i in range(1,n+1):  # 1부터 n+1까지 돈다
    lst = list(set(combinations(coin_list,i)))  # coin_list중에서 1개~n+1개 조합을 만들고 set화 시켜서 다시 list화 시켜줌
    # value = 0
    for j in lst: # i개로 만든 lst를 돈다.
        value = 0 # value를 0으로 다시 초기화
        value += sum(j) # lst의 합을 value에 저장
        all_case.append(value)  # all_case에 value를 더해준다.
    all_case = list(set(all_case))  # all_case를 set화 시켜주고 다시 list로 바꿔준다.
for idx,answer in enumerate(all_case):  # all_case를 돌면서 
    if idx + 1 != answer :  # idx+1 와 그 수가 다르면, 그 idx+1이 답이다.(그게 만들 수 없는 최솟값이니까)
        print(idx + 1)
        break
