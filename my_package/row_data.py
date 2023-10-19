import os

import pandas as pd

"""
获取一行的数据，转为列表，保留4位小数
返回一个列表
"""


def get_row_data(start_raw_col: tuple, xl_path: os) -> list[float]:
    """
    获取表中一行的信息
    :param xl_path: 文件的绝对路径
    :param start_raw_col: 行是Excel中对应的行，不用加减任何数字
                            列从0开始数
    :return: 读取的列表
    """
    df = pd.read_excel(xl_path, sheet_name='Sheet1')
    row, col = start_raw_col
    row -= 2
    col -= 1
    data = df.iloc[row, col: col + 10]  # 特定的行和列  总共有10列数据 -- 10个百分比组别
    array = data.values

    print_belong_info(row, col, df)

    return [round(i, 4)for i in array.tolist()]


def print_belong_info(row: int, col: int, df_: pd) -> None:
    """
    打印坐标从属信息，即行标题的信息
    """
    col -= 1  # 往前1列
    print(f'前一列：{df_.iloc[row, col]}')


if __name__ == '__main__':
    root = r'/Users/wangpengcheng/PycharmProjects/MStar/绘制论文结果图/excel_package'
    xl_ = r'MStar-AlexNet结果汇总.xlsx'

    xl = os.path.join(root, xl_)
    # 行列号就是表中对应的行列号，不用加1减1
    data_lst = get_row_data(start_raw_col=(18, 2), xl_path=xl)
    print(data_lst)
