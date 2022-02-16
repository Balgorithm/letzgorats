import sys
input = sys.stdin.readline

n = int(input())  # n 입력받기 
answer = 0  
for h in range(n+1):  # h는 0시부터 n+1시 바로 직전까지
    for m in range(60): # m은 0분부터 59분까지
        for s in range(60): # s는 0초부터 59초까지
            if '3' in str(h) + str(m) + str(s): # str(h)에 3 이 있거나 str(m)에 3이 있거나 str(s)에 3이 있거나를
                answer += 1       # 아예 "str(h) + str(m) + str(s) 를 하나로 스트링화해서 거기서 3이 있으면"으로 해도 같은 말이다.
print(answer)
