#Pandas输出Excel自适应调整宽高
#https://cloud.tencent.com/developer/article/1770494
#https://www.jianshu.com/p/a3aed25b3c28

from openpyxl.utils import get_column_letter
from pandas import ExcelWriter
import numpy as np

def to_excel_auto_column_weight(df: pd.DataFrame, writer: ExcelWriter, sheet_name):
    """DataFrame保存为excel并自动设置列宽"""
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    #  计算表头的字符宽度
    column_widths = (
        df.columns.to_series().apply(lambda x: len(x.encode('utf-8'))).values/3*2
    )
    #  计算每列的最大字符宽度
    max_widths = (
        df.astype(str).applymap(lambda x: len(x.encode('utf-8'))).agg(max).values/3*2
    )
    # 计算整体最大宽度
    widths = np.max([column_widths, max_widths], axis=0)
    # 设置列宽
    worksheet = writer.sheets[sheet_name]
    for i, width in enumerate(widths, 1):
        # openpyxl引擎设置字符宽度时会缩水0.5左右个字符，所以干脆+2使左右都空出一个字宽。
        worksheet.column_dimensions[get_column_letter(i)].width = width + 2
 
 with pd.ExcelWriter(savepath, engine='openpyxl') as writer:
     to_excel_auto_column_weight(df, writer, "sheet_name")
     
      
