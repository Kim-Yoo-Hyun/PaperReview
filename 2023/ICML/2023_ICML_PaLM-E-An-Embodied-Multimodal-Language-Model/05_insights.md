# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: We propose embodied language models to directly incorporate real-world continuous sensor modalities into language models and thereby establish the link between words and percepts.
- 출발 문제 단서: However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive textual data may lead to representations ...
- 주장된 효과 단서: Further, in our experiments we show that current state-of-the-art visuallanguage models trained on typic

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- Language-conditioned perception을 바로 action/policy token으로 연결하는 방식을 3D object state, affordance, contact-aware manipulation으로 확장할 수 있다.
- 2D image 중심 VLA가 놓치는 pose, metric distance, occlusion을 3D representation이나 scene memory로 보강하는 연구 질문으로 이어진다.

## 이 논문이 끝난 지점
- 논문이 도달한 지점: Further, in our experiments we show that current state-of-the-art visuallanguage models trained on typic
- robot action까지 보인 경우에도 3D state grounding, closed-loop correction, force/tactile feedback, unseen embodiment generalization은 별도 검증이 필요하다.

## 다음 연구 질문
- 3D geometry token을 VLA policy에 넣을 때 action success와 language following 중 어느 부분이 실제로 개선되는가?
- open-vocabulary instruction과 metric manipulation constraint를 같은 representation에서 안정적으로 맞출 수 있는가?
- long-horizon task에서 memory/action token이 누적될 때 failure recovery를 어떻게 설계할 수 있는가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: COCO / accuracy, mAP, success rate
- 내 연구 확장 benchmark 후보: CALVIN, LIBERO, RLBench, Open X-Embodiment
- 내 연구 확장 metric 후보: success rate, task completion, generalization gap, collision
- 검증 초점: language-conditioned manipulation success, unseen object/task generalization, closed-loop recovery를 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Problem cue: However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive textual data may lead to representations ...
- Method cue: We propose embodied language models to directly incorporate real-world continuous sensor modalities into language models and thereby establish the link between words and percepts.
- Result cue: Further, in our experiments we show that current state-of-the-art visuallanguage models trained on typic
