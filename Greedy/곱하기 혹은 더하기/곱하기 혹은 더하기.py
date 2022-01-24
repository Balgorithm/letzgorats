import sys
input = sys.stdin.readline

number_str = input().replace('0','').strip()  # 0은 어차피 필요가 없으니까 없애준다.
answer = int(number_str[0]) # 처음 값
for num in number_str[1:]:  # number_str를 1번째부터 돌면서 
    if answer + int(num) > answer * int(num): # 더한 값이 곱한 값보다 크면 
        answer += int(num) # 더해주고
    else: # 안 크면 
        answer *= int(num)  # 곱해준다.
print(answer)
