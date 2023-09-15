import numpy as np
import pandas as pd
from Data_Processing.RW_CSV.RW_CSV import Read_File
# import nltk
# nltk.download('vader_lexicon')

class Read_NLTK:
    def __init__(self):
        self.file_path = Read_File().file_paths
        self.ndtv_file = Read_File.return_new_path(Read_File, 'ndtv')
        self.republic_file = Read_File.return_new_path(Read_File, 'republic')
        self.cnn_file = Read_File.return_new_path(Read_File, 'cnn')

    def read_file(self, ind):
        
        data = pd.read_csv(self.file_path[ind])
        data_arr = data.to_numpy()
        return data_arr


    def analyze_string(self, str):
        from nltk.sentiment import SentimentIntensityAnalyzer
        analyzer = SentimentIntensityAnalyzer()
        val = analyzer.polarity_scores(str)
        return val
    
    def analyze_arr_india(self, ind):
        np_arr = self.read_file(ind)
        ls=[]
        for i in np_arr:
            if(isinstance(i[3], str)==True):
                score = self.analyze_string(i[3])
                score_l = list(map(str, score.values()))
                score_s = ", ".join(score_l)
                i = [i[1], i[4], i[5], score_s]
                ls.append(np.array(i))
        nP_arr_2 = np.array(ls)
        return nP_arr_2
    
if __name__ == "__main__":
    Process_obj = Read_NLTK()
    np_arr = Process_obj.analyze_arr_india(1)
    Read_File.write_file(Read_File(), np_arr, Process_obj.ndtv_file)