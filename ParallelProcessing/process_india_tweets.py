from Data_Processing.Process_1_NLTK.Process_1_NLTK import Read_File, Read_NLTK
from Data_Processing.Process_2_NLTK.Process_2_NLTK import Analyze_auto_NLTK
from Data_Computing.Compute_NLTP_1.Compute_NLTP import Compute_NLTP
from Data_Computing.Compute_NLTP_2.Compute_NLTP_2 import Compute_NLTP_2_General, Compute_NLTP_2_Likes
import multiprocessing


class process_india:
    def __init__(self) -> None:
        self.file_paths = Read_File().file_paths

    def automate_ndtv(self, op_list):
        data_processing = op_list[0]
        data_computing = op_list[1]
        if data_processing[0] == 1:
            p1_obj = Read_NLTK()
            np_arr = p1_obj.analyze_arr_india(1)
            Read_File.write_file(Read_File(), np_arr, p1_obj.ndtv_file)

        if data_processing[1] == 1:
            p2_obj = Analyze_auto_NLTK()
            p2_obj.update_emotion_csv('NDTV')

        if data_computing[0] == 1:
            c1_obj = Compute_NLTP()
            c1_obj.compute_plot_pie_emotions('NDTV', 'emotions')
            c1_obj.compute_plot_pie_emotions('NDTV', 'likes')

        if data_computing[1] == 1:
            c2_likes_obj = Compute_NLTP_2_Likes()
            c2_tweets_obj = Compute_NLTP_2_General()
            c2_likes_obj.combine_month_day_plot('NDTV')
            c2_tweets_obj.combine_month_day_plot('NDTV')

    def automate_republic(self, op_list):
        data_processing = op_list[0]
        data_computing = op_list[1]
        if data_processing[0] == 1:
            p1_obj = Read_NLTK()
            np_arr = p1_obj.analyze_arr_india(2)
            Read_File.write_file(Read_File(), np_arr, p1_obj.republic_file)

        if data_processing[1] == 1:
            p2_obj = Analyze_auto_NLTK()
            p2_obj.update_emotion_csv('REPUBLIC')

        if data_computing[0] == 1:
            c1_obj = Compute_NLTP()
            c1_obj.compute_plot_pie_emotions('REPUBLIC', 'emotions')
            c1_obj.compute_plot_pie_emotions('REPUBLIC', 'likes')

        if data_computing[1] == 1:
            c2_likes_obj = Compute_NLTP_2_Likes()
            c2_tweets_obj = Compute_NLTP_2_General()
            c2_likes_obj.combine_month_day_plot('REPUBLIC')
            c2_tweets_obj.combine_month_day_plot('REPUBLIC')

    def automate_cnn(self, op_list):
        data_processing = op_list[0]
        data_computing = op_list[1]
        if data_processing[0] == 1:
            p1_obj = Read_NLTK()
            np_arr = p1_obj.analyze_arr_india(0)
            Read_File.write_file(Read_File(), np_arr, p1_obj.cnn_file)

        if data_processing[1] == 1:
            p2_obj = Analyze_auto_NLTK()
            p2_obj.update_emotion_csv('CNN')

        if data_computing[0] == 1:
            c1_obj = Compute_NLTP()
            c1_obj.compute_plot_pie_emotions('CNN', 'emotions')
            c1_obj.compute_plot_pie_emotions('CNN', 'likes')

        if data_computing[1] == 1:
            c2_likes_obj = Compute_NLTP_2_Likes()
            c2_tweets_obj = Compute_NLTP_2_General()
            c2_likes_obj.combine_month_day_plot('CNN')
            c2_tweets_obj.combine_month_day_plot('CNN')


if __name__ == "__main__":
    obj = process_india()

    ndtv_args = [(0, 0), (1, 1)]
    cnn_args = [(0, 0), (1, 1)]
    republic_args = [(0, 0), (1, 1)]

    ndtv_process = multiprocessing.Process(target=obj.automate_ndtv, args=(ndtv_args,))
    cnn_process = multiprocessing.Process(target=obj.automate_cnn, args=(cnn_args,))
    republic_process = multiprocessing.Process(target=obj.automate_republic, args=(republic_args,))

    ndtv_process.start()
    cnn_process.start()
    republic_process.start()

    ndtv_process.join()
    cnn_process.join()
    republic_process.join()
