n = input() # 첫 째줄 입력
myList = list(map(int,input().split())) # 공백 구분된 정수를 입력받아 리스트로 저장

myMax = max(myList) # 최댓값
sum = sum(myList) # 리스트 합 저장

print(sum * 100 / myMax / int(n)) # 계산식: (리스트의 합 * 100) / (리스트의 최댓값 * 리스트의 길이)
