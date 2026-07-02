# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: 1-click 3-click 5-click bounding box ground-truth mask‡ SAM+XMem++ SAM+Cutie SAM 2 56.9 56.7 64.7 68.4 70.1 75.3 70.6 72.2 77.6 67.6 69.4 74.4 72.7 74.1 79.3 Table 4: ...

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- Large-scale pretraining feature를 3D perception의 initialization, pseudo-label, open-vocabulary semantic prior로 사용할 수 있다.
- 2D foundation model의 강한 recognition prior를 3D consistency, view aggregation, robot task relevance로 재해석해야 한다.

## 이 논문이 끝난 지점
- 2D/vision-language representation 성능 이후에도 3D metric alignment, temporal consistency, robot interaction feedback은 별도 문제로 남는다.

## 다음 연구 질문
- 2D foundation feature를 3D point/gaussian/map에 정렬할 때 어떤 consistency loss나 aggregation이 가장 안정적인가?
- segmentation/recognition prior가 affordance나 manipulation success까지 설명하는가?
- foundation model confidence를 3D map uncertainty로 변환해 active perception에 사용할 수 있는가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: KITTI / accuracy, mIoU, IoU
- 내 연구 확장 benchmark 후보: ImageNet, COCO, ScanNet, S3DIS
- 내 연구 확장 metric 후보: accuracy, mIoU, Recall@K, success rate
- 검증 초점: 2D recognition transfer, 3D semantic consistency, downstream robotics utility를 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Method cue: 1-click 3-click 5-click bounding box ground-truth mask‡ SAM+XMem++ SAM+Cutie SAM 2 56.9 56.7 64.7 68.4 70.1 75.3 70.6 72.2 77.6 67.6 69.4 74.4 72.7 74.1 79.3 Table 4: ...
