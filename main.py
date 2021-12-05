from day01.sonar_sweep import count_increase, count_increase_sliding_windows

if __name__ == '__main__':
    with open('inputs.txt', mode='r') as f:
        lines = f.readlines()

    inputs = [int(line) for line in lines]
    print(f"""**How many measurements are larger than the previous measurement?**
    {count_increase(inputs)}
    **How many sums are larger than the previous sum?**
    {count_increase_sliding_windows(inputs)}
    """)
