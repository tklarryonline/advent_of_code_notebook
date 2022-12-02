from collections import deque


def count_fishes_recursive(fish_ages: list[int], days: int = 0) -> int:
    if days == 0:
        return len(fish_ages)

    new_ages = []
    for age in fish_ages:
        if age == 0:
            new_ages += [6, 8]
        else:
            new_ages.append(age - 1)

    return count_fishes_recursive(fish_ages=new_ages, days=days - 1)


def count_fishes_deque(fish_ages: list[int], days: int = 0) -> int:
    totals = deque(fish_ages.count(i) for i in range(9))
    for _ in range(days):
        totals.rotate(-1)
        totals[6] += totals[8]
    return sum(totals)


def part01_count_fishes(inputs: str, days=80) -> int:
    fish_ages = [int(s.strip()) for s in inputs.split(',')]

    return count_fishes_deque(fish_ages, days=days)
