# 재료 갯수가 주어질 때, 최고점 기준으로
# 위, 아래 양방향 모두 앞수를 초과하지 않는다면 총합을, 초과한다면 0을 리턴

# 재료 갯수, 재료 점수 입력받기
n = int(input())
num_list = list(map(int, input().split()))

# 재료점수 총합 구해놓기
answer = sum(num_list)
# 정렬 후 마지막 index 숫자가 제일 큰 점수의 재료
high_num = sorted(num_list)[-1]
# 제일 큰 점수의 재료 index 찾기
index = num_list.index(high_num)
# 현재 재료 직전 점수
pre_num = high_num
# 최고점 이후 재료 검증
for x in range(index+1, n):
    # 이번 index의 재료의 점수가 전 index 보다 크다면 0리턴
    if num_list[x] > pre_num:
        answer = 0
        break
    pre_num = num_list[x]
# 최고점 리셋
pre_num = high_num
# 최고점 이전 재료 검증
for x in range(index-1, 0, -1):
    # 이번 index의 재료의 점수가 전 index 보다 크다면 0리턴
    if num_list[x] > pre_num:
        answer = 0
        break
    pre_num = num_list[x]
print(answer)
