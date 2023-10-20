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
        possible_amounts_of_money = []

        # Create a dictionary to keep track of island states (money and marines) before each calculation
        original_island_states = {island: (island.money, island.marines) for island in self.island_bst.values()}

        for crew in crew_numbers:
            current_crew = crew
            total_money_earned = 0

            for island in self.island_bst.values():
                if current_crew <= 0:
                    break
                if island.marines == 0:
                    continue

                crew_to_send = min(current_crew, island.marines)
                money_earned = min((crew_to_send * island.money) / island.marines, island.money)

                total_money_earned += money_earned
                island.marines -= crew_to_send
                island.money -= money_earned
                current_crew -= crew_to_send

            # Append the total money earned for the current crew size
            possible_amounts_of_money.append(total_money_earned)

            # Restore the original island states
            for island in self.island_bst.values():
                island.money, island.marines = original_island_states[island]

        return possible_amounts_of_money

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        island.money = new_money
        island.marines = new_marines
