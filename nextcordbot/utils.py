import os

def up_dir(location, levels=1):
    for _ in range(levels):
        location = os.path.dirname(location)
        