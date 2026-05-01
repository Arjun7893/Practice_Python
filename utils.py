def find_max(numbers):
    output = numbers[0]
    for number in numbers:
        if number > output:
            output = number
    return output