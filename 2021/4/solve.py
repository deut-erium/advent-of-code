with open('input.txt') as f:
    data = f.read().strip().split('\n\n')
    draws = list(map(int,data[0].split(',')))
    boards = [list(map(int,d.split())) for d in data[1:]]
    
ROW_AND_COLS = [set(range(x,x+5)) for x in range(0,25,5)]+[set(range(i,25,5)) for i in range(5)]

def check_bingo(marked_pos: set):
    return any( not(rc-marked_pos) for rc in ROW_AND_COLS)

NUM_BOARDS = len(boards)
board_rep = [ {v:i for i,v in enumerate(board)} for board in boards]
marked_pos = [set() for _ in range(NUM_BOARDS)]

finished_draws = {}

for draw_number, draw in enumerate(draws):
    for board_num,(brep,mark_pos) in enumerate(zip(board_rep,marked_pos)):
        if board_num not in finished_draws:
            pos_draw = brep.get(draw,None)
            if pos_draw is not None:
                brep.pop(draw)
                mark_pos.add(pos_draw)
            if check_bingo(marked_pos[board_num]):
                score = draw*sum(brep)
                finished_draws[board_num]=(draw_number,score)

board_order = sorted(finished_draws.items(),key=lambda x:(x[1][0],-x[1][1]))
print(board_order[0])
print(board_order[-1])

