# name = ['Kim', 'Lee', 'Park']
#
# try:
#     z = 'Ki'
#     x = name.index(z)
#     print(z, x + 1)
# except Exception as e:
#     print(e)
#     print('error')
# else:
#     print('ok')
# finally:
#     print('ok')

try:
    a = 'Park'
    if a == 'Kim':
        print('pass')
    else:
        raise ValueError
except ValueError:
    print('except')
else:
    print('else')
