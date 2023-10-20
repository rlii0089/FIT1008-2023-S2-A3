from data_structures.bst import BinarySearchTree
from data_structures.linked_stack import LinkedStack
from island import Island


class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.island_bst = BinarySearchTree()
        for island in islands:
            if island.marines > 0:
                self.island_bst.__setitem__(island.money_per_marine(), island)

        self.crew = crew

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        selected_islands = []
        current_crew = self.crew

        island_stack = LinkedStack()
        island_in_order_iterator = self.island_bst.__iter__()
        for i in range(self.island_bst.__len__()):
            island_stack.push(island_in_order_iterator.__next__().item)

        while current_crew > 0 and not island_stack.is_empty():
            current_island = island_stack.pop()
            crew_to_send = min(current_crew, current_island.marines)
            selected_islands.append((current_island, crew_to_send))
            current_crew -= crew_to_send

        return selected_islands

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        max_money_per_crew = []

        for crew in crew_numbers:
            self.crew = crew
            selected_islands = self.select_islands()

            total_money = 0
            for island, crew_sent in selected_islands:
                total_money += min(island.money * crew_sent / island.marines, island.money)

            max_money_per_crew.append(total_money)

        return max_money_per_crew

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        island.money = new_money
        island.marines = new_marines
