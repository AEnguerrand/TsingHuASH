import os
def write_output(filename, slideshow):
    with open(filename + ".out", 'w+') as f:
        i = 0
        size_ssw = len(slideshow)
        f.write(str(size_ssw)+"\n")
        while i < size_ssw:
            if type(slideshow[i]) is int:
                f.write(str(slideshow[i])+ '\n')
            else:
                f.write(' '.join(str(x) for x in slideshow[i]) + '\n')
            i += 1
    print("FILE RESULT PRINT IN:", filename + ".out")

def debug_ouput(slideshow):
    print("--- DEBUG OUPUT ---")
    size_ssw = len(slideshow)
    print("Slideshow size:", size_ssw)
    i = 0
    while i < size_ssw:
        print("picture  ids:", slideshow[i])
        i += 1
    print("--- END DEBUG OUPUT ---")
