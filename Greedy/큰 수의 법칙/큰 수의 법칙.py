import sys
input = sys.stdin.readline # input()보다 빠르다. 습관화

# n,m,k 입력받기 - map, int, input().split() 사용
n, m, k = map(int,input().split())
numbers = list(map(int,input().split())) # 숫자 배열 입력받기
biggest_num, second_num = sorted(numbers)[-1], sorted(numbers)[-2] # 어차피 제일 큰 수랑 그 다음 큰 수 밖에 안 쓰인다.
answer = (m // k) * k * biggest_num + (m % k) * second_num # 규칙성 찾고 적용
print(answer) 
