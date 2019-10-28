from p5 import *
from random import randrange
from typing import Tuple


def collatz(n: int) -> int:
    """Lazily generate the Collatz Conjecture series. The series is
    defined as follows:

        f(n) = n/2     if n is even
               3n + 1  if n is odd

        a_i = n        if i == 0
              f(a_i-1) if i != 0

    Args:
        n (int): Number to start the sequence at

    Yields:
        int: Next collatz number in the sequence, starting with the
             n passed in
    """
    # Yeild the input so that the sequence starts with the seed
    yield n

    # This probably won't loop infinitely but math doesn't really know
    # as long as the current n is not the end of the sequence then
    # return the next item
    while n != 1:
        # If n is even
        if n % 2 == 0:
            # Return n / 2
            n = n / 2

        # If n is odd
        else:
            # Return 3 * n + 1. 3 * any number will always be odd
            # so 3n + 1 is always even so we can skip a step by just
            # returning the following number and skipping all odds this
            # way
            n = (3 * n + 1) / 2

        # Cast the result to an integer and yield it
        yield int(n)


def color(step: int=10) -> Tuple[int, int, int]:

    r, g, b = randrange(0, 255), randrange(0, 255), randrange(0, 255)
    r_inc = bool(randrange(0, 1))
    g_inc = bool(randrange(0, 1))
    b_inc = bool(randrange(0, 1))
    yield r, g, b
    while True:
        if r_inc:
            r += step
            r_inc = r < 255 - step
        else:
            r -= step
            r_inc = r < step

        if g_inc:
            g += step
            g_inc = g < 255 - step
        else:
            g -= step
            g_inc = g < step

        if b_inc:
            b += step
            r_inc = b < 255 - step
        else:
            b -= step
            r_inc = b < step

        yield r, g, b


def setup():
    size(800, 600)
    background(51)


i = 10
colors = color()


def draw():
    global i

    if i == 10:
        input(">")
        background(51)

    colors = color()
    r, g, b = next(colors)

    sequence = list(collatz(i))
    # print(sequence)

    length = 12
    angle = 0.25
    reset_matrix()
    translate(width / 2, height)

    for collatz_number in reversed(sequence):
        if collatz_number % 2 == 0:
            rotate(angle)
        else:
            rotate(-angle * 1.5)

        stroke_weight(5)

        stroke(r, g, b, 10)
        r, g, b = next(colors)

        line((0, 0), (0, -length))

        translate(0, -length)

        # print("DONE")

    i += 1

    # print(i)

    if i > 10_000:
        no_loop()


if __name__ == '__main__':
    run()
