# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: We present Dreamer, a general algorithm that outperforms specialized expert algorithms across a wide range of domains while using fixed hyperparameters, making reinforcement learning readily applicable to new ...
- 출발 문제 단서: The actor and critic predict actions at and values vt and learn from trajectories of abstract representations predicted by the world model. problem without human data has been ...
- 주장된 효과 단서: Minecraft Diamond Max Mean 100K 1M 10M 100M Env steps Unified configuration Figure 1: Benchmark summary. a, Using fixed hyperparameters across all domains, Dreamer outperforms tuned expert algorithms ...

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- 논문이 제안한 representation/method를 3D scene understanding과 robot decision-making 사이의 중간 표현으로 재해석할 수 있다.
- 핵심 단서를 그대로 쓰기보다 geometry, semantics, action constraint 중 무엇을 보강해야 하는지 확인하는 출발점으로 삼는다.

## 이 논문이 끝난 지점
- 논문이 도달한 지점: Minecraft Diamond Max Mean 100K 1M 10M 100M Env steps Unified configuration Figure 1: Benchmark summary. a, Using fixed hyperparameters across all domains, Dreamer outperforms tuned expert algorithms ...
- 저자가 남긴 확장 방향: As a high-performing algorithm that is based on a learned world model, Dreamer paves the way for future research directions, including teaching agents world knowledge from internet videos ...
- 논문이 다룬 task 범위 밖의 3D consistency, robotics transfer, open-world generalization은 후속 연구 질문으로 남는다.

## 다음 연구 질문
- 이 방법의 핵심 representation이 3D geometry와 semantic grounding을 동시에 보존하는가?
- 동일한 idea가 online robot perception/action setting에서도 유지되는가?
- failure case가 data 부족, geometry mismatch, language ambiguity, policy limitation 중 어디에서 오는가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: 자동 추출에서 명확한 dataset 단서 없음 / 자동 추출에서 명확한 metric 단서 없음
- 내 연구 확장 benchmark 후보: ScanNet, Matterport3D, nuScenes, CALVIN
- 내 연구 확장 metric 후보: mIoU, accuracy, success rate, generalization gap
- 검증 초점: paper task 성능과 3D/robotics downstream utility를 함께 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Problem cue: The actor and critic predict actions at and values vt and learn from trajectories of abstract representations predicted by the world model. problem without human data has been ...
- Method cue: We present Dreamer, a general algorithm that outperforms specialized expert algorithms across a wide range of domains while using fixed hyperparameters, making reinforcement learning readily applicable to new ...
- Result cue: Minecraft Diamond Max Mean 100K 1M 10M 100M Env steps Unified configuration Figure 1: Benchmark summary. a, Using fixed hyperparameters across all domains, Dreamer outperforms tuned expert algorithms ...
