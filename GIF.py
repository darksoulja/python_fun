import imageio.v3 as iio

filenames = ['Pikachu1.png', 'Pikachu2.png','Pikachu3.png']
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('Pikachu_Cards.gif', images, duration = 500, loop = 0)