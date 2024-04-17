# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Gabby")


# The game starts here.

label start:
    #scene bg classroom
    show proj 11
    "Gabby" "This is my first project of the semester"    # transition/transforms
    #show gabby at right #left/center top change position of images
    #show gabby happy at left with move #pixellate/dissolve/vpunch images
    #hide gabby happy
    #call love #to call the function/label can jump back to statement
    #jump love # to skip to another area
"""
menu:
    "Beep":
        show gabby happy at right
        $ animal = 'fox' #python statement
    "Boop":
        show gabby sad at center
    if 1 + 2 == 3:
        $ return true



label gabproj:

label iarproj:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
"""
    return
