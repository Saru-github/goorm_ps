# 무게와 반복 횟수가 주어 질때, 1RM 에 대한 값을 구하여라.

# 무게와 반복 횟수 입력 받기
W, R = map(int, input().split())
# 1RM 구하는 식 적용 및 소수점 제거
RM = int(W * (1 + R / 30))
# 1RM 출력
print(RM)
