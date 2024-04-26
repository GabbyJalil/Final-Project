
define g = Character("Gabby")
define i = Character("Iaroslav")

label start:
    scene white
    "THIS PROJECT IS CALLED: Architecture Spring 2024"
    "CODE: GEUBRINARIZKY JALIL"
    "IMAGES: IAROSLAV BUTIN"

    "Hello, people"

    "This is more of an archive for what two Arch students were doing over the Spring 2024 semester rather than a Visual Novel"

    "The programs used during this semester was Rhino 8 and Adobe Illustrator"

    "They had to pick two random words to base their projects on"
   
    "They developed a jewel which settled in a Jewel Chamber which settled in a landscape based on those two words"
   
    "One Arch student's name is Gabby"

    "She got CLOSED and REVERBERATION"

    "Another's name is Iaroslav"

    "He got REPEATING and IMPOSING"

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
        show white
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
    $ gab1 = 1
    $ gprojcompleted += 1
    g "This was my first project"
    g "Honestly this was a boring project bc it was strictly 2D"
    g "The spikey things were supposed to resemble closed, similar to 'keep out'"
    g "reverberation was visualized as sound bouncing around or ripples"
    hide proj 11
    jump goptions
label g2:
    show proj 21 at top
    g "This assignment was a little bit better bc it was working with 3D"
    g "I was fast with it too"
    g "I produce a lot of iterations in 1 day, but at the end I could only choose 1"
    g "I had to choose the more bulky one because it was easier to 3D print"
    g "Reverberation was visualized as wavy tectonic plates shifting"
    g "Closed was visualized as the spikey gears."
    $ gab2 = 1
    $ gprojcompleted += 1
    hide proj 21
    jump goptions
label g3:
    show proj 31 at top
    $ gab3 = 1
    $ gprojcompleted += 1
    "The Jewel Chamber was intended to feel cave like"
    "I wanted it to be dark with only a small hole ommiting light"
    "Closed off and Alone was the vibe"
    "Even the threshold was small that symbolized to keep out or to be locked in"
    "The inside was to convey how sound usually echoes in caves"
    hide proj 31
    jump goptions
label g4:
    show proj 41 at top
    "We had to carve out a mass of landscape for our jewel chamber to settle in"
    "I decided to bury mines to emphasize that enclosure"
    "The funky curves represent reverberation"
    "Making the staircase was the hardest part actually..."
    "..."
    "Those damn stairs"
    $ gab4 = 1
    $ gprojcompleted += 1
    hide proj 41
    jump goptions
label g5:
    show white at top
    "You see I have Assignment 5, but at this point in time I just wanted this project to be dealt and over with"
    "So nothing for you to see here"
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
        show white
        i "Looks like you already seen everything that I have to offer"
        if gab == 0:
            i "Let's go see Gabby's next"
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
    show a 1 at top
    $ iar1 = 1
    $ iprojcompleted += 1
    i "For the first assignment I chose to use the forms that look familiar to a lot of people on subconscious level."
    i "I wanted to create an object that would be coherent despite it being complicated in terms of its linework."
    hide a 1
    jump ioptions
label i2:
    show a 2 at top
    $ iar2 = 1
    $ iprojcompleted += 1
    i "For the second assignment I went with a structure that is intuitive and pleasant it its simplicity."
    i "The majority of this peace is done using elementary geometric forms(the columns and the platforms are extruded circles)"
    i "but the dome breaks that pattern, and that makes the model more exciting."
    hide a 2
    jump ioptions
label i3:
    show a 3 at top
    $ iar3 = 1
    $ iprojcompleted += 1
    i "For my model I created a room, and my main objectives were that it should be heavy, primal and make invite the light."
    i "I wanted it to be just as alien as my model, but at the same time be understandable."
    hide a 3
    jump ioptions
label i4:
    show a 4 at top
    $ iar4 = 1
    $ iprojcompleted += 1
    i "The concept for my landscape was that you can’t get outside, and that is why there’s a tunnel system that goes around the chamber."
    i "his way the visitor must follow the path and has a very calculated experience of this place."
    i "The further you get on this path the more the inside of the chamber reveals itself."
    hide a 4
    jump ioptions
label i5:
    show white at top
    $ iar5 = 1
    $ iprojcompleted += 1
    i "Unfortunately, Assignment 5 was still being in production when developing this Final Project"
    i "..."
    i "Oh Well ig lol"
    jump ioptions

label oops:
    i "Try again you already chose that"
    jump ioptions

label end:
    "This is the end"
    "Hoped you liked it"
    "CREDITS: Code made by Gabby / Images implemented by Iar and Gabby / Script made by Iar and Gabby"
    return
