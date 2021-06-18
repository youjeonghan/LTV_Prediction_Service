# LTV_Prediction_Service
![LTV_project_thumbnail](https://user-images.githubusercontent.com/57481424/122573079-5cbe3b80-d089-11eb-9d8d-db2d12c33b62.png)
※ 해당 데이터는 aloha factory의 모바일 게임 draw hammer의 실제 데이터를 제공 받아 만들어졌다. 해당 데이터는 프로젝트에 포함되어 있지 않다.

<br/>

## 예측모델
머신러닝과 딥러닝을 통해 모델을 구현하고 더 우수한 성능이 나온 딥러닝을 채택했다.<br/>
![image](https://user-images.githubusercontent.com/57481424/122574771-fa663a80-d08a-11eb-8b0b-5f1e67763426.png)<br/>
**👉 Shallow Learning Loss : 0.06618**

<br/>

![image](https://user-images.githubusercontent.com/57481424/122574780-ff2aee80-d08a-11eb-840d-4fa36f2bd354.png)<br/>
**👉 Deep Learning Loss : 0.0065**

위의 Loss 값들이 매우 작은 이유는 해당 광고의 수입을 예측하여 달러로 치환하여 구현했기 때문입니다.

<br/>

![image](https://user-images.githubusercontent.com/57481424/122574980-35686e00-d08b-11eb-9d19-94f35195f7ea.png)<br/>
**👉 인공 신경망 - 다층 퍼셉트론**

Optimizer는 Adam을 채택했고 하이퍼파라미터의 튜닝은 리스트에 파라미터 값들을 입력하면 해당 조건에서 자동 튜닝되도록 만들었다.
dropout, batch normalization 기법을 통해 성능을 최대한 향상 시켰다.

<br/>

## 예측 페이지
![image](https://user-images.githubusercontent.com/57481424/122574206-64321480-d08a-11eb-92a0-a27510e497be.png)<br/>
**👉 메인 페이지 (예측 페이지)**

<br/>

## 예측 페이지
![image](https://user-images.githubusercontent.com/57481424/122574355-8a57b480-d08a-11eb-8bf3-b81862880b46.png)<br/>
**👉 기기OS 분석 페이지**

<br/>

![image](https://user-images.githubusercontent.com/57481424/122574421-993e6700-d08a-11eb-9e52-3e9f75a78099.png)<br/>
**👉 사용기기 분석 페이지**

<br/>

![image](https://user-images.githubusercontent.com/57481424/122574461-a22f3880-d08a-11eb-8729-1f351391c80e.png)<br/>
**👉 요일 분석 페이지**

<br/>

![image](https://user-images.githubusercontent.com/57481424/122576211-67c69b00-d08c-11eb-8aab-f11c02fdb81a.png)<br/>
**👉 지역 분석 페이지**

<br/>

![image](https://user-images.githubusercontent.com/57481424/122574506-ac513700-d08a-11eb-8628-79f7249cb530.png)<br/>
**👉 시간 분석 페이지**

<br/>

## 사용 스택
- 분석 환경

  python
  
  pytorch
  
  MongoDB
  
  AWS EC2 (DB 서버)
  
  Colab
  
  <br/>
  
- 프론트엔드

  React
  
  And Design
  
  Webpack
  
  <br/>
  
- 백엔드

  python
  
  Django
  
  Postman
  
  MongoDB
