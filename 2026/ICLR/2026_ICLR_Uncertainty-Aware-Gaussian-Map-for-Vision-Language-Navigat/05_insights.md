# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: For training, we mitigate this cost through offline pretraining.

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- Language/semantic goal을 metric 3D map, BEV, scene graph, frontier/map memory와 연결해 navigation state representation으로 사용할 수 있다.
- Navigation의 핵심 병목을 visual-language matching만이 아니라 spatial memory, localization, graph planning 문제로 재정의할 수 있다.

## 이 논문이 끝난 지점
- navigation 성능을 보인 뒤에도 geometry-aware memory의 누적 오류, unseen scene transfer, semantic grounding failure는 후속 연구 지점으로 남는다.

## 다음 연구 질문
- 3D map/scene graph/gaussian map 중 어떤 representation이 language/semantic goal following에 가장 안정적인가?
- semantic goal grounding과 metric path planning을 분리해야 하는가, 아니면 end-to-end로 결합해야 하는가?
- online exploration 중 잘못된 language grounding을 어떻게 감지하고 수정할 수 있는가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: Matterport3D, Habitat, R2R, RxR / accuracy, AP, mAP, SPL, SR
- 내 연구 확장 benchmark 후보: R2R, RxR, VLN-CE, Habitat
- 내 연구 확장 metric 후보: SR, SPL, nDTW, collision
- 검증 초점: instruction/semantic goal following, path efficiency, unseen environment generalization, online correction을 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Method cue: For training, we mitigate this cost through offline pretraining.
