students = [
    {'name': '김철수', 'score': 85},
    {'name': '이영희', 'score': 72},
    {'name': '박민수', 'score': 90},
    {'name': '정수진', 'score': 65},
    {'name': '최동현', 'score': 88}
]
# 여기에 들어갈 코드를 작성해주세요.

for student in students:
    if student['score'] >= 80:
        print(student['name'])

# for 반복문으로 students 리스트를 순회한다.
# 각 학생은 딕셔너리이므로 students['score']로 점수에 접근한다.
# if 조건문으로 점수가 80점 이상인지 확인한다.
# 조건을 만족하면 students['name']을 출력한다.