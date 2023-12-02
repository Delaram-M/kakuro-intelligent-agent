import copy
import timeit

from puzzle import KakuroPuzzle, KakuroClue, KakuroClueCell, KakuroBlackCell, KakuroWhiteCell
from puzzle import DOWN, RIGHT
from backtracking import KakuroAgent, DIGITS
from intelligent_backtracking import IntelligentKakuroAgent


cells = []

# 5X5 sample:
# sample puzzle's source: https://www.kakuros.com/

# row 1
cells.append(KakuroBlackCell((0, 0)))
cells.append(KakuroBlackCell((0, 1)))
cells.append(KakuroClueCell((0, 2), KakuroClue(DOWN, 4, 22), None))
cells.append(KakuroClueCell((0, 3), KakuroClue(DOWN, 4, 12), None))
cells.append(KakuroBlackCell((0, 4)))
# row 2
cells.append(KakuroBlackCell((1, 0)))
cells.append(KakuroClueCell((1, 1), KakuroClue(DOWN, 2, 15), KakuroClue(RIGHT, 2, 12)))
cells.append(KakuroClueCell((1, 4), KakuroClue(DOWN, 2, 9), None))
# row 3
cells.append(KakuroClueCell((2, 0), None, KakuroClue(RIGHT, 4, 13)))
# row 4
cells.append(KakuroClueCell((3, 0), None, KakuroClue(RIGHT, 4, 29)))
# row 5
cells.append(KakuroBlackCell((4, 0)))
cells.append(KakuroClueCell((4, 1), None, KakuroClue(RIGHT, 2, 4)))
cells.append(KakuroBlackCell((4, 4)))

puzzle = KakuroPuzzle(5, 5, cells)

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

