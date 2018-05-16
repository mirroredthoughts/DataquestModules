## 3. Condensing the Class Size Data Set ##

class_size=data["class_size"]
class_size=class_size[class_size["GRADE "]=="09-12"]
class_size=class_size[class_size["PROGRAM TYPE"]=="GEN ED"]
print(class_size.head())


## 5. Computing Average Class Sizes ##

import numpy as np
import pandas as pd

class_size=class_size.groupby("DBN").agg(np.mean)
class_size.reset_index(inplace=True)
data["class_size"]=class_size
print(data["class_size"].head())


## 7. Condensing the Demographics Data Set ##

demographics=data["demographics"]
demographics=demographics[demographics["schoolyear"]==20112012]
print(demographics.head())


data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]
print(data["demographics"].head())

## 9. Condensing the Graduation Data Set ##

graduation=data["graduation"]
graduation=graduation[graduation["Cohort"]=="2006"]
graduation=graduation[graduation["Demographic"]=="Total Cohort"]

print(graduation.head())

data["graduation"] = data["graduation"][data["graduation"]["Cohort"] == "2006"]
data["graduation"] = data["graduation"][data["graduation"]["Demographic"] == "Total Cohort"]
print(data["graduation"].head())

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

data["ap_2010"]['AP Test Takers ']=pd.to_numeric(data["ap_2010"]['AP Test Takers '],errors="coerce")

data["ap_2010"]['Total Exams Taken']=pd.to_numeric(data["ap_2010"]['Total Exams Taken'],errors="coerce")

data["ap_2010"]['Number of Exams with scores 3 4 or 5']=pd.to_numeric(data["ap_2010"]['Number of Exams with scores 3 4 or 5'],errors="coerce")

print(data["ap_2010"].dtypes)

## 12. Performing the Left Joins ##

combined = data["sat_results"]

combined=combined.merge(data["ap_2010"],on="DBN",how="left")
combined=combined.merge(data["graduation"],on="DBN",how="left")
print(combined.head(5))
print(combined.shape)

## 13. Performing the Inner Joins ##

combined = combined.merge(data["class_size"],on="DBN",how="inner")
combined = combined.merge(data["demographics"],on="DBN",how="inner")
combined = combined.merge(data["survey"],on="DBN",how="inner")
combined = combined.merge(data["hs_directory"],on="DBN",how="inner")

print(combined.head(5))
print(combined.shape)


## 15. Filling in Missing Values ##

combined=combined.fillna(combined.mean())
combined=combined.fillna(0)
print(combined.head(5))

## 16. Adding a School District Column for Mapping ##

def extractstring(dbn):
    return dbn[0:2]


combined["school_dist"]=combined["DBN"].apply(extractstring)
print(combined["school_dist"].head())