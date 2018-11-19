# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

N = 100

def GenerateSchoolDatasets():
    df = pd.DataFrame({
            'StudentID':pd.Series(range(N), index=list(range(N)),dtype='int32'),
            'Gender':np.random.randint(0,2,N),
            'Test Score':np.random.normal(loc=70, scale=10, size=N).astype(int),
            'Midterm Score':np.random.randint(0,101,N),
            'Final Exam Score':np.random.randint(0,101,N),
            'Attendance Rate':(np.random.random(N)*100).astype(int)
            })
    df['Ans']=[1 if df['Test Score'][i]*0.3 +
                    df['Midterm Score'][i]*0.3 +
                    df['Final Exam Score'][i]*0.3 +
                    df['Attendance Rate'][i]*0.1 > 60 
                 else 0 
                 for i in range(N)]
    return df
    
if __name__== "__main__":
    Train = GenerateSchoolDatasets()
    
    Train.to_json(path_or_buf='Train.data')
    