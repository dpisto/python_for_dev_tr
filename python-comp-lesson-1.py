# original function


def old_process_incoming_data(data_list):
    temp = []
    for datum in data_list:
        temp.append(datum // 2 * 67 - 5)
    return temp


# refractored with comprehension


def process_incoming_data(data_list):
    return [datum // 2 * 67 - 5 for datum in data_list]


# test if first function matches second function

if __name__ == "__main__":
    data_list = [0, 5, 10, 15]
    print(process_incoming_data(data_list) == old_process_incoming_data(data_list))
