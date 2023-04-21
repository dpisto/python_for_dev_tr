# exercise


def corrected_value(value):
    return value * 32


if __name__ == "__main__":
    data_list = [1, 2, 3]
    results = map(corrected_value, data_list)
    print(list(results))
