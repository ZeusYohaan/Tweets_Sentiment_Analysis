import numpy as np
import matplotlib.pyplot as plt
from Data_Computing.Compute_NLTP_1.Compute_NLTP import savePLot

import pandas as pd

from Data_Processing.Process_1_NLTK.Process_1_NLTK import Read_NLTK
from Data_Processing.Process_2_NLTK.Process_2_NLTK import Analyze_auto_NLTK
from SQL.sql import SQL


class Compute_NLTP_2_Likes:
    def __int__(self):
        self.P_NLTP_1 = Read_NLTK()
        self.P_NLTP_2 = Analyze_auto_NLTK()
        self.SVFIG = savePLot
        self.SQL = SQL()

    def modify_percentages(self, dict1):
        total = sum(list(dict1.values()))
        for i in dict1.keys():
            dict1[i] = dict1[i] / total
        return dict1

    def get_NpArr_emotions(self, dict1, emotions):
        ls = []
        for i in dict1.keys():
            dict_val = dict1[i]
            ls.append(dict_val[emotions])
        return np.array(ls)

    def reverse_date(self, str, name):
        if name == 'CNN':
            date = str.split('-')
            day = date[2]
            month = date[1]
            year = date[0]
            date = day + '-' + month + '-' + year
            return date
        else:
            return str

    def get_monthYear_date(self, str, name):
        if name == 'CNN':
            str = self.reverse_date(str, name)
        date = str.split('-')
        month = date[1]
        year = date[2]
        return month + '-' + year

    def get_month_dict(self, name):
        pd_df = SQL.get_pdDf_sql(SQL(), name)
        np_arr = pd_df.to_numpy()
        data_dict = {}
        for i in np_arr:
            date = i[2]
            monthYear1 = self.get_monthYear_date(date, name)
            data_dict[monthYear1] = {'negative': 0, 'positive': 0, 'neutral': 0}
        for i in np_arr:
            date = i[2]
            monthYear2 = self.get_monthYear_date(date, name)
            emotion = i[7]
            if emotion == 'extreme positve' or emotion == 'positive-neutral':
                val_dict = data_dict[monthYear2]
                val_emotion = val_dict['positive']
                val_emotion = val_emotion + int(i[1])
                val_dict['positive'] = val_emotion
                data_dict[monthYear2] = val_dict

            elif emotion == 'neutral':
                val_dict = data_dict[monthYear2]
                val_emotion = val_dict['neutral']
                val_emotion = val_emotion + int(i[1])
                val_dict['neutral'] = val_emotion
                data_dict[monthYear2] = val_dict

            elif emotion == 'negative-neutral' or emotion == 'extreme-negative':
                val_dict = data_dict[monthYear2]
                val_emotion = val_dict['negative']
                val_emotion = val_emotion + int(i[1])
                val_dict['negative'] = val_emotion
                data_dict[monthYear2] = val_dict
        return data_dict

    def get_day_dict(self, name):
        year_dict = {}
        pd_df = SQL.get_pdDf_sql(SQL(), name)
        np_arr = pd_df.to_numpy()
        data_dict = {}
        for i in np_arr:
            date = i[2]
            monthYear1 = self.reverse_date(date, name)
            data_dict[monthYear1] = {'negative': 0, 'positive': 0, 'neutral': 0}
        for i in np_arr:
            date = i[2]
            monthYear2 = self.reverse_date(date, name)
            emotion = i[7]
            if emotion == 'extreme positve' or emotion == 'positive-neutral':
                val_dict = data_dict[monthYear2]
                val_emotion = val_dict['positive']
                val_emotion = val_emotion + int(i[1])
                val_dict['positive'] = val_emotion
                data_dict[monthYear2] = val_dict

            elif emotion == 'neutral':
                val_dict = data_dict[monthYear2]
                val_emotion = val_dict['neutral']
                val_emotion = val_emotion + int(i[1])
                val_dict['neutral'] = val_emotion
                data_dict[monthYear2] = val_dict

            elif emotion == 'negative-neutral' or emotion == 'extreme-negative':
                val_dict = data_dict[monthYear2]
                val_emotion = val_dict['negative']
                val_emotion = val_emotion + int(i[1])
                val_dict['negative'] = val_emotion
                data_dict[monthYear2] = val_dict
        return data_dict

    def combine_month_day_plot(self, name):
        day_data_dict = self.get_day_dict(name)
        for i in day_data_dict.keys():
            day_data_dict[i] = self.modify_percentages(day_data_dict[i])

        month_data_dict = self.get_month_dict(name)
        for i in month_data_dict.keys():
            month_data_dict[i] = self.modify_percentages(month_data_dict[i])

        x_axis_month = pd.to_datetime(list(month_data_dict.keys()), format='%m-%Y')
        x_axis_day = pd.to_datetime(list(day_data_dict.keys()), format='%d-%m-%Y')

        month_neutral_y = self.get_NpArr_emotions(month_data_dict, 'neutral')
        month_positive_y = self.get_NpArr_emotions(month_data_dict, 'positive')
        month_negative_y = self.get_NpArr_emotions(month_data_dict, 'negative')

        day_neutral_y = self.get_NpArr_emotions(day_data_dict, 'neutral')
        day_positive_y = self.get_NpArr_emotions(day_data_dict, 'positive')
        day_negative_y = self.get_NpArr_emotions(day_data_dict, 'negative')

        # Create a figure and two subplots (axes)
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

        # Plot monthly data on the first subplot (bar chart)
        ax1.bar(x_axis_month, month_neutral_y, color='coral', label='Neutral', width=20)
        ax1.bar(x_axis_month, month_positive_y, color='deepskyblue', label='Positive', bottom=month_neutral_y, width=20)
        ax1.bar(x_axis_month, month_negative_y, color='lime', label='Negative',
                bottom=month_neutral_y + month_positive_y, width=20)
        ax1.set_ylabel("Ratio")
        ax1.set_title(f"{name}-Emotion Analysis (Monthly) by number of Likes")
        ax1.legend()

        # Plot daily data on the second subplot (line chart)
        ax2.plot(x_axis_day, day_neutral_y, color='coral', label='Neutral')
        ax2.plot(x_axis_day, day_positive_y, color='deepskyblue', label='Positive')
        ax2.plot(x_axis_day, day_negative_y, color='lime', label='Negative')
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Ratio")
        ax2.set_title(f"{name}-Emotion Analysis (Daily) by number of Likes")
        ax2.legend()

        plt.setp(ax2.get_xticklabels(), rotation=45)
        plt.tight_layout()
        savePLot().saveFig(plt, name, 'Stage-2', 'mix_stage2_likes')
        # Show the plot
        plt.show()


