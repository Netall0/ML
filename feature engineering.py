import pandas as pd
import os

print(os.getcwd())


def feature_engineering(df) -> pd.DataFrame:
    df.copy()

    #TODO  test cabin column 

    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

    df['Title'] = df['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())


    df['AgeBand'] = pd.cut(df['Age'], bins=[0,12,18,35,60,100],
                    labels=['Child','Teen','Adult','Middle','Senior'])
    



    return df

    
