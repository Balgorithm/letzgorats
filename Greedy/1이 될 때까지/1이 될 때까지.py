import sys
input = sys.stdin.readline

total_cnt = 0 # 총 계산 횟수
n, k = map(int,input().split()) # n,k 입력받기

while n != 1 :  # n이 1이 될때까지 반복
    if n % k == 0:  # k배수면, k로 나눠주기
        n /= k 
    else: # 그렇지 않으면, 1 빼주기
        n -= 1
    total_cnt += 1  # 총 계산횟수 1 증가
print(total_cnt) 
