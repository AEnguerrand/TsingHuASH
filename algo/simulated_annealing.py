from visualization import scoring
import random
import numpy as np
from algo import outil


def calculate_probability(current_score, new_score, temperature):
    return np.exp(- (current_score - new_score) / temperature)


def run(pictures,initial_path=[], max_iteration=1000, temperature=5):
    if (initial_path == []):
        initial_path = outil.trieur_orientation(pictures)

    temperature_min = 1
    size = len(initial_path) - 1
    current_path = initial_path.copy()
    best_path = initial_path.copy()
    current_score = scoring.score_final(initial_path,pictures)
    best_score = current_score

    factor = 0.99
    iter_temperature = 0
    while (temperature > temperature_min):
        iteration = 1
        iter_temperature += 1

        print(f'new temp {temperature}')
        while (iteration < max_iteration):
            i = random.randint(0, size)
            j = random.randint(0, size)
            # we need i<j
            if i >= j:
                continue

            new_score = scoring.eval_swap(current_path,current_score, i, j, pictures)
            # print(new_score)
            p = random.random()
            min_probability = calculate_probability(current_score, new_score, temperature)

            if (p < min_probability):
                # print(f'yes {min_probability}')
                new_path = outil.swap_special(current_path, i, j)
                if (new_score > best_score):
                    best_path = new_path.copy()
                    best_score = new_score
                    print(f'{best_score}\t Temp {temperature} \n Iter temp {iter_temperature}')
                current_path = new_path
                current_score = new_score
            iteration +=1


        temperature *= factor


    # while (temperature > temperature_min):
    #     iteration = 1
    #     print(f'temp {temperature}')
    #     while (iteration < max_iteration):
    #         i = random.randint(0, size)
    #         j = random.randint(0, size)
    #         # we need i<j
    #         if i >= j:
    #             continue
    #
    #         new_path = outil.swap_special(current_path, i, j)
    #         new_score = scoring.score_final(new_path,pictures)
    #
    #         # new_score = scoring.eval_swap(current_path, i, j, pictures)
    #         # print(new_score)
    #         p = random.random()
    #         min_probability = calculate_probability(current_score, new_score, temperature)
    #
    #         if (p < min_probability):
    #             print(f'yes {min_probability}')
    #             print(current_score)
    #             # new_path = outil.swap_special(current_path, i, j)
    #             if (new_score > best_score):
    #                 best_path = new_path.copy()
    #                 best_score = new_score
    #                 print(f'BEEST\n{best_score}')
    #             current_path = new_path
    #             current_score = new_score
    #         iteration += 1
    #     temperature *= factor

    print(f'finished with {best_score}')
    return best_path
