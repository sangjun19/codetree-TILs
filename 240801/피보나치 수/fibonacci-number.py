def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)

def main():
    n = int(input())
    print(fibo(n))
    
if __name__ == "__main__":
    main()