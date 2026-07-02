# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level actions to follow natural language navigation directions.
- 출발 문제 단서: This paradigm enables efficient data collection and high visual fidelity compared to 3D scanning or creating synthetic environments; however, scenes are only observed from a sparse set of ...
- 주장된 효과 단서: To establish context for our results, we consider random and hand-crafted agents shown in Tab.

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- Language/semantic goal을 metric 3D map, BEV, scene graph, frontier/map memory와 연결해 navigation state representation으로 사용할 수 있다.
- Navigation의 핵심 병목을 visual-language matching만이 아니라 spatial memory, localization, graph planning 문제로 재정의할 수 있다.

## 이 논문이 끝난 지점
- 논문이 도달한 지점: To establish context for our results, we consider random and hand-crafted agents shown in Tab.
- 논문 내 한계/논의 단서: In models presented here, we took an approach where observations were mapped directly to low-level control in an end-to-end manner; however, exploring modular approaches is exciting future work.
- navigation 성능을 보인 뒤에도 geometry-aware memory의 누적 오류, unseen scene transfer, semantic grounding failure는 후속 연구 지점으로 남는다.

## 다음 연구 질문
- 3D map/scene graph/gaussian map 중 어떤 representation이 language/semantic goal following에 가장 안정적인가?
- semantic goal grounding과 metric path planning을 분리해야 하는가, 아니면 end-to-end로 결합해야 하는가?
- online exploration 중 잘못된 language grounding을 어떻게 감지하고 수정할 수 있는가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: ImageNet, Matterport3D, Habitat, R2R, VLN-CE / mAP, SPL, SR, nDTW, success rate
- 내 연구 확장 benchmark 후보: R2R, RxR, VLN-CE, Habitat
- 내 연구 확장 metric 후보: SR, SPL, nDTW, collision
- 검증 초점: instruction/semantic goal following, path efficiency, unseen environment generalization, online correction을 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Problem cue: This paradigm enables efficient data collection and high visual fidelity compared to 3D scanning or creating synthetic environments; however, scenes are only observed from a sparse set of ...
- Method cue: We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level actions to follow natural language navigation directions.
- Result cue: To establish context for our results, we consider random and hand-crafted agents shown in Tab.
