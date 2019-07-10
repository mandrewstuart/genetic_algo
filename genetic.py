#IMPORT LIBARARIES
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
line = f.readline()
data = line.split(',')
while(len(line) > 2):
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
    line = f.readline()
    data = line.split(',')



YY = Y
Y = numpy.asarray(YY[1])

#PARAMETERS TO SET
#How many columns do you want to keep?
n2use = 30
#what's an acceptable difference of the above
plus_or_minus = 0
#How many children to create in the algorithm?
generation_size = 200
#How many generations would you like to run?
num_generations = 10


#This runs on auto.
n_cols = len(X[0])
indiv_odds = n_cols*[float(n2use)/n_cols]
best_quantity = int(n_cols**0.5)
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
    for c3 in range(n_cols):
        n = 0.
        for c4 in range(len(best)):
            if best[c4][1][c3] == '1':
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
    elif elem[0] > best[-1][0]:
        best.sort(reverse=True)
        best.pop()
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
def assembleMatrix(string):
    XX = []
    for row in X:
        xx = [1]
        for col in range(0,len(string)):
            if (string[col] == '1'):
                xx.append(row[col])
        XX.append(xx)
    return XX


#This is a single child's code. Currently the function is not called - but 
#it is implemeted directly in the executive part of the code
#Suppose you have 100 columns of data, this number correponds with 1s and 0s to whether or not a columns is included
def spawnChild():
    try:
        temp_odds = indiv_odds
        indices = set()
        for _ in range(n2use):
            total_odds = sum(temp_odds)
            chooser = random.random() * total_odds
            so_far = 0
            index = -1
            while so_far < chooser and index < len(temp_odds):
                index += 1
                so_far += temp_odds[index]
            temp_odds[index] = 0
            indices.add(index)
        string = ''
        for _ in range(len(indiv_odds)):
            if _ in indices:
                string += '1'
            else:
                string += '0'
        return string
    except Exception as e:
        print(e)


initModel()
#START
for c0 in range(0,num_generations):
    print(str(c0) + ' - ' + str(datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")))
    print(str(getEdge('top')[0]) + ' ... ' + str(getEdge('bottom')[0]))
    for c1 in range(0,generation_size):
        print('generation: ' + str(c0) + ' - child: ' + str(c1))
        string = spawnChild()
        XXX = assembleMatrix(string)
        runModel()
        score = scoreModel()
        save([score, string])
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