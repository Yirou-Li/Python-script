脚本说明

命令行参数：
-i 或 --input：指定输入的 .xlsx 文件路径（必需）。
-o 或 --output：指定输出的 .txt 文件路径（必需）。
-sheet 或 --sheet_name：可选，指定工作表名称（如果有多个工作表）。
功能：
如果未指定 -sheet，默认读取第一个工作表。
如果指定 -sheet，则读取指定的工作表。
分隔符：
默认使用制表符 (\t) 作为分隔符。如果需要其他分隔符（如逗号），可以修改 delimiter 参数。
使用方法

1. 安装依赖

确保已安装 pandas 和 openpyxl 库：

pip install pandas openpyxl
2. 运行脚本

将脚本保存为 xlsx_to_txt.py，然后在终端中运行：

基本用法：
python xlsx_to_txt.py -i CRBC_metadata.xlsx -o CRBC_metadata.txt
指定工作表：
python xlsx_to_txt.py -i CRBC_metadata.xlsx -o CRBC_metadata.txt -sheet Sheet2
示例

输入文件 (CRBC_metadata.xlsx)

Name	Age	City
Alice	25	New York
Bob	30	Los Angeles
Charlie	35	Chicago
运行命令

python xlsx_to_txt.py -i CRBC_metadata.xlsx -o CRBC_metadata.txt
输出文件 (CRBC_metadata.txt)

Name    Age City
Alice   25  New York
Bob     30  Los Angeles
Charlie 35  Chicago
扩展功能

自定义分隔符： 如果需要使用逗号作为分隔符，可以修改 xlsx_to_txt 函数中的 delimiter 参数：
df.to_csv(txt_file, sep=',', index=False, encoding='utf-8')
处理空值： 如果数据中存在空值，可以使用 na_rep 参数指定替换值：
df.to_csv(txt_file, sep=delimiter, index=False, encoding='utf-8', na_rep='N/A')
