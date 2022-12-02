def part1():
    f = open('input.txt', 'r')
    max_calories, current_calories = 0, 0
    for line in f:
        if line == '\n':
            max_calories = max(max_calories, current_calories)
            current_calories = 0
        else:
            current_calories += int(line)
    return max_calories

def part2(topn: int) -> int:
    f = open('input.txt', 'r')
    max_calories = [0 for length in range(topn)]
    current_calories = 0
    for line in f:
        if line == '\n':
            swap_helper(max_calories, current_calories)
            current_calories = 0
        else:
            current_calories += int(line)
    return sum(max_calories)

def swap_helper(max_calories: list[int], to_swap: int):
    for idx, item in enumerate(max_calories):
        if to_swap > item:
            temp = to_swap
            to_swap = item
            max_calories[idx] = temp


if __name__ == '__main__':
    # print(part1())
    print(part2(3))