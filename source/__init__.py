from collections import defaultdict

import numpy as np
import pandas
from pandas import DataFrame


class MineSvm:
    """
    使用一个svm来做分类
    """
    """
    先读取数据 在做数据的初始化
    """

    def __init__(self):
        self.molecular_desc = []
        self.activity = []

    def get_data(self):
        self.molecular_desc = pandas.read_excel("../files/Molecular_Descriptor.xlsx")
        # 只选择了第一列与第三列
        self.activity = pandas.read_excel(io="../files/ERα_activity.xlsx", usecols=[0, 2])
        relative_result = []
        kens = []
        pears = []
        spears = []
        result = []
        d = defaultdict(int)
        for i in range(1, self.molecular_desc.shape[1]):
            try:
                name = self.molecular_desc.iloc[:, i].name
                d[name] = 0
                df = pandas.DataFrame()
                df[name] = self.molecular_desc.iloc[:, i]
                df['plC50'] = self.activity.iloc[:, 1]
                # df = pandas.DataFrame([self.activity.iloc[:, 1], self.molecular_desc.iloc[:, i]],columns=['xx',name])
                # df = df.fillna(value=0)
                ken = df.corr(method='kendall')
                pear = df.corr()
                spear = df.corr(method='spearman')
                ken.iat[0, 1] = ken.iat[0, 1] if not np.isnan(ken.iat[0, 1]) else 0
                pear.iat[0, 1] = pear.iat[0, 1] if not np.isnan(pear.iat[0, 1]) else 0
                spear.iat[0, 1] = spear.iat[0, 1] if not np.isnan(spear.iat[0, 1]) else 0
                kens.append([name, ken.iat[0, 1]])
                pears.append([name, pear.iat[0, 1]])
                spears.append([name, spear.iat[0, 1]])
            except Exception:
                pass
        print('xx')
        kens.sort(key=lambda z: z[1])
        pears.sort(key=lambda z: z[1])
        spears.sort(key=lambda z: z[1])
        print('1')
        for i in range(len(kens)):
            d[kens[i][0]] += i
            d[pears[i][0]] += i
            d[spears[i][0]] += i
        print('2')
        for x in d.keys():
            result.append([x, d[x]])
        result.sort(key=lambda z: z[1], reverse=True)
        writer = pandas.ExcelWriter('../results/corr.xlsx')
        kens.reverse()
        pears.reverse()
        spears.reverse()
        df = DataFrame(kens)
        df.to_excel(writer, 'kens')
        df = DataFrame(pears)
        df.to_excel(writer, 'pears')
        df = DataFrame(spears)
        df.to_excel(writer, 'spears')
        df = DataFrame(result)
        df.to_excel(writer, 'result')
        writer.save()
        print('over')


demo = MineSvm()
demo.get_data()
