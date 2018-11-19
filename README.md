# DecisionTree
Project2 DecisionTree

# 簡介
1. 設計一個可以區分優秀學生的資料集，透過產生器產生100個學生資料
2. 使用Decision tree 建立一個分類模型
3. 分析與比較

# 1.資料產生
    GenerateData.py
'StudentID':學生ID，每筆資料獨立
'Gender':學生性別，0為男生，1為女生
'Test Score':小考平均成績，所有學生成績以70為中心點取標準差為10的常態分布資料
'Attendance Rate':出席率，平均分布
'Midterm Score':期中成績，平均分布
'Final Exam Score':期末成績，平均分布

'Ans':設定0為壞學生，1為好學生
      取30% Test Score
        30% Midterm Score
        30% Final Exam Score
        10% Attendance Rate
 
 # 2. Decision Tree 訓練
    TrainAndAnalysysData.py
 ![image](picture or gif url)
