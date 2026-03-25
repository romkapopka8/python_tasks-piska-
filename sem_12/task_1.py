s = input().split()
res = [int(s[i]) for i in range(len(s))]
def is_positive(num: int) ->bool:
    if num >= 0:
        return True
    else:
        return False
def count_positive(numbers: list) -> int:
    count = 0
    for i in range(len(numbers)):
        if is_positive(numbers[i]) == True:
            count += 1
    return count
def count_negative(numbers: list) -> int:
    count = 0
    for i in range(len(numbers)):
        if is_positive(numbers[i]) == False:
            count += 1
    return count

print(count_positive(res))
print(count_negative(res))
