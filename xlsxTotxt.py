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

