# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: To handle this task, we propose LIRA: Language Instructed Reconstruction Assistant.
- 출발 문제 단서: Existing language instruction-guided online 3D reconstruction systems mainly rely on explicit instructions or queryable maps, showing inadequate capability to handle implicit and complex instructions.
- 주장된 효과 단서: Experiments demonstrate that LIRA outperforms existing methods in the reasoning reconstruction task and is capable of running in real time.

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- 3D observation을 language model이 다룰 수 있는 token/memory/query interface로 바꾸는 방식을 spatial reasoning과 embodied planning에 사용할 수 있다.
- LLM/VLM의 commonsense를 쓰되, 3D geometry가 제공하는 metric constraint로 hallucination을 제어하는 방향이 중요하다.

## 이 논문이 끝난 지점
- 논문이 도달한 지점: Experiments demonstrate that LIRA outperforms existing methods in the reasoning reconstruction task and is capable of running in real time.
- 3D QA/reasoning 성능 이후에도 metric grounding, benchmark leakage, embodied action validation은 별도 검증이 필요하다.

## 다음 연구 질문
- LLM이 답한 spatial reasoning이 실제 3D metric relation과 일치하는지 어떻게 자동 검증할 수 있는가?
- 3D scene token과 language token 사이 alignment를 dense annotation 없이 학습할 수 있는가?
- reasoning output을 robot planner/action policy로 넘길 때 필요한 intermediate representation은 무엇인가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: ScanNet, ScanRefer, Nr3D, Sr3D / accuracy, mIoU, IoU, AP, mAP
- 내 연구 확장 benchmark 후보: ScanNet, SQA3D, EmbodiedScan, Matterport3D
- 내 연구 확장 metric 후보: accuracy, mIoU, grounding accuracy, task success
- 검증 초점: 3D spatial reasoning, answer grounding, embodied task transfer를 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Problem cue: Existing language instruction-guided online 3D reconstruction systems mainly rely on explicit instructions or queryable maps, showing inadequate capability to handle implicit and complex instructions.
- Method cue: To handle this task, we propose LIRA: Language Instructed Reconstruction Assistant.
- Result cue: Experiments demonstrate that LIRA outperforms existing methods in the reasoning reconstruction task and is capable of running in real time.
