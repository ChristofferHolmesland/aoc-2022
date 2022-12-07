def part_one():
    max_calories = 0
    running_sum = 0

    with open('day1.txt', 'r') as f:
        for line in f:
            line = line.strip()

            if line == '':
                if running_sum > max_calories:
                    max_calories = running_sum
                running_sum = 0
            else:
                running_sum += int(line)

    print(max_calories)

def part_two():
    max_calories = []
    running_sum = 0

    with open('day1.txt', 'r') as f:
        for line in f:
            line = line.strip()

            if line == '':
                if len(max_calories) < 3:
                    max_calories.append(running_sum)
                    max_calories.sort()
                elif running_sum > max_calories[0]:
                    max_calories.append(running_sum)
                    max_calories.sort()
                    max_calories.pop(0)

                running_sum = 0
            else:
                running_sum += int(line)

    print(sum(max_calories))


if __name__ == '__main__':
    part_two()