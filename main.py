from sys import argv

from PIL import Image  # install by > python3 -m pip install --upgrade Pillow  # ref. https://pillow.readthedocs.io/en/latest/installation.html#basic-installation

print("Quante immagini vuoi inserire? ")
num = int(input())

images = []
for i in range(0,num):
    str = input("nome immagine dal desktop: ")
    images.append(Image.open("C:\\Users\\User\\OneDrive\\Desktop\\" + str))

#images = [
#    Image.open("C:\\Users\\User\\OneDrive\\Desktop\\" + f)
#    for f in ["foto2.jpeg", "foto1.jpeg"]
#]

pdf_path = r"C:\Users\User\OneDrive\Desktop\new.pdf"

images[0].save(
    pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)