import numpy as np

data = np.loadtxt('input.txt', dtype=str, comments=None)
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
# Position setup
# The width of the text file, creating a wavelength.
wavelength = len(data[0])
height = data.size
counts = np.zeros(len(slopes))
for el, slope in enumerate(slopes):
    xpos = 0
    ypos = 0  # height index
    # Tree setup
    treeCount = 0
    while ypos < (height - 1):
        xpos += slope[0]
        ypos += slope[1]
        if data[ypos][int(xpos % wavelength)] in '#':
            treeCount += 1
    counts[el] = treeCount
print(np.prod(counts))
