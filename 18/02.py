daily_food = []

def count_food(days: list[int]):
    return sum(daily_food[i - 1] for i in days)
