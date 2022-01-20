import sys
input = sys.stdin.readline

n, m, k = input()
numbers = list(map(int,input().split()))
sorted_numbers = sorted(numbers)[-2:]
answer = 0
if k <=2 :
  print(sorted_numbers[-1] * k)
else:
  for num in sorted_numbers:
    answer += num
         
