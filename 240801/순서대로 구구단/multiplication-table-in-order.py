def main():
    a, b = map(int, input().split())
    for i in range(1, 10):
        if a < b:
            for j in range(a, b + 1):
                print(f"{j} * {i} = {j * i}", end="    ")
        else:
            for j in range(a, b - 1, -1):
                print(f"{j} * {i} = {j * i}", end="    ")
        print()

if __name__ == "__main__":
    main()