def stats_decorator(func):
    def wrapper(numbers):
        count = len(numbers)
        total = sum(numbers)
        avg = total / count
        max_num = max(numbers)
        min_num = min(numbers)
        print("Numbers:", numbers)
        print("Count:", count)
        print("Average:", avg)
        print("Maximum:", max_num)
        print("Minimum:", min_num)
        func(numbers)
    return wrapper

@stats_decorator
def printStats(t):
    pass

def read_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            numbers = [int(num) for num in line.split()]
            printStats(numbers)

# Example usage:
read_file('q4_test.txt')