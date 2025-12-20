'''Batman is going on a scouting trip, surveying an area where he thinks Harley Quinn might commit her next crime spree. The area has many hills with different heights and Batman wants to find the tallest one to get the best vantage point. His scout trip consists of n + 1 points at different altitudes. Batman starts his trip at point 0 with altitude 0.

Write a function highest_altitude() that accepts an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.'''


def highest_altitude(gain):
    current_altitude = 0
    max_altitude = 0
    for g in gain:
        current_altitude += g
        max_altitude = max(max_altitude, current_altitude)
    return max_altitude


if __name__ == '__main__':
    gain = [-5, 1, 5, 0, -7]
    print(highest_altitude(gain))

    gain = [-4, -3, -2, -1, 4, 3, 2]
    print(highest_altitude(gain))