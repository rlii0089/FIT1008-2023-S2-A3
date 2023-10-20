from data_structures.bst import BinarySearchTree
from data_structures.heap import MaxHeap
from data_structures.linked_stack import LinkedStack
from island import Island


class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, n_pirates: int) -> None:
        self.n_pirates = n_pirates
        self.islands = BinarySearchTree()

    def add_islands(self, islands: list[Island]) -> None:
        for island in islands:
            self.islands.__setitem__(island.name, island)

    def simulate_day(self, crew: int) -> list[tuple[Island, int]]:
        choices = []
        selected_islands = LinkedStack()

        for _ in range(self.n_pirates):
            max_score = -1
            chosen_island = None
            crew_to_send = 0

            for island in self.islands:
                remaining_crew = self.n_pirates * crew
                money_looted = min((crew * island.item.money) / island.item.marines, island.item.money)
                score = 2 * crew - remaining_crew + money_looted

                if score > max_score:
                    max_score = score
                    chosen_island = island
                    crew_to_send = min(remaining_crew, island.item.marines)

            if chosen_island:
                choices.append((chosen_island, crew_to_send))
                selected_islands.push(chosen_island)

        while not selected_islands.is_empty():
            current_island = selected_islands.pop()
            current_island.item.money -= (current_island.item.marines * crew) // self.n_pirates
            current_island.item.marines -= (current_island.item.marines * crew) // self.n_pirates

        return choices
