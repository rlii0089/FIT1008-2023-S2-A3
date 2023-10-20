from data_structures.bst import BinarySearchTree
from data_structures.linked_stack import LinkedStack
from island import Island


class Mode2Navigator:
    """
    A class that simulates the Davy Back Fight among pirates, where they compete to loot islands most efficiently.

    This class is responsible for simulating of the Davy Back Fight, a game where pirates take turns selecting islands
    to loot, optimising their choices to maximise their daily scores, which are based on the remaining crew and the
    money looted.

    Data Structures used:
    - List: Used to store the islands.
    - BinarySearchTree: Used to store the islands.
    - LinkedStack: Used to store the islands selected by the pirates.

    Example:
    If there are 3 pirates with crews of 100  and there are islands A, D, and E with money and marine values as follows:
    navigator = Mode2Navigator(3)
    islands = [Island("A", 400, 100), Island("D", 350, 90), Island("E", 300, 100)]
    - The first pirate makes 400 gold by going to Island A and sending 100 their crew.
    - The second pirate makes 350 gold by going to Island D and sending 90 of their crew.
    - The third pirate makes 300 gold by going to Island E and sending 100 of their crew.
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Initialise the object with the given number of pirates.

        Worst Case Complexity: O(1)
        Best Case Complexity: O(1)
        """
        self.n_pirates = n_pirates
        self.islands = BinarySearchTree()

    def add_islands(self, islands: list[Island]) -> None:
        """
        Add a list of islands to the seas.

        We loop through the list of islands and add them to the BinarySearchTree.

        Worst Case Complexity: O(Nlog(N)) or less, where N is the length of the 'islands' list.
        Best Case Complexity: O(Nlog(N)) or less, where N is the length of the 'islands' list.

        Parameters:
        - islands (list[Island]): A list of islands to add to the seas.
        """
        for island in islands:
            self.islands.__setitem__(island.name, island)

    def simulate_day(self, crew: int) -> list[tuple[Island, int]]:
        """
        Simulate a day of the Davy Back Fight.

        We use a LinkedStack to store the islands selected by the pirates. We loop through the pirates and select
        islands for each pirate. For each pirate, we select the island with the best score. We append the selected
        island to the LinkedStack and update the island's money and marine values.

        Worst Case Complexity: O(N^2), where N is the number of pirates.
        Best Case Complexity: O(N^2), where N is the number of pirates.

        Parameters:
        - crew (int): The number of pirates in the crew.

        Returns:
        - A list of tuples containing the selected islands and the number of pirates sent
        """
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
