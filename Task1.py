def change_bites(number: int) -> int: 
    if int.bit_length(number) > 16:
        print(f"Range = 0 - 65535")
        return -1
    lower = (number & 0xFF) << 8
    higher = number >> 8
    result = lower + higher
    return result


if __name__ == "__main__":
    print(change_bites(128))
