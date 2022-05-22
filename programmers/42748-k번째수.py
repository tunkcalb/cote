def solution(array, commands):
    answer = []

    for commands_idx in commands:
        commands_array = array[commands_idx[0]-1:commands_idx[1]]
        commands_array.sort()
        answer.append(commands_array[commands_idx[2]-1])
    return answer