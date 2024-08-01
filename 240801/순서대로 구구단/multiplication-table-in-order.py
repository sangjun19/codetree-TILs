def main():
    a, b = map(int, input().split())
    for i in range(1, 10):
        print(f"{a} * {i} = {a * i}", end='  ')
        print(f"{b} * {i} = {a * i}", end='  ')
        print()

if __name__ == "__main__":
    main()