class Compute_NLTP_2_General:
    def __init__(self):
        self.SQL = SQL()

    def __int__(self):
        self.P_NLTP_1 = Read_NLTK()
        self.P_NLTP_2 = Analyze_auto_NLTK()
        self.SQL = SQL()

    def modify_percentages(self, dict1):
        total = sum(list(dict1.values()))
        for i in dict1.keys():
            dict1[i] = dict1[i] / total
        return dict1

    def get_NpArr_emotions(self, dict1, emotions):
        ls = []
        for i in dict1.keys():
            dict_val = dict1[i]
            ls.append(dict_val[emotions])
        return np.array(ls)

    def reverse_date(self, str, name):
        if name == 'CNN':
            date = str.split('-')
            day = date[-1]
            month = date[-2]
            year = date[-3]
            date = day + '-' + month + '-' + year
            return date
        else:
            return str

    def get_monthYear_date(self, str, name):
        if name == 'CNN':
            str = self.reverse_date(str, name)
        date = str.split('-')
        month = date[1]
        year = date[2]
        return month + '-' + year

    def get_month_dict(self, name):
        pd_df = SQL.get_pdDf_sql(SQL(), name)
        np_arr = pd_df.to_numpy()
        data_dict = {}
        for i in np_arr:
            date = i[2]
            monthYear1 = self.get_monthYear_date(date, name)
            data_dict[monthYear1] = {'negative': 0, 'positive': 0, 'neutral': 0}
        for i in np_arr:
            date = i[2]
            monthYear2 = self.get_monthYear_date(date, name)
            emotion = i[7]
            if emotion == 'extreme positve' or emotion == 'positive-neutral':
                val_dict = data_dict[monthYear2]
                val_emotion = val_dict['positive']
                val_emotion = val_emotion + 1
                val_dict['positive'] = val_emotion
                data_dict[monthYear2] = val_dict

            elif emotion == 'neutral':
                val_dict = data_dict[monthYear2]
                val_emotion = val_dict['neutral']
                val_emotion = val_emotion + 1
                val_dict['neutral'] = val_emotion
                data_dict[monthYear2] = val_dict

            elif emotion == 'negative-neutral' or emotion == 'extreme-negative':
                val_dict = data_dict[monthYear2]
                val_emotion = val_dict['negative']
                val_emotion = val_emotion + 1
                val_dict['negative'] = val_emotion
                data_dict[monthYear2] = val_dict
        print(data_dict)
        return data_dict

    def get_day_dict(self, name):
        pd_df = SQL.get_pdDf_sql(SQL(), name)
        np_arr = pd_df.to_numpy()
        data_dict = {}
        for i in np_arr:
            date = i[2]
            monthYear1 = self.reverse_date(date, name)
            data_dict[monthYear1] = {'negative': 0, 'positive': 0, 'neutral': 0}
        for i in np_arr:
            date = i[2]
            monthYear2 = self.reverse_date(date, name)
            emotion = i[7]
            if emotion == 'extreme positve' or emotion == 'positive-neutral':
                val_dict = data_dict[monthYear2]
                val_emotion = val_dict['positive']
                val_emotion = val_emotion + 1
                val_dict['positive'] = val_emotion
                data_dict[monthYear2] = val_dict

            elif emotion == 'neutral':
                val_dict = data_dict[monthYear2]
                val_emotion = val_dict['neutral']
                val_emotion = val_emotion + 1
                val_dict['neutral'] = val_emotion
                data_dict[monthYear2] = val_dict

            elif emotion == 'negative-neutral' or emotion == 'extreme-negative':
                val_dict = data_dict[monthYear2]
                val_emotion = val_dict['negative']
                val_emotion = val_emotion + 1
                val_dict['negative'] = val_emotion
                data_dict[monthYear2] = val_dict
        print(data_dict)
        return data_dict

    def combine_month_day_plot(self, name):
        day_data_dict = self.get_day_dict(name)
        for i in day_data_dict.keys():
            day_data_dict[i] = self.modify_percentages(day_data_dict[i])
        month_data_dict = self.get_month_dict(name)
        print(month_data_dict)
        for i in month_data_dict.keys():
            month_data_dict[i] = self.modify_percentages(month_data_dict[i])
        print(month_data_dict)
        x_axis_month = pd.to_datetime(list(month_data_dict.keys()), format='%m-%Y')
        x_axis_day = pd.to_datetime(list(day_data_dict.keys()), format='%d-%m-%Y')

        month_neutral_y = self.get_NpArr_emotions(month_data_dict, 'neutral')
        month_positive_y = self.get_NpArr_emotions(month_data_dict, 'positive')
        month_negative_y = self.get_NpArr_emotions(month_data_dict, 'negative')

        day_neutral_y = self.get_NpArr_emotions(day_data_dict, 'neutral')
        day_positive_y = self.get_NpArr_emotions(day_data_dict, 'positive')
        day_negative_y = self.get_NpArr_emotions(day_data_dict, 'negative')

        # Create a figure and two subplots (axes)
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

        # Plot monthly data on the first subplot (bar chart)
        ax1.bar(x_axis_month, month_neutral_y, color='coral', label='Neutral', width=20)
        ax1.bar(x_axis_month, month_positive_y, color='deepskyblue', label='Positive', bottom=month_neutral_y, width=20)
        ax1.bar(x_axis_month, month_negative_y, color='lime', label='Negative',
                bottom=month_neutral_y + month_positive_y, width=20)
        ax1.set_ylabel("Ratio")
        ax1.set_title(f"{name}-Emotion Analysis (Monthly) by Number of Tweets")
        ax1.legend()

        # Plot daily data on the second subplot (line chart)
        ax2.plot(x_axis_day, day_neutral_y, color='coral', label='Neutral')
        ax2.plot(x_axis_day, day_positive_y, color='deepskyblue', label='Positive')
        ax2.plot(x_axis_day, day_negative_y, color='lime', label='Negative')
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Ratio")
        ax2.set_title(f"{name}-Emotion Analysis (Daily) by Number of Tweets")
        ax2.legend()

        plt.setp(ax2.get_xticklabels(), rotation=45)
        plt.tight_layout()
        savePLot().saveFig(plt, name, 'Stage-2', 'mix_stage2_tweets')
        # Show the plot
        plt.show()


if __name__ == "__main__":
    obj1 = Compute_NLTP_2_Likes()
    obj1.combine_month_day_plot('CNN')
    obj2 = Compute_NLTP_2_General()
    obj2.combine_month_day_plot('CNN')
