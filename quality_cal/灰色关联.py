import pandas as pd
import 熵权法

quality_data = pd.read_excel("E:/毕设/轴承（毕设）/轴承及指标体系.xlsx", sheet_name="样本数据1",header=0, index_col=0)
n = quality_data.index.size
rho = 0.5

# 根据指标类型统一转换为正趋势,这里只有润滑需要转换。
quality_data["润滑（脂填充量%）"] = 1-quality_data["润滑（脂填充量%）"]

# 数据无量纲化
quality_data_stand1 = pd.DataFrame(columns=quality_data.columns,index=quality_data.index)
for col in quality_data_stand1.columns:
    c_mean = quality_data[col].mean()
    quality_data_stand1[col] = (quality_data[col])/c_mean

# 确定最优参考序列，后续考虑换成系统内用户确定的标准，可维护
best_series = {}
for col in quality_data_stand1.columns:
    best_series[col] = quality_data_stand1[col].max()

# 两级最小差和两级最大差
min_min = min(quality_data_stand1.min())
max_max = max(quality_data_stand1.max())
association = pd.DataFrame(columns=quality_data.columns,index=quality_data.index)
for col in quality_data_stand1:
    for index in quality_data_stand1.index:
        association[col][index] = (min_min + rho*max_max)/(best_series[col]-quality_data_stand1[col][index]+rho*max_max)

count = {}
# 这里用了熵权法的权重
weight = 熵权法.cal_weight()
for index in association.index:
    for col in association.columns:
        count[index] = count.get(index, 0) + weight[col]*association[col][index]

# 结果
print(sorted(count.items(), key=lambda x: x[1], reverse=True))