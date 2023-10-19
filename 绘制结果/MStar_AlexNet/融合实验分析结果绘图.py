from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as mtick


def main(xl_abs_path: str, fusion_raw_: int, random_raw_: int) -> None:
    # sourcery skip: merge-list-append, move-assign-in-block
    df = pd.read_excel(xl_abs_path)

    # 每行的首尾坐标列数
    start_col = START_COL - 1
    end_col = start_col + GRP_COL_NUM

    # 每行的初始行数：有一个指标值和百分比 ， 共2行，减掉2行，
    fusion_raw_, random_raw_ = fusion_raw_ - 2, random_raw_ - 2
    fs_dict, rdm_dict = get_fusion_rdm_dict(df, end_col, fusion_raw_, random_raw_, start_col)
    avg_perf_up_lst = get_max_avg_avglst(fs_dict, rdm_dict)

    draw_fig(avg_perf_up_lst)


def draw_fig(avg_perf_up_lst):
    x_ = ['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', ]
    # 绘制柱状图
    plt.figure(figsize=(7, 5))
    plt.bar(x_, avg_perf_up_lst, color='#3876B1')
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

    plt.xlabel('training sample percentage')
    plt.ylabel("performance improvements")

    plt.savefig("./结果图/MStar_AlexNet_performance_average_lift_histogram.png")
    # plt.show()


def get_max_avg_avglst(fs_dict, rdm_dict):
    """
    用numpy统计 7 * 10 的性能结果，按列取均值
    :param fs_dict:
    :param rdm_dict:
    :return:
    """
    ind_res_lst = []
    arr1 = np.empty((7, 10))
    for ind in ind_list:  # acc pre recall f1
        fs_data_lst = fs_dict[ind]
        rdm_data_lst = rdm_dict[ind]
        perf_lst = []  # acc   5% 10% - 90%

        # 5% 10% 20%  循环
        for data_idx in range(len(fs_data_lst)):
            if ind != 'hamming':
                perf_improv = (fs_data_lst[data_idx] - rdm_data_lst[data_idx]) / rdm_data_lst[data_idx]
            else:
                perf_improv = (rdm_data_lst[data_idx] - fs_data_lst[data_idx]) / rdm_data_lst[data_idx]
            perf_lst.append(perf_improv)

        ind_res_lst.append(perf_lst)
        print_max_avg_info(ind, perf_lst)
    arr1 = np.array(ind_res_lst)

    return np.mean(arr1, axis=0)


def print_max_avg_info(ind, perf_lst):
    """
    打印每个指标列表中最大值和平均值： 提升的百分比
    :param ind:
    :param perf_lst:
    :return:
    """
    print(f'{ind}: {perf_lst}')
    print(f'{ind}_max: {round(max(perf_lst) * 100, 2)}%')
    print(f'{ind}_avg: {round(mean(perf_lst) * 100, 2)}%')
    print('')


def get_fusion_rdm_dict(df, end_col, fusion_raw_, random_raw_, start_col) -> tuple[dict[str, list], dict[str, list]]:
    """
    获取xl表中融合组和随机组的各指标数据
    :param df: pd文件对象
    :param start_col: 初始一行开始的列数
    :param end_col: 初始一行结束的的列数
    :param fusion_raw_: 融合组行数
    :param random_raw_: 随机组行数
    :return: 指标组的字典，随机组的字典
    """
    ind_dict = {}
    random_dict = {}
    for idx, ind in enumerate(ind_list, start=1):
        fusion_data_lst = df.iloc[fusion_raw_, start_col: end_col].values.tolist()
        ind_dict[ind] = fusion_data_lst

        random_data_lst = df.iloc[random_raw_, start_col: end_col].values.tolist()
        random_dict[ind] = random_data_lst

        start_col = start_col + COL_GAP
        end_col = start_col + GRP_COL_NUM

    return ind_dict, random_dict


if __name__ == '__main__':
    COL_GAP = 13  # 指标的间距
    GRP_COL_NUM = 10  # 一组的长度

    ind_list = ['accuracy', 'precision', 'recall', 'f1', 'kappa', 'hamming', 'jaccard']

    xl = r'/Users/wangpengcheng/PycharmProjects/MStar/绘制论文结果图/绘制结果/MStar_AlexNet/MStar-AlexNet结果汇总.xlsx'

    fusion_raw_start = 24
    random_raw_start = 21
    START_COL = 2

    main(xl, fusion_raw_=fusion_raw_start, random_raw_=random_raw_start)
