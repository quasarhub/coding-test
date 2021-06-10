# 모든 원소의 값이 0 보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0 으로 초기화): 하나 큰 값으로 리스트 생성
count_list = [0] * (max(array) + 1)

for i in range(len(array)):
    count_list[array[i]] += 1      # 정렬되지 않은 각 값에 해당하는 인덱스의 값 증가

for i in range(len(count_list)):   # 리스트에 기록된 정렬 정보 확인
    for j in range(count_list[i]):
        print(i, end=' ')          # 등장한 횟수만큼 인덱스 출력
