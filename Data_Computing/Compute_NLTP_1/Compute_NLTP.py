import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from SQL.sql import SQL


class savePLot:
    def __init__(self):
        pass

    def saveFig(self, plot, name, subname, fileName):
        basefile = f'C:\\Users\\Homeu\\PycharmProjects\\NewsTweets\\Plot_Outputs\\{name}\\{subname}\\{fileName}.jpg'
        plot.savefig(basefile)


class Compute_NLTP:
    def __init__(self) -> None:
        self.sql = SQL()
        self.SVFIG = savePLot()

    def get_num_emotions(self, name):
        em_d = {'extreme positve': 0, 'positive-neutral': 0, 'neutral': 0, 'negative-neutral': 0, 'extreme-negative': 0}
        data_arr = self.sql.get_pdDf_sql(name).to_numpy()
        for i in data_arr:
            num = em_d[i[7]]
            em_d[i[-1]] = num + 1
        return em_d

    def get_num_likes(self, name):
        like_d = {'extreme positve': 0, 'positive-neutral': 0, 'neutral': 0, 'negative-neutral': 0,
                  'extreme-negative': 0}
        data_arr = self.sql.get_pdDf_sql(name).to_numpy()
        for i in data_arr:
            num = like_d[i[7]]
            like_d[i[7]] = num + i[1]
        print(like_d)
        return like_d

    def compute_plot_bar_emotions(self, name, op):
        if op == "emotions":
            d = self.get_num_emotions(name)
        else:
            d = self.get_num_likes(name)
        sum_v = sum(list(d.values()))
        for j in d.keys():
            i = d[j]
            i = i / sum_v
            i = round(100 * i, 3)
            d[j] = i
        y_ax = list(d.values())
        x_ax = list(d.keys())
        plt.bar(x_ax, y_ax)
        if name == 'emotions':
            plt.title(f"Specific emotions by {name} based on number of tweets")
        else:
            plt.title(f"Specific emotions by {name} based on likes")
        plt.xlabel('Emotions Recorded')
        plt.ylabel('Percentage(%)')
        if name == "emotions":
            self.SVFIG.saveFig(plt, name, 'Stage-1', 'specific_bar_stage1_tweets')
        else:
            self.SVFIG.saveFig(plt, name, 'Stage-1', 'specific_bar_stage1_likes')
        plt.show()
        plt.close()

        y = [y_ax[0] + y_ax[1], y_ax[2], y_ax[3] + y_ax[4]]
        x = ['positive', 'neutral', 'negative']
        plt.bar(x, y)
        if name == 'emotions':
            plt.title(f"Overall emotions by {name} based on number of tweets")
        else:
            plt.title(f"Overall emotions by {name} based on likes")
        plt.xlabel('Emotions Recorded')
        plt.ylabel('Percentage(%)')
        if name == "emotions":
            self.SVFIG.saveFig(plt, name, 'Stage-1', 'overall_bar_stage1_tweets')
        else:
            self.SVFIG.saveFig(plt, name, 'Stage-1', 'overall_bar_stage1_likes')
        plt.show()
        plt.close()

    def compute_plot_pie_emotions(self, name, op):
        if op == "emotions":
            d = self.get_num_emotions(name)
        else:
            d = self.get_num_likes(name)
        sum_v = sum(list(d.values()))
        for j in d.keys():
            i = d[j]
            i = i / sum_v
            i = round(100 * i, 3)
            d[j] = i
        values = list(d.values())
        labels = list(d.keys())
        explode_1 = (0.05, 0.05, 0.05, 0.05, 0.05)
        fig, ax = plt.subplots(figsize=(8.3, 8.3))
        ax.pie(values, labels=[f"{label}: {value}" for label, value in zip(labels, values)], explode=explode_1,
               autopct='%1.1f%%')
        if name == 'emotions':
            plt.title(f"Specific emotions by {name} based on number of tweets")
        else:
            plt.title(f"Specific emotions by {name} based on likes")
        plt.legend(labels, loc="upper left")
        plt.show()
        plt.close()

        values_2 = [values[0] + values[1], values[2], values[3] + values[4]]
        labels_2 = ['positive', 'neutral', 'negative']
        explode_2 = (0.05, 0.05, 0.05)
        fig, ax = plt.subplots(figsize=(8.3, 8.3))
        ax.pie(values_2, labels=[f"{label}: {value}" for label, value in zip(labels_2, values_2)], explode=explode_2,
               autopct='%1.1f%%')
        if name == 'emotions':
            plt.title(f"Overall emotions by {name} based on number of tweets")
        else:
            plt.title(f"Overall emotions by {name} based on likes")
        plt.legend(labels_2, loc="upper left")
        if name == "emotions":
            self.SVFIG.saveFig(plt, name, 'Stage-1', 'overall_pie_stage1_tweets')
        else:
            self.SVFIG.saveFig(plt, name, 'Stage-1', 'overall_pie_stage1_likes')
        plt.show()
        plt.close()


if __name__ == "__main__":
    obj = Compute_NLTP()
    obj.compute_plot_pie_emotions('NDTV', 'e')
