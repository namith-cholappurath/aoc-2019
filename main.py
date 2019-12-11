import pandas as pd 
import math

def fuelCalc(mass):
	currentFuel = math.floor(mass/3)-2
	if( currentFuel <=0):
		return 0
	else:
		return currentFuel + fuelCalc(currentFuel)
inputfile="https://adventofcode.com/2019/day/1/input"
moduleWeight=pd.read_csv("day1Input.csv",header=None)
moduleFuel=moduleWeight.applymap(lambda x:fuelCalc(x))
print(moduleFuel.sum())
