## Device : 머신러닝 파트 디렉토리입니다
> XGBoost 사용을 위한 파일들입니다.  

- rss_csv : 가장 최근 버전의 기계 학습에 사용되었던 csv 데이터 파일입니다.
  - rss_csv_nonzero.csv : 측정되지 않은 AP의 RSS를 -99로 채우는 방식을 사용했던 csv 데이터 파일입니다.
  - rss_csv_previous.csv : 이전 버전의 radio map을 기반으로 생성했던 csv 데이터 파일입니다.
- xgb_classifier_model_v2 : 가장 최근 버전의 기계 학습에 사용된 xgboost 모델입니다.
  - xgb_classifier_model_vnz : rss_csv_nonzero 데이터를 바탕으로 학습된 모델입니다.
  - xgb_classifier_model_v1 : rss_csv_previous 데이터를 바탕으로 학습된 모델입니다.
- xgboost_test.py : xgboost 모델을 생성하고 학습시키는 python 파일입니다.
  - 해당 파일에서 pickle 형태로 xgboost 모델을 생성합니다.
