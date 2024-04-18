# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Gabby")
define i = Character("Iaroslav")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Hello, people"

    "This is more of an archive for what two Arch students were doing over the Spring 2024 semester rather than a Visual Novel"

    "One Arch student's name is Gabby"

    "Another's name is Iaroslav"

    "Pick which student you'd like to examine their projects of"
$ gab = 0
$ iar = 0
$ gprojcompleted = 0
$ iprojcompleted = 0
menu:
    "Gabby":
        $ gab += 1
        jump gabproj
    "Iaroslav":
        $ iar += 1
        jump iarproj
    # This ends the game.

label gabproj:
    g "Which Assignment do you want to do first?"

$ gab1 = 0
$ gab2 = 0
$ gab3 = 0
$ gab4 = 0
$ gab5 = 0
label goptions:
    if gab == 6:
        g "Looks like you already seen everything that I have to offer"
        if iar == 0:
            g "Let's go see Iar's next"
            jump iarproj
        else:
            jump end
    menu:
        "Assignment 1: Overlaid Figures":
            if gab1 == 1:
                jump oopsie
            else:
                jump g1
        "Assignment 2: The Jewel":
            if gab2 == 1:
                jump oopsie
            else:
                jump g2
        "Assignment 3: Jewel Chamber":
            if gab3 == 1:
                jump oopsie
            else:
                jump g3
        "Assignment 4: Terrain and Procession":
            if gab4 == 1:
                jump oopsie
            else:
                jump g4
        "Assignment 5: Frame Meets Mass":
            if gab5 == 1:
                jump oopsie
            else:
                jump g5

label oopsie:
    g "Try again you already chose that"
    jump goptions

label g1:
    show proj 11
    $ gab1 = 1
    $ gab += 1
    jump goptions
label g2:
    show proj 21
    $ gab2 = 1
    $ gab += 1
    jump goptions
label g3:
    show proj 12
    $ gab3 = 1
    $ gab += 1
    jump goptions
label g4:
    show proj 21
    $ gab4 = 1
    $ gab += 1
    jump goptions
label g5:
    show proj 23
    $ gab5 = 1
    $ gab += 1
    jump goptions

label iarproj:
    i "This is Iar"
    show proj 12 at top
    jump end

label end:
    "this is the end"
    return
"""
define i = Character("Gabby")


# The game starts here.

label start:
    scene bg classroom
    show gabby happy    # transition/transforms
    show gabby at right #left/center top change position of images
    show gabby happy at left with move #pixellate/dissolve/vpunch images
    hide gabby happy
    call love #to call the function/label can jump back to statement
    jump love # to skip to another area
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

    return
"""