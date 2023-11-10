screen extras():
    modal True
    tag extra
    add Solid(lighttheme_text[0]):
        alpha 0.35
    frame at pagein:
        xfill False
        yfill False
        xalign 0.5 yalign 0.5 xminimum 579 yminimum 620 ypadding 0
        background Frame("gui/extras/home/main.png",0,0,10,10)
        vbox:
            style_prefix "mmextras"
            ypos -12
            xalign 0.5
            spacing 10
            text _("Extras") font "gui/fonts/Lindale-Regular.ttf" size 125 outlines [ (absolute(4), darktheme_text[0], absolute(0), absolute(0)),(absolute(2), "#201a18", absolute(0), absolute(0)) ] color darktheme_text[0] xalign 0.5 text_align 0.5
            textbutton _("Galleries") action ShowMenu("gallery")
            textbutton _("Music Room") action ShowMenu("music_room")
            textbutton _("Legacy Content") action ShowMenu("legacy")
            if renpy.loadable("images/NextExit/bg/strato day.jpg"):
                textbutton _("DLC Content") action ShowMenu("dlc_menu")
            else:
                textbutton _("DLC Content") action ShowMenu("dlc_menu_unbought")
            textbutton _("Custom Content") action ShowMenu("mods")
            textbutton _("Credits") action ShowMenu("credits")
            #textbutton _("{size=-5}Back")
    key "game_menu" action Hide("extras"),With(dissolve)
style mmextras_button:
    hover_background Transform("gui/extras/home/hover.png",xalign=0.5,yalign=0.5)
    idle_background None
    insensitive_color "#201a18"
    insensitive_background None
    xalign 0.5
style mmextras_button_text:
    outlines [ (absolute(1), "#201a18", absolute(0), absolute(0)) ]
    color darktheme_text[0]
    size 60
    text_align 0.5
    xalign 0.5

# if not persistent.goofball_mode:
#     imagebutton:
#         auto "images/ui/extras/receipt_checkbox_%s.png"
#         action ToggleField(persistent, "goofball_mode")
# elif goofball_mode:
#     $ grantTrophyWithTrophyID("Born just in time for dank memes")
#     imagebutton:
#         auto "images/ui/extras/receipt_checkedcheckbox_%s.png"
#         action ToggleField(persistent, "goofball_mode")
screen dlc_menu():
    tag extra
    modal True
    fixed:
        add "images/bg/20 Las Vegas Strip Night.jpg"
        vbox:
            xalign 0.5 yalign 0.3
            add "images/NextExit/nextexitlogo.png" xalign 0.5
            add "gui/confirm/rv.png" xalign 1.0
            frame:
                background Frame("gui/confirm/confirmbg.png",15,15)
                xalign 0.5 yalign 0.5
                xpadding 80
                xmaximum 1200
                yminimum 400
                top_padding 25
                bottom_padding 30
                vbox:
                    xalign 0.5
                    yalign 0.5
                    style_prefix "yesno"
                    label _("Highway Blossoms: Next Exit takes place approximately one month after the events of main game. It's {b}highly recommended{/b} you play through the game in its entirety before continuing on to the DLC."):
                        xalign 0.5
                        text_size 40
                    null height 5
                    textbutton _("I understand! Let's go to Las Vegas! (Begin DLC)"):
                        action Start("nextexit_start")
                        text_size 35
                        text_idle_outlines [ (absolute(5), "#53453700", absolute(0), absolute(0)), (absolute(2), "#474135", absolute(0), absolute(0)) ]
                        text_hover_outlines [ (absolute(5), "#474135", absolute(0), absolute(0)), (absolute(2), "#ff7152", absolute(0), absolute(0)) ]
                        at transform:
                            alpha 0.7
                            on hover:
                                ease 0.3 alpha 1.0
                            on idle:
                                ease 0.2 alpha 0.7

                    textbutton _("Okay! I'll be back soon! (Return to Main Menu)"):
                        action Hide("dlc_menu")
                        text_size 35
                        text_idle_outlines [ (absolute(5), "#53453700", absolute(0), absolute(0)), (absolute(2), "#474135", absolute(0), absolute(0)) ]
                        text_hover_outlines [ (absolute(5), "#474135", absolute(0), absolute(0)), (absolute(2), "#ff7152", absolute(0), absolute(0)) ]
                        at transform:
                            alpha 0.7
                            on hover:
                                ease 0.3 alpha 1.0
                            on idle:
                                ease 0.2 alpha 0.7

        at transform:
            on show:
                alpha 0.0
                ease .25 alpha 1.0
            on hide:
                ease .2 alpha 0.0

    key "game_menu" action Hide("dlc_menu")
