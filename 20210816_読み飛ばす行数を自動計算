def skiprows_count(input_file,col_name,read_sheet):
    #input_file 读取文件路径
    #col_name 用来识别是否是列名的字段
    #read_sheet 要读取的sheet名

    skiprows=0
    df=pd.read_excel(input_file,skiprows=skiprows,sheet_name=read_sheet).fillna("-")
    
    if col_name in df.columns.values.tolist(): 
        pass

    else: 
        for index,row in df.iterrows(): 
            if col_name in row.values.tolist(): 
                skiprows=index+1 
            break
            
    return skiprows 
    
df=pd.read_excel(file_path,skiprows=skiprows_count(file_path,"月份","汇总"),sheet_name="汇总").fillna("-") 

df
