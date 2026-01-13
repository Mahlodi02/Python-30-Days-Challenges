# Number Analyzer Prog


numbers = []
N = int(input("Enter how many numbers you are going to add to a list: "))

for i in range(N):
    user = int(input("Enter list of numbers: "))
    numbers.append(user)
print(numbers)

sum_numbers = sum(numbers)
print(f"Sum_numbers: {sum_numbers}")

avarage_numbers = sum_numbers / N
print(f"Avarage_numbers: {avarage_numbers}")

max_number = max(numbers)
print(f"Maximum_number: {max_number}")

min_number = min(numbers)
print(f"mMinimum_number: {min_number}")

for num in numbers:
    if num % 2 == 0:
        print(f"{num}, even")
    else:
        print(f"{num}, odd")
    