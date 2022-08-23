class Car():
    """
    Car class
    Author : yoo
    Date : 2022.08.18
    """

    # 클래스 변수
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        # self.car_count = 10 동일 변수
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return f'str {self._company} - {self._details}'

    def __repr__(self):
        return f'repr {self._company} - {self._details}'

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print(f'Current ID : {id(self)}')
        print(f'Car Detail Info : {self._company} {self._details.get("price")}')


# Self 의미
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)

# dir & __dict__ 확인
print(dir(car1))

print()
print()

print(car1.__dict__)

# Doctring
print(Car.__doc__)
print()

# 실행
car1.detail_info()
Car.detail_info(car1)
car2.detail_info()
Car.detail_info(car2)
# 비교
print(car1.__class__)
print(id(car1.__class__), id(car2.__class__))

print()
print()

# 공유 확인
print(Car.car_count)
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(dir(car1))

# 접근
print(Car.car_count)
print(car1.car_count)

print()
# 삭제 확인
del car2
print(Car.car_count)
print(car1.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모클래스 변수))


