from p5 import *
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
    """Generator for the color sequence. It is randomly "seeded" and
    then each rgb goes up or down randomly

    Args:
        step (int, optional): How big the step is between each generation

    Yields:
        Tuple[int, int, int]: red, green, blue values
    """
    # Randomly seed the r g b values
    r, g, b = (random_uniform(0, 255), random_uniform(0, 255),
               random_uniform(0, 255))

    # Randomly determine if each r g and b value is increasing or not
    r_inc = True
    g_inc = True
    b_inc = True
    r_step = random_uniform(step)
    g_step = random_uniform(step)
    b_step = random_uniform(step)

    # Yield the initial r, g, b values
    yield r, g, b

    # Loop and yeild forever
    while True:
        # If r is increasing
        if r_inc:
            # Increment r by the step
            r += r_step
            # Ensure that the next step will be within the limits
            # if not then set the flag to decreasing
            r_inc = r < 255 - r_step
        # If r is decreasing
        else:
            # Decrement r by the step
            r -= r_step
            # Ensure that the next step will be within the limits
            # if not then set the flag to increasing
            r_inc = r < r_step

        # See above
        if g_inc:
            g += g_step
            g_inc = g < 255 - g_step
        else:
            g -= g_step
            g_inc = g < g_step

        # See above
        if b_inc:
            b += b_step
            b_inc = b < 255 - b_step
        else:
            b -= b_step
            b_inc = b < b_step

        # Yield the red, green, and blue values
        yield r, g, b


def setup():
    """Set up the canvas as a 800, 600 window on the screen
    """
    size(800, 600)
    stroke_weight(3)


def draw():
    """Draw the new frame each loop of the program
    """

    max_frames = 1_000

    # Normally this would be just in the setup but for some reason
    # python P5 doesn't like just setting the background in the setup
    # loop
    if frame_count == 1:
        background(51)

    # Instantiate a new generator for the colors of the line. The generator
    # picks a random starting point and then
    colors = color(5)

    # Set up the default length and angle
    length = height / 35
    angle = (width / height) * 0.25

    # Reset the matrix to the initial translation
    reset_matrix()
    translate(width / 2, height)

    # Loop through the collatz sequence for the current frame count.
    # Reversed so we can start at 1 and then go to n
    for collatz_number in reversed(list(collatz(frame_count))):
        # If the current number is even rotate to the right
        if collatz_number % 2 == 0:
            rotate(angle)

        # If it is odd then rotate to the left with some extra "umph"
        # because it looks better
        else:
            rotate(-angle * 1.5)

        # Set the stroke to the current color and add some alpha so that
        # overlapping paths have more color
        r, g, b = next(colors)
        stroke(r, g, b, 20)

        # Draw the line for the collatz sequence
        line((0, 0), (0, -length))

        # Translate to the end of the line
        translate(0, -length)

    # Check if we are at the end, if so stop looping
    if frame_count > max_frames:
        no_loop()


if __name__ == '__main__':
    run()
