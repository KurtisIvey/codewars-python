# Example:
# Input: [1, 2, 3, 4, 5]
# Output: [2, 4]

def filter_even(numbers):
    def even(number):
        return number % 2 == 0
    output = filter(even, numbers)
    print(list(output))
    return output

# cleaner
def filter_even2(numbers):
    output = list(filter(lambda number: number % 2 == 0, numbers))
    print(output)
    return output

def filter_even3(numbers):
    output = []
    for num in numbers:
        if num % 2 == 0:
            output.append(num)
    print(output)
    return output


filter_even([1,2,3,4,5])
filter_even2([1,2,3,4,5])
filter_even3([1,2,3,4,5])
