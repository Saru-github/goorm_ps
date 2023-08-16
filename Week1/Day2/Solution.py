# 작업물 갯수, 현재 시간, n개의 작업물 소요시간이 주어질 때, 작업이 완료된 시점의 시각을 구하시오.

# 작업물의 갯수
n = int(input())
# 현재 시, 분
cur_hour, cur_minute = map(int, input().split())
# n개의 작업물이 걸리는 시간의 리스트
taken_time_list = [int(input()) for _ in range(n)]
# 총 작업물 소요시간 + 현재분 
total_minute = sum(taken_time_list) + cur_minute

# 작업물을 마친 분, 시 구하기
end_minute = total_minute % 60
end_hour = cur_hour + total_minute // 60

# 시 가 24가 넘어 갔을 땐, 0으로 리셋
if end_hour >= 24:
    end_hour %= 24

print(end_hour, end_minute)
