def average(array):
    new_set = set(array)
    set_length = len(new_set)
    answer = sum(new_set) / set_length
    return answer

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)