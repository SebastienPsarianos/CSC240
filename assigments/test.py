from math import sqrt

def construtor_case(prev):
    return sqrt(1* prev  + 5)


prev = sqrt(7)
for i in range(100):
    print(prev)
    prev = construtor_case(prev)

print(prev ** 2)