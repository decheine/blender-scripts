# Run this in the script in Blender in an empty file.
from pathlib import Path
import bpy
import os

# Change to the target directory.
new_directory = "<directory to place fixed models>"
origin_directory = "<directory containing models with undesirable origins>"

# List of model filepaths. 
# Change extension as needed, you just need to make sure to change the import_scene and export_scene functions to match 
model_filepaths = [f for f in Path(origin_directory).glob('**/*.fbx') if f.is_file()]
    
# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".fbx"):
        filepath = os.path.join(directory, filename)
        
        # Import the .fbx file
#       # You can change the type for other filetypes
        bpy.ops.import_scene.fbx(filepath=filepath)
        
        # Set the origin to geometry for all imported objects
        for obj in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = obj
            # Lock the z location.
            bpy.context.view_layer.objects.active.lock_location[2] = True
            
            bpy.context.selected_objects[0].location[0] = 0
            bpy.context.selected_objects[0].location[1] = 0
            if( abs(bpy.context.selected_objects[0].rotation_euler[0]) < 0.001):
                bpy.context.selected_objects[0].rotation_euler[0] = 0
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='BOUNDS')
            
        # Export the .fbx file
        print("Exporting", filename)
        bpy.ops.export_scene.fbx(filepath=filepath, use_selection=True)
        
        # Clean up by deleting all objects in the scene
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

    
