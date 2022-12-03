def part1():
    f = open('input.txt', 'r')
    priority_sum = 0
    for line in f:
        c1 = {}
        c2 = {}
        for idx, character in enumerate(line):
            if character == '\n':
                continue
            if idx >= len(line) // 2:
                break
            c1[character] = True
        for idx, character in enumerate(line):
            if idx < len(line) // 2:
                continue
            c2[character] = True
        for character in c1.keys():
            if character in c2:
                priority_sum += determine_priority(character)
                break
    return priority_sum

def determine_priority(character: str) -> int:
    if character.isupper():
        return ord(character) - 38 # magic number to convert ASCII value for uppercase to priority
    else:
        return ord(character) - 96 # magic number to convert lowercase to priority

def part2():
    f = open('input.txt', 'r')
    priority_sum = 0
    lines = f.readlines()
    counter = 0
    while counter < len(lines):
        r1, r2, r3 = {}, {}, {}
        for character in lines[counter]:
            r1[character] = True
        counter += 1
        for character in lines[counter]:
            r2[character] = True
        counter += 1
        for character in lines[counter]:
            r3[character] = True
        for character in r1.keys():
            if (character in r2) and (character in r3) and (character != '\n'):
                priority_sum += determine_priority(character)
                break
        counter += 1
    return priority_sum


if __name__ == '__main__':
    # print(part1())
    print(part2())