# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...
- 출발 문제 단서: Consider a scenario where a robot, initially trained to retrieve juice from a fridge, fails ∗
- 주장된 효과 단서: Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- Dataset/benchmark 설계 방식을 연구 아이디어의 evaluation protocol과 failure taxonomy를 잡는 기준으로 사용할 수 있다.
- 새 방법을 제안하기 전, 이 benchmark가 어떤 input, annotation, split, metric을 표준화했는지 확인해야 한다.

## 이 논문이 끝난 지점
- 논문이 도달한 지점: Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...
- benchmark는 task를 정의하지만, 실제 robot deployment나 open-world generalization을 완전히 대변하지 못할 수 있다.

## 다음 연구 질문
- 현재 benchmark metric이 3D CV 성능과 robotics task success 사이의 차이를 충분히 드러내는가?
- 새로운 representation/method가 train/test split이 아니라 scene/object/task shift에서 강한지 어떻게 확인할 수 있는가?
- annotation schema가 language, geometry, action failure를 분리해서 분석할 수 있는가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: ImageNet, LIBERO / mAP, success rate
- 내 연구 확장 benchmark 후보: paper-defined benchmark
- 내 연구 확장 metric 후보: paper-defined metrics, generalization gap, failure rate
- 검증 초점: benchmark coverage, split validity, metric-task alignment를 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Problem cue: Consider a scenario where a robot, initially trained to retrieve juice from a fridge, fails ∗
- Method cue: Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...
- Result cue: Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...
