# N개의 합 출력

n = input() # 첫 번째 줄 입력
numbers = list(input()) # 입력한 갯수 만큼 numbers 배열 생성

sum = 0 # 합 구하기

for i in numbers : # numbers 배열 순회
    sum += int(i) # 형 변환

print(sum)