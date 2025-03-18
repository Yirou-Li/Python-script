import pandas as pd
import argparse

def xlsx_to_txt(xlsx_file, txt_file, sheet_name=None, delimiter='\t'):
    """
    将 .xlsx 文件转换为 .txt 文件。

    参数:
        xlsx_file (str): 输入的 .xlsx 文件路径。
        txt_file (str): 输出的 .txt 文件路径。
        sheet_name (str): 可选，指定工作表名称。
        delimiter (str): 分隔符，默认为制表符 ('\t')。
    """
    try:
        # 读取 .xlsx 文件
        if sheet_name:
            df = pd.read_excel(xlsx_file, sheet_name=sheet_name)
        else:
            df = pd.read_excel(xlsx_file)

        # 将 DataFrame 写入 .txt 文件
        df.to_csv(txt_file, sep=delimiter, index=False, encoding='utf-8')

        print(f"转换成功！文件已保存为: {txt_file}")
    except Exception as e:
        print(f"转换失败: {e}")

def main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="将 .xlsx 文件转换为 .txt 文件")

    # 添加命令行参数
    parser.add_argument('-i', '--input', required=True, help="输入的 .xlsx 文件路径")
    parser.add_argument('-o', '--output', required=True, help="输出的 .txt 文件路径")
    parser.add_argument('-sheet', '--sheet_name', help="可选，指定工作表名称")

    # 解析命令行参数
    args = parser.parse_args()

    # 调用转换函数
    xlsx_to_txt(args.input, args.output, args.sheet_name)

if __name__ == "__main__":
    main()
