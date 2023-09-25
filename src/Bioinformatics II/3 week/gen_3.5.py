def count_subpeptides(n):
    return n * (n + 1) // 2 + 1

if __name__ == "__main__":
    n = int(input())
    subpeptide_count = count_subpeptides(n)
    print(subpeptide_count)
