import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import random
df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()
populationmean = statistics.mean(data)
standarddeviation = statistics.stdev(data)
def randomMean(counter):
	dataset = []
	for i in range(counter):
		randomindex = random.randint(0,len(data)-1)
		value = data[randomindex]
		dataset.append(value)
	mean = statistics.mean(dataset)
	return mean
	##st = statistics.stdev(dataset)
def plot(meanList):
	df = meanList
	mean = statistics.mean
	##fig = ff.create_distplot([data, ["temp"], show_hist = False])
	##fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "MEAN"))
	##fig.show()
def main():
	meanList = []
	for i in range(1000):
		setofmeans = randomMean(100)
		meanList.append(setofmeans)
	plot(meanList)
	mean = statistics.mean(meanList)
	##print ("Population Mean:", populationmean)
	##print ("Standard Deviation:", standarddeviation)
	##print ("Sample Mean:", mean)
	print ("Mean:", mean)
main()
print ("Population Mean", populationmean)
def standarddeviation():
	meanList = []
	for i in range(1000):
		setofmeans = randomMean(100)
		meanList.append(setofmeans)
	st = statistics.stdev(meanList)
	print ("Sample Standard Deviation:", st)
standarddeviation()
