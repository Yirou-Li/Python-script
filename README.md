# Python-script
以下是一个 Python 脚本，用于将 .xlsx 文件转换为 .txt 文件。该脚本使用 pandas 库读取 .xlsx 文件，并将其内容写入 .txt 文件。

脚本代码

import pandas as pd

def xlsx_to_txt(xlsx_file, txt_file, delimiter='\t'):
    """
    将 .xlsx 文件转换为 .txt 文件。

    参数:
        xlsx_file (str): 输入的 .xlsx 文件路径。
        txt_file (str): 输出的 .txt 文件路径。
        delimiter (str): 分隔符，默认为制表符 ('\t')。
    """
    try:
        # 读取 .xlsx 文件
        df = pd.read_excel(xlsx_file)

        # 将 DataFrame 写入 .txt 文件
        df.to_csv(txt_file, sep=delimiter, index=False, encoding='utf-8')

        print(f"转换成功！文件已保存为: {txt_file}")
    except Exception as e:
        print(f"转换失败: {e}")

# 示例用法
if __name__ == "__main__":
    xlsx_file = "CRBC_metadata.xlsx"  # 输入的 .xlsx 文件
    txt_file = "CRBC_metadata.txt"    # 输出的 .txt 文件
    xlsx_to_txt(xlsx_file, txt_file)
说明

依赖库：
需要安装 pandas 和 openpyxl 库。如果未安装，可以使用以下命令安装：
pip install pandas openpyxl
参数：
xlsx_file：输入的 .xlsx 文件路径。
txt_file：输出的 .txt 文件路径。
delimiter：分隔符，默认为制表符 (\t)。可以更改为其他符号，如逗号 (,)。
输出：
生成的 .txt 文件会包含 .xlsx 文件的所有数据，每行对应一行数据，列之间用指定的分隔符分隔。
示例：
如果 CRBC_metadata.xlsx 文件内容如下：
Name	Age	City
Alice	25	New York
Bob	30	Los Angeles
Charlie	35	Chicago
转换后的 CRBC_metadata.txt 文件内容如下：
Name    Age City
Alice   25  New York
Bob     30  Los Angeles
Charlie 35  Chicago
运行脚本

将脚本保存为 xlsx_to_txt.py。
在终端中运行脚本：
python xlsx_to_txt.py
扩展功能

指定工作表： 如果 .xlsx 文件包含多个工作表，可以指定要转换的工作表：
df = pd.read_excel(xlsx_file, sheet_name="Sheet1")  # 替换为实际工作表名称
自定义分隔符： 如果需要使用逗号作为分隔符，可以修改 delimiter 参数：
xlsx_to_txt(xlsx_file, txt_file, delimiter=',')
处理空值： 如果数据中存在空值，可以使用 na_rep 参数指定替换值：
df.to_csv(txt_file, sep=delimiter, index=False, encoding='utf-8', na_rep='N/A')
