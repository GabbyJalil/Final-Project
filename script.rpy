
define g = Character("Gabby")
define i = Character("Iaroslav")

label start:
    scene white
    "THIS PROJECT IS CALLED: Architecture Spring 2024"
    "CODE: GEUBRINARIZKY JALIL"
    "IMAGES: IAROSLAV BUTIN"

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

label gabproj:
    g "Hey this is Gabby"
    g "Which Assignment do you want to do first?"

$ gab1 = 0
$ gab2 = 0
$ gab3 = 0
$ gab4 = 0
$ gab5 = 0

label goptions:
    if gprojcompleted == 5:
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
    show proj 11 at top
    g "This is my First Project "
    $ gab1 = 1
    $ gprojcompleted += 1
    jump goptions
label g2:
    show proj 21 at top
    $ gab2 = 1
    $ gprojcompleted += 1
    jump goptions
label g3:
    show proj 31 at top
    $ gab3 = 1
    $ gprojcompleted += 1
    jump goptions
label g4:
    show proj 41 at top
    $ gab4 = 1
    $ gprojcompleted += 1
    jump goptions
label g5:
    show proj 5 at top
    $ gab5 = 1
    $ gprojcompleted += 1
    jump goptions

label iarproj:
    i "This is Iar"
    i "Which one of these projects would you like to choose"

$ iar1 = 0
$ iar2 = 0
$ iar3 = 0
$ iar4 = 0
$ iar5 = 0

label ioptions:
    if iprojcompleted == 5:
        i "Looks like you already seen everything that I have to offer"
        if gab == 0:
            i "Let's go see Iar's next"
            jump gabproj
        else:
            jump end
    menu:
        "Assignment 1: Overlaid Figures":
            if iar1 == 1:
                jump oops
            else:
                jump i1
        "Assignment 2: The Jewel":
            if iar2 == 1:
                jump oops
            else:
                jump i2
        "Assignment 3: Jewel Chamber":
            if iar3 == 1:
                jump oops
            else:
                jump i3
        "Assignment 4: Terrain and Procession":
            if iar4 == 1:
                jump oops
            else:
                jump i4
        "Assignment 5: Frame Meets Mass":
            if iar5 == 1:
                jump oops
            else:
                jump i5

label i1:
    show proj 11 at top
    $ iar1 = 1
    $ iprojcompleted += 1
    jump ioptions
label i2:
    show proj 21 at top
    $ iar2 = 1
    $ iprojcompleted += 1
    jump ioptions
label i3:
    show proj 12 at top
    $ iar3 = 1
    $ iprojcompleted += 1
    jump ioptions
label i4:
    show proj 21 at top
    $ iar4 = 1
    $ iprojcompleted += 1
    jump ioptions
label i5:
    show proj 23 at top
    $ iar5 = 1
    $ iprojcompleted += 1
    jump ioptions

label oops:
    i "Try again you already chose that"
    jump ioptions

label end:
    "this is the end"
    return