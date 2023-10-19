import os
import pandas as pd

"""
获取5%到90%内的 9*10 列表的数据
1、每一列降序排列选择前三的数据，共计10列
2、top1、top2、top3的3个列表输出，封装到一个字典中
"""


def get_top3_lst(xl_abs_path: str, start_row_col: tuple) -> dict:
    """
    输入xl的绝对路径，起始数据的左上角坐标，返回top3数据的列表
    :param xl_abs_path:
    :param start_row_col:
    :return: 以字典的形式返回top1、top2、top3对应的列表
    """
    df = pd.read_excel(xl_abs, sheet_name='Sheet1')
    row, col = start_row_col
    row -= 2
    col -= 1

    top3_total_lst = []

    # 遍历输入列后面的10个列
    for _ in range(col, col + col_total):
        top3_col = get_1col_top3(_, row, df)
        top3_total_lst.append(top3_col)

    # print(top3_total_lst)
    top1_lst = [_[0] for _ in top3_total_lst]
    top2_lst = [_[1] for _ in top3_total_lst]
    top3_lst = [_[2] for _ in top3_total_lst]

    return {'top1': top1_lst, 'top2': top2_lst, 'top3': top3_lst}


def get_1col_top3(col: int, row: int, df: pd) -> list:
    """
    在列表中一列的数据，降序取前三
    :param col: 列数
    :param row: 行数
    :param df:
    :return:
    """
    data = df.iloc[row: row + row_interval, col]  # 特定的行和列
    array = data.values
    lst = array.tolist()
    col_lst = [round(float(_), 4) for _ in lst]
    col_lst.sort(reverse=True)
    return col_lst[:3]


if __name__ == '__main__':
    row_interval = 9  # 行的间隔 -- 9个指标
    col_total = 10  # 总共有10列数据 -- 10个百分比组别

    root = r'/Users/wangpengcheng/PycharmProjects/MStar/绘制论文结果图/excel_package'
    xl_ = r'MStar-AlexNet结果汇总.xlsx'

    xl_abs = os.path.join(root, xl_)
    # start_row_col: 是左上角的数据框的坐标，行列号就是表中对应的行列号，不用加1减1
    top_dict = get_top3_lst(xl_abs_path=xl_abs, start_row_col=(3, 54))
    print(top_dict['top1'])
