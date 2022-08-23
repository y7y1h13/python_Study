# 지능형 리스트
chars = '_+)(*'
code_list1 = []
for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars]

print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))


print(code_list3)
print(code_list4)

print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()

# Generator 생성
import array

# Generator : 한 번에 한 개의 항목을 생성(매모리 유지 X)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(type(array_g))
print(array_g.tolist())

print()
print()

# 제너레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

print()
print()

# 리스트 주의
mark1 = [['~'] * 3 for _ in range(4)] # 주소 값이 다 다름
mark2 = [['~'] * 3] * 4 # 복사가 된거라 다 같은 주소 값

print()

# 수정
mark1[0][1] = 'X'
mark2[0][1] = 'X'

print(mark1)
print(mark2)

# 증명
print([id(i) for i in mark1])
print([id(i) for i in mark2])














