import pandas as pd
import math

def cal_weight():
    quality_data = pd.read_excel("E:/毕设/轴承（毕设）/轴承及指标体系.xlsx", sheet_name="样本数据1",header=0, index_col=0)
    n = quality_data.index.size
    m = quality_data.columns.size
    # 数据标准化
    quality_data_stand = pd.DataFrame(columns=quality_data.columns)
    for col in quality_data_stand.columns:
        c_min = min(quality_data[col])
        c_max = max(quality_data[col])
        quality_data_stand[col] = (quality_data[col]-c_min)/(c_max-c_min)

    # 计算指标内比重
    for col in quality_data_stand:
        quality_data_stand[col] = quality_data_stand[col]/quality_data_stand[col].sum()

    # 求信息熵
    dic_mess = {}
    for col in quality_data_stand:
        sum_result = 0
        for index in quality_data_stand.index:
            if quality_data_stand[col][index] == 0:
                sum_result += quality_data_stand[col][index]
            else:
                sum_result += quality_data_stand[col][index]*math.log(quality_data_stand[col][index])
        dic_mess[col] = -1/math.log(n)*sum_result

    # 得出权重
    weight = {}
    for key in dic_mess:
        weight[key] = (1-dic_mess[key])/(m-sum(dic_mess.values()))
    return weight


if __name__ == "__main__":
    cal_weight()