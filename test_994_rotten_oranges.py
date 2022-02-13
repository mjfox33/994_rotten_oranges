import code_994_rotten_oranges as c

def test_example_1():
    s = c.Solution()
    assert s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4

def test_example_2():
    s = c.Solution()
    assert s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1

def test_example_3():
    s = c.Solution()
    assert s.orangesRotting([[0,2]]) == 0