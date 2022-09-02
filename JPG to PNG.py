from PIL import Image
import os

for img in os.listdir("./Pokedex"):
    new_img = Image.open(f"./Pokedex/{img}")
    clean_name = os.path.splitext(f"{img}")[0] #we do this as the extension should be saved as png so we divide the name
    new_img.save(f"./New Pokedex/{clean_name}.png", "png")

print("All done!")