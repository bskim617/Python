"""
날짜 : 2023/01/02
이름 : 김보성
내용 : 파이썬 기본 입출력 실습하기
"""

# 파이썬 입력
num = input('숫자 입력 : ')

# 파이썬 출력
print('num : ', num)
print('num type : ', type(num))

# 문자열 숫자 변환
r1 = int(num) + 1
print('r1 : ', r1)

# 출력 옵션
print('010', '1234', '5678', sep='-')
print('Hello', end='~ ') # 다음 출력문과 한줄로 출력
print('Python', end=' ')
print('Programming')

# 서식문자
print('%d년 %d월 %d일 %s요일' % (2023, 1, 2, '월'))

# 포맷문자
print('{}년 {}월 {}일 {}요일'.format(2023, 1, 2, '월'))