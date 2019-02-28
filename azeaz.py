
solution = solution_init
energy = score(solution)
best_solution = solution
best_energy = energy
k = 0
kmax = 1000

while (k < kmax and e > emax):
    temp_solution = voisin(solution)
    temp_energy = score(temp_solution)
    if temp_energy < energy and aleatoire() < exp((temp_energy-energy) / temp(k, kmax)):
        solution = temp_solution
        energy = temp_energy
    if energy < best_energy:
        best_solution = solution
        best_energy = energy
    k = k+1
    
return best_solution