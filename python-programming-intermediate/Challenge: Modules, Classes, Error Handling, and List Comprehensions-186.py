## 2. Introduction to the Data ##

import csv
years={}
nfl_suspensions=list(csv.reader(open('nfl_suspensions_data.csv','r')))[1:]
print(nfl_suspensions)

for r in nfl_suspensions:
    row_year=r[5]
    if row_year in years:
        years[row_year]=years[row_year]+1
    else:
        years[row_year]=1
print(years)

## 3. Unique Values ##

print(nfl_suspensions)

teams=[row[1] for row in nfl_suspensions]
unique_teams=set(teams)

games=[row[2] for row in nfl_suspensions]
unique_games=set(games)

## 4. Suspension Class ##

class Suspension():
    def __init__(self,rowlist):
        self.name=rowlist[0]
        self.team=rowlist[1]
        self.games=rowlist[2]
        self.year=rowlist[3]
        
        
third_suspension=Suspension(nfl_suspensions[2])

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year=int(row[5])
        except Exception:
            self.year=0
            
    def get_year(self):
        return(self.year)
    
missing_year=Suspension(nfl_suspensions[22])
twenty_third_year=missing_year.get_year()