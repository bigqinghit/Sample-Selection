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
    fig, axs = plt.subplots(4, 2)  # 返回一个图像对象fig 和 一个轴对象数组，它包含了每个子图的轴对象
    fig.suptitle('OpenSarShip01_ResNet50')

    paint(axs)
    plt.tight_layout()

    plt.savefig('融合组与随机组对比.tiff', format='tiff')
    plt.show()


def paint(axs_: plt) -> None:
    accuracy(0, 0, axs_)
    precision(0, 1, axs_)
    recall(1, 0, axs_)
    f1(1, 1, axs_)
    kappa(2, 0, axs_)
    haiming(2, 1, axs_)
    jaccard(3, 0, axs_)


def accuracy(i: int, j: int, axs: plt):
    axs[i, j].set_title(inspect.currentframe().f_code.co_name)

    accuracy_col = 2
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, accuracy_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, accuracy_col), xl_path=xl_path)

    x = list(range(10))
    axs[i, j].plot(x, fusion_group, color='r', label='fusion')
    axs[i, j].plot(x, random_avg_group, color='k', label='random')
    axs[i, j].legend(fontsize='small')

    axs[i, j].set_xticks(x)
    axs[i, j].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i, j].set_yticks([89.6, 90.8])  # 设置纵坐标刻度的位置  -- 值域显示范围
    # 在 0-100 之间
    axs[i, j].set_yticklabels(['89.6%', '90.8%'])


def precision(i: int, j: int, axs: plt):
    axs[i, j].set_title(inspect.currentframe().f_code.co_name)

    precision_col = 15
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, precision_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, precision_col), xl_path=xl_path)

    x = list(range(10))
    axs[i, j].plot(x, fusion_group, color='r', label='fusion')
    axs[i, j].plot(x, random_avg_group, color='k', label='random')
    axs[i, j].legend(fontsize='small')

    axs[i, j].set_xticks(x)
    axs[i, j].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i, j].set_yticks([50, 90])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在 0-100 之间
    axs[i, j].set_yticklabels(['50%', '90%'])


def recall(i: int, j: int, axs: plt):
    axs[i, j].set_title(inspect.currentframe().f_code.co_name)

    recall_col = 28
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, recall_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, recall_col), xl_path=xl_path)

    x = list(range(10))
    axs[i, j].plot(x, fusion_group, color='r', label='fusion')
    axs[i, j].plot(x, random_avg_group, color='k', label='random')
    axs[i, j].legend(fontsize='small')

    axs[i, j].set_xticks(x)
    axs[i, j].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i, j].set_yticks([52, 62])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在 0-100 之间
    axs[i, j].set_yticklabels(['52%', '62%'])


def f1(i: int, j: int, axs: plt):
    axs[i, j].set_title(inspect.currentframe().f_code.co_name)

    f1_col = 41
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, f1_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, f1_col), xl_path=xl_path)

    x = list(range(10))
    axs[i, j].plot(x, fusion_group, color='r', label='fusion')
    axs[i, j].plot(x, random_avg_group, color='k', label='random')
    axs[i, j].legend(fontsize='small')

    axs[i, j].set_xticks(x)
    axs[i, j].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i, j].set_yticks([0.896, 0.908])  # 设置纵坐标刻度的位置 -- 单位为1
    # 在 0-0.25 之间
    axs[i, j].set_yticklabels(['0.896', '0.908'])


def kappa(i: int, j: int, axs: plt):
    axs[i, j].set_title(inspect.currentframe().f_code.co_name)

    kappa_col = 54
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, kappa_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, kappa_col), xl_path=xl_path)

    x = list(range(10))
    axs[i, j].plot(x, fusion_group, color='r', label='fusion')
    axs[i, j].plot(x, random_avg_group, color='k', label='random')
    axs[i, j].legend(fontsize='small')

    axs[i, j].set_xticks(x)
    axs[i, j].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i, j].set_yticks([0.05, 0.35])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在 0-0.25 之间
    axs[i, j].set_yticklabels(['0.05', '0.35'])


def haiming(i: int, j: int, axs: plt):
    axs[i, j].set_title(inspect.currentframe().f_code.co_name)

    kappa_col = 67
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, kappa_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, kappa_col), xl_path=xl_path)

    x = list(range(10))
    axs[i, j].plot(x, fusion_group, color='r', label='fusion')
    axs[i, j].plot(x, random_avg_group, color='k', label='random')
    axs[i, j].legend(fontsize='small')

    axs[i, j].set_xticks(x)
    axs[i, j].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i, j].set_yticks([0.092, 0.104])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在0-1之间
    axs[i, j].set_yticklabels(['0.092', '0.104'])


def jaccard(i: int, j: int, axs: plt):
    axs[i, j].set_title(inspect.currentframe().f_code.co_name)

    kappa_col = 80
    fusion_group = get_row_data(start_raw_col=(FUSION_RAW, kappa_col), xl_path=xl_path)
    random_avg_group = get_row_data(start_raw_col=(RANDOM_RAW, kappa_col), xl_path=xl_path)

    x = list(range(10))
    axs[i, j].plot(x, fusion_group, color='r', label='fusion')
    axs[i, j].plot(x, random_avg_group, color='k', label='random')
    axs[i, j].legend(fontsize='small')

    axs[i, j].set_xticks(x)
    axs[i, j].set_xticklabels(['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])

    axs[i, j].set_yticks([0.81, 0.835])  # 设置纵坐标刻度的位置  -- 单位为1
    # 在 0-0.2 之间
    axs[i, j].set_yticklabels(['0.81', '0.835'])


if __name__ == '__main__':
    idctor_lst = ['accuracy', 'precision', 'recall', 'f1', 'kappa', 'haiming', 'jaccard']
    FUSION_RAW = 38
    RANDOM_RAW = 19

    root = r'/Users/wangpengcheng/PycharmProjects/MStar/绘制论文结果图/绘制结果/OpenSarShip01_ResNet50'
    f = r'OpenSarShip01_resnet50_结果汇总.xlsx'

    xl_path = os.path.join(root, f)
    main()
