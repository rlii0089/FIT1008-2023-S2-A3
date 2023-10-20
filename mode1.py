from data_structures.bst import BinarySearchTree
from data_structures.linked_stack import LinkedStack
from island import Island


class Mode1Navigator:
    """
    Navigator for plundering islands to maximise crew's earnings.

    This class is responsible for selecting islands to plunder based on the best money-to-marine ratio
    to maximise the earnings of the crew. It also allows for calculations of earnings with different
    crew configurations and updating island information.

    Data Structures used:
    - BinarySearchTree: Used to efficiently store and manage islands with their money-to-marine ratio.

    An example:
    If the crew has 100 pirates and there are islands A, B, and C with money and marine values as follows:
    - Island A: Money = 400, Marines = 100
    - Island B: Money = 300, Marines = 150
    - Island C: Money = 100, Marines = 5

    The navigator will select islands based on the best money-to-marine ratio. With 100 pirates,
    it might choose to send 50 pirates to Island A, 50 pirates to Island B, and earn the maximum possible money.
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Initialise the Navigator with a list of islands and the crew size.

        We use a BinarySearchTree to store islands with their money-to-marine ratio.
        Insertion into a BinarySearchTree is O(log(N)) on average, giving us a worst-case complexity of O(Nlog(N))
        or less.

        Worst Case Complexity: O(Nlog(N)) or less, where N is the length of the 'islands' list.
        """
        self.island_bst = BinarySearchTree()
        for island in islands:
            if island.marines > 0:
                self.island_bst.__setitem__(island.money_per_marine(), island)

        self.crew = crew

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Select islands to plunder based on the best money-to-marine ratio.

        We iterate through the islands, and for each iteration, it selects the island with the
        best money-to-marine ratio. The BinarySearchTree is used to efficiently find the island with the best ratio,
        and the operation is O(log(N)) in the worst case. The loop iterates at most N times, leading to a worst-case
        complexity of O(Nlog(N)) or less. The best-case complexity is O(log(N)) or less.

        Worst Case Complexity: O(Nlog(N)) or less, where N is the number of islands.
        Best Case Complexity: O(log(N)) or less.
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
        Calculate earnings with different crew configurations.

        We calculate the earnings with different crew sizes, and for each crew
        size, it iterates through the islands using a loop. For C different crew sizes and N islands, it results in a
        complexity of O(C*N).

        Worst Case Complexity: O(C*N), where C is the length of 'crew_numbers' and N is the number of islands.
        Best Case Complexity: O(N), where N is the number of islands.

        Parameters:
        - crew_numbers: A list of crew sizes to calculate earnings for.

        Returns:
        A list of earnings corresponding to each crew size in 'crew_numbers'.
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
        Update the money and marine values of an island.

        We update the money and marines for an island, and it involves no searching or
        iteration. Therefore, it has a complexity of O(1).

        Worst Case Complexity: O(1)
        Best Case Complexity: O(1)

        Parameters:
        - island: The island to update.
        - new_money: The new money value for the island.
        - new_marines: The new marine count for the island.
        """
        island.money = new_money
        island.marines = new_marines
