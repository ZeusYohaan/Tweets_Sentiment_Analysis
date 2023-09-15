import numpy as np
import pandas as pd


class Read_File:
    def __init__(self):
        self.file_paths = [r'C:\Users\Homeu\PycharmProjects\NewsTweets\Data_Storage\indian_Tweets\cnn_clean.csv',
                           r'C:\Users\Homeu\PycharmProjects\NewsTweets\Data_Storage\indian_Tweets\ndtv_clean.csv',
                           r'C:\Users\Homeu\PycharmProjects\NewsTweets\Data_Storage\indian_Tweets\republic_clean.csv']

    def modify_file(self, file_path, col_name, news_name):
        data = pd.read_csv(file_path)
        col = data.columns.tolist()
        if col_name not in col:
            for i in col_name:
                data[i] = None
            str = news_name + '_new.csv'
            new_path = r'C:\Users\Homeu\PycharmProjects\NewsTweets/Data_Storage/indian_Tweets/{}'.format(str)
            data.to_csv(new_path, index=False)
        return new_path

    def write_file(self, np_arr, file_path):
        np.savetxt(file_path, np_arr, delimiter=',', fmt='%s', header='id, likes, date, neg, neu, pos, compound')

    def return_new_path(self, news_name):
        str = news_name + '_new.csv'
        new_path = r'C:\Users\Homeu\PycharmProjects\NewsTweets\Data_Storage/indian_Tweets/{}'.format(str)
        return new_path
