from random import randint


def calc_hash_and_x_pow(s, x, p):
    n = len(s)
    x_pow_i = 1
    h = 0
    for i in range(n):
        h += ord(s[i]) * x_pow_i % p
        h %= p
        if i < n - 1:
            x_pow_i *= x
            x_pow_i %= p
    return h, x_pow_i


def main():
    p = 1_000_000_007
    x = randint(1, p - 1)
    pattern = input()
    text = input()
    m = len(pattern)
    n = len(text)

    answer = []
    pattern_hash, x_pow = calc_hash_and_x_pow(pattern, x, p)
    h_window = calc_hash_and_x_pow(text[-m:], x, p)[0]
    if h_window == pattern_hash:
        if text[-m:] == pattern:
            answer.append(n - m)

    for i in range(n - m - 1, -1, -1):
        h_window = ((h_window - ord(text[i + m]) * x_pow % p) % p * x % p + ord(text[i]))
        h_window %= p
        if h_window == pattern_hash:
            if text[i:i + m] == pattern:
                answer.append(i)

    print(*reversed(answer))


if __name__ == "__main__":
    main()
