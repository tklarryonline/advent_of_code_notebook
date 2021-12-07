def simple_power_consumption(numbers: list[str]) -> int:
    # Converts the numbers to 2x2 matrix of digits
    matrix = [
        [int(bit) for bit in number.strip()]
        for number in numbers
    ]

    # Then transposes the matrix
    matrix = [
        sorted(m)
        for m in zip(*matrix)
    ]

    gamma = ''.join(
        '1' if m.index(1) < (len(m) / 2) else '0'
        for m in matrix
    )
    # Then flips gamma to get epsilon
    epsilon = bin((int(gamma, 2) ^ (2**(len(gamma)+1) - 1)))[3:]

    return int(gamma, 2) * int(epsilon, 2)
