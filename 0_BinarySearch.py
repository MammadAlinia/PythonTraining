def get_input_list(time: int):
    tmp_list = []
    for i in range(time):
        tmp_list.append(int(input("enter number: ")))
    return tmp_list


def findIndex_linear(item: int, n_list: list):
    print(len(n_list))
    for i in range(0, len(n_list)):
        if n_list[i] == item:
            return i
        if i == len(n_list) - 1:
            print(n_list[i], 'is not ', item)
            return None


def findIndex_binary_Loop(item: int, n_list: list):
    start = 0
    end = len(n_list) - 1
    while start <= end:
        mid = (start + end) // 2
        print(start, mid, end)

        if n_list[mid] == item:
            return mid
        elif item > n_list[mid]:
            start = mid + 1
        elif item < n_list[mid]:
            end = mid - 1


def findIndex_func(item: int, n_list: list, start: int, end: int):
    mid = (start + end) // 2
    print(start, mid, end)

    if n_list[mid] == item:
        return mid
    elif item > n_list[mid]:
        start = mid + 1
        return findIndex_func(item, n_list, start, end)
    elif item < n_list[mid]:
        end = mid - 1
        return findIndex_func(item, n_list, start, end)


num_list = get_input_list(5)

num_list.sort()


N = int(input("Search For: "))

print(num_list)
result = findIndex_linear(N, num_list)
# result = findIndex_binary_Loop(N, num_list)
# result = findIndex_func(N, num_list, 0, len(num_list) - 1)
print(result)
if result is not None:
    print('Found it at index ☻ ', result)
else:
    print("Not found !:○")
