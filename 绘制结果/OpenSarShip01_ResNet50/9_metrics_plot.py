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
            metrics_dict_=metrics_dict, random_lst_=random_avg_lst, save_img_name=metric
        )
        col += ROW_GROUP_INTERVAL


def draw_chart_9_metrics_random(metrics_dict_: dict, random_lst_: list, save_img_name: str) -> None:
    """
    画9个指标和随机组的折线，并最后保存为tiff格式的文件
    :param metrics_dict_: 指标组的字典形式数据
    :param random_lst_: 随机组的数据
    :param save_img_name: 保存图片的名称
    """
    x = ['5%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%']

    font_size = 'small'
    fig, axs = plt.subplots(3, 1, figsize=(10, 10))  # 设置图像大小
    fig.suptitle(save_img_name, fontsize=16, fontweight='bold')  # 图像的子标题
    fig.subplots_adjust(left=0.08, right=0.92, bottom=0.08, top=0.92)

    for ax in axs:
        if save_img_name in {'accuracy', 'precision', 'recall'}:
            ax.set_ylabel(f'{save_img_name}(%)')
        else:
            ax.set_ylabel(save_img_name)

    # axs[2].set_xlabel('training sample percentage(%)')
    axs[2].set_xlabel('training sample percentage')

    color_lst = [
        (40, 120, 181),
        (191, 115, 52),
        (255, 136, 132),
        (98, 76, 124)
    ]

    color_lst = [[_ / 255 for _ in i] for i in color_lst]
    line_1, line_2, line_3, random_color = color_lst

    metrics = [
        ['Brenner', 'Vollath', 'variance'],
        ['SMD2', 'SMD', 'entropy'],
        ['energy', 'contrast', 'Laplacian']
    ]

    for sub_plot_idx in range(len(metrics)):
        for metric_idx in range(len(metrics[0])):
            metric = metrics[sub_plot_idx][metric_idx]
            axs[sub_plot_idx].plot(x, metrics_dict_[metric],
                                   color=color_lst[metric_idx], label=metric)

        axs[sub_plot_idx].plot(x, random_lst_, color=random_color, label='random_avg', linestyle='--')
        pos = 'upper right' if save_img_name == 'hamming' else 'upper left'
        axs[sub_plot_idx].legend(loc=pos, fontsize=font_size)

    save_prefix = r'OpenSarShip01_ResNet50_'
    plt.savefig(f'{os.path.join(excel_folder, img_save_dir, save_prefix + save_img_name)}.{img_format}',
                format=img_format)
    plt.show()


if __name__ == '__main__':
    ROW_GROUP_INTERVAL = 13  # 指标表格中行的组间隔

    excel_folder = r'/Users/wangpengcheng/PycharmProjects/MStar/绘制论文结果图/绘制结果/OpenSarShip01_ResNet50'
    f_xl = 'OpenSarShip01_resnet50_结果汇总.xlsx'
    xl_abs_path = os.path.join(excel_folder, f_xl)

    img_save_dir = r'结果图'
    # metric_lst = ['Brenner', 'Vollath', 'variance', 'SMD2', 'SMD', 'entropy', 'energy', 'contrast', 'Laplacian']

    img_format = 'png'
    main(xl_path=xl_abs_path, initial_row_column_count=(3, 2), random_avg_raw=19)
