def parse_input(filename):
    pictures = []
    header = []
    with open(filename) as f:
        i = 0

        header = list(map(int, f.readline().rstrip().split(" ")))

        while i < header[0]:
            r = list(map(str, f.readline().rstrip().split(" ")))
            pictures.append(r)
            i += 1
    return header, pictures

def debug_input(header, pictures):
    print("--- DEBUG INPUT ---")
    print("Pictures nb:", header[0])
    i = 0
    while i < header[0]:
        print("picture  id:", i)
        print("         type:", pictures[i][0])
        print("         tags nb:", pictures[i][1])
        print("         tags list :", pictures[i][2:])
        i += 1
    print("--- END DEBUG INPUT ---")
