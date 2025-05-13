# Example:
# Input: [1, 2, 3]
# Output: "1-2-3"

def join_with_dash(numbers):
    output = '-'.join(str(num) for num in numbers)
    print(output)
    return output

join_with_dash([1,2,3,4,5])