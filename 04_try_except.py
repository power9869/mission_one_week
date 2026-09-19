students = {
	101 : {'name' : '김철수', 'score' : 85},
	102 : {'name' : '이영희', 'score' : 92},
	103 : {'name' : '박민수', 'score' : 67},
	104 : {'name' : '정수진', 'score' : 55},
	105 : {'name' : '최동현', 'score' : 78}
}

# 여기에 들어갈 함수를 작성해주세요.
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def get_student_info(students, student_id):
    try:
        student_id = int(student_id)
    except (ValueError, TypeError):
        return "유효하지 않은 ID 형식입니다."		

    try:
        student = students[student_id]
    except KeyError:
        return "해당 ID의 학생이 존재하지 않습니다."

	grade = get_grade(student['score'])
	retrun f"이름: {student['name']}, 점수: {student['score']}, 등급: {grade}"


# 테스트 코드
print(get_student_info(students, '102')) # 정상 조회
print(get_student_info(students, 104)) # 정수로 직접 전달
print(get_student_info(students, '999')) # 존재하지 않는 ID
print(get_student_info(students, 'abc')) # 잘못된 형식