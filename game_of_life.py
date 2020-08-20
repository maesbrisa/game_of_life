import copy

def get_next_stage(init) -> list:
    next_stage = copy.deepcopy(init)
    for y, row in enumerate(init):
        print(row)
        for x, element in enumerate(row):
            counter_alives = 0
            print('Checking cell, ' + str(y) 
            + ' ' + str(x) + ' with value ' + str(element))
            # check left one y x-1 
            if x > 0:
                print('x > 0, checking left')
                print(y,x-1,init[y][x-1])
                if init[y][x-1] == 1:
                    print('neighbor alive')
                    counter_alives += 1
            # check right one y x+1
            if x < len(init[0])-1:
                print('x < row length, checking right')
                print(y, x+1,init[y][x+1])
                if init[y][x+1] == 1:
                    print('neighbor alive')
                    counter_alives += 1
            # check up y+1 x
            if y < len(init)-1:
                print('y < column length, checking up')
                print(y+1,x,init[y+1][x])
                if init[y+1][x] == 1:
                    print('neighbor alive')
                    counter_alives += 1
            # check down y-1 x
            if y < 0:
                print('y > 0, checking down')
                print(y-1,x,init[y-1][x])
                if init[y-1][x] == 1:
                    print('neighbor alive')
                    counter_alives += 1
            print('counter alives ', str(counter_alives))
            if counter_alives == 3:
                next_stage[y][x] = 1
            elif counter_alives == 2 and init[y][x] == 1:
                next_stage[y][x] = 1
            else:
                next_stage[y][x] = 0
    return next_stage

if __name__ == "__main__":    
    rows = int(input('Number of rows > '))
    columns = int(input('Number of columns > '))
    print('Enter ' + str(rows*columns) + ' values as follows: 1 0 0')
    board = []
    for y in range(rows):
        row = list(map(int, input().split()))
        board.append(row)
    print(get_next_stage(board))