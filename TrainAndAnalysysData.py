# -*- coding: utf-8 -*-
import pandas as pd
import graphviz 
from sklearn import tree

if __name__== "__main__":
    df = pd.read_json('Train.data')
    
    Train = df[['StudentID','Gender','Test Score','Attendance Rate',
                'Midterm Score','Final Exam Score']]
    Target = df[['Ans']]
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(Train, Target)
    
    dot_data = tree.export_graphviz(clf, 
                                    out_file=None,
                                    feature_names=Train.columns.values,  
                                    class_names=['Bad','Good'],
                                    filled=True, 
                                    rounded=True,  
                                    special_characters=True) 
    graph = graphviz.Source(dot_data) 
    graph.view()