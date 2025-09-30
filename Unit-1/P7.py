def count_less_than(race_times, threshold): 
    count = 0
    for i in race_times:
        if i < threshold:
            count += 1
    print(count)


if __name__ == '__main__':
    race_times = [1, 2, 3, 4, 5, 6]
    threshold = 4
    count_less_than(race_times, threshold)

    race_times = []
    threshold = 4
    count_less_than(race_times, threshold)