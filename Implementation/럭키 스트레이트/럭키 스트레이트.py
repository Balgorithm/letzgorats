import sys
input = sys.stdin.readline

n = input().strip() # 정수를 스트링 형태로 입력받기
half = len(n) //2 # half라는 변수에 n의 길이//2 를 저장 
left = 0   
right = 0
for idx,num in enumerate(n):
    if idx < half:  # idx가 half전까지면, left에 숫자를 더해주고
        left += int(num)
    else: # half부터는 right에 숫자를 더해준다.
        right += int(num)
if left == right :  # 같으면 럭키
    print("LUCKY")
else: # 다르면, 레디
    print("READY")럭