screen dlc_menu_unbought():
    tag extra
    modal True
    fixed:
        add "dlc kv big":
            xalign 0.5 yalign .3 zoom .8
        vbox:
            xalign 0.5 yalign 0.3
            #add "images/NextExit/nextexitlogo.png" xalign 0.5
            add "gui/confirm/rv.png" xalign 1.0
            frame:
                background Frame("gui/confirm/confirmbg.png",15,15)
                xalign 0.5 yalign 0.5
                xpadding 80
                xmaximum 1200
                yminimum 400
                top_padding 25
                bottom_padding 30
                vbox:
                    xalign 0.5
                    yalign 0.5
                    style_prefix "yesno"
                    label _("Highway Blossoms: Next Exit takes place approximately one month after the events of main game. You can purchase it wherever you bought Highway Blossoms!"):
                        xalign 0.5
                        text_size 40
                    null height 5
                    # textbutton _("I understand! Let's go to Las Vegas! (Begin DLC)"):
                    #     action Start("nextexit_start")
                    #     text_size 35
                    #     text_idle_outlines [ (absolute(5), "#53453700", absolute(0), absolute(0)), (absolute(2), "#474135", absolute(0), absolute(0)) ]
                    #     text_hover_outlines [ (absolute(5), "#474135", absolute(0), absolute(0)), (absolute(2), "#ff7152", absolute(0), absolute(0)) ]
                    #     at transform:
                    #         alpha 0.7
                    #         on hover:
                    #             ease 0.3 alpha 1.0
                    #         on idle:
                    #             ease 0.2 alpha 0.7

                    textbutton _("Okay! I'll be back soon! (Return to Main Menu)"):
                        action Hide("dlc_menu_unbought")
                        text_size 35
                        text_idle_outlines [ (absolute(5), "#53453700", absolute(0), absolute(0)), (absolute(2), "#474135", absolute(0), absolute(0)) ]
                        text_hover_outlines [ (absolute(5), "#474135", absolute(0), absolute(0)), (absolute(2), "#ff7152", absolute(0), absolute(0)) ]
                        at transform:
                            alpha 0.7
                            on hover:
                                ease 0.3 alpha 1.0
                            on idle:
                                ease 0.2 alpha 0.7

        at transform:
            on show:
                alpha 0.0
                ease .25 alpha 1.0
            on hide:
                ease .2 alpha 0.0

    key "game_menu" action Hide("dlc_menu")
default togglefit = False
default view_gallery_help = True
transform closeup_buttonanim:
    zoom .35 alpha .5
    on hover:
        alpha .75
    on idle:
        alpha .5
    on selected_idle:
        alpha 1.0
transform closeup_buttonanim_ui:
    zoom .15 alpha .5

    on hover:
        alpha .75
    on idle:
        alpha .5
        time 5
        ease 3 alpha 0.0
        time 10
        ease 5 alpha .5
        repeat
    on selected_idle:
        alpha 1.0
