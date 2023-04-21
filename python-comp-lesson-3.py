# conditionals in comprehensions

# function with for loop


def find_usable_data(data_list):
    temp = []
    for datum in data_list:
        if datum > 90 and datum % 2 == 0:
            temp.append(datum)
        else:
            temp.append(-100)
    return temp


# comprehension equivilent


def find_usable_data_c(data_list):
    return [datum if datum > 90 and datum % 2 == 0 else -100 for datum in data_list]


# test code

if __name__ == "__main__":
    data_list = [1, 2, 90, 91, 92, 93, 94]
    print(find_usable_data_c(data_list) == find_usable_data(data_list))
