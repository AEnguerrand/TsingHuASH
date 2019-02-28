import sys
import parsing.input
import parsing.ouput
import calc.calc_basical
import algo.outil
import random
import visualization.scoring
def start():
    if len(sys.argv) != 2:
        print("[COMPUTE] [YOU NEED TO GIVE INPUT FILE]")
        exit(1)
    header, pictures = parsing.input.parse_input(sys.argv[1])
    #parsing.input.debug_input(header, pictures)
    
    #slideshow = calc.calc_basical.basical(header, pictures)

    ## REMOVE IT
    slideshow = []
    slideshow.append(0)
    slideshow.append(3)
    slideshow.append(list(map(str, (1, 2))))
    ## END - REMOVE IR
    out = algo.outil.trieur_orientation(pictures)
    random.shuffle(out)
    slideshow = out
    print(visualization.scoring.score_final(slideshow,pictures))
    #parsing.ouput.debug_ouput(slideshow)
    parsing.ouput.write_output(sys.argv[1], slideshow)
if __name__ == '__main__':
    start()