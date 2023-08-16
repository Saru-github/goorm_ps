# 첫 줄에는 식의 갯수가 주어지고, 다음 t개의 문제식이 주어질 때, 모두 계산한 값을 출력하시오.
# 식의갯수 입력받기
t = int(input())
anser = 0
# 한 줄씩 식 입력받기, 나머지처리를 위한 int식 적용 
for i in range(t):
    anser += int(eval(input()))
print(anser) 