screen gallery_closeup(images):
    style_prefix "mmextras"

    # $ togglefit = None

    # Use normal hide UI binds (H, Triangle, etc.) so as to not subvert user expectations.
    key "hide_windows" action ToggleVariable("view_gallery_help", true_value=True, false_value=False), With(Dissolve(0.1))

    # Legacy compatibility.
    key "mouseup_3" action ToggleVariable("view_gallery_help", true_value=True, false_value=False), With(Dissolve(0.1))
    key "K_BACKSPACE" action ToggleVariable("view_gallery_help", true_value=True, false_value=False), With(Dissolve(0.1))

    # Make scrollable with right stick on controllers. Uses "step" instead of pixel counts.
    # [akemi] ※ TODO: Whenever the new scroll animator becomes available on Ren'Py 8 stable (and behaves less broken than it currently does in the nightlies), implement it for better smoothness.
    # See: https://github.com/renpy/renpy/blob/b3611b04cd45faf09a201a841ec1479bf494042f/renpy/common/00action_other.rpy#L634-L705
    key "akemi_cgviewer_up" action Scroll("cgviewer", "vertical decrease", amount="step")
    key "akemi_cgviewer_down" action Scroll("cgviewer", "vertical increase", amount="step")
    key "akemi_cgviewer_left" action Scroll("cgviewer", "horizontal decrease", amount="step")
    key "akemi_cgviewer_right" action Scroll("cgviewer", "horizontal increase", amount="step")

    vbox:
        xsize 1920 xalign 0.5
        side "c":
                area (0, 0, 1920, 1080) xalign 0.5
                viewport id "cgviewer":
                    xalign 0.5
                    draggable True
                    yinitial 0.5
                    xinitial 0.5
                    if togglefit:
                        frame:
                            padding(0,0,0,0) xfill True background ("#000")
                            add images[closeup_page]:
                                maxsize (1920,5000) align (0.5,0.45) alpha 0.5
                            add images[closeup_page]:
                                xalign 0.5 yalign 0.5
                                maxsize(1920,1080)
                    else:
                        xfill True yfill True
                        add images[closeup_page]:
                           xalign 0.5 yalign 0.5
    if view_gallery_help:
        frame:
            xalign 1.0 yalign 1.0
            background Frame("gui/extras/home/main.png",130,130,10,10)
            top_padding 130
            xpadding 10
            bottom_padding 10
            xsize 579
            vbox:
                xalign .5
                spacing 40
                vbox:
                    xalign .5
                    hbox:
                        xalign .5 spacing 20
                        imagebutton idle "gui/galleries/zoom.png" hover "gui/galleries/zoom.png" action ToggleVariable("togglefit", true_value=True, false_value=False), SelectedIf(togglefit == False), With(Dissolve(0.5)) at closeup_buttonanim tooltip _("Zoom to full resolution.") keysym "akemi_cgviewer_zoom"
                        imagebutton idle "gui/galleries/fill.png" hover "gui/galleries/fill.png" action ToggleVariable("togglefit", true_value=True, false_value=False), SelectedIf(togglefit == True), With(Dissolve(0.5)) at closeup_buttonanim tooltip _("Fit image to screen.") keysym "akemi_cgviewer_zoom"
                        imagebutton idle "gui/galleries/hideui.png" hover "gui/galleries/hideui.png" action ToggleVariable("view_gallery_help",true_value=True,false_value=False),With(Dissolve(0.1)) at closeup_buttonanim tooltip _("Hide UI.")
                    $ tooltip = GetTooltip()
                    if tooltip:
                        text "[tooltip]" xalign .5 outlines [ (absolute(1), "#201a18", absolute(0), absolute(0)) ] color darktheme_text[0] size 33 text_align 0.5
                    else:
                        text _("Drag to move view.") xalign .5 outlines [ (absolute(1), "#201a18", absolute(0), absolute(0)) ] color darktheme_text[0] size 33 text_align 0.5
                hbox:
                    xalign .5
                    spacing 30
                    hbox:
                        text "PREVIOUS" size 28 outlines [ (absolute(1), "#201a18", absolute(0), absolute(0)) ] color darktheme_text[0] text_align 0.0
                        imagebutton auto "gui/galleries/back_%s.png":
                            action [SetVariable("closeup_page", closeup_page - 1),With(Dissolve(0.25)),SensitiveIf(closeup_page > 0)]
                            keysym "akemi_pageleft"
                    hbox:
                        text "NEXT" size 28 outlines [ (absolute(1), "#201a18", absolute(0), absolute(0)) ] color darktheme_text[0] text_align 0.0
                        imagebutton auto "gui/galleries/next_%s.png":
                            action [SetVariable("closeup_page", closeup_page + 1),With(Dissolve(0.25)),SensitiveIf(closeup_page < len(images) - 1)]
                            keysym "akemi_pageright"

                textbutton _("Return"):
                    xalign 0.5
                    yalign 0.975
                    action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]
                    keysym "akemi_returntosuperview" default_focus True
    else:
        imagebutton idle "gui/galleries/hideui.png" hover "gui/galleries/hideui.png" action ToggleVariable("view_gallery_help",true_value=True,false_value=False),With(Dissolve(0.1)) at closeup_buttonanim_ui tooltip _("Hide UI.") xalign 0.975 yalign 0.975
