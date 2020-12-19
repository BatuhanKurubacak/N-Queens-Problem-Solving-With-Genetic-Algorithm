# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import random
import fitness
#import matplotlib.pyplot as plt

population=8
populationArray= []
optSolution=[]
unique_list=[]

def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    return unique_list
      

for x in range(0,8):
    
    new=[]
    for y in range(0,8):
        new.append(random.randrange(100)%8)
    populationArray.append(new)
      
#print(populationArray)
    
#initial state
for x in range(0,8):
    print(str(x+1)+".Indiviual= ",end="", flush=True)
    
    for y in range(0,8):
       print(str(populationArray[x][y])+" ",end="", flush=True)
    print("\n")

generation=100000
for q in range(0,generation):
#CALCULATION FITNESS
    fitnessGen=[]
    for l in range(0,8):
        fitnessGen.append(0)

    for k in range(0,8):
        for l in range(0,8):
            index=populationArray[k][l]
            #print(index)
            right=1 
            for m in range(l+1,8):
                if populationArray[k][m]==index and right==1: 
                    fitnessGen[k]=fitnessGen[k]+1
                    right=0
            left=1 
            for m in range(8,l-1):
                if populationArray[k][m]==index and left==1: 
                    fitnessGen[k]=fitnessGen[k]+1
                    left=0
        #right diagonal
            dur=1
            ddr=1
            rightd=1
            for n in range(l+1,8):
                if populationArray[k][n]==index-rightd and dur==1:
                    fitnessGen[k]=fitnessGen[k]+1
                    dur=0
                if populationArray[k][n]==index+rightd and ddr==1:
                    fitnessGen[k]=fitnessGen[k]+1
                    ddr=0
                    rightd=+1
        #left diagonal
            dul=1;
            ddl=1;
            leftd=1;
            for n in range(8,l-1):
                if populationArray[k][n]==index-leftd and dul==1:
                    fitnessGen[k]=fitnessGen[k]+1
                    dur=0
                
                if populationArray[k][n]==index+leftd and ddl==1:
                    fitnessGen[k]=fitnessGen[k]+1
                    ddr=0
                    leftd=+1

#Roulette Selection
    fitnessTotal=0;
    for x in range(0,8):
        #print(str(q)+".Generation "+str(x+1)+". Individual Fitness = "+str(28-fitnessGen[x]))
        
        fitnessGen[x]=28-fitnessGen[x]
        fitnessTotal=fitnessTotal+fitnessGen[x]
    optSolution.append(fitnessTotal)  
    selectRandomGen1=random.randrange(1000)%fitnessTotal
    selectRandomGen2=random.randrange(1000)%fitnessTotal

    selectedgen1=0;
    selectedgen2=0;
    countPopulation=0;
    for x in range(0,8):
        countPopulation=fitnessGen[x]+countPopulation;
        if selectRandomGen1<=countPopulation and selectedgen1==0:
            gen1=x;
            selectedgen1=1;
        
        if(selectRandomGen2<=countPopulation and selectedgen2==0):
            gen2=x;
            selectedgen2=1;


    
    new3=[]
    for y in range(0,8):
        new3.append(populationArray[gen1][y])
        #print(str(new3))
    

    
    new4=[]
    for y in range(0,8):
        new4.append(populationArray[gen2][y])
        #print(str(new4)+"\n")

###Crossover
    randomCrossover=random.randrange(1000)%8
    for x in range(0,randomCrossover):    
        populationArray[gen1][x]=new4[x]
        for x in range(0,randomCrossover):
            populationArray[gen2][x]=new3[x]

    

####Mutation
    list1=[]
    mProbability=10
    for x in range(0,8):
        #print("\n")
        rMutation2=random.randrange(1000)%100
        if rMutation2<=mProbability:
            random1=random.randrange(1000)%8
            if populationArray[gen1][x]==random1:
                list1.append(random1+1)
               
            else:
                list1.append(random1)
                
        else:
            list1.append(populationArray[gen1][x])
    #print(str(gen1+1)+".Individual Mutation "+str(list1))
    #print(str(gen1+1)+".Individual "+str(populationArray[gen1]))
    
    
    
    fitnew1=fitness.fitness(list1)
    fitparent1=fitness.fitness(populationArray[gen1])
    if fitnew1>=fitparent1:
        populationArray[gen1]=list1
    
   

        
    list2=[]
    for x in range(0,8):
        
        rMutation2=random.random()*100
        if rMutation2<=mProbability:
            random2=random.randrange(1000)%8
            if populationArray[gen2][x]==random2:
                list2.append(random2+1)
            else:
                list2.append(random2)
                
        else:
            list2.append(populationArray[gen2][x])
    
    
    fitnew2=fitness.fitness(list2)
    fitparent2=fitness.fitness(populationArray[gen2])
    if fitnew2>=fitparent2:
        populationArray[gen2]=list2
    #print(str(gen2+1)+".Individual Mutation "+str(list2))
    #print(str(gen2+1)+".Individual "+str(populationArray[gen2]))
    answer=[]
    best=0
    
    for x in range(0,8):
        value=fitness.fitness(populationArray[x])
        bestposition=[]
        if value>=best:
            best=value
            bestposition=populationArray[x]
    
        
        elif value==25:
            
            answer=populationArray[x]
            #print(answer)
            for i in range(100):
                answer.append(random.randrange(8))
            newAnswer=unique(answer)
            populationArray[x]=newAnswer
            #print(populationArray[x])
            point=fitness.fitness(populationArray[x])
            #print(point)
        elif  value==28:
            bestposition=(populationArray[x])
            break
   
print(bestposition)
print(best)
'''
plt.plot(optSolution)
plt.ylabel('Total Fitness')
plt.xlabel('Generation')
'''
fittest=0
index1=0
for x in range(0,8):
    if fittest<fitnessGen[x]:   
        fittest=fitnessGen[x]
        index1=x
print("The Fittest Arrangement For N-queens Problem "+str(index1+1)+".Indiviual Fitness:"+str(fitnessGen[index1]))    
print("The arrangement: "+str(populationArray[index]))
    
        
     