def solution(numbers):
    e=0
    for i in range(0,len(numbers)):
        e=e+numbers[i]
    e=e/len(numbers)
    return e
        