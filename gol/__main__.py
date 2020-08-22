import logging
from common.gol import get_next_stage

if __name__ == "__main__":    
    logging.basicConfig(level=logging.INFO)
    rows = int(input('Number of rows > '))
    columns = int(input('Number of columns > '))
    print('Enter ' + str(rows*columns) + ' values as follows: 1 0 0')
    board, phase = [], 0
    for y in range(rows):
        row = list(map(int, input().split()))
        board.append(row)
    while any(1 in row for row in board):
        logging.info('Phase > '+ str(phase))
        next_stage = get_next_stage(board)
        logging.info(next_stage)
        board = next_stage
        phase += 1
    logging.info('End')