# 2차원 배열의 구간합 구하기 문제

# D[i][j] 구간 합 공식
# D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j] 

import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # n , m 입력

# 2차원 배열 A 초기화
A = [[0] * (n+1)] 
D = [[0] * (n+1) for _ in range(n+1)] 

for i in range(n): # 배열 A를 입력 받아 초기화
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1,n+1):
    for j in range(1,n+1):
        # 누적 합 공식을 활용하여 D[i][j]를 계산
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 예제 입력된 구간 합 배열 출력
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1 -1]
    print(result)