def divisible_by_3_and_4_generator(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

def main():
    try:
        n = int(input())
        generator = divisible_by_3_and_4_generator(n)
        for num in generator:
            print(num, end=" ")
        print()
    except ValueError:
        print( )

if __name__ == "__main__":
    main()
