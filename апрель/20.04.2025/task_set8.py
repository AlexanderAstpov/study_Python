files_list = ["photo.png",
              "photo1.png",
              "Photo.png",
              "new_year.rar",
              "2025.docx",
              "Tree.PNG",
              "photo.jpeg",
              "photo.txt",
              "dithub.git",
              ".env",
              "bebepng",
              "tree.Png"
              ]

st = {i.lower() for i in files_list if ".png" in i.lower()}

for i in st:
    print(i)

