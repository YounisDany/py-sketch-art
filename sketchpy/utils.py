


import pkg_resources
import subprocess

def get_svg(image_path, output_path=None):
    """Usage: \n
    from sketchpy import canvas
    canvas.get_svg()
    
    opens a local window from converting image files to svg files\n
    requires internet connection!!!"""

   

    exe_path = pkg_resources.resource_filename("sketchpy3", "files/trace.exe")
    try:
        if output_path != None:
            subprocess.run([exe_path, image_path, output_path], shell=True)
        else:
            subprocess.run([exe_path, image_path], shell=True)

    except Exception as e:
        print("An error occurred:", e)

