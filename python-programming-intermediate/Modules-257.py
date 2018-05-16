## 1. Introduction to Modules ##

import math

root=math.sqrt(99)
flr=math.floor(89.9)

## 2. Importing Using An Alias ##

import math as m

root=m.sqrt(33)

## 3. Importing A Specific Object ##

from math import *

root=math.sqrt(1001)

## 4. Variables Within Modules ##

import math

print(math.pi)

## 5. The CSV Module ##

import csv

nfl=list(csv.reader(open("nfl.csv")))

## 6. Counting How Many Times a Team Won ##

import csv
f = open("nfl.csv", "r")
nfl = list(csv.reader(f))
patriots_wins=0
for n in nfl:
    winner=n[2]
    if winner=="New England Patriots":
        patriots_wins=patriots_wins+1
        
        

## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins(team_name):
    wins=0
    for n in nfl:
        team=n[2]
        if team==team_name:
            wins=wins+1
    return wins

cowboys_wins=nfl_wins("Dallas Cowboys")
falcons_wins=nfl_wins("Atlanta Falcons")

        