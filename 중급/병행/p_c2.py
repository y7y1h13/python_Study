# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B Point'
    print('End')


tmp = iter(generator_ex1())

# print(tmp)
#print(next(tmp))
#print(next(tmp))
#print(next(tmp))

for v in generator_ex1():
    # print(v)
    pass

# Generator Ex2
tmp2 = [x * 3 for x in generator_ex1()]
tmp3 = (x * 3 for x in generator_ex1())  # 제너레이터

print(tmp2)
print(tmp3)

for i in tmp3:
    print(i)

# for i in tmp2:

print()
print()

# Generator Ex3(중요 함수)
# count, takewhilefilterfalse, accumulate, chain, product, groupby

import itertools


gen1 = itertools.count(1, 2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# 무한임


# 조건
gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))

for v in gen2:
    pass
    # print(v)

print()


# 필터 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print(v)

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 11)])

for v in gen4:
    print(v)


# 연결1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))

print(list(gen5))

# 연결2
gen6 = itertools.chain(enumerate('ABBCDE'))

print(list(gen6))


# 개별
gen7 = itertools.product('ABCDE')

print(list(gen7))

# 개별(모든 경우의 수)
gen8 = itertools.product('ABCDE', repeat=4)

print(list(gen8))

# 그룹화
gen9 = itertools.groupby('AAABBCCCDDEEE')

# print(list(gen9))
for chr, group in gen9:
    print(chr, ' : ', list(group))