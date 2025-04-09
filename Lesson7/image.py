import os

class Image:
    
    photo_extensions = ["jpeg", "jpg", "png", "gif", "svg", "tiff"] 

    def __init__(self, path=input("Where is the image located?\t")):

        for dir, subdir, file in os.walk(path):
            for x in file:
                for ext in x.split("."):
                    if ext in Image.photo_extensions:
                        self.path = os.path.join(path, x)

# i = Image()
# file = i.path
# os.startfile(file)