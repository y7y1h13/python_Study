# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *=2

print(l, id(l))
print(l, id(m))

# sort vs sorted
# reverse, key=len, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len))
print('sorted - ', sorted(f_list, key=lambda x: x[-1]))
print(f_list)

# sort : 정렬 후 객체 직접 변경
# 반환 값 확인(None)
print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse=True), f_list)
print('sort - ', f_list.sort(key=len), f_list)
print('sort - ', f_list.sort(key=lambda x : x[-1]), f_list)

# list vs Array 적합 한 사용법 설명
# 리스트 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환)
