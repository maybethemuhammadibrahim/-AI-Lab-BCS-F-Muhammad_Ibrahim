import random

random.seed()

def encode(num):
    return [int(b) for b in format(num, "05b")]

def decode(bits):
    return int("".join(str(b) for b in bits), 2)

def fitness(bits):
    x = decode(bits)
    return x * x + 2 * x

def roulette(pop):
    scores = [fitness(c) for c in pop]
    total = sum(scores)
    probs = [s / total for s in scores]
    return random.choices(pop, weights=probs, k=2)

def crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    return c1, c2

def mutate(chrom, rate):
    for i in range(len(chrom)):
        if random.random() < rate:
            chrom[i] = 1 - chrom[i]
    return chrom

def genetic(pop_size=6, gens=15, rate=0.05):
    population = [encode(random.randint(0, 31)) for _ in range(pop_size)]
    for _ in range(gens):
        new_pop = []
        while len(new_pop) < pop_size:
            parents = roulette(population)
            c1, c2 = crossover(parents[0], parents[1])
            new_pop.append(mutate(c1, rate))
            if len(new_pop) < pop_size:
                new_pop.append(mutate(c2, rate))
        population = new_pop
    best = max(population, key=fitness)
    return best

best_chrom = genetic()
best_x = decode(best_chrom)
print("best chromosome:", best_chrom)
print("best x:", best_x)
print("best fitness:", fitness(best_chrom))