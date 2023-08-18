# n개의 숫자를 2진수로 변환하여, 1이 많은 갯수를 내림차순으로 정렬할 때, k 번째 위치한 수는!?

# 입력
n, k = map(int, input().split())
num_list = map(int, input().split())

# 본래의 수, 1의 갯수를 가지는 리스트 생성
bin_num_list = []
for x in num_list:
    bin_num_list.append([x, int(str(format(x, 'b')).count('1'))])

# 1의 갯수가 많은 순(index1번째), 동일하면 본래 수가큰수 (index0번째) 내림차순 정렬
bin_num_list.sort(key=lambda x: (x[1], x[0]), reverse=True)

# k번째 (k-1 index) 의 본래의 수 (index 0번째) 출력
print([bin_num_list[i][0] for i in range(n)][k-1])
