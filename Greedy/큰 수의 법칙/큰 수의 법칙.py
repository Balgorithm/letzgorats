'''풀이 방법 1'''
import sys
input = sys.stdin.readline # input()보다 빠르다. 습관화

# (n : 자연수 ,m : 숫자가 총 더해지는 횟수, k: 연속 k번을 초과해서 더할 수 없는 수 k) 입력받기 - map, int, input().split() 사용 
n, m, k = map(int,input().split())
numbers = list(map(int,input().split())) # 숫자 배열 입력받기
biggest_num, second_num = sorted(numbers)[-1], sorted(numbers)[-2] # 어차피 제일 큰 수랑 그 다음 큰 수 밖에 안 쓰인다.
answer = (m // k) * k * biggest_num + (m % k) * second_num # 규칙성 찾고 적용- (묶음 개수를 최댓값과 곱해주고 나머지 사잇값들을 second 값으로 채워주면) 최대값 나온다.
print(answer) 

'''풀이 방법 2'''
import sys
from collections import deque # 방법 생각해봤는데 굳이 더하고 빼고 반복안해도 된다.
# dq = deque(numbers[-2:]) # 최댓갑과 그 다음으로 큰 값이 담긴 덱 dq가 생성된다.
input = sys.stdin.readline

n, m, k = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
biggest = numbers[-1]
second = numbers[-2]
answer = 0

num = biggest   # 맨 처음은 num을 biggest로 설정
biggest_check = True # num이 현재 biggest인지 판별하는 변수 True
go_to_answer = False # while문 탈출 조건식
i = 0
while i < m: # m번 반복
  if not biggest_check :
    answer += num #  여기서 num은 second
    num = biggest # 한번만 second를 더해주고 다시 num을 biggest로 갱신
    i += 1 # 1번 수행
  for _ in range(k):
    if i+1 > m:
        break
        go_to_answer = True
    answer += num
    i += 1
  if go_to_answer :
      break
  num = second # biggest를 k번 더했으면
  biggest_check = False
print(answer)
