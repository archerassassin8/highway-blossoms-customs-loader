# Highway Blossoms Customs Loader
A custom scene loader for the visual novel Highway Blossoms.

Installation:
	1) Download the latest release of the Highway Blossoms Customs Loader (HBCL).
	2) Navigate to your Highway Blossoms installation directory. (On Steam you can right click on the game in your library and go to "Manage > Browse Local Files")
	3) Unzip HBLC and drag the contents (extras.rpy, mods.rpy, and the mods folder) into the "game" folder in the HB directory.
	
	You will know it installed correctly if you see the "Custom Content" option in the Extras menu.

How To Add Mods:
	1) Drag the mod's folder you want to install into the ".../Highway Blossoms/game/mods" folder
	2) Thats it (assuming the file structure is correct)

Custom Content Creation:
	Included in the mods folder you will find a mod template. This shows the basic file structure of what a mod requires to work. 

	Here's a breakdown.:

		assets: This folder is where any custom assets you might want to use will reside. Custom assets can be images, sounds, etc.

		image.png: This is the image that displays in the Custom Content menu. You will want to use some image editing tool to put an image over the white "Template" box.
		
		info.json: This file holds information about your mod so it can display and load it correctly in-game. IMPORTANT! The "name" has to be the same as the name of the folder it resides in and the name of the script (ex: Template.rpy). ALSO IMPORTANT! The "label" needs to match the label defined at the top of the script and CANNOT contain spaces.
		
		Template.rpy: This is the file that actually holds the scene's scripting. The template is a short little scene that shows of some basic things you can do in Ren'Py. This file will NEED to be renamed to whatever you want to call your scene. Remember to double check that your label matches with the info.json!
		
		Template_includes.rpy: This file is used to declare any custom assets you might want to use. You should probably name it (mod name)_includes.rpy.
		
		
		
		
Why?:
	I know that literally nobody makes mods for this game... but I might. Like yeah, you could just overwrite the Jumbo scene, but if more than 1 mod gets made I'd probably want a mod loader.