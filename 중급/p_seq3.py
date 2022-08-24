# 해시테이블
# 해시값이 중복되면 어떻게 처리함?
# key에 value를 저장하는 구조
# 파이썬 dict 해쉬 테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해시 주소 -> key에 대한 value 참조

# Dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

# 해시는 불변형만 가능
print(hash(t1))

# 리스트는 가변형 따라서 해시 불가능
# print(hash(t2))

print()
print()

# Dict Setdefault
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의
new_dict3 = {k: v for k, v in source} # 키가 중복되어서 덮어쓰기가 일어남
