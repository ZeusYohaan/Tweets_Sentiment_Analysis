from SQL.sql import SQL
import pandas as pd
from Data_Processing.Process_1_NLTK.Process_1_NLTK import Read_NLTK


class Analyze_auto_NLTK:
    def __init__(self):
        self.main_ndtv_file = Read_NLTK().ndtv_file
        self.main_republic_file = Read_NLTK().republic_file
        self.main_cnn_file = Read_NLTK().cnn_file
        self.sql_obj = SQL()

    def read_csv(self, news):
        if news == 'NDTV':
            data = pd.read_csv(self.main_ndtv_file)
            data_arr = data.to_numpy()
            return data_arr, data
        elif news == 'REPUBLIC':
            data = pd.read_csv(self.main_republic_file)
            data_arr = data.to_numpy()
            return data_arr, data
        elif news == 'CNN':
            data = pd.read_csv(self.main_cnn_file)
            data_arr = data.to_numpy()
            return data_arr, data
        else:
            return None, None

    def get_emotion_text(self, val):
        val_f = float(val)
        if val_f <= -0.8:
            return 'extreme-negative'
        elif -0.8 <= val_f <= -0.35:
            return 'negative-neutral'
        elif -0.35 <= val_f <= 0.35:
            return 'neutral'
        elif 0.35 <= val_f <= 0.8:
            return 'positive-neutral'
        elif 0.8 <= val_f <= 1:
            return 'extreme positve'

    def update_emotion_csv(self, news):
        func = self.read_csv(news)
        pd_df = func[1]
        np_arr = func[0]
        ls = []
        if np_arr is not None:
            for i in np_arr:
                str = self.get_emotion_text(i[6])
                ls.append(str)
            pd_df['emotions'] = ls
            pd_df.to_csv(self.main_ndtv_file, index=False)
            # SQL Update
            self.sql_obj.upload_csv_sql(self.main_ndtv_file, news)


# if __name__ == "__main__":
#     anal_obj = Analyze_auto_NLTK()
#     anal_obj.update_emotion_csv('NDTV')
