import pandas as pd
import 熵权法


# 计算在第j级的样本个数，假设是一批样本数据，来自一种型号的
def count_R(col, quality_data, stand):
    count = 0
    for one in quality_data[col]:
        if one <= stand:
            count += 1
    return count


weight = 熵权法.cal_weight()

quality_data = pd.read_excel("E:/毕设/轴承（毕设）/轴承及指标体系.xlsx", sheet_name="样本数据1", header=0, index_col=0)
n = quality_data.index.size
quality_needs = pd.read_excel("E:/毕设/轴承（毕设）/轴承及指标体系.xlsx", sheet_name="机体杆端球轴承-数值类型", header=0, index_col=0)
quality_data["润滑（脂填充量%）"] = 1 - quality_data["润滑（脂填充量%）"]
quality_needs.loc["润滑（脂填充量%）"] = 1 - quality_needs.loc["润滑（脂填充量%）"]
R = pd.DataFrame(columns=quality_needs.columns, index=quality_needs.index)
# 计算模糊矩阵new_R
for col in quality_needs.index:
    for grade in quality_needs.columns:
        R[grade][col] = count_R(col, quality_data, quality_needs[grade][col])
new_R = pd.DataFrame(columns=quality_needs.columns, index=quality_needs.index)
flag = 0
for grade in R.columns:
    if flag == 0:
        flag = grade
        new_R[grade] = R[grade] / n
        continue
    else:
        new_R[grade] = (R[grade] - R[flag]) / n
        flag = grade

# 计算隶属度
membership = {}
for grade in new_R.columns:
    for col in new_R.index:
        membership[grade] = membership.get(grade, 0) + weight[col] * new_R[grade][col]
print(sum(weight.values()))