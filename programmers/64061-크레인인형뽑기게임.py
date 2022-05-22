def solution(board, moves):
    basket = list()
    # 바구니를 리스트로 생성
    basket.append(0)

    # 0이 아닌 경우에만 담을 것이기 때문에 인덱스를 위해 0 추가
    answer = 0
    for idx in moves:
        for board_idx in range(len(board[0])):
            if board[board_idx][idx - 1] != 0:
                # 0이 아닌 숫자가 나올 때까지 길이만큼 반복
                if basket[-1] == board[board_idx][idx - 1]:
                    basket.pop()
                    answer += 2
                # 바구니의 맨위 값과 같을 경우 터뜨리고 answer에 +2
                else:
                    basket.append(board[board_idx][idx - 1])

                # 다를 경우 append
                board[board_idx][idx - 1] = 0
                # 두 경우 모두 원래 자리에 0을 넣어 비워줌
                break

    # 크레인 수행했으므로 다음 moves로 넘어가기 위해 break
    return answer
