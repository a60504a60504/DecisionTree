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
    * 期末[0 59.5]*0.3+期中[55.5 82.5]*0.3+小考[0 76.5]*0.3+出席[0 100]*0.1=[16.65 75.55]
        * 誤判率:(60-16.65)/(75.55-16.65)=74%
        * 進入此狀態發生機率:(59.5%)*(82.5%)*(1-76.5%)*(1-55.5%)=5%
        * 期末成績<=59.5    
        * 55.5<期中成績<=82.5     
        * 小考平均<=76.5
    * 期末[0 24]*0.3+期中[82.5 100]*0.3+小考[82.5 100]*0.3+出席[0 100]*0.1=[49.5 77.2]
        * 誤判率:(60-49.5)/(77.2-49.5)=38%
        * 進入此狀態發生機率:(59.5%)*(1-82.5%)*(24%)*(1-82.5%)=0.4%
        * 期末成績<=24      
        * 期中成績>82.5           
        * 小考平均>82.5
    * 期末[24 59.5]*0.3+期中[82.5 100]*0.3+小考[0 100]*0.3+出席[0 100]*0.1=[31.95 87.85]
        * 誤判率:(60-31.95)/(87.85-31.95)=50%
        * 進入此狀態發生機率:(59.5%)*(1-82.5%)*(1-24%)=8%
        * 24<期末成績<=59.5       
        * 期中成績>82.5
    * 期末[59.5 100]*0.3+期中[26 100]*0.3+小考[0 54]*0.3+出席[0 100]*0.1=[25.65 86.2]
        * 誤判率:(60-25.65)/(86.2-25.65)=57%
        * 進入此狀態發生機率:(1-59.5%)*(1-26%)*(54%)*(1-11.5%)=14%
        * 期末成績>59.5     
        * 期中成績>26             
        * 小考平均<=54        
        * 學生ID>11.5
    * 期末[59.5 100]*0.3+期中[26 100]*0.3+小考[54 100]*0.3+出席[0 100]*0.1=[41.85 100]
        * 誤判率:(60-41.85)/(100-41.85)=31%
        * 進入此狀態發生機率:(1-59.5%)*(1-26%)*(1-54%)=14%
        * 期末成績>59.5     
        * 期中成績>26             
        * 小考平均>54
* 壞學生:
    * 期末[0 59.5]*0.3+期中[0 82.5]*0.3+小考[0 76.5]*0.3+出席[0 100]*0.1=[0 75.55]
        * 誤判率:(75.55-60)/(75.55-0)=21%
        * 進入此狀態發生機率:(59.5%)*(82.5%)*(76.5%)=38%
        * 期末成績<=59.5    
        * 期中成績<=82.5          
        * 小考平均<=76.5
    * 期末[0 59.5]*0.3+期中[0 55.5]*0.3+小考[0 76.5]*0.3+出席[0 100]*0.1=[0 67.45]
        * 誤判率:(67.45-60)/(67.45-0)=11%
        * 進入此狀態發生機率:(59.5%)*(82.5%)*(1-76.5%)*(55.5%)=6%
        * 期末成績<=59.5    
        * 期中成績<=55.5          
        * 小考平均<=76.5
    * 期末[0 24]*0.3+期中[82.5 100]*0.3+小考[0 82.5]*0.3+出席[0 100]*0.1=[24.75 71.95]
        * 誤判率:(71.95-60)/(71.95-24.75)=25%
        * 進入此狀態發生機率:(59.5%)*(1-82.5%)*(24%)*(82.5%)=2%
        * 期末成績<=24      
        * 期中成績>82.5           
        * 小考平均<=82.5
    * 期末[59.5 100]*0.3+期中[0 26]*0.3+小考[0 100]*0.3+出席[0 100]*0.1=[17.85 77.8]
        * 誤判率:(77.8-60)/(77.8-17.85)=30%
        * 進入此狀態發生機率:(1-59.5%)*(26%)=10%
        * 期末成績>59.5     
        * 期中成績<=26
    * 期末[59.5 100]*0.3+期中[26 100]*0.3+小考[0 54]*0.3+出席[0 100]*0.1=[25.65 86.2]
        * 誤判率:(86.2-60)/(86.2-25.65)=43%
        * 進入此狀態發生機率:(1-59.5%)*(1-26%)*(54%)*(11.5%)=2%
        * 期末成績>59.5     
        * 期中成績>26             
        * 小考平均<=54        
        * 學生ID<=11.5
* **綜合誤判率:33%**
# 4. 討論
* 誤判率3成，很有可能是因為資料量不足的關係，如果加大學生資料N，可能可以降低誤判率
* 觀察到Decision Tree可能會把學生ID及性別納入分類依據，而造成overfit，如果要解決overfit問題可以考慮先把不必要的欄位做刪除加快速度並增加準確度。
