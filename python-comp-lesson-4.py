# Nest loop example
def calculate_value_l(data_list, divisors_list):
    temp = []
    for datum in data_list:
        for divisor in divisors_list:
            temp.append(datum / divisor)
    return temp


# nested comprehension example
def calculate_value_c(data_list, divisors_list):
    return [data / divisor for data in data_list for divisor in divisors_list]


# test
if __name__ == "__main__":
    data_list = [2, 4, 6, 8, 10]
    divisors_list = [2]
    print(
        calculate_value_c(data_list, divisors_list)
        == calculate_value_l(data_list, divisors_list)
    )
