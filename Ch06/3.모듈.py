"""
이름 : 김보성
날짜 : 2023/01/11
내용 : 파이썬 모듈 실습하기
"""

import sub2.calc
import sub2.calc as c
from sub2.calc import *

r1 = sub2.calc.plus(1, 2)
print('r1 :', r1)

r2 = c.minus(2, 3)
print('r2 :', r2)

r3 = multi(3, 4)
print('r3 :', r3)

r4 = div(4, 2)
print('r4 :', r4)