from random import randrange

from graphics import GraphWin, Line, Point

# initialize graphics window
width = 1000
height = 1000
window = GraphWin("sorting", width, height,)
window.setCoords(0, 0, width, height)

# array of numbers to be sorted
numbers = [randrange(height) for _ in range(width)]

lines = [
    Line(Point(index, 0), Point(index, value)).draw(window)
    for index, value in enumerate(numbers)
]


def draw(compindex1: int, compindex2: int) -> None:
    """
    Update the window, highlighting the lines representing
    the numbers currently being compared
    """

    lines[compindex1].setFill("red")
    lines[compindex2].setFill("red")

    for index, value in enumerate(numbers):
        # if there is discrepancy between value in `numbers` and height of line,
        # then we must redraw the line to show the correct height
        if not lines[index].getP2().getY() == value:
            lines[index].undraw()
            lines[index] = Line(Point(index, 0), Point(index, value)).draw(window)

    lines[compindex1].setFill("black")
    lines[compindex2].setFill("black")


def insertionSort(low: int, high: int) -> None:
    for i in range(low, high):
        key = numbers[i]

        j = i - 1
        while j >= 0 and key <= numbers[j]:
            draw(j, j + 1)

            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key


def quicksort(low: int, high: int) -> None:
    if low < high:
        if high - low > 10:
            pi = partition_r(low, high)

            # recursively sort first and second half, divided by partition
            quicksort(low, pi - 1)
            quicksort(pi + 1, high)
        else:
            insertionSort(low, high + 1)


def partition(low: int, high: int) -> int:
    i = low - 1

    pivot = numbers[high]

    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1

            numbers[i], numbers[j] = numbers[j], numbers[i]

        draw(high, j)

    numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]

    return i + 1


def partition_r(low: int, high: int) -> int:
    r = randrange(low, high)

    numbers[r], numbers[high] = numbers[high], numbers[r]

    return partition(low, high)


if __name__ == '__main__':
    # getMouse() used to make the graphics window wait for a mouse input so it waits before doing the next step
    window.getMouse()

    quicksort(0, len(numbers) - 1)

    window.getMouse()