default creditscreen_choice = "hb_credits"
screen credits():
    key "game_menu" action Hide("credits"),With(dissolve)
    # Ensure this replaces the main menu.
    tag extra
    modal True
    $ grantTrophyWithTrophyID("You Really Do Care!")
    if creditscreen_choice == "ne_credits":
        add "stratoex evening":
            xalign .5 yalign 0.0
    add "gui/extras/backdrop.png"
    if creditscreen_choice == "ne_credits":
        add "nextexitlogo":
            xalign .975 yalign .3
    # The background.

    text _("{font=gui/fonts/Lindale-Regular.ttf}Credits") ypos 30 size 125 outlines [ (absolute(5), "#f6f2e4", absolute(0), absolute(0)), (absolute(3), "#252425", absolute(0), absolute(0)) ] color "#f6f2e4" xalign 0.0 text_align 0.0 font "gui/fonts/Lindale-Regular.ttf" xpos 125
    textbutton _("Return") xalign 0.97 ypos 70 text_size 97 text_idle_outlines [ (absolute(6), "#ff7152", absolute(0), absolute(0)), (absolute(3), "#252425", absolute(0), absolute(0)) ] text_hover_outlines [ (absolute(6), "#f6f2e4", absolute(0), absolute(0)), (absolute(3), "#252425", absolute(0), absolute(0)) ] text_color "#f6f2e4" text_align 0.0 background None action Hide("credits"),With(Dissolve(.5))
    # A grid of buttons.
    window:
        background None yminimum None yalign 0.0 ypos .225
        ymargin 0 xmargin 0 ypadding 0 xpadding 0 xfill False yfill False
        hbox:
            ymaximum 653
            xfill True yfill True
            xpos 150
            yalign 0.0
        #grid for images
            use expression creditscreen_choice
    hbox:
        yalign 0.175 xpos 100 spacing 7
        style_prefix "withinoptions"
        textbutton "Highway Blossoms" action SetVariable("creditscreen_choice","hb_credits"), SelectedIf(creditscreen_choice == "hb_credits"), With(Dissolve(0.5)):
                        selected_foreground None text_idle_outlines [ (absolute(4), "#252425", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_selected_outlines [ (absolute(4), "#ff7152", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_hover_outlines [ (absolute(4), "#ff7152", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_color "#f6f2e4" text_size 30
        if renpy.has_label("nextexit_start"):
            textbutton "Next Exit" action SetVariable("creditscreen_choice", "ne_credits"),SelectedIf(creditscreen_choice == "ne_credits"), With(Dissolve(0.5)):
                selected_foreground None text_idle_outlines [ (absolute(4), "#252425", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_selected_outlines [ (absolute(4), "#ff7152", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_hover_outlines [ (absolute(4), "#ff7152", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_color "#f6f2e4" text_size 30
        textbutton "Voice Cast" action SetVariable("creditscreen_choice","va_credits"), SelectedIf(creditscreen_choice == "va_credits"), With(Dissolve(0.5)):
            selected_foreground None text_idle_outlines [ (absolute(4), "#252425", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_selected_outlines [ (absolute(4), "#ff7152", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_hover_outlines [ (absolute(4), "#ff7152", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_color "#f6f2e4" text_size 30
        textbutton "Localization" action SetVariable("creditscreen_choice","tl_credits"), SelectedIf(creditscreen_choice == "tl_credits"), With(Dissolve(0.5)):
            selected_foreground None text_idle_outlines [ (absolute(4), "#252425", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_selected_outlines [ (absolute(4), "#ff7152", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_hover_outlines [ (absolute(4), "#ff7152", absolute(0), absolute(0)), (absolute(2), "#252425", absolute(0), absolute(0)) ] text_color "#f6f2e4" text_size 30
screen hb_credits():
    hbox:
        spacing 120
        vbox:
            spacing 10
            for i in hb_devlist[0:4]:
                vbox:
                    text i.role color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                    null height -4
                    text i.name xpos 15 size 30 color "#f6f2e4"
        vbox:
            spacing 10
            for i in hb_devlist[4:9]:
                vbox:
                    text i.role color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                    null height -4
                    text i.name xpos 15 size 30 color "#f6f2e4"
        vbox:
            spacing 10
            for i in hb_devlist[9:15]:
                vbox:
                    text i.role color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                    null height -4
                    text i.name xpos 15 size 30 color "#f6f2e4"
        vbox:
            spacing 10
            for i in hb_devlist[15:19]:
                vbox:
                    text i.role color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                    null height -4
                    text i.name xpos 15 size 30 color "#f6f2e4"
screen ne_credits():
    hbox:
        spacing 120
        vbox:
            spacing 10
            for i in ne_devlist[0:4]:
                vbox:
                    text i.role color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                    null height -4
                    text i.name xpos 15 size 30 color "#f6f2e4"
        vbox:
            spacing 10
            for i in ne_devlist[4:7]:
                vbox:
                    text i.role color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                    null height -4
                    text i.name xpos 15 size 30 color "#f6f2e4"
        vbox:
            spacing 10
            for i in ne_devlist[7:12]:
                vbox:
                    text i.role color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                    null height -4
                    text i.name xpos 15 size 30 color "#f6f2e4"

screen va_credits():
    hbox:
        spacing 120
        vbox:
            spacing 10
            for i in va_devlist[0:5]:
                vbox:
                    text i.role color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                    null height -4
                    text i.name xpos 15 size 30 color "#f6f2e4"
        vbox:
            spacing 10
            for i in va_devlist[5:10]:
                vbox:
                    text i.role color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                    null height -4
                    text i.name xpos 15 size 30 color "#f6f2e4"
        vbox:
            spacing 10
            for i in va_devlist[10:15]:
                vbox:
                    text i.role color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                    null height -4
                    text i.name xpos 15 size 30 color "#f6f2e4"
        vbox:
            spacing 10
            for i in va_devlist[15:20]:
                vbox:
                    text i.role color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                    null height -4
                    text i.name xpos 15 size 30 color "#f6f2e4"
screen tl_credits():
    vbox:
        text _("Chinese Translation") color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))] xalign .5
        add "cntlcred" xalign .5

        hbox:
            spacing 20
            vbox:
                text _("Translation") color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))] xalign .5
                hbox:
                    spacing 10
                    vbox:
                        text "craft" size 30 color "#f6f2e4"
                        text "alu" size 30 color "#f6f2e4"
                        text "asky" size 30 color "#f6f2e4"
                        text "quinnh" size 30 color "#f6f2e4"
                        text "mycalendula" size 30 color "#f6f2e4"
                        text "Almeria" size 30 color "#f6f2e4"
                        text "benzoin" size 30 color "#f6f2e4"
                        text "ccp00a" size 30 color "#f6f2e4"
                        text "Dimoon_LY" size 30 color "#f6f2e4"
                        text "edwardli222" size 30 color "#f6f2e4"
                    vbox:
                        text "bukkun" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                        text "west" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                        text "KAGI" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                        text "kh12138" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                        text "kwang2017" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                        text "Dandirion" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                        text "shadoweyer" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                        text "thesheeponfire" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                        text "virgosnow" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                        text "Xuekovsky" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                        text "catndice" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"

            vbox:
                text _("Proofreading") color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                text "Mordin" size 30 color "#f6f2e4"
                text "Hinoki" size 30 color "#f6f2e4"
                text "num9ber" size 30 color "#f6f2e4"
                text "wkywk" size 30 color "#f6f2e4"
                text "Canny" size 30 color "#f6f2e4"

                text "Alwaysmadowl" size 30 color "#f6f2e4"
                text "andingsky" size 30 color "#f6f2e4"
                text "jjmint123" size 30 color "#f6f2e4"
                text "Dimmon_LY" size 30 color "#f6f2e4"
                text "Ectopistes" size 30 color "#f6f2e4"
                text "Henry" size 30 color "#f6f2e4"
                text "Erudito93" size 30 color "#f6f2e4"
                text "Sing{font=gui/fonts/SourceHanSans-Regular.otf}浠{/font}" size 30 color "#f6f2e4"
            vbox:
                text _("Testing") color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                text "virgosnow" size 30 color "#f6f2e4"
                text "alu" size 30 color "#f6f2e4"
                text "west" size 30 color "#f6f2e4"
                text "Dandirion" size 30 color "#f6f2e4"
                text "sun" size 30 color "#f6f2e4"
                text "Canny" size 30 color "#f6f2e4"
                text "Alwaysmadowl" size 30 color "#f6f2e4"
                text _("Technical Support") color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
                text "sun" size 30 color "#f6f2e4"

    vbox:
        text _("Russian Translation") color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))] xalign .5
        add "mehlate_crop" xalign .5
        text _("Translation") color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
        text "Vladimir “Leinstay” Belyaev" size 30 color "#f6f2e4"
        text "Alina “Penguin” Martynchik" size 30 color "#f6f2e4"
        text "Kirill “Mr_Useless” Ruzanov" size 30 color "#f6f2e4"
        text "Kirill “RedCat” Kovalev" size 30 color "#f6f2e4"
        text "Evgeniy “Demonic” Avdeev" size 30 color "#f6f2e4"
        text "Daniel “Eyvind” Yaddas" size 30 color "#f6f2e4"
        text "Sergey “Serj” Lyadov" size 30 color "#f6f2e4"
        text _("Additional Thanks") color "#f6f2e4" outlines[ (absolute(3),"#ff7152",absolute(0),absolute(0)),(absolute(2), "#252425", absolute(0), absolute(0))]
        hbox:
            vbox:
                text "Azamat Ezhaev" size 30 color "#f6f2e4"
                text "Andrey Zhidkov" size 30 color "#f6f2e4"
                text "Marina Azarova" size 30 color "#f6f2e4"
                text "Sergey Chichvarkin" size 30 color "#f6f2e4"
            vbox:
                text "Aleksey Ivanov" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                text "Kirill Abramov" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                text "Nikita Bazhenov" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
                text "Digital Shadow" size 30 xalign 1.0 text_align 1.0 color "#f6f2e4"
