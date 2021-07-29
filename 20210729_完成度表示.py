import datetime

printnum=0
maxnum=len(df)
for index,row in df.iterrows():
    #打印进度
    #A：逢10打印
    if (index+1)%10==0:
        print("\r"+datetime.datetime.now().isoformat(timespec='minutes')+"　　"+str(index+1)+"件目実行開始")
    
    #B：全部打印
    #考虑到index存在不从0开始且筛选后不连续的情况，
    #所以计算完成度时使用index而使用printnum
    printnum=printnum+1
    print("\r"+datetime.datetime.now().isoformat(timespec='minutes')+"　　"+str(index+1)+"件目実行開始（完成度："+str(round(printnum/maxnum*100,2))+"%）　　　　　　　　", end="")
   
