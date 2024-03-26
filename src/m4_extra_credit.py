###############################################################################
# Done: 1. (5 pts)
#
#   For this extra credit question, we are going to create a program that can
#   draw a house out of stars. This is very similiar to the shapes that you did
#   on your exam review. Feel free to copy any of the code you wrote for those
#   practice problems if you think it would be helpful.
#   
#   For this _TODO_, write a function called house() that takes 2 parameters:
#       height      <-- int
#       width       <-- int
#
#   We are going to define a house like this. It is essentially two different
#   shapes put together: a triangle and a box (that is open at the top).
#
#   The box has the same dimensions as the height and the width given.
#
#   The triangle is two stars wider than the house and is as tall as it can
#   until it reaches a point (one *) or two *'s.
#
#   So for example, if the function is given these dimensions:
#
#       height = 4
#       width = 5
#
#   it would print:
#
#      *
#     ***
#    *****
#   *******
#    *   *
#    *   *
#    *   *
#    *****
#
#   Also, notice that if the width is odd (like above) there is a pointy
#   roof. However, if the width is even, the roof would have to be flat on
#   top.
#
#   So, if the function is given these dimensions:
#
#   height = 4
#   width = 6
#
#   it would print:
#
#      **
#     ****
#    ******
#   ********
#    *    *
#    *    *
#    *    *
#    ******
#
#   The smallest house you can have is one with a height of 2 and width of 3.
#   If the function is given any dimensions smaller than these, it should print:
#
#       "Invalid dimensions!"
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def house(height, width):
    if height < 2 or width < 3:
        print("Invalid dimensions!")
        return
    
    def print_roof():
        roof_width = width + 2 if width % 2 == 0 else width + 3
        for i in range(1, height + 1):
            spaces = " " * (roof_width - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)
    
    def print_box():
        for i in range(height):
            print("*" + " " * (width - 2) + "*")
    
    print_roof()
    print_box()

house(4, 5)
print()
house(4, 6)
print()
house(2, 3)
print()
house(1, 3)
