from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""

    # Create the matrix with dummy data
    cost = [[(0, None) for i in range(len(b) + 1)] for elements in range(len(a) + 1)]

    # Create the starting cell of the matrix
    cost[0][0] = (0, None)

    # Create a container for the minimum of the below 3 options
    minimum = []

    # Create the rows of the matrix
    for i in range(len(a) + 1):
        # Create the columns of the matrix
        for j in range(len(b) + 1):
            # If we insert characters calculate the value
            if j >= 0:
                minimum = [cost[i][j - 1][0] + 1, Operation.INSERTED]

            # If we delete characters calculate the value
            if i > 0:
                if minimum[0] > cost[i - 1][j][0] + 1:
                    minimum = [cost[i - 1][j][0] + 1, Operation.DELETED]
                elif j == 0:
                    minimum = [cost[i - 1][j][0] + 1, Operation.DELETED]

            # If we substitute characters calculate the value
            if i > 0 and j > 0:
                if a[i - 1] == b[j - 1] and minimum[0] > cost[i - 1][j - 1][0]:
                    minimum = [cost[i - 1][j - 1][0], Operation.SUBSTITUTED]
                elif a[i - 1] != b[j - 1] and minimum[0] > cost[i - 1][j - 1][0] + 1:
                    minimum = [cost[i - 1][j - 1][0] + 1, Operation.SUBSTITUTED]

            # Store the values in the cost matrix within a tuple
            if (i != 0 or j != 0):
                cost[i][j] = tuple(minimum)
    return cost
