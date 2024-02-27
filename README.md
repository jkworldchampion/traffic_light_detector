traffic_light_detector
=======================
Traffic light Detector for Korea urban road/한국형 신호등 인식 프로그램
-------------
우리는 한국 도심에 있는 교통 상황을 확인하기 위해 다음과 같은 프로그램을 만들었다.
# 학습 데이터 분석

## 1. Confusion Matrix(혼합행렬)

다음 테이블을은 Confusion Matrix의 구성이다.

![스크린샷 2024-02-27 041442](https://github.com/Dongwon-tuna/traffic_light_detector/assets/61178312/baf88f4d-2c21-415d-a200-dc42ae01a9d5)

위 구성을 참고하여 우리가 학습한 데이터의 Confusion Marix를 분석할 수 있다. 

대체적으로 green과 left와 red의 TP와 FP는 신뢰 가능성의 수치를 보였으나, 절대적인 yellow 데이터 부재와 Train, Val, Test 분류 실수로 인하여 유효한 데이터를 가져오지 못 하였다.(추후 재 학습 예정)

![confusion_matrix_normalized](https://github.com/Dongwon-tuna/traffic_light_detector/assets/61178312/f2df126c-c8bc-4c5c-83cd-9f6d7c490687)



## 2. Precision-Recall Curve

Precision은 Positive라고 **예측**한 비율 중 **실제** Positive의 비율이다.

Recall은 **실제** Positive의 비율 중 Positive로 **예측**한 비율이다.

Precision-Recall Curve가 반비례하는 곡선의 그래프처럼 보이는 이유는 Threshold가 100%에서 0%로 감소함에 따라 예측 정확도가 감소하기 때문이다.

이해를 돕기 위하여 예시를 들어 설명한다. 가장 범인일 것 같은 용의자를 나열한 다음 가장 엄격한 기소 기준을 선정한다면 예측의 정확도는 높아진다. 하지만 기준을 점차 내림에 따라 시민인 경우도 기소되는 경우가 발생하므로 예측 정확도는 떨어지게 된다. 계속해서 기소 기준을 낮추게 된다면 그만큼 실제 범인을 찾는 비율(Recall)이 늘어나겠지만 정확하지 못한 예측 또한 증가하여 Precision이 지속적으로 감소하게 된다.

그렇기에 Precision 값과 Recall 값의 관계는 Trade-off(상충 관계)의 특성을 띈다. 다음 특성에 의하여 이상적인 그래프의 모양은 꼭짓점이 우측 상단에 위치한 **ㄱ** 자 모양이다.

위 구성을 참고하여 우리가 학습한 데이터의 Precision-Recall Curve를 분석할 수 있다.

우측 상단에 꼭짓점이 위치한 ㄱ자 모양이므로, 학습한 Precision 값과 Recall값의 Trade-off 특성을 확인할 수 있다.

![PR_curve](https://github.com/Dongwon-tuna/traffic_light_detector/assets/61178312/157a1906-827f-4239-9e4e-b09900d62402)


## 3. Precision-Confidence Curve

다음 그래프에서는 Confidence 값에 따른 Precision값의 변화를 볼 수 있다. 이상적인 데이터의 흐름은 대체적으로 높은 Confidence 레벨에서 high Precision을 반환하는 것이다.

다음과 같이 로그함수 개형을 띄는 이유는 앞서 말한 기소 기준과 용의자, 범인의 관계에 대입하여 설명가능하다. 기소 기준(Confidence)을 낮추어서 마구잡이로 범인을 잡아들이는 대신, 선량한 시민까지 잡아들일 수 있기에 정확하지 못한 예측이 증가하여 Precision 값이 낮아진다. 그렇기에 낮은 Confidence에서 낮은 Precision 값을 띄는 것을 확인할 수 있다. 반대로 엄격한 기소 기준을 대입한다면 높은 Confidence에서는 높은 Precision값을 확인할 수 있다. 그렇기에 급격한 로그함수의 개형이 이상적이고, 학습한 결과를 분석하여 보면 대체적으로 많은 구간에서 0.8 이상의 Precision값을 나타내기에 이상적인 데이터의 흐름이라고 판단 가능하다.

위 특성을 반영하여 우리가 학습한 Precision-Confidence Curve는 0.0부터 0.2 사이의 Confidence 레벨에서 급격한 상승을 하여 일정한 값에 수렴하는 로그함수 개형을 띈다.

![P_curve](https://github.com/Dongwon-tuna/traffic_light_detector/assets/61178312/5c57e782-f042-49f5-8f0a-60ce9194eeb6)


## 4. Recall-Confidence Curve

다음 그래프에서는 Confidence 값에 따른 Recall값의 변화를 볼 수 있다. 이상적인 데이터의 흐름은 대체적으로 낮은 Confidence 레벨에서 high Recall을 반환하는 것이다.


다음과 같이 로그함수 Y축 대칭의 개형을 띄는 이유는 앞서 말한 기소 기준과 용의자, 범인의 관계에 대입하여 설명가능하다. 기소 기준(Confidence)을 낮추게 마구잡이로 범인을 잡아들인다면 실제로 잡히는 범죄자의 수는 증가한다. 기소 기준을 낮추어 조사를 한다면 법이 아닌 규칙과 규범을 어긴 범죄자까지 모두 잡아들일 수 있기 때문에 실제 범인을 찾는 비율(Recall)은 증가한다. 그렇기에 낮은 Confidence에서 높은 Recall 값을 띄는 것을 확인할 수 있다. 반대로 높은 Confidence에서는 낮은 Recall 값을 확인 가능하다. 기소 기준이 매우 까다롭고 높다면 실제로 잡히는 범인의 수는 절대적으로 감소할 수 밖에 없기 때문이다. 그렇기에 급격한 로그함수의 Y축 대칭 개형이 이상적이고, 학습한 결과를 분석하여 보면 대체적으로 많은 구간에서 0.8 이상의 Recall값을 나타내기에 이상적인 데이터의 흐름이라고 판단 가능하다.

위 특성을 반영하여 우리가 학습한 Recall-Confidence Curve는 0.7부터 1.0 사이의 Confidence 레벨에서 급격한 기울기를 보이며 감소하는 음의 무한대로 수렴하는 로그함수 개형을 띈다.

![R_curve](https://github.com/Dongwon-tuna/traffic_light_detector/assets/61178312/c0ccfd0b-364d-4de7-ae3b-4473e5649e83)

## 5. F1_curve

F1 score는 Precision과 Recall 값의 조화평균의 값이다.

Precision 과 Recall의 Trade-off 관계에 의하여 균일한 Precision 과 Recall 사이에서 F1 score는 상대적으로 큰 값을 갖는다. 아래의 산술평균, 조화평균 이미지를 통하여 F1 score의 특성을 파악 가능하다.

![스크린샷 2024-02-27 043547](https://github.com/Dongwon-tuna/traffic_light_detector/assets/61178312/f5dc97ad-19b5-401e-8492-04da0f9dc9c7)

위 구성을 참고하여 우리가 학습한 데이터의 F1_curve를 분석할 수 있다. 

이상적인 학습 데이터의 경우에는 Confidence 레벨과 F1사이의 관계가 높은 봉우리를 그리고, 그 것은 모델의 좋은 성능을 방증한다.

![F1_curve](https://github.com/Dongwon-tuna/traffic_light_detector/assets/61178312/8f52f82b-64e1-4a89-a4b1-a0d9e2f62d6e)


## 6. train 데이터와 val데이터의 상세 그래프

![results](https://github.com/Dongwon-tuna/traffic_light_detector/assets/61178312/0e1a9bfe-f7cf-4f5b-80be-c4f4f70828f6)


X-axis: Epochs, Y-axis: Value

1) box_loss: Ground truth(테스트에 활용된 실제 데이터)와 예측된 bounding box 내의 좌표(cordinates)와 차원(dimensions)의 오차를 측정하는 것. 작은 box_loss의 값일수록 예측된 bounding box의 정보가 정확하다. 

2) cls_loss: Ground truth와 각 이미지의 물체의 예측된 클래스의 일치 확률의 오차를 측정하는 것. 작은 cls_loss의 값일수록 물체의 클래스를 정확히 예측하는 모델이다.

3) dfl_loss: 물체의 다양한 scale과 aspect ratio(종횡비)를 인지할 수 있는 능력을 향상시키기 위해 고안된 deformable convolution layers이다. 낮은 dfl_loss의 값일수록 물체를 쉽게 변화시키고, 다양한 형태로 변화를 줄 수 있다.

4) precision: 개념은 앞서 언급. 다음의 그래프는 Confidence 레벨에 따라 분류하는 것이 아니라, 절대적인 precision, 즉 예측의 정확성이기에 1.0(100%)의 값으로 수렴하는것이 이상적인 그래프이다.(Confidence 레벨에 따른 precision값과 Epochs에 따른 precision값은 연관성이 없다.)

5) recall: 개념은 앞서 언급.  다음의 그래프는 Confidence 레벨에 따라 분류하는 것이 아니라, 절대적인 recall, 즉 다수의 올바른 값의 반환이기에 1.0(100%)의 값으로 수렴하는것이 이상적인 그래프이다.(Confidence 레벨에 따른 recall값과 Epochs에 따른 recall값은 연관성이 없다.) 

6) mAP50: AP는 precision과 recall을 그래프로 나타냈을 때의 면적이다(아래 사진자료 참고). 모든 class의 AP에 대해 평균값을 낸 것이 바로 mAP(mean AP)이다. mAP50은 그 그래프의 면적이 50(0.5)인 것이고, 다음 항목은 면적을 50으로 설정하고 100번 학습을 시켰을 때 모델의 정확성에 대한 추이를 나타낸 그래프이다. 정확성이 1.0(100%) 에 수렴하는 것으로 보아 유의미한 값으로 학습이 되었다.

7) mAP50-95: mAP50-95 represents the average mAP at different IoU thresholds (from 0.5 to 0.95 in steps of 0.05) (0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95).다음 항목은 mAP50-95로 설정하고 100번 학습을 시켰을 때 모델의 정확성에 대한 추이를 나타내었고, 정확성이 1.0(100%) 에 수렴하는 것으로 보아 유의미한 값으로 학습이 되었다.

![스크린샷 2024-02-27 063901](https://github.com/Dongwon-tuna/traffic_light_detector/assets/61178312/d7715536-e8d7-4468-b99b-dfc8f4fded65)


# 실행 결과

다음은 신호등 정보에 대해 학습한 model이 신호등 상태 감지를 하는 상황. 
![red_good](https://github.com/jkworldchampion/traffic_light_detector/assets/83493949/77fab8cf-bf80-4034-b198-86964b4d4cb1)  

빨간불과 좌회전이 동시에 켜진 신호등을 판단하는 상황.  
![red, right](https://github.com/jkworldchampion/traffic_light_detector/assets/83493949/03dbe116-fa77-44db-aea5-83ad21b16f3a)  

초록불과 좌회전이 동시에 켜진 신호등을 판단하는 상황.  
![green_right](https://github.com/jkworldchampion/traffic_light_detector/assets/83493949/032b0537-e254-4318-81ff-79df5c96a46c)  

다양한 영상에서 실시간으로 탐지가 가능한 것으로 보아, 충분히 활용 가능성이 있는 것으로 판단함 있는 것으로 판단됨.  