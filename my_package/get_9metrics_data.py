import os

import pandas as pd


def get_row_data(start_row_col: tuple, xl_path: os) -> tuple[str, list[float]]:
    """
    获取表中一行的信息
    :param xl_path: 文件的绝对路径
    :param start_row_col: 行是Excel中对应的行，不用加减任何数字
                          列从0开始数
    :return: 读取的列表
    """
    df = pd.read_excel(xl_path, sheet_name='Sheet1')
    row, col = start_row_col
    row -= 2
    col -= 1
    data = df.iloc[row, col: col + 10]  # 特定的行和列  总共有10列数据 -- 10个百分比组别
    array = data.values

    _ = print_belong_info(row, col, df)

    return _, array.tolist()


def print_belong_info(row: int, col: int, df_: pd) -> str:
    """
    打印坐标从属信息，即行标题的信息
    返回所属指标的名称：contrast_等间隔、Laplacian_等间隔
    """
    col -= 1  # 往前1列
    _ = df_.iloc[row, col]
    if '_' in _:
        _ = _.split('_')[-2]  # 去掉中文

    return _


NINE_METRICS_COUNT = 9


def get_9_metrics(excel_file_path: str, start_raw_col: tuple) -> dict:
    """
    获取表格中9个指标的值，组成列表的形式并以字典的形式返回
    :param excel_file_path: excel文件的绝对路径，包含文件名
    :param start_raw_col: 起始表格的行列数 -- 元祖形式，对应的是表中的行列，不增减
    :return: 返回字典，key是指标名称，value是浮点型数据的列表
    """
    metric = {}

    row, col = start_raw_col
    for _ in range(NINE_METRICS_COUNT):
        idctor, data_lst = get_row_data(start_row_col=(row, col), xl_path=excel_file_path)
        metric[idctor] = data_lst
        row += 1

    return metric


if __name__ == '__main__':
    f = r'/Users/wangpengcheng/PycharmProjects/MStar/绘制论文结果图/绘制结果/OpenSarShip01_ResNet50/' \
        r'OpenSarShip01_resnet50_结果汇总.xlsx'

    # idctor, data_lst = get_row_data(start_row_col=(3, 2), xl_path=f)
    # print(f'{idctor}: {data_lst}')
    # print(type(data_lst[0]))  # <class 'numpy.float64'>
    res_dict = get_9_metrics(f, (3, 2))
    print(res_dict)
    print(len(res_dict))
