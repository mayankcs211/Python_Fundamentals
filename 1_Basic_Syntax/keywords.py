# 35 keywords are present in Python

import keyword

for n, i in enumerate(keyword.kwlist, start=1):
    if i.startswith('__'):
        continue
    else:
        print(f'{n} : {i}')
