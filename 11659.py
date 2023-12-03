# 구간합 구하기
# 문제
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 
# 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

# 출력
# 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

import sys
input = sys.stdin.readline

suNo, quizNo = map(int,input().split()) # 입력으로 주어지는 수의 개수 N과 합을 구해야 하는 횟수 M를 받아옴

numbers = list(map(int,input().split())) # 수열로 주어지는 N개의 수를 리스트로 받아옴

prefix_sum = [0] # 누적 합을 저장할 배열 초기화

temp = 0

for i in numbers : # 누적 합 배열을 계산
    temp += i
    prefix_sum.append(temp) # 합 배열 만들기


for i in range(quizNo) : # 합 배열을 활용하여 구간 합을 계산하고 출력
    s, e = map(int , input().split())
    print(prefix_sum[e] - prefix_sum[s - 1]) # 합 배열에서 구간 합 구하기