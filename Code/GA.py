#!/usr/bin/env python
# coding: utf-8



def population_initializer(pop_ind):
    inputFile = open("Ass1Input.txt",'r')
    candidates=inputFile.read()#read text file into string 'population'
    #print(candidates)#prints the text file output as it is
    lines = candidates.split('\n')#splits population based on the next line character; making each line an item in the list
    #print(lines)
    list1,list2,list3,list4,list5,list6,list7,list8 = (lines[i] for i in range(0,len(lines)))#storing each line in a seperate list for easier mainpulation

    list_1=list1.split()
    list_2=list2.split()
    list_3=list3.split()
    list_4=list4.split()
    list_5=list5.split()
    list_6=list6.split()
    list_7=list7.split()
    list_8=list8.split()
    #print(list_1)
    pop = list_1 + list_2 + list_3 + list_4 + list_5 + list_6 + list_7 + list_8#Further splitting each box i.e., 4 values per box and concatenating the output into a single list
    #print(pop)

    new_list=[]
    for i in range(len(pop)):# allows us to view each digit/bit as an individual item in the list i.e., new_list
        for j in range(len(pop[i])):
            new_list.append(pop[i][j])

    #print(new_list)
    #print(len(new_list))

    start = 0
    end = 256
    step = 4
    org_pop=[]
    for i in range(start, end, step):
        x = i
        org_pop.append(new_list[x:x+step])
    #print (org_pop)
    population=[]
    population.append(org_pop)
    for i in range(pop_ind):
        pop=randomizer(org_pop)
        population.append(pop)
    
    #print(population)
    return population




def fitness(inputFile):
   
    inputFile=open("Draft.txt",'r') 

    currentText = ""
    currentLine = ""
    puzzlePieces = []
    currentNumber = []
   

    ROWSIZE = 8
    COLUMNSIZE = 8

    for i in range(ROWSIZE):
        row = []

        currentText = inputFile.readline()
        currentLine = currentText
        currentNumber = currentLine.split()
        
        for i in range(8):
            
            row.append(currentNumber[i])

        puzzlePieces.append(row)

    numberOfMismatches = 0

    i = 0
    while i < ROWSIZE - 1:
        numberOfMismatches += CountRowMismatches(puzzlePieces[i], puzzlePieces[i + 1])
        i += 1

    i = 0
    while i < COLUMNSIZE - 1:
        firstColumn = []
        secondColumn = []

        for j in range(0, ROWSIZE):
            firstColumn.append(puzzlePieces[j][i])
            secondColumn.append(puzzlePieces[j][i + 1])

        numberOfMismatches += CountColumnMismatches(firstColumn, secondColumn)
        i += 1

    #print("Number of mismatches : ", end = '')
    #print(numberOfMismatches, end = '')
    #print("\n", end = '')
    
    inputFile.close()
    #print(numberOfMismatches)
    return numberOfMismatches

    
def CountRowMismatches(first, second):
        numberOfMismatches = 0

        i = 0
        while i < len(first):
            if first[i][2] != second[i][0]:
                numberOfMismatches += 1
            i += 1

        return numberOfMismatches

def CountColumnMismatches(first, second):
        numberOfMismatches = 0

        i = 0
        while i < len(first):
            if first[i][1] != second[i][3]:
                numberOfMismatches += 1
            i += 1
        
        return numberOfMismatches




def randomizer(pop):# randomly swaps tiles of the original individual to create random copies of it. For population initialization purposes
    arr=pop.copy()
    temp1=[]
    temp2=[]
    for i in range(len(arr)):
            p1=random.randint(len(arr))#choose index#1 at random i.e., between 0-63
            p2=random.randint(len(arr))#choose index#2 at random i.e., between 0-63
            temp1=arr[p1]
            temp2=arr[p2]
            arr.pop(p1)
            arr.insert(p1,temp2)
            arr.pop(p2)
            arr.insert(p2,temp1)
    return arr




def transform(pop):
    new_list=[]
    for i in range(len(pop)):# allows us to view each digit/bit as an individual item in the list i.e., new_list and add spaces and new line where required
        if i%8==0 and i!=0:
            new_list.pop()
            new_list.append('\n')
        for j in range(len(pop[i])):
            new_list.append(pop[i][j])
        new_list.append(' ')

    new_list.pop()
  
    new_string=''
    new_string = ''.join([str(e) for e in new_list])#converts the list into a string 
    
    with open('Draft.txt', 'w') as file:
        file.write(new_string)
    return file




def transform_best(pop):
    new_list=[]
    for i in range(len(pop)):# allows us to view each digit/bit as an individual item in the list i.e., new_list and add spaces and new line where required
        if i%8==0 and i!=0:
            new_list.pop()
            new_list.append('\n')
        for j in range(len(pop[i])):
            new_list.append(pop[i][j])
        new_list.append(' ')

    new_list.pop()
  
    new_string=''
    new_string = ''.join([str(e) for e in new_list])#converts the list into a string 
    
    with open('best.txt', 'w') as file:
        file.write(new_string)
    return new_string




