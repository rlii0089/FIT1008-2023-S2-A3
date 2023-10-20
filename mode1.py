from data_structures.bst import BinarySearchTree
from island import Island


class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        island_bst = BinarySearchTree()
        for island in islands:
            if island.marines > 0:
                island_bst.__setitem__((island.money / island.marines),
                                       island
                                       )

        self.island_bst = island_bst
        self.crew = crew

    def find_max_money_island(self):
        current_node = self.island_bst.root

        if current_node is None:
            return None

        while current_node.right:
            current_node = current_node.right
        return current_node

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        selected_islands = []
        current_crew = self.crew

        while current_crew > 0:
            max_money_island = self.find_max_money_island()
            if max_money_island is None:
                break
            elif max_money_island.item.marines == 0:
                break

            crew_to_send = min(current_crew, max_money_island.item.marines)
            selected_islands.append((max_money_island.item, crew_to_send))
            current_crew -= crew_to_send

            self.island_bst.__delitem__(max_money_island.key)

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
