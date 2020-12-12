
from time import time
from node import *


class Searcher(object):
    """Searcher that manuplate searching process."""

    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def print_path(self, state):
        path = []
        while state:
            path.append(state)
            state = state.prev
        path.reverse()
        print("\n-->\n".join([str(state) for state in path]))

    def hill_climbing(self):
        """Run hill climbing search."""
        # TODO Implement hill climbing.
        stack = [self.start]

        while stack:
            state = stack.pop()
            if state == self.goal:
                self.print_path(state)
                print ("Find solution")
                break

            h_val = state.manhattan_distance() + state.hamming_distance()
            next_state = False
            # s1=state.next()
            for s in state.next():
                h_val_next = s.manhattan_distance() + s.hamming_distance()
                if h_val_next <= h_val:
                    next_state = s
                    h_val = h_val_next
                    stack.append(next_state)
                    #break

            if not next_state:
                self.print_path(state)
                print ("Cannot find solution")
                break



if __name__ == "__main__":



    print("Search for solution: Hill CLimbing\n")
    start = Node([8,1,3,7,0,4,6,2,5])
    goal = Node([1, 2, 3, 8, 0, 4, 7, 6, 5])


    search = Searcher(start, goal)
    search.hill_climbing()
    start_time = time()
    end_time = time()
    elapsed = end_time - start_time
    print("Search time: %s" % elapsed)
    print("Number of initialized node: %d" % Node.n)