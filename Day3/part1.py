import numpy as np

data = np.loadtxt('input.txt', dtype=str, comments=None)

# Position setup
# The width of the text file, creating a wavelength.
wavelength = len(data[0])
height = data.size
ypos = 0  # height index
xpos = 0
# Tree setup
treeCount = 0
while ypos < (height - 1):
    ypos += 1
    xpos += 3
    if data[ypos][int(xpos % wavelength)] in '#':
        treeCount += 1
print(treeCount)
