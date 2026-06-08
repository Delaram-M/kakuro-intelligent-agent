import copy
import timeit

from puzzle import KakuroPuzzle, KakuroClue, KakuroClueCell, KakuroBlackCell, KakuroWhiteCell
from puzzle import DOWN, RIGHT
from backtracking import KakuroAgent, DIGITS
from intelligent_backtracking import IntelligentKakuroAgent


cells = []

# puzzle from https://krazydad.com/

# row 1
cells.append(KakuroBlackCell((0, 0)))
cells.append(KakuroBlackCell((0, 1)))
cells.append(KakuroBlackCell((0, 2)))
cells.append(KakuroClueCell((0, 3), KakuroClue(DOWN, 2, 7), None))
cells.append(KakuroClueCell((0, 4), KakuroClue(DOWN, 4, 11), None))
cells.append(KakuroBlackCell((0, 5)))

# row 2
cells.append(KakuroBlackCell((1, 0)))
cells.append(KakuroClueCell((1, 1), KakuroClue(DOWN, 2, 13), None))
cells.append(KakuroClueCell((1, 2), KakuroClue(DOWN, 4, 16), KakuroClue(RIGHT, 2, 5)))
cells.append(KakuroBlackCell((1, 5)))

# row 3
cells.append(KakuroClueCell((2, 0), None, KakuroClue(RIGHT, 4, 10)))
cells.append(KakuroClueCell((2, 5), KakuroClue(DOWN, 2, 17), None))

# row 4
cells.append(KakuroClueCell((3, 0), None, KakuroClue(RIGHT, 2, 11)))
cells.append(KakuroClueCell((3, 3), KakuroClue(DOWN, 2, 3), KakuroClue(RIGHT, 2, 11)))

# row 5
cells.append(KakuroBlackCell((4, 0)))
cells.append(KakuroClueCell((4, 1), None, KakuroClue(RIGHT, 4, 19)))

# row 6
cells.append(KakuroBlackCell((5, 0)))
cells.append(KakuroClueCell((5, 1), None, KakuroClue(RIGHT, 2, 11)))
cells.append(KakuroBlackCell((5, 4)))
cells.append(KakuroBlackCell((5, 5)))


puzzle = KakuroPuzzle(6, 6, cells)

# unintelligent agent:
unintelligent_agent = KakuroAgent(copy.deepcopy(puzzle))
unintelligent_start = timeit.default_timer()
unintelligent_agent.solve()
unintelligent_stop = timeit.default_timer()
unintelligent_time = unintelligent_stop - unintelligent_start


intelligent_agent = IntelligentKakuroAgent(copy.deepcopy(puzzle))
intelligent_start = timeit.default_timer()
intelligent_agent.solve()
intelligent_stop = timeit.default_timer()
intelligent_time = intelligent_stop - intelligent_start


print("Unintelligent agent solved the puzzle in: \t", str(unintelligent_time))
print("Intelligent agent solved the puzzle in: \t", str(intelligent_time))
print("The intelligent agent was about", str(round(unintelligent_time/intelligent_time)), "times faster.")

