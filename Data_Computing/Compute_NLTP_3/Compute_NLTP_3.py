from Data_Computing.Compute_NLTP_2.Compute_NLTP_2 import Compute_NLTP_2_General, Compute_NLTP_2_Likes
import matplotlib.pyplot as plt

class Compute_NLTP_3_General:
    def __init__(self):
        self.C_NLTP2_G = Compute_NLTP_2_General()

    def combined_news_data_month(self, news_list):
        n1 = news_list[0]
        n2 = news_list[1]
        n3 = news_list[2]

        month_dict = {}
        n1_month_dict = self.C_NLTP2_G.get_month_dict(n1)
        n2_month_dict = self.C_NLTP2_G.get_month_dict(n2)
        n3_month_dict = self.C_NLTP2_G.get_month_dict(n1)


class Compute_NLTP_3_Likes:
    def __init__(self):
        self.C_NLTP2_L = Compute_NLTP_2_Likes()