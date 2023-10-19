
import inspect
import os.path

import matplotlib.pyplot as plt

from 绘制论文结果图.my_package.row_data import get_row_data


def main():
    sub_1()
    sub_2()
    sub_3()
    sub_4()

    plt.show()


def sub_1():
    fig, axs_2 = plt.subplots(2, 1, figsize=(10, 10))  # 返回一个图像对象fig 和 一个轴对象数组，它包含了每个子图的轴对象
    paint_sub1(axs_2)
    plt.tight_layout()
    _ = os.path.join(save_dir, f'{save_prefix}_sub1_acc_pre.{img_format}')
    plt.savefig(_, format=img_format)


def sub_2():
    fig, axs_2 = plt.subplots(2, 1, figsize=(10, 10))  # 返回一个图像对象fig 和 一个轴对象数组，它包含了每个子图的轴对象
    paint_sub2(axs_2)
    plt.tight_layout()
    _ = os.path.join(save_dir, f'{save_prefix}_sub2_rcl_f1.{img_format}')
    plt.savefig(_, format=img_format)


def sub_3():
    fig, axs_3 = plt.subplots(2, 1, figsize=(10, 10))  # 返回一个图像对象fig 和 一个轴对象数组，它包含了每个子图的轴对象
    paint_sub3(axs_3)
    plt.tight_layout()
    _ = os.path.join(save_dir, f'{save_prefix}_sub3_kap_hm.{img_format}')
    plt.savefig(_, format=img_format)


def sub_4():
    fig, axs_4 = plt.subplots(1, 1, figsize=(8, 5))  # 返回一个图像对象fig 和 一个轴对象数组，它包含了每个子图的轴对象
    paint_sub4(axs_4)
    plt.tight_layout()
    _ = os.path.join(save_dir, f'{save_prefix}_sub4_jcd.{img_format}')
    plt.savefig(_, format=img_format)


def paint_sub1(axs_: plt) -> None:
    accuracy(0, axs_)
    precision(1, axs_)


def paint_sub2(axs_: plt) -> None:
    recall(0, axs_)
    f1(1, axs_)


def paint_sub3(axs_: plt) -> None:
    kappa(0, axs_)
    hamming(1, axs_)


def paint_sub4(axs_: plt) -> None:
    jaccard(axs_)


def accuracy(i: int, axs: plt):
    accuracy_col = 2
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, accuracy_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, accuracy_col), xl_path=xl_path)

    x = list(range(10))
    # axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='Reinforcement Learning')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='Random')
    axs[i].legend(fontsize='medium', loc='upper left')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    min_v = 19
    max_v = 94

    axs[i].set_yticks([min_v, max_v])  # 设置纵坐标刻度的位置  -- 单位为1
    axs[i].set_yticklabels([f'{min_v}%', f'{max_v}%'])  # 在 0-100 之间

    axs[i].set_ylabel('accuracy(%)', fontdict={'weight': 'bold'})


def precision(i: int, axs: plt):
    precision_col = 15
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, precision_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, precision_col), xl_path=xl_path)

    x = list(range(10))
    # axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='Reinforcement Learning')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='Random')
    axs[i].legend(fontsize='medium', loc='upper left')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    min_v = 12
    max_v = 94
    axs[i].set_yticks([min_v, max_v])  # 设置纵坐标刻度的位置  -- 单位为1
    axs[i].set_yticklabels([f'{min_v}%', f'{max_v}%'])  # 在 0-100 之间

    axs[i].set_xlabel('training sample percentage', fontdict={'weight': 'bold'})
    axs[i].set_ylabel('precision(%)', fontdict={'weight': 'bold'})


def recall(i: int, axs: plt):
    recall_col = 28
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, recall_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, recall_col), xl_path=xl_path)

    x = list(range(10))
    # axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='Reinforcement Learning')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='Random')
    axs[i].legend(fontsize='medium', loc='upper left')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    min_v = 18
    max_v = 94

    axs[i].set_yticks([min_v, max_v])  # 设置纵坐标刻度的位置  -- 单位为1
    axs[i].set_yticklabels([f'{min_v}%', f'{max_v}%'])  # 在 0-100 之间

    axs[i].set_ylabel('recall(%)', fontdict={'weight': 'bold'})


def f1(i: int, axs: plt):
    f1_col = 41
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, f1_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, f1_col), xl_path=xl_path)

    x = list(range(10))
    # axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='Reinforcement Learning')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='Random')
    axs[i].legend(fontsize='medium', loc='upper left')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i].set_yticks([0, 0.5, 1])  # 设置纵坐标刻度的位置 -- 单位为1
    # 在 0-0.25 之间
    axs[i].set_yticklabels(['0', '0.125', '0.25'])

    axs[i].set_xlabel('training sample percentage', fontdict={'weight': 'bold'})
    axs[i].set_ylabel('f1', fontdict={'weight': 'bold'})


def kappa(i: int, axs: plt):
    kappa_col = 54
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, kappa_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, kappa_col), xl_path=xl_path)

    x = list(range(10))
    # axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='Reinforcement Learning')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='Random')
    # axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='random')
    axs[i].legend(fontsize='medium', loc='upper left')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i].set_yticks([0, 0.5, 1])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在 0-0.25 之间
    axs[i].set_yticklabels(['0', '0.1', '0.2'])

    axs[i].set_ylabel('kappa', fontdict={'weight': 'bold'})


def hamming(i: int, axs: plt):
    kappa_col = 67
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, kappa_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, kappa_col), xl_path=xl_path)

    x = list(range(10))
    # axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='Reinforcement Learning')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='Random')
    axs[i].legend(fontsize='medium', loc='upper right')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i].set_yticks([0, 0.5, 1])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在0-1之间
    axs[i].set_yticklabels(['0', '0.5', '1'])

    axs[i].set_xlabel('training sample percentage', fontdict={'weight': 'bold'})
    axs[i].set_ylabel('hamming', fontdict={'weight': 'bold'})


def jaccard(axs: plt):
    kappa_col = 80
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, kappa_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, kappa_col), xl_path=xl_path)

    x = list(range(10))
    # axs.plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs.plot(x, fusion_group, color=COLOR_FUSION, label='Reinforcement Learning')
    axs.plot(x, random_avg_group, color=COLOR_RANDOM, label='Random')
    axs.legend(fontsize='medium', loc='upper left')

    axs.set_xticks(x)
    axs.set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs.set_yticks([0, 0.5, 1])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在 0-0.2 之间
    axs.set_yticklabels(['0', '0.1', '0.2'])

    axs.set_xlabel('training sample percentage', fontdict={'weight': 'bold'})
    axs.set_ylabel('jaccard', fontdict={'weight': 'bold'})


if __name__ == '__main__':
    COLOR_FUSION = (216, 56, 58)
    COLOR_RANDOM = (30, 30, 32)

    COLOR_FUSION = [i / 255 for i in COLOR_FUSION]
    COLOR_RANDOM = [i / 255 for i in COLOR_RANDOM]

    FUSION_RAW = 24
    RANDOM_RAW = 21

    # 保存的图像名字
    save_prefix = 'MStar_AlexNet_RL_vs_Random_'

    # fig_title = r'MStar_AlexNet'

    root = r'/Users/wangpengcheng/PycharmProjects/MStar/绘制论文结果图/绘制结果/MStar_AlexNet'
    f = r'MStar-AlexNet结果汇总.xlsx'
    save_dir = os.path.join(root, '结果图')

    img_format = 'png'

    xl_path = os.path.join(root, f)
    main()
