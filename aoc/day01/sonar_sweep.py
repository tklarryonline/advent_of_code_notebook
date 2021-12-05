def count_increase(measurements: list[int]) -> int:
    return len([
        measurements[i]
        for i in range(1, len(measurements))
        if measurements[i] > measurements[i-1]
    ])


def count_increase_sliding_windows(measurements: list[int]) -> int:
    windows = [
        x + y + z
        for x, y, z in zip(measurements[:-2], measurements[1:-1], measurements[2:])
    ]
    return count_increase(windows)


if __name__ == '__main__':
    with open('inputs.txt', mode='r') as f:
        lines = f.readlines()

    inputs = [int(line) for line in lines]
    print(f"""**How many measurements are larger than the previous measurement?**
    {count_increase(inputs)}
    **How many sums are larger than the previous sum?**
    {count_increase_sliding_windows(inputs)}
    """)
