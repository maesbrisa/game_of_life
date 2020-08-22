from gol.common.gol import get_next_stage

def test_common():
    assert get_next_stage([[0,1,1],[0,0,1],[0,0,0]]) == [[0,0,1],[0,0,0],[0,0,0]]

def test_all_zeros():
    assert get_next_stage([[0,0,0],[0,0,0],[0,0,0]]) == [[0,0,0],[0,0,0],[0,0,0]]

def test_empty_list():
    assert get_next_stage([]) == []