import pandas as pd
import os

def process_file():
    header_list = ["names","price"]
    cwd = os.getcwd()
    print(cwd)
    try:
        df = pd.read_csv(cwd + "\\inputfiles\\dataset1.csv",names=header_list)
        df1 = pd.read_csv(cwd + "\\inputfiles\\dataset2.csv",names=header_list)
        df = df.dropna()
        df1 = df1.dropna()
        df2 = pd.concat([df,df1])
        df2["First Name"] = df2.apply(lambda x: x.names.split(" ")[0], axis=1)
        df2["Last Name"] = df2.apply(lambda x: x.names.split(" ")[1], axis=1)
        df2["Above_100"] = df2.apply(lambda x: 'true' if x.price > 100 else 'false', axis=1)
        df2 = df2.drop(['names'],axis=1)
        df2.to_csv(cwd + "\\outputfiles\outputdataset.csv",index=False)
    except Exception as e:
        print(e)
        exit(1)

if __name__ == '__main__':
    process_file()