from game_of_life import get_next_stage

def test_get_next_stage():
    assert get_next_stage([[0,1,1],[0,0,1],[0,0,0]]) == [[0,0,1],[0,0,0],[0,0,0]]
