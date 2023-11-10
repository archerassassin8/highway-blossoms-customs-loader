

label mod_test:

    $ camera_reset()
    $ layer_move("background", 2000)
    $ layer_move("background2", 1200)
    $ layer_move("middle", 1000)
    $ layer_move("forward", 600)

    $ amber_seatbelt = True

    $ marina_seatbelt = True

    scene bg Desert onlayer background:
        xpos -0.14 ypos -0.27 xanchor 0.1 yanchor 0.2 zoom 1.19
        block:
            ypos -0.27
            ease 1.5 ypos -0.265
            ease 1.5 ypos -0.27
            repeat
    show rv_interior onlayer background2:
        xpos -0.14 ypos -0.14 zoom 1.12
    scene rv_front_dash onlayer forward:
        zoom 0.87 ypos -0.03
    show rv_glass day onlayer forward:
        zoom 0.87
    show rv_front day onlayer forward:
        zoom 0.83 xpos -0.094 ypos 0.75
    scene amber driving neutral front onlayer middle:
        xpos 905 ypos -36
    show marina riding neutral front onlayer middle:
        xpos 17 ypos -13
    show black onlayer flatoverlay

    $ layer_move("background", 1700)
    $ layer_move("background2", 1200)
    $ layer_move("middle", 825)
    $ layer_move("forward", 600)

    $camera_move(0, 200, -1150, 0, duration=0)

    hide black onlayer flatoverlay with dissolve

play ambient enginenoise fadein 1.5
$ ambient_notify()
play music CongaWonga fadein 1.5
$ music_notify()
window show

"This is the narrator."

Amber "Whoa, I'm Amber HighwayBlossoms!"

Marina "Marina."

play sound "sounds/sfx/turning_off_the_engine.ogg"
$ sfx_notify()
stop ambient fadeout 0.5

"I cut the ignition, a sound plays."

stop music fadeout 2.0

$ voice("Jumbo Laugh_echo", tag="jumbo")

show amber resting onlayer middle:
        xpos 905 ypos -36
show marina riding nervous tilt onlayer middle:
        xpos 17 ypos -13
        
show jumbo creepier onlayer middle:
    zoom 0.36
    alpha 0.0
    xalign 0.5
    yalign 0.90
    ease 0.50 alpha 1.0 zoom 0.38 yalign 0.65
    
"JUMBO JUMPSCARE!{nw}"

$ voice_sustain()

stop music fadeout 1.5

show jumbo creepy onlayer middle:
    zoom 0.38
    alpha 1.0
    xalign 0.5
    yalign 0.65
    ease 2.5 alpha 0.5 zoom 0.01 yalign 0.95
    
show amber driving nervous front onlayer middle:
        xpos 905 ypos -36
show marina riding nervous front onlayer middle:
        xpos 17 ypos -13
        
Marina "Horrific"

play sound "mods/Template/assets/amber_roadtrip.mp3"
show amber standing uncanny onlayer middle:
    xpos 1100 ypos -36
    
Amber "highway blossoms road trip"

$ renpy.pause(3, hard=True)
    
stop ambient fadeout 0.5

window hide

show black onlayer flatoverlay with dissolve

show logoanimation onlayer flatoverlay:
    zoom 1.2 xalign 0.5 yalign 0.65

$ layer_move("middle", 1001)

play music "<from 238>sounds/music/hawaiiain_and_salt.ogg" fadein 1.0 fadeout 3.0 noloop
$ music_notify()
pause 15.0

hide logoanimation onlayer flatoverlay
with Dissolve(1.0)

return
