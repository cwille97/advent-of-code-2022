def part1():
    total_score = 0
    f = open('input.txt', 'r')
    for line in f:
        local_score = 0
        line = line.split()
        if line[1] == 'X': # rock
            local_score += 1
            if line[0] == 'A': # rock
                local_score += 3
            elif line[0] == 'B': # paper
                local_score += 0
            elif line[0] == 'C': # scissors
                local_score += 6
        elif line[1] == 'Y': # paper
            local_score += 2
            if line[0] == 'A': # rock
                local_score += 6
            elif line[0] == 'B': # paper
                local_score += 3
            elif line[0] == 'C': # scissors
                local_score += 0
        elif line[1] == 'Z': # scissors
            local_score += 3
            if line[0] == 'A': # rock
                local_score += 0
            elif line[0] == 'B': # paper
                local_score += 6
            elif line[0] == 'C': # scissors
                local_score += 3
        total_score += local_score
    return total_score

def part2():
    total_score = 0
    f = open('input.txt', 'r')
    for line in f:
        local_score = 0
        line = line.split()
        if line[1] == 'X': # lose
            local_score += 0
            if line[0] == 'A': # rock
                local_score += 3
            elif line[0] == 'B': # paper
                local_score += 1
            elif line[0] == 'C': # scissors
                local_score += 2
        elif line[1] == 'Y': # draw
            local_score += 3
            if line[0] == 'A': # rock
                local_score += 1
            elif line[0] == 'B': # paper
                local_score += 2
            elif line[0] == 'C': # scissors
                local_score += 3
        elif line[1] == 'Z': # win
            local_score += 6
            if line[0] == 'A': # rock
                local_score += 2
            elif line[0] == 'B': # paper
                local_score += 3
            elif line[0] == 'C': # scissors
                local_score += 1
        total_score += local_score
    return total_score

if __name__ == '__main__':
    # print(part1())
    print(part2())