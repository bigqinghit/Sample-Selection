import os

import matplotlib.pyplot as plt

from 绘制论文结果图.my_package.get_9metrics_data import get_9_metrics
from 绘制论文结果图.my_package.row_data import get_row_data


def main(xl_path: str, initial_row_column_count: tuple, random_avg_raw: int) -> None:
    """
    获取表中9个指标的数据并画图，最后保存图片为tiff格式
    :param random_avg_raw: 随机组的行数
    :param xl_path: xl表的绝对路径
    :param initial_row_column_count: 初始的行列数
    :return:
    """
    raw, col = initial_row_column_count
    evaluation_metrics_lst = ['accuracy', 'precision', 'recall', 'f1', 'kappa', 'hamming', 'jaccard']

    for metric in evaluation_metrics_lst:
        # 9个指标，以字典形式返回
        metrics_dict = get_9_metrics(start_raw_col=(raw, col), excel_file_path=xl_path)
        random_avg_lst = get_row_data(start_raw_col=(random_avg_raw, col), xl_path=xl_path)

        draw_chart_9_metrics_random(
            metrics_data_dict=metrics_dict, random_lst_=random_avg_lst, save_img_name=metric
        )
        col += ROW_GROUP_INTERVAL


def draw_chart_9_metrics_random(metrics_data_dict: dict, random_lst_: list, save_img_name: str) -> None:
    """
    画9个指标和随机组的折线，并最后保存为tiff格式的文件
    :param metrics_data_dict: 指标组的字典形式数据
    :param random_lst_: 随机组的数据
    :param save_img_name: 保存图片的名称
    """

    x = ['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%']

    font_size = 'small'
    fig, axs = plt.subplots(3, 1, figsize=(10, 10))  # 设置保存的图像大小
    fig.suptitle(save_img_name, fontsize=16, fontweight='bold')  # 图像的子标题
    # fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
    fig.subplots_adjust(left=0.08, right=0.92, bottom=0.08, top=0.92)

    for ax in axs:
        if save_img_name in {'accuracy', 'precision', 'recall'}:
            ax.set_ylabel(f'{save_img_name}(%)')
        else:
            ax.set_ylabel(save_img_name)

    # axs[2].set_xlabel('training sample percentage(%)')
    axs[2].set_xlabel('training sample percentage')

    #           蓝色          淡蓝              粉色              淡紫色
    colors = [(40, 120, 181),
              (191, 115, 52),
              (255, 136, 132),
              (98, 76, 124)]
    colors = [[_ / 255 for _ in color] for color in colors]
    line_1, line_2, line_3, random_color = colors

    metrics = [['Brenner', 'Vollath', 'variance'],
               ['SMD2', 'SMD', 'entropy'],
               ['energy', 'contrast', 'Laplacian']]

    for i in range(3):
        for j in range(3):
            axs[i].plot(x, metrics_data_dict[metrics[i][j]], color=colors[j], label=metrics[i][j])

        axs[i].plot(x, random_lst_, color=random_color, label='random_avg', linestyle='--')

        if save_img_name == 'hamming':
            axs[i].legend(loc='upper right', fontsize=font_size)
        else:
            axs[i].legend(loc='upper left', fontsize=font_size)

    save_prefix = r'MStar_AlexNet_'
    # plt.savefig(f'{os.path.join(excel_folder, img_save_dir, save_prefix + save_img_name)}.tiff', format='tiff')
    plt.savefig(f'{os.path.join(excel_folder, img_save_dir, save_prefix + save_img_name)}.png', format='png')
    plt.show()


if __name__ == '__main__':
    ROW_GROUP_INTERVAL = 13  # 指标表格中行的组间隔

    random_avg_raw_ = 21  # 平均随机在哪一行

    excel_folder = r'/Users/wangpengcheng/PycharmProjects/MStar/绘制论文结果图/绘制结果/MStar_AlexNet'
    f_xl = 'MStar-AlexNet结果汇总.xlsx'
    xl_abs_path = os.path.join(excel_folder, f_xl)

    img_save_dir = r'结果图'

    main(xl_path=xl_abs_path, initial_row_column_count=(3, 2), random_avg_raw=random_avg_raw_)
