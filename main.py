import shutil, pathlib
pathlib.Path("/output").mkdir(parents=True, exist_ok=True)
shutil.copyfile("image.png", "/output/entry.png")
