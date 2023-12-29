import heapq
import itertools

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                target_row, target_col = divmod(state[i][j] - 1, 3)
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

def is_goal(state):
    return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def actions(state):
    i, j = next((i, j) for i, row in enumerate(state) for j, value in enumerate(row) if value == 0)
    possible_actions = []
    if i > 0:
        possible_actions.append(('up', (i, j), (i - 1, j)))
    if i < 2:
        possible_actions.append(('down', (i, j), (i + 1, j)))
    if j > 0:
        possible_actions.append(('left', (i, j), (i, j - 1)))
    if j < 2:
        possible_actions.append(('right', (i, j), (i, j + 1)))
    return possible_actions

def apply_action(state, action):
    i, j = action[1]
    new_i, new_j = action[2]
    new_state = [row.copy() for row in state]
    new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
    return new_state

def solve_eight_puzzle(initial_state):
    initial_node = PuzzleNode(state=initial_state, heuristic=manhattan_distance(initial_state))
    heap = [initial_node]
    heapq.heapify(heap)
    visited = set()
    
    while heap:
        node = heapq.heappop(heap)
        if is_goal(node.state):
            return construct_solution(node)
        visited.add(tuple(itertools.chain(*node.state)))
        
        for action in actions(node.state):
            child_state = apply_action(node.state, action)
            child_node = PuzzleNode(state=child_state, parent=node, action=action[0], cost=node.cost + 1, heuristic=manhattan_distance(child_state))
            
            if tuple(itertools.chain(*child_state)) not in visited:
                heapq.heappush(heap, child_node)

    return None  # No solution found

def construct_solution(node):
    solution = []
    while node.parent:
        solution.append((node.action, node.state))
        node = node.parent
    solution.reverse()
    return solution

# Example usage:
initial_state = [[1, 2, 3], [8, 4, 6], [7, 5, 0]]
solution = solve_eight_puzzle(initial_state)

if solution:
    for step, state in enumerate(solution):
        action, state = state
        print(f"Step {step + 1}: {action}")
        for row in state:
            print(row)
        print("------")
else:
    print("No solution found.")


    ukta.makhija@inmantec.edu,
    navneet.tyagi@inmantec.edu,
    exam@inmantec.edu