def tournament_selection(pop,fitness_score, window_size):#funtions chooses k i.e., window_size number of individuals at random and chooses the fittest one
    best = random.randint(len(pop))
    for i in range(0,len(pop),window_size-1):#bigger window_size means more selection pressure and vice versa
        if fitness_score[i] < fitness_score[best]:#minimizing the fitness function i.e., number of mismatches
            best = i
    return pop[best]  #returns best individual after the tournament




def mutation_swap(arr, mut_fac):#Swaps two random tiles with a certain probability
    array=arr.copy()
    temp1=[]
    temp2=[]
    for i in range(len(arr)):
        if mut_fac > random.rand():
            p1=random.randint(len(array))#choose index#1 at random i.e., between 0-63
            p2=random.randint(len(array))#choose index#2 at random i.e., between 0-63
            temp1=array[p1]
            temp2=array[p2]
            array.pop(p1)
            array.insert(p1,temp2)
            array.pop(p2)
            array.insert(p2,temp1)
    return array




def mutation_rotate(arr, mut_fac):
    array=arr.copy()
    index = random.randint(1,4)#Rotates a tile with a certain probability
    #i.e., 1=90 degrees, 2=180 degrees 3=270 degrees etc.
    ele=[]
    for i in range(len(array)):#rotates a single tile within a row with mutation probablity
        if mut_fac > random.rand() :# random floating point number generated between 0-1
            ele = array[i][index:] + array[i][:index]
            array.pop(i)
            array.insert(i, ele)
    return array




def mutation_sort_a(arr, mut_fac):#sorts a tile (ascending order) within a row with a certain probability
    array=arr.copy()
    for i in range(len(array)):
        if mut_fac > random.rand():# random floating point number generated between 0-1
            array[i].sort()
    return array




def mutation_sort_d(arr, mut_fac):#sorts a tile (ascending order) within a row with a certain probability
    array=arr.copy()
    for i in range(len(array)):
        if mut_fac > random.rand():# random floating point number generated between 0-1
            array[i].sort(reverse=True)
    return array




#Survivor Selection
def survivor_selection(arr, fitness_score):#fitness based
    worst_fitness=0
    worst_index=0
    for i in range(0,len(arr)):
        if fitness_score[i]>worst_fitness:#returns the index of the least fit candidate solution
            worst_fitness=fitness_score[i]
            worst_index=i
    
    return worst_index




def genetic_algorithm(pop_ind, n_iter, mut_r, mut_sw, mut_so_a, mut_so_d, k):
    
    # random initial population and the original indvidual 
    population = population_initializer(pop_ind)
    
    #keeping track of the best candidate solution
    best = population[0]
    best_fitness = fitness(transform(population[0]))
    
    #iterate for a number of generations
    for iteration in range(n_iter):
    
        #transform each individual into the form accepted by the fitness function
        #evaluate fitness of each individual
        fitness_score = []
        fitness_score = [fitness(transform(i)) for i in population]
        
        #check for the new best solution
        for i in range(0,len(population)):
            if fitness_score[i] < best_fitness:
                best = population[i]
                best_fitness = fitness_score[i]
                best_op=transform_best(best)
                
        #parent selection i.e., touranment selection
        selected = []
        selected = tournament_selection(population, fitness_score, k)
       
        #Apply variation operators to get offspring
        offspring=[]

        offspring = mutation_swap(selected, mut_sw)#swaps tiles within an individual
        
        offspring = mutation_rotate(selected, mut_r)#rotates tiles within an individual
        
        offspring = mutation_sort_a(selected, mut_so_a)#sorts tiles in ascending order within an individual
        
        offspring = mutation_sort_d(selected, mut_so_d)#sorts tiles in descending order within an individual
        
        #Survivor selection
        discard_index=0
        discard_index = survivor_selection(population, fitness_score)# replaces the worst fit individual with the offspring i.e., Steady State GA
        
        population.pop(discard_index)
        population.insert(discard_index,offspring)
             
    #return[best_op, best_fitness]
    print(best_op)
    print("Number of mismatches are: ",best_fitness)
    



from numpy import random as random
pop_ind = 50 # number of candidate solutions 
n_iter = 20 # number of iterations the genetic algorithm will run
mut_r = 0.5 # mutation (rotation) probability
mut_sw = 0.6 # mutation (swap) probability
mut_so_a = float(1/5) # mutation (sort-ascending) probability
mut_so_d = float(1/5) # mutation (sort-descending) probability
k = 2 # tournament selection window size

genetic_algorithm(pop_ind, n_iter, mut_r, mut_sw, mut_so_a, mut_so_d, k)






