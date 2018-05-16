## 2. Introduction to the Data Set ##

import pandas as pd
titanic=pd.read_csv('train.csv')
cols = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
titanic = titanic[cols].dropna()

## 3. Creating Histograms In Seaborn ##

import seaborn as slt
import matplotlib.pyplot as plt
slt.distplot(titanic["Age"])
plt.show()

## 4. Generating A Kernel Density Plot ##

import seaborn as slt
import matplotlib.pyplot as plt

slt.kdeplot(titanic["Age"],shade=True)
plt.xlabel("Age")

## 5. Modifying The Appearance Of The Plots ##

import seaborn as slt
import matplotlib.pyplot as plt

slt.kdeplot(titanic["Age"],shade=True)
slt.set_style('white')
plt.xlabel("Age")
slt.despine(left=True,bottom=True)

## 6. Conditional Distributions Using A Single Condition ##

import matplotlib.pyplot as plt
import seaborn as slt

g=slt.FacetGrid(titanic,col="Pclass",size=6)
g.map(slt.kdeplot,"Age",shade=True)
slt.despine(left=True,bottom=True)
plt.show()

## 7. Creating Conditional Plots Using Two Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 8. Creating Conditional Plots Using Three Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass",hue="Sex",size=3)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 9. Adding A Legend ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass",hue="Sex",size=3)
g=(g.map(sns.kdeplot, "Age", shade=True).add_legend())
sns.despine(left=True, bottom=True)
plt.show()