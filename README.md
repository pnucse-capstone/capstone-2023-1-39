### 1. 프로젝트 소개

# WMI, Where am I?
> __무선 네트워크 기술을 활용한 사용자 인증 및 자원 통합 관리 플랫폼__ 입니다.  
> 부산대학교 김태운 교수님의 지도로 진행되며, 김태운 교수님의 자료를 참고합니다.  
 
<br>  
<p align="center">
 <img src="https://github.com/pnucse-capstone/capstone-2023-1-39/assets/71700079/a3647860-fb31-4725-a7a5-ed2faaefb689">
</p>  
<br>  

> ❓: 실내 위치 추정 기법의 정확도를 개선하는 것이 주요 목표입니다.  

> :bulb: 실내 위치 추정 기법을 기반으로 주변의 IoT 자원을 제어할 수 있습니다.

> 🗺️ 실내 위치 추정 기법을 기반으로 실내에서의 최단 경로를 안내받을 수 있습니다. 

> :closed_lock_with_key: 기기 기반의 인증 방식을 고안하여 더욱 안전하게 서비스를 이용할 수 있습니다.  

### 2. 팀 소개

|심진섭|이준희(팀장)|이민경|
|:-:|:-:|:-:|
|<img src="https://avatars.githubusercontent.com/u/71700079?s=400&u=9e9338f1a22b811003f826b00c9b797a01aea381&v=4" width="100" height="100">|<img src="https://avatars.githubusercontent.com/u/80378041?v=4" width="100" height="100">|<img src="https://avatars.githubusercontent.com/u/48466069?v=4" width="100" height="100">|
|프론트엔드 개발 <br> MQTT 환경 구축 <br> 머신러닝 서버 구축|백엔드 개발 <br> 데이터 전처리 <br> 배포 환경 구성|UI 기획 <br> 보고서 작성 <br> 데이터 수집|
|dndlzm123@pusan.ac.kr|abc980823@pusan.ac.kr|anfrhrl98@pusan.ac.kr|

### 3. 시스템 구성도

![image](https://github.com/pnucse-capstone/capstone-2023-1-39/assets/71700079/0483272a-ca6e-4253-8b22-a44cb003cee2)

❓ Backend  
|이름|개발 IDE|버전|비고|
|:-:|:-:|:-:|:-:|
|Springboot|IntelliJ|v3.0.6|메인 서버 개발|
|AWS RDB(Maria DB)|-|v10.6|메인 서버용 데이터베이스|
|Python|VSCode|v3.9.2|머신러닝용 서버 개발|
|DRF(Django Rest Framework)|VSCode|v3.14.0|머신러닝용 서버 배포|  

❓ Frontend  
|이름|개발 IDE|버전|비고|
|:-:|:-:|:-:|:-:|
|Vue.js|VSCode|Vue 3|메인 서버 개발|
|Node.js|-|v18.16.0|Javascript 개발 환경|
|Firebase Cloud Messaging|VSCode|-|PWA 푸시 알림 전송 API|  

❓ Device  
|이름|개발 IDE|버전|비고|
|:-:|:-:|:-:|:-:|
|Raspberry Pi|VSCode|3B+|사용자 지급용 라즈베리파이|
|Raspberry Pi|VSCode|4B|제어 가능한 자원|  

❓ Devops  
|이름|버전|비고|
|:-:|:-:|:-:|:-:|
|AWS EC2|ubuntu 20.04 LTS|메인 서버(Springboot) 배포|
|AWS ALB|-|메인 서버 HTTPS 로드밸런서|
|AWS Route 53|-|도메인 네임서버 연결|  

### 4. 소개 및 시연 영상
TBD

### 5. 설치 및 사용법

본 프로젝트의 서비스는 PWA를 통해 제공됩니다.  
아래의 링크로 접속하여 __홈 화면에 추가__ 기능을 통해 별도의 설치 없이 사용이 가능합니다.  
```
wmi-project-d857c.web.app
```
