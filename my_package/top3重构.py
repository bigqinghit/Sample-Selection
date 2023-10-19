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
    with pd.ExcelFile(xl_abs_path) as xl:
        df = pd.read_excel(xl, sheet_name='Sheet1')
        row, col = start_row_col
        row -= 2
        col -= 1

        # 遍历输入列后面的10个列，并获取每列前三个最大值组成一个二维列表
        top3_total_lst = [get_1col_top3(col + i, row, df) for i in range(COL_TOTAL)]

        # print(top3_total_lst)
        # 将二维列表转置，并分别取第一行、第二行、第三行作为top1、top2、top3对应的列表
        top1_lst, top2_lst, top3_lst = zip(*top3_total_lst)
        return {'top1': list(top1_lst), 'top2': list(top2_lst), 'top3': list(top3_lst)}


def get_1col_top3(col: int, row: int, df: pd.DataFrame) -> list:
    """
    在列表中一列的数据，降序取前三
    :param col: 列数
    :param row: 行数
    :param df:
    :return:
    """
    data = df.iloc[row: row + ROW_INTERVAL, col]  # 特定的行和列
    array = data.values
    lst = array.tolist()

    # 对每个元素四舍五入保留四位小数，并降序排序后取前三个元素组成一个新列表
    return sorted([round(float(x), 4) for x in lst], reverse=True)[:3]


if __name__ == '__main__':
    # 定义常量并用大写表示
    ROW_INTERVAL = 9  # 行间隔 -- 9个指标
    COL_TOTAL = 10  # 总共有10列数据 -- 10个百分比组别

    root = r'/Users/wangpengcheng/PycharmProjects/MStar/绘制论文结果图/excel_package'
    xl_ = r'MStar-AlexNet结果汇总.xlsx'

    xl_abs = os.path.join(root, xl_)

    # 使用f-string格式化字符串
    print(f"开始处理{xl_abs}文件...")

    # start_row_col: 是左上角数据
    # start_row_col: 是左上角数据框的坐标，行列号就是表中对应的行列号，不用加1减1
    top_dict = get_top3_lst(xl_abs_path=xl_abs, start_row_col=(3, 54))
    print(top_dict['top1'])
    print(type(top_dict['top1']))
