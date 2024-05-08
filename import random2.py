import random

def generate_random_list(length=10, start=1, end=100):
    random_list = [random.randint(start, end) for _ in range(length)]
    return random_list

if __name__ == "__main__":
    length = int(input("Enter the length of the random list: "))
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    
    random_numbers = generate_random_list(length, start_range, end_range)
    print("Generated Random List:", random_numbers)
    
    sorted_numbers = sorted(random_numbers)
    print("Sorted Random List:", sorted_numbers)
