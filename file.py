import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

fig = ff.create_distplot([data], ["Reading Time"], show_hist=False)
fig.show()

print("Population Mean: ", statistics.mean(data))

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["Reading Time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("Sampling Mean: ", statistics.mean(mean_list))
    
setup()