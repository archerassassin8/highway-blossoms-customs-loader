init python:
    import os
    import json
    
    path = os.getcwd() + "/game/mods"
    
    #path = ...\Highway Blossoms\game\mods
    #if opening getting a "cannot find /game/mods" looking error, just hardcode your own mods directory above
    
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]

    class Mod:
        def __init__(self, name, author, date, desc, label):
            self.name = name
            self.author = author
            self.date = date
            self.desc = desc
            self.label = label
            
    
    mod_list = []
    
    for folder in subfolders:
        if os.path.isfile(folder + "/info.json"):
            with open(folder + "/info.json", 'r') as info_file:
                info_data = json.load(info_file, object_hook=lambda d: Mod(**d))
            mod_list.append(Mod(info_data.name, info_data.author, info_data.date, info_data.desc, info_data.label))
    
    

screen mods():
    tag extra
    modal True
    # The background.
    add "gui/extras/backdrop.png"
    text "{font=gui/fonts/Lindale-Regular.ttf}Custom Content" ypos 30 size 125 outlines [ (absolute(5), "#f6f2e4", absolute(0), absolute(0)), (absolute(3), "#252425", absolute(0), absolute(0)) ] color "#f6f2e4" xalign 0.0 text_align 0.0 font "gui/fonts/Lindale-Regular.ttf" xpos 125
    textbutton _("Return") xalign 0.97 ypos 70 text_size 97 text_idle_outlines [ (absolute(6), "#ff7152", absolute(0), absolute(0)), (absolute(3), "#252425", absolute(0), absolute(0)) ] text_hover_outlines [ (absolute(6), "#f6f2e4", absolute(0), absolute(0)), (absolute(3), "#252425", absolute(0), absolute(0)) ] text_color "#f6f2e4" text_align 0.0 background None action Hide("mods"), With(Dissolve(.5))

    window:
        background None yminimum None yalign .7 ymaximum None
        ymargin 0 xmargin 0 ypadding 0 left_padding 200 xfill False yfill False
        top_padding 200

        side "c r":

            viewport id "vp":
                draggable True
                mousewheel True
                vbox:
                    spacing 15
                    for mod in mod_list:
                        window:
                            background  "/mods/" + mod.name + "/image.png"
                            left_padding 535
                            ypadding 12
                            ysize 295
                            hbox:
                                yfill True
                                spacing 100
                                vbox:
                                    xmaximum 800
                                    text "[mod.name]" color "#f6f2e4" outlines [ (absolute(3), "#252425", absolute(0), absolute(0)) ]
                                    text "[mod.desc] \n\n{b}Author: [mod.author]\nDate Created: [mod.date]{/b}" size 25 xoffset 16 color "#f6f2e4"
                                textbutton "Read" idle_background Transform("gui/extras/dumpster fire/you are making a mistake_idle.png", alpha=0.5) hover_background "gui/extras/dumpster fire/you are making a mistake_idle.png" action Start(mod.label) yalign 1.0 text_size 45 text_outlines [ (absolute(4), "#ff7152", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_yalign 0.0 xpadding 0 ymargin 0 ypadding 0 text_yoffset -5 text_color "#f6f2e4"

            vbar value YScrollValue("vp")