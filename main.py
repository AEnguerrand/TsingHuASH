import sys
import parsing.input

def start():
    if len(sys.argv) >= 2:
        print("[COMPUTE] [YOU NEED TO GIVE INPUT FILE]")
    header, pictures = parsing.input.parse_input(sys.argv[1])
    parsing.input.debug_input(header, pictures )
    

if __name__ == '__main__':
    start()