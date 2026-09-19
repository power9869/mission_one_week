# 여기에 들어갈 코드를 작성해주세요.

def sum_even(number):
    total = 0
    for num in number:
        if num % 2 == 0:
            total += num
    return total

result1 = sum_even([1,2,3,4,5,6])
print(result1) #12(2+4+6)

result2 = sum_even([10,15,20,25,30])
print(result2) #60(10+20+30)

result3 = sum_even([1,3,5,7])
print(result3) #0(짝수 없음)

# 힌트
# def 키워드로 함수를 정의하고, 매개변수 number를 받는다.
# 합계를 저장할 변수를 0으로 초기화한다.
# for 반복문으로 리스트를 순회하여 짝수인지 확인한다.
# 짝수 판별 : num%2==0(2로 나눈 나머지가 0이면 짝수)
# return으로 합계를 반환한다.

# 출력 예시
# 12
# 60
# 0