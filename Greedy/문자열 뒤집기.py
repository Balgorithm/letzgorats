import sys
input = sys.stdin.readline

str = input().strip() # 스트링을 입력받기
number = str[0] # 첫 숫자를 number라는 변수에 저장
flip = 0  # flip 초기값 0으로 저장
for i in str: # 스트링을 돌면서 
    if number != i : # number가 현재 가리키는 숫자(i)와 다르면 
        flip += 1 # flip 수 1 증가 
        number = i  # number도 i로 갱신
        
if flip % 2 == 0:   # flip이 짝수면
    print(flip//2)    # flip//2 이 정답
else:   # flip이 홀수면
    print(flip//2 + 1)    # flip//2 + 1 이 정답
