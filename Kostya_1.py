# Угадайте что это за алгоритм

def binary_search(lst, key):
    b = 0
    e = len(lst) - 1
    
    while b <= e:

        mid_index = int((b + e) / 2)
        mid_value = lst[mid_index]
    
        if mid_value == key:
            return mid_index
        elif mid_value < key:
            b = mid_index + 1
        else:
            e = mid_index - 1

    return -1


def main():
    lst = [58, 90, 93, 94, 100, 111, 123, 2345, 2600]
    key = 111
    print(binary_search(lst, key))


if __name__ == "__main__":
    main()

# Ваши ответы пишите тут ниже