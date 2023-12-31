import copy


DOWN = 'down'
RIGHT = 'right'

DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class KakuroAgent:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    # solve the puzzle using backtracking
    def solve(self):
        solution = self.backtracking_search(self.puzzle)
        if solution is not None:
            solution.print_puzzle()
            puzzle = solution
        else:
            print("no solution found")

    def backtracking_search(self, puzzle):
        return self.recursive_backtracking(copy.deepcopy(puzzle))

    def recursive_backtracking(self, assignment):
        if assignment.is_complete() and assignment.is_consistent():
            print("YAY!")
            return assignment
        clue = self.select_unassigned_clue(assignment)
        if clue is not None:
            cell_set = assignment.get_cell_set(clue)
            value_sets = self.order_domain_values(clue, cell_set, assignment)
            for value_set in value_sets:
                if self.is_consistent(clue, copy.deepcopy(value_set), copy.deepcopy(assignment)):
                    assignment.assign_clue(clue, value_set)
                    assignment.print_puzzle()
                    result = self.recursive_backtracking(copy.deepcopy(assignment))
                    if result is not None:
                        return result

        return None

    def select_unassigned_clue(self, assignment):
        for clue in assignment.clues:
            if not assignment.is_clue_assigned(clue):
                return clue

    def order_domain_values(self, clue, cell_set, assignment):
        value_sets = []
        assigned_cells = []
        unassigned_cells = []
        allowed_values = copy.deepcopy(DIGITS)
        for cell in cell_set:
            if cell.value == 0:
                unassigned_cells.append(cell)
            else:
                if cell.value in allowed_values:
                    allowed_values.remove(cell.value)
                assigned_cells.append(cell)
        current_sum = 0
        for cell in assigned_cells:
            current_sum += cell.value
        net_goal_sum = clue.goal_sum - current_sum
        net_cell_count = clue.length - len(assigned_cells)
        unassigned_value_sets = self.sum_to_n(net_goal_sum, net_cell_count, allowed_values)
        for unassigned_value_set in unassigned_value_sets:
            variable_set = copy.deepcopy(cell_set)
            value_set = []
            for cell in variable_set:
                if cell.value == 0:
                    value_set.append(unassigned_value_set.pop(0))
                else:
                    value_set.append(cell.value)
            value_sets.append(value_set)
        return value_sets

    # returns different ways to write integer n as the sum of k numbers between 1 and 9 with no repeated numbers
    def sum_to_n(self, n, k, allowed_values):
        if k == 1 and n in allowed_values:
            return [[n]]
        combos = []
        for i in allowed_values:
            allowed_values_copy = copy.deepcopy(allowed_values)
            allowed_values_copy.remove(i)
            if n - i > 0:
                combos += [[i] + combo for combo in self.sum_to_n(n - i, k - 1, allowed_values_copy)]
        for combo in combos:
            if any(combo.count(x) > 1 for x in combo):
                combos.remove(combo)
        return combos

    def is_consistent(self, clue, value_set, assignment):
        assignment.assign_clue(clue, value_set)
        assignment.print_puzzle()
        return assignment.is_consistent()



