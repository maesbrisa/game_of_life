import copy
import logging

def get_next_stage(init) -> list:
    next_stage = copy.deepcopy(init)
    for y, row in enumerate(init):
        logging.debug(row)
        for x, element in enumerate(row):
            counter_alives = 0
            logging.debug('Checking cell, ' + str(y) 
            + ' ' + str(x) + ' with value ' + str(element))
            # check left one y x-1 
            if x > 0:
                logging.debug('x > 0, checking left')
                logging.debug(y,x-1,init[y][x-1])
                if init[y][x-1] == 1:
                    logging.debug('neighbor alive')
                    counter_alives += 1
            # check right one y x+1
            if x < len(init[0])-1:
                logging.debug('x < row length, checking right')
                logging.debug(y, x+1,init[y][x+1])
                if init[y][x+1] == 1:
                    counter_alives += 1
            # check up y+1 x
            if y < len(init)-1:
                logging.debug('y < column length, checking up')
                logging.debug(y+1,x,init[y+1][x])
                if init[y+1][x] == 1:
                    logging.debug('neighbor alive')
                    counter_alives += 1
            # check down y-1 x
            if y < 0:
                logging.debug('y > 0, checking down')
                logging.debug(y-1,x,init[y-1][x])
                if init[y-1][x] == 1:
                    logging.debug('neighbor alive')
                    counter_alives += 1
            logging.debug('counter alives ', str(counter_alives))
            if counter_alives == 3:
                next_stage[y][x] = 1
            elif counter_alives == 2 and init[y][x] == 1:
                next_stage[y][x] = 1
            else:
                next_stage[y][x] = 0
    return next_stage

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