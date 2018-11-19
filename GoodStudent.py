# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 09:09:53 2018

@author: a6050
"""

import pandas as pd
import numpy as np

def GenerateSchoolDatasets():
    df = pd.DataFrame({
            'StudentID':pd.Series(range(100), index=list(range(100)),dtype='int32'),
            'Gender':np.random.randint(0,2,100),
            'Test Score':np.random.randint(0,101,100),
            'Midterm Score':np.random.randint(0,101,100),
            'Final Exam Score':np.random.randint(0,101,100),
            'Attendance Rate':np.random.random(100)
            })
    return df
    
if __name__== "__main__":
    df = GenerateSchoolDatasets()