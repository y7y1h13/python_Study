class Car():
    """
    Car class
    Author : yoo
    Date : 2022.08.18
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return f'str {self._company} - {self._details}'

    def __repr__(self):
        return f'repr {self._company} - {self._details}'

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print(f'Current ID : {id(self)}')
        print(f'Car Detail Info : {self._company} {self._details.get("price")}')

    # Instance Method
    def get_price(self):
        return f'Before Car Price -> company : {self._company}, price: {self._details.get("price")}'

    # Instance Method
    def get_price_culc(self):
        return f'Before Car Price -> company : {self._company}, price: {self._details.get("price") * Car.price_per_raise}'

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            return print('Please Enter 1 or More')
        cls.price_per_raise = per
        print('Succeed! price increased')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return f'Ok! This car is {inst._company}'
        return 'Sorry! This car is not Bmw'


# Self 의미
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})

# 전체 정보
print(car1.detail_info())
print(car2.detail_info())

# 가격 정보(직접)
print(car1._details.get('price'))  # 자기 인스턴스 변수에 접근하는건 좋지 않음... private로 처리
print(car2._details['price'])

# 가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 직접 접근
Car.price_per_raise = 1.4

print()

# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 클래스 메소드 사용
Car.raise_price(1.6)

# 가격 확인
print(car1.get_price_culc())
print(car2.get_price_culc())

print()

# 인스턴스로 호출(staticmethod)
print(car1.is_bmw(car1))
print(car1.is_bmw(car2))

# 클래스로 호출(staticmethod)
print(Car.is_bmw(car1))
