# DecisionTree
Project2 DecisionTree

# 簡介
1. 設計一個可以區分優秀學生的資料集，透過產生器產生100個學生資料
2. 使用Decision tree 建立一個分類模型
3. 分析與比較

# 1.資料產生
    GenerateData.py 產生 Train.data(json格式)
- 'StudentID':學生ID，每筆資料獨立
- 'Gender':學生性別，0為男生，1為女生
- 'Test Score':小考平均成績，所有學生成績以70為中心點取標準差為10的常態分布資料
- 'Attendance Rate':出席率，平均分布
- 'Midterm Score':期中成績，平均分布
- 'Final Exam Score':期末成績，平均分布
---
- 'Ans':設定0為壞學生，1為好學生
    - 取30% Test Score
    - 取30% Midterm Score
    - 取30% Final Exam Score
    - 取10% Attendance Rate
    - 上述加總成績超過60分設定為好學生
---
![產生資料](https://github.com/a60504a60504/DecisionTree/blob/master/Pictures/df.PNG)

# 2. Decision Tree 訓練
    TrainAndAnalysysData.py 產生 Source.gv.pdf(DecisionTree圖)
![DecisionTree](https://github.com/a60504a60504/DecisionTree/blob/master/Pictures/DecisionTree.PNG)

# 3. 分析結果

* 根據Decision Tree分類
* 好學生:
    * 期末成績<=59.5\t  55.5<期中成績<=82.5     小考平均<=76.5
        * 結果[0 59.5]*0.3+[55.5 82.5]*0.3+[0 76.5]*0.3+[0 100]*0.1=[16.65 75.55]
    * 期末成績<=24      期中成績>82.5           小考平均>82.5
        * 結果[0 59.5]*0.3+[55.5 82.5]*0.3+[0 76.5]*0.3+[0 100]*0.1=[16.65 75.55]
    * 期末成績>24       期中成績>82.5
    * 期末成績>59.5     期中成績>26             小考平均<=54        學生ID>11.5
    * 期末成績>59.5     期中成績>26             小考平均>54
* 壞學生:
    * 期末成績<=59.5    期中成績<=82.5          小考平均<=76.5
    * 期末成績<=59.5    期中成績<=55.5          小考平均<=76.5
    * 期末成績<=24      期中成績>82.5           小考平均<=82.5
    * 期末成績>59.5     期中成績<=26
    * 期末成績>59.5     期中成績>26             小考平均<=54        學生ID<=11.5
