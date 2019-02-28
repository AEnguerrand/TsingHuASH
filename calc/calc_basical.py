import random

def basical(header, pictures):
    slideshow = []

    i = 0
    while i < header[0]:
        pictures[i][1:] = pictures[i][0:]
        pictures[i][0] = i
        i += 1

    pictures_v = []
    pictures_h = []
    i = 0
    while i < header[0]:
        if pictures[i][1] == 'V':
            pictures_v.append(pictures[i])
        else:
            pictures_h.append(pictures[i])
        i += 1

    rand_sel = random.randint(0,len(pictures_h) - 1)
    picture_start = pictures_h[rand_sel]

    print(picture_start)

    return slideshow