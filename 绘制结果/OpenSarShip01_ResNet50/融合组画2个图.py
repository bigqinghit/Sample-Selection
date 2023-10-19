"""
颜色模型：选择CMYK而非RGB
1、top3指标组和5组随机组对比
2、融合组和平均随机组
3、平均指标组和平均随机组 -- 前40%数据
4、指标组混淆矩阵贴上
"""
import inspect
import os.path

import matplotlib.pyplot as plt

from 绘制论文结果图.my_package.row_data import get_row_data


# 在from ... import ...语句中，from后面跟着的是模块的名称（可以是一个包的相对路径），
# 而import后面跟着的是要从该模块中导入的对象（可以是变量、函数、类等）的名称。
# 例如，在上面给出的例子中，我们使用了语句from my_package.subpackage2.module2 import my_function
# 来从模块my_package.subpackage2.module2中导入名为my_function的函数


def main():
    sub_1()
    sub_2()
    # sub_3()
    # sub_4()

    plt.show()


def sub_1():
    fig, axs_2 = plt.subplots(4, 1, figsize=(10, 10))  # 返回一个图像对象fig 和 一个轴对象数组，它包含了每个子图的轴对象
    paint_sub1(axs_2)
    plt.tight_layout()
    _ = os.path.join(save_dir, f'{save_prefix}_sub1_acc_pre_rcl_f1.{img_format}')
    plt.savefig(_, format=img_format)


def sub_2():
    fig, axs_2 = plt.subplots(3, 1, figsize=(10, 10))  # 返回一个图像对象fig 和 一个轴对象数组，它包含了每个子图的轴对象
    paint_sub2(axs_2)
    plt.tight_layout()
    _ = os.path.join(save_dir, f'{save_prefix}_sub2_kp_hm_jcd.{img_format}')
    plt.savefig(_, format=img_format)


def paint_sub1(axs_: plt) -> None:
    accuracy(0, axs_)
    precision(1, axs_)
    recall(2, axs_)
    f1(3, axs_)


def paint_sub2(axs_: plt) -> None:
    kappa(0, axs_)
    hamming(1, axs_)
    jaccard(2, axs_)


def accuracy(i: int, axs: plt):
    accuracy_col = 2
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, accuracy_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, accuracy_col), xl_path=xl_path)

    x = list(range(10))
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='random')
    axs[i].legend(fontsize='medium', loc='upper left')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    min_v = 89.6
    max_v = 90.8

    axs[i].set_yticks([min_v, max_v])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在 0-100 之间
    axs[i].set_yticklabels([f'{min_v}%', f'{max_v}%'])

    axs[i].set_ylabel('accuracy(%)', fontdict={'weight': 'bold'})


def precision(i: int, axs: plt):
    precision_col = 15
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, precision_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, precision_col), xl_path=xl_path)

    x = list(range(10))
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='random')
    axs[i].legend(fontsize='medium', loc='upper left')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    min_v = 40
    max_v = 90

    axs[i].set_yticks([min_v, max_v])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在 0-100 之间
    axs[i].set_yticklabels([f'{min_v}%', f'{max_v}%'])


    axs[i].set_ylabel('precision(%)', fontdict={'weight': 'bold'})


def recall(i: int, axs: plt):
    recall_col = 28
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, recall_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, recall_col), xl_path=xl_path)

    x = list(range(10))
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='random')
    axs[i].legend(fontsize='medium', loc='upper left')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    min_v = 52
    max_v = 62

    axs[i].set_yticks([min_v, max_v])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在 0-100 之间
    axs[i].set_yticklabels([f'{min_v}%', f'{max_v}%'])
    axs[i].set_ylabel('recall(%)', fontdict={'weight': 'bold'})


def f1(i: int, axs: plt):
    f1_col = 41
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, f1_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, f1_col), xl_path=xl_path)

    x = list(range(10))
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='random')
    axs[i].legend(fontsize='medium', loc='upper left')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    min_v = 0.895
    max_v = 0.91

    axs[i].set_yticks([min_v, max_v])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在 0-100 之间
    axs[i].set_yticklabels([f'{min_v}', f'{max_v}'])

    axs[i].set_xlabel('training sample percentage', fontdict={'weight': 'bold'})
    axs[i].set_ylabel('f1', fontdict={'weight': 'bold'})


def kappa(i: int, axs: plt):
    kappa_col = 54
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, kappa_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, kappa_col), xl_path=xl_path)

    x = list(range(10))
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='random')
    axs[i].legend(fontsize='medium', loc='upper left')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i].set_yticks([0.05, 0.35])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在 0-0.25 之间
    axs[i].set_yticklabels(['0.05', '0.35'])

    axs[i].set_ylabel('kappa', fontdict={'weight': 'bold'})


def hamming(i: int, axs: plt):
    # axs[i].set_title(inspect.currentframe().f_code.co_name)

    kappa_col = 67
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, kappa_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, kappa_col), xl_path=xl_path)

    x = list(range(10))
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='random')
    axs[i].legend(fontsize='medium', loc='upper right')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i].set_yticks([0.092, 0.104])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在0-1之间
    axs[i].set_yticklabels(['0.092', '0.104'])

    # axs[i].set_xlabel('training sample percentage', fontdict={'weight': 'bold'})
    axs[i].set_ylabel('hamming', fontdict={'weight': 'bold'})


def jaccard(i: int, axs: plt):
    kappa_col = 80
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, kappa_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, kappa_col), xl_path=xl_path)

    x = list(range(10))
    axs[i].plot(x, fusion_group, color=COLOR_FUSION, label='fusion')
    axs[i].plot(x, random_avg_group, color=COLOR_RANDOM, label='random')
    axs[i].legend(fontsize='medium', loc='upper left')

    axs[i].set_xticks(x)
    axs[i].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i].set_yticks([0.81, 0.835])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在 0-0.2 之间
    axs[i].set_yticklabels(['0.81', '0.835'])

    axs[i].set_xlabel('training sample percentage', fontdict={'weight': 'bold'})
    axs[i].set_ylabel('jaccard', fontdict={'weight': 'bold'})


if __name__ == '__main__':
    COLOR_FUSION = (216, 56, 58)
    COLOR_RANDOM = (30, 30, 32)

    COLOR_FUSION = [i / 255 for i in COLOR_FUSION]
    COLOR_RANDOM = [i / 255 for i in COLOR_RANDOM]

    idctor_lst = ['accuracy', 'precision', 'recall', 'f1', 'kappa', 'haiming', 'jaccard']
    FUSION_RAW = 38
    RANDOM_RAW = 19

    fig_title = r'OpenSarShip01_ResNet50'

    save_prefix = 'OpenSarShip01_ResNet50_Fusion_vs_Random_'

    root = r'/Users/wangpengcheng/PycharmProjects/MStar/绘制论文结果图/绘制结果/OpenSarShip01_ResNet50'
    f = r'OpenSarShip01_resnet50_结果汇总.xlsx'
    save_dir = os.path.join(root, '结果图')

    img_format = 'png'

    xl_path = os.path.join(root, f)
    main()
