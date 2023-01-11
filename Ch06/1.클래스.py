"""
이름 : 김보성
날짜 : 2023/01/11
내용 : 파이썬 클래스 실습하기
"""

from sub1.Car import Car
from sub1.Account import Account

bmw = Car('BMW', '검정색', 5000)
bmw.speedUp()
bmw.speedDown()
bmw.show()

sonata = Car('소나타', '흰색', 3000)
sonata.speedUp()
sonata.speedDown()
sonata.show()

kb = Account('국민은행', '101-21-1001', '김유신', 10000)
kb.deposit(40000)
#캡슐화
# kb.__blance += 1
kb.withdraw(5000)
kb.show()

wr = Account('우리은행', '101-20-1021', '김춘추', 20000)
wr.deposit(10000)
wr.withdraw(7000)
wr.show()
