# Heatmap for all scans, including scan dates, 
# texture phantoms and the number of slices   

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os
# Data: dates, textures, and number of slices
data = [
    ("03.02.25", "horizontal", 45), ("03.02.25", "vertical", 43), ("03.02.25", "diagonal", 46), 
    ("03.02.25", "honeylarge", 12), ("03.02.25", "honeymedium", 13), ("03.02.25", "honeysmall", 12),
    ("03.02.25", "sinusoidal", 46), ("03.02.25", "square", 52), ("03.02.25", "star4", 10),
    ("03.02.25", "star8", 11), ("04.12.24", "horizontal", 44), ("04.12.24", "vertical", 42),
    ("04.12.24", "diagonal", 46), ("04.12.24", "honeylarge", 13), ("04.12.24", "honeymedium", 13),
    ("04.12.24", "honeysmall", 12), ("04.12.24", "sinusoidal", 46), ("04.12.24", "square", 51),
    ("04.12.24", "star4", 10), ("04.12.24", "star8", 11), ("05.02.25", "horizontal", 44),
    ("05.02.25", "vertical", 39), ("05.02.25", "diagonal", 40), ("05.02.25", "honeylarge", 13),
    ("05.02.25", "honeymedium", 12), ("05.02.25", "honeysmall", 12), ("05.02.25", "sinusoidal", 45),
    ("05.02.25", "square", 50), ("05.02.25", "star4", 9), ("05.02.25", "star8", 11), 
    ("10.02.25", "horizontal", 44), ("10.02.25", "vertical", 36), ("10.02.25", "diagonal", 44),
    ("10.02.25", "honeylarge", 12), ("10.02.25", "honeymedium", 13), ("10.02.25", "honeysmall", 12),
    ("10.02.25", "sinusoidal", 45), ("10.02.25", "square", 33), ("10.02.25", "star4", 9),
    ("10.02.25", "star8", 11), ("11.11.24", "horizontal", 43), ("11.11.24", "vertical", 42),
    ("11.11.24", "diagonal", 46), ("11.11.24", "honeylarge", 13), ("11.11.24", "honeymedium", 13),
    ("11.11.24", "honeysmall", 13), ("11.11.24", "sinusoidal", 47), ("11.11.24", "square", 50),
    ("11.11.24", "star4", 10), ("11.11.24", "star8", 11), ("12.02.25_abdomen", "horizontal", 21),
    ("12.02.25_abdomen", "vertical", 15), ("12.02.25_abdomen", "diagonal", 22), ("12.02.25_abdomen", "honeylarge", 5),
    ("12.02.25_abdomen", "honeymedium", 5), ("12.02.25_abdomen", "honeysmall", 6), ("12.02.25_abdomen", "sinusoidal", 22),
    ("12.02.25_abdomen", "square", 16), ("12.02.25_abdomen", "star4", 4), ("12.02.25_abdomen", "star8", 5),
    ("12.02.25_brain", "horizontal", 44), ("12.02.25_brain", "vertical", 31), ("12.02.25_brain", "diagonal", 43),
    ("12.02.25_brain", "honeylarge", 12), ("12.02.25_brain", "honeymedium", 13), ("12.02.25_brain", "honeysmall", 12),
    ("12.02.25_brain", "sinusoidal", 45), ("12.02.25_brain", "square", 34), ("12.02.25_brain", "star4", 9),
    ("12.02.25_brain", "star8", 11), ("12.03.25", "horizontal", 42), ("12.03.25", "vertical", 38),
    ("12.03.25", "diagonal", 44), ("12.03.25", "honeylarge", 13), ("12.03.25", "honeymedium", 12), 
    ("12.03.25", "honeysmall", 12), ("12.03.25", "sinusoidal", 44), ("12.03.25", "square", 51),
    ("12.03.25", "star4", 9), ("12.03.25", "star8", 10), ("13.02.25_abdomen", "horizontal", 21),
    ("13.02.25_abdomen", "vertical", 20), ("13.02.25_abdomen", "diagonal", 21), ("13.02.25_abdomen", "honeylarge", 5),
    ("13.02.25_abdomen", "honeymedium", 6), ("13.02.25_abdomen", "honeysmall", 6), ("13.02.25_abdomen", "sinusoidal", 22),
    ("13.02.25_abdomen", "square", 24), ("13.02.25_abdomen", "star4", 4), ("13.02.25_abdomen", "star8", 4),
    ("13.02.25_brain", "horizontal", 43), ("13.02.25_brain", "vertical", 40), ("13.02.25_brain", "diagonal", 44),
    ("13.02.25_brain", "honeylarge", 12), ("13.02.25_brain", "honeymedium", 12), ("13.02.25_brain", "honeysmall", 13),
    ("13.02.25_brain", "sinusoidal", 45), ("13.02.25_brain", "square", 35), ("13.02.25_brain", "star4", 8),
    ("13.02.25_brain", "star8", 11), ("13.11.24", "horizontal", 43), ("13.11.24", "vertical", 42),
    ("13.11.24", "diagonal", 45), ("13.11.24", "honeylarge", 13), ("13.11.24", "honeymedium", 13),
    ("13.11.24", "honeysmall", 13), ("13.11.24", "sinusoidal", 47), ("13.11.24", "square", 47),
    ("13.11.24", "star4", 9), ("13.11.24", "star8", 10), ("14.03.25", "horizontal", 40),
    ("14.03.25", "vertical", 39), ("14.03.25", "diagonal", 42), ("14.03.25", "honeylarge", 9),
    ("14.03.25", "honeymedium", 11), ("14.03.25", "honeysmall", 3), ("14.03.25", "sinusoidal", 25),
    ("14.03.25", "square", 32), ("14.03.25", "star4", 8), ("14.03.25", "star8", 9), ("15.11.24", "horizontal", 42),
    ("15.11.24", "vertical", 41), ("15.11.24", "diagonal", 45), ("15.11.24", "honeylarge", 13),
    ("15.11.24", "honeymedium", 14), ("15.11.24", "honeysmall", 13), ("15.11.24", "sinusoidal", 46),
    ("15.11.24", "square", 51), ("15.11.24", "star4", 10), ("15.11.24", "star8", 11),
    ("16.01.25", "horizontal", 39), ("16.01.25", "vertical", 42), ("16.01.25", "diagonal", 45),
    ("16.01.25", "honeylarge", 12), ("16.01.25", "honeymedium", 12), ("16.01.25", "honeysmall", 13),
    ("16.01.25", "sinusoidal", 46), ("16.01.25", "square", 52), ("16.01.25", "star4", 8),
    ("16.01.25", "star8", 10), ("16.10.24", "horizontal", 44), ("16.10.24", "vertical", 41),
    ("16.10.24", "diagonal", 45), ("16.10.24", "honeylarge", 12), ("16.10.24", "honeymedium", 13),
    ("16.10.24", "honeysmall", 12), ("16.10.24", "sinusoidal", 46), ("16.10.24", "square", 52),
    ("16.10.24", "star4", 9), ("16.10.24", "star8", 10), ("16.12.24", "horizontal", 43),
    ("16.12.24", "vertical", 40), ("16.12.24", "diagonal", 44), ("16.12.24", "honeylarge", 13),
    ("16.12.24", "honeymedium", 13), ("16.12.24", "honeysmall", 12), ("16.12.24", "sinusoidal", 45),
    ("16.12.24", "square", 34), ("16.12.24", "star4", 10), ("16.12.24", "star8", 12),
    ("17.02.25_abdomen", "horizontal", 22), ("17.02.25_abdomen", "vertical", 19),
    ("17.02.25_abdomen", "diagonal", 21), ("17.02.25_abdomen", "honeylarge", 5),
    ("17.02.25_abdomen", "honeymedium", 5), ("17.02.25_abdomen", "honeysmall", 5),
    ("17.02.25_abdomen", "sinusoidal", 22), ("17.02.25_abdomen", "square", 25),
    ("17.02.25_abdomen", "star4", 4), ("17.02.25_abdomen", "star8", 4), ("17.02.25_brain", "horizontal", 43),
    ("17.02.25_brain", "vertical", 42), ("17.02.25_brain", "diagonal", 44),
    ("17.02.25_brain", "honeylarge", 12), ("17.02.25_brain", "honeymedium", 12),
    ("17.02.25_brain", "honeysmall", 12), ("17.02.25_brain", "sinusoidal", 42),
    ("17.02.25_brain", "square", 52), ("17.02.25_brain", "star4", 10), ("17.02.25_brain", "star8", 10),
    ("17.03.25", "horizontal", 19), ("17.03.25", "vertical", 20), ("17.03.25", "diagonal", 20),
    ("17.03.25", "honeylarge", 5), ("17.03.25", "honeymedium", 4), ("17.03.25", "honeysmall", 4),
    ("17.03.25", "sinusoidal", 20), ("17.03.25", "square", 25), ("17.03.25", "star4", 3),
    ("17.03.25", "star8", 4), ("18.12.24", "horizontal", 42), ("18.12.24", "vertical", 43),
    ("18.12.24", "diagonal", 46), ("18.12.24", "honeylarge", 12), ("18.12.24", "honeymedium", 12),
    ("18.12.24", "honeysmall", 12), ("18.12.24", "sinusoidal", 45), ("18.12.24", "square", 54),
    ("18.12.24", "star4", 9), ("18.12.24", "star8", 10), ("19.03.25_abdomen", "horizontal", 21),
    ("19.03.25_abdomen", "vertical", 16), ("19.03.25_abdomen", "diagonal", 20),
    ("19.03.25_abdomen", "honeylarge", 5), ("19.03.25_abdomen", "honeymedium", 5),
    ("19.03.25_abdomen", "honeysmall", 4), ("19.03.25_abdomen", "sinusoidal", 21),
    ("19.03.25_abdomen", "square", 17), ("19.03.25_abdomen", "star4", 3), ("19.03.25_abdomen", "star8", 5),
    ("19.03.25_brain", "horizontal", 11), ("19.03.25_brain", "vertical", 11),
    ("19.03.25_brain", "diagonal", 12), ("19.03.25_brain", "honeylarge", 2),
    ("19.03.25_brain", "honeymedium", 3), ("19.03.25_brain", "honeysmall", 2),
    ("19.03.25_brain", "sinusoidal", 12), ("19.03.25_brain", "square", 12),
    ("19.03.25_brain", "star4", 2), ("19.03.25_brain", "star8", 2), ("21.01.25", "horizontal", 44),
    ("21.01.25", "vertical", 42), ("21.01.25", "diagonal", 44), ("21.01.25", "honeylarge", 13),
    ("21.01.25", "honeymedium", 13), ("21.01.25", "honeysmall", 11), ("21.01.25", "sinusoidal", 46),
    ("21.01.25", "square", 51), ("21.01.25", "star4", 9), ("21.01.25", "star8", 11),
    ("22.10.24", "horizontal", 45), ("22.10.24", "vertical", 42), ("22.10.24", "diagonal", 45),
    ("22.10.24", "honeylarge", 12), ("22.10.24", "honeymedium", 12), ("22.10.24", "honeysmall", 12),
    ("22.10.24", "sinusoidal", 45), ("22.10.24", "square", 51), ("22.10.24", "star4", 8),
    ("22.10.24", "star8", 9),
]

df = pd.DataFrame(data, columns=["Date", "Texture", "Number of Slices"])

pivot_df = df.pivot(index="Date", columns="Texture", values="Number of Slices")

fig, ax = plt.subplots(figsize=(15, 8))
sns.heatmap(pivot_df, annot=True, cmap="coolwarm", fmt="d", linewidths=0.5)

ax.set_title('Number of Slices for Each Texture on Different Dates')
ax.set_xlabel('3D printed Phantom Textures')
ax.set_ylabel('CT Scan Dates')
plt.tight_layout()
os.chdir("C:/Users/Bio İzmir/Desktop/violinplots")
plt.savefig("ct_slices_each_date.png", dpi=600)
# Show the plot
plt.show()
