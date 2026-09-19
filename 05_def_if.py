def safe_average(data):
    if not isinstance(data, list):
        return "입력은 리스트여야 합니다."

    numbers = [
        item for item in data
        if isinstance(item, (int, float)) and not isinstance(item, bool)
    ]

    if not numbers:
        return 0

    return round(sum(numbers) / len(numbers), 2)

# 테스트 코드
print(safe_average([10, 20, 30, 40, 50]))          # 정상 케이스
print(safe_average([85, 'N/A', 90, None, 78, 92])) # 숫자와 비숫자 혼합
print(safe_average([10, 20.5, '30', 40, 'hello'])) # 문자열 '30'은 무시
print(safe_average(['a', 'b', 'c', None]))         # 숫자 없음
print(safe_average("not a list"))                  # 리스트가 아님
print(safe_average([]))                            # 빈 리스트