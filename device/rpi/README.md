## Device : Raspberry pi 파일 디렉토리입니다.
> 실제로 Raspberry pi에서 동작하는 로직들이 들어간 파일입니다.
> Raspberry pi에서 위치를 추정할 때 관여하는 모든 파일을 보관합니다.

- rss-setup.py : radio map을 구성할 때, 제자리에서 다회의 측정을 하는 코드입니다.
- rss-realtime.py : 실시간으로 사용자가 RSS 값을 측정하여 서버로 전송하는 코드입니다.
  - 실시간으로 측정과 동시에 위치 계산이 진행됩니다.
  - 그 방식은 ```1NN Algorithm + 실시간 Queueing``` 방식입니다.
- load_utility.py : 파일을 불러오거나 계산에 사용되는 모듈입니다.
  - radio map과 ap list를 불러올 수 있습니다.
  - 사용자의 위치를 계산하는 함수가 포함되어 있습니다.
- clientQueue.py : 실시간 Queueing에 사용되는 Queue 모듈입니다.
- realtime_test_basic.py : 최초에 ```1NN Algorithm```만을 사용했던 코드입니다.
- rss-realtime_queuever.py : 실시간 전송이 아닌 ```누적 계산``` 방식을 사용했던 코드입니다.
- rss-realtime-xgboost.py : 머신러닝(XGBoost)을 이용한 위치 추정 코드입니다.
  - 실시간으로 측정된 RSS 값을 가공하여 Python 서버로 전송합니다.
  - 응답으로 받은 위치를 Springboot 서버로 재전송합니다.
- file_tokenize.py : 데이터 전처리 및 가공 코드입니다.
  - 실시간으로 측정된 RSS 값을 계산에 용이하게 가공합니다.
  - 계산된 위치를 서버로 전송하기 위해 가공합니다.
- file_tokenize_queuever.py : 실시간 전송이 아닌 ```누적 계산``` 방식을 위해 사용했던 코드입니다.
- uniqueCode.txt : 기기 기반 인증을 위해 고유 코드를 입력받는 파일입니다.
