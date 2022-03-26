import numpy as np
import pandas as pd
import Weibull_plot


class Weibull_fit:
    def __init__(self, fpath):
        self.fpath = fpath
        self.life_data = pd.DataFrame()

    def get_fit_data(self):
        self.life_data = pd.read_excel(self.fpath, sheet_name="寿命试验数据", header=0, index_col=0)
        self.life_data = self.life_data.sort_values("Ti")
        self.life_data["rank"] = range(1, len(self.life_data) + 1)

    def experience_Fn(self):
        """
        中位秩函数处理
        """
        self.life_data["Ft"] = (self.life_data["rank"] - 0.3) / (self.life_data.index.size + 0.4)

    def liner_trans(self):
        """
        线性变换
        """
        """        
        self.life_data["Xi"] = 0.1
        self.life_data["Yi"] = 0.1
        
        for index in self.life_data.index:
            self.life_data["Xi"][index] = math.log(self.life_data["Ti"][index])
            self.life_data["Yi"][index] = math.log(math.log(1/(1-self.life_data["Ft"][index])))"""
        self.life_data["Xi"] = np.log(self.life_data["Ti"])
        self.life_data["Yi"] = np.log(np.log(1/(1-self.life_data["Ft"])))

    def fit_para(self):
        """
        线性拟合；最小二乘估计
        param：A和B是线性方程的参数，线性逆变换回到威布尔双参数上
        """
        lxx = 0
        lxy = 0
        x_ba = self.life_data["Xi"].mean()
        y_ba = self.life_data["Yi"].mean()
        for index in self.life_data.index:
            lxx += (self.life_data["Xi"][index]-x_ba)**2
            lxy += (self.life_data["Xi"][index]-x_ba)*(self.life_data["Yi"][index]-y_ba)
        B_hat = lxx/lxy
        A_hat = y_ba - B_hat*x_ba
        beta = B_hat
        yita = np.exp(A_hat/-B_hat)
        return {"yita":yita,"beta":beta}


if __name__ == "__main__":
    my_fit = Weibull_fit("E:/毕设/轴承（毕设）/轴承及指标体系.xlsx")
    my_fit.get_fit_data()
    my_fit.experience_Fn()
    my_fit.liner_trans()
    result = my_fit.fit_para()
    print(result)
    Weibull_plot.weibull_acc_fig(c=result["yita"], k=result["beta"])
