def number_of_fake_baskets(N: int, w: int, d: int, P: int) -> int:
    sum_of_baskets = w * sum(range(1, N))
    if P == sum_of_baskets:
        return N
    return int((sum_of_baskets - P) / d)


if __name__ == "__main__":
    print(number_of_fake_baskets(5, 2, 1, 16))
