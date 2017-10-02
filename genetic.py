#IMPORT LIBARARIES
from __future__ import math
import random
import numpy
#Note: I am looking at R^2 with OLS but any technique with a metric for success will work
from sklearn import linear_model
import datetime


#THIS SECTIONS IS FOR A PARTICULAR DATASET
#It should fit into whatever model you are using. For this case, a numpy array works.
X = []
Y = [[],[],[],[],[]]
f = open('training.csv', 'r')
line = f.readline()
while(len(line) > 2):
    line = f.readline()
    data = line.split(',')
    x = []
    for l in range(1, 3594):
        x.append(float(data[l]))
    if (data[3594]=='Topsoil'):
        x.append(1)
    else:
        x.append(0)
    X.append(x)
    for l in range(0, 5):
        Y[l].append(float(data[3595+l]))


YY = Y
Y = numpy.asarray(YY[1])

#PARAMETERS TO SET
#How many columns do you want to keep?
n2use = 30
#what's an acceptable difference of the above
plus_or_minus = 0
#How many children to create in the algorithm?
generation_size = 2000
#How many generations would you like to run?
num_generations = 100


#This runs on auto.
n_cols = len(X[0])
indiv_odds = n_cols*[float(n2use)/n_cols]
best_quantity = int(n_cols/n2use/2)
best = []


#These next 3 functions should handle initilizing, running, and scoring the model.
def initModel():
    global clf
    clf = linear_model.LinearRegression()


def runModel():
    catch = clf.fit(numpy.asarray(XXX), Y)


def scoreModel():
    return clf.score(XXX, Y)


#This happens in between generations. It's how we choose the next columns for the next generation
def reshape():
    for c3 in range(0,n_cols):
        n = 0.
        for c4 in range(0, len(best)):
            if ((best[c4][1] & (2**c3)) == (2**c3)):
                n = n + 1/(1-best[c4][0])
        indiv_odds[c3] = n
    total = 0
    for c3 in indiv_odds:
        total = total + c3
    for c3 in range(0, len(indiv_odds)):
        indiv_odds[c3] = n2use*indiv_odds[c3]/total


#A child's attempt at the "Hall of Fame" to produce more children like it
#It assumes a bigger score is better
def save(elem):
    if (len(best)<best_quantity):
        best.append(elem)
    else:
        e = getEdge('bottom')
        if (e[0]<elem[0]):
            best.remove(e)
            best.append(elem)


#Find the top or bottom of the "Hall of Fame"
def getEdge(b):
    if (b=='top') and (len(best)>0):
        e = best[0]
        for c3 in best:
            if (e[0] < c3[0]):
                e = c3
        return e
    elif(len(best)>0):
        e = best[0]
        for c3 in best:
            if (e[0] > c3[0]):
                e = c3
        return e
    else:
        return [[0],[0]]


#Reshape your dataset in order to put it the way it's needed for your model, based on the child's code
def assembleMatrix():
    result = str(bin(string))[3:]
    XX = []
    for c3 in X:
        xx = [1]
        for c4 in range(0,len(result)):
            if (result[c4] == '1'):
                xx.append(c3[c4])
        XX.append(xx)
    return XX


#This is a single child's code. Currently the function is not called - but 
#it is implemeted directly in the executive part of the code
#Suppose you have 100 columns of data, this number correponds with 1s and 0s to whether or not a columns is included
def spawnChild():
    for c2 in range(0,n_cols):
        string = string << 1
        if (random.random() < indiv_odds[c2]):
            n = n + 1
            string = string + 1
    return string



initModel()
#START
for c0 in range(0,num_generations):
    print str(c0) + ' - ' + str(datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))
    print str(getEdge('top')[0]) + ' ... ' + str(getEdge('bottom')[0])
    for c1 in range(0,generation_size):
        #print 'generation: ' + str(c0) + ' - child: ' + str(c1)
        n = 0
        string = 0
        for c2 in range(0,n_cols):
            string = string << 1
            if (random.random() < indiv_odds[c2]):
                n = n + 1
                string = string + 1
        if ((n>=(n2use-plus_or_minus)) and (n<=(n2use+plus_or_minus))):
            #assemble matrix
            #print str(string)
            XXX = assembleMatrix()
            runModel()
            score = scoreModel()
            #check result against the best
            save([score, string])
            print str(score)
    reshape()
    if (getEdge('top')[0] == getEdge('bottom')[0]):
        break


#Best child's including parameters
result = str(bin(getEdge('top')[1]))[3:]
#the best score
getEdge('top')[0]





#Optional
'''
import matplotlib.pyplot as plt
zxcv = list(bin(getEdge('top')[1])[3:])
for c5 in range(0, len(zxcv)):
    zxcv[c5] = (1 if zxcv[c5] == '1' else 0)


plt.plot(zxcv)
plt.show()
'''