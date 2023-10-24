import pandas as pd
import load_utility as ut
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, multilabel_confusion_matrix
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from xgboost import plot_importance

def print_result(result):
    result = str(result[0])

    if(len(result) == 1):
        print('(0, ' + result[0] + ')')
    if(len(result) == 2):
        print('(' + result[0] + ',' + result[1] + ')')
    if(len(result) == 3):
        if(result[0] == 1):
            print('(' + result[0] + result[1] + ',' + result[2] + ')')
        else:
            print('(' + result[0] + ',' + result[1] + result[2] + ')')
    if(len(result) == 4):
        print('(' + result[0] + result[1] + ',' + result[2] + result[3] + ')')

df = pd.read_csv('rss_csv.csv')
X = df.iloc[:, :107] # RSS 값
Y = df['result'] # 레이블 값
ap_list = ut.load_ap_list()

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=39)
encoder = LabelEncoder()
y_train = encoder.fit_transform(y_train) # 그대로 레이블 값을 사용할 수 없다. 정수 값으로 Encoding 필요
y_test = encoder.fit_transform(y_test)

"""
XGBoost 모델 선언
1. n_estimators : 학습 모델의 수 높을 수록 성능 향상의 가능성 높아지나, 속도 저하 위험
2. learning_rate : alpha 계수, 너무 크면 gradient 발산 가능성, 너무 작으면 학습 속도 느림
3. max_depth : 최대 탐색 깊이, 너무 깊으면 과적합 가능성, 너무 얕으면 일반화 불가
4. min_samples_split : 분할 종료 최소 샘플 수(Early stopping), 크면 과적합 방지, 학습 저하 가능성
5. min_samples_leaf : 단말의 최소 샘플 수, 위와 유사
6. random_state : 시드 값
"""
xgb_classifier = XGBClassifier(
    n_estimator = 400,
    learning_rate = 0.1,
    early_stopping_rounds = 10,
    eval_metric=['merror', 'mlogloss', 'auc'],
    random_state=42,
    objective="multi:softmax")

xgb_classifier.fit(x_train, y_train, verbose=1, eval_set=[(x_train, y_train), (x_test, y_test)])
y_pred = xgb_classifier.predict(x_test)
y_pred_train = xgb_classifier.predict(x_train)
print("Learning finished!! Accuracy : ", accuracy_score(y_pred, y_test))
print("Learning finished!! Accuracy : ", accuracy_score(y_pred_train, y_train))
#conmat = confusion_matrix(y_pred, y_test)
#plt.figure(figsize=(10, 8))
#sns.heatmap(conmat, annot=True, fmt='d', cmap='Reds')

"""
results = xgb_classifier.evals_result()
epoch = len(results['validation_0']['auc'])
x_axis = range(0, epoch)

fig, ax = plt.subplots(figsize = (9, 5))
ax.plot(x_axis, results['validation_0']['mlogloss'], label="Train")
ax.plot(x_axis, results['validation_1']['mlogloss'], label = "Test")
ax.legend()

plt.ylabel('Logloss')
plt.title('XGBoost Logloss')
plt.show()
"""

fig, ax = plt.subplots(figsize=(10,15))
plot_importance(xgb_classifier, ax=ax)
plt.show()