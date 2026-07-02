# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: Whereas standard policy gradient methods perform one gradient update per data sample, we propose a novel objective function that enables multiple epochs of minibatch updates.
- 출발 문제 단서: Q-learning (with function approximation) fails on many simple problems1 and is poorly understood, vanilla policy gradient methods have poor data effiency and robustness; and trust region policy optimization ...
- 주장된 효과 단서: Our experiments test PPO on a collection of benchmark tasks, including simulated robotic locomotion and Atari game playing, and we show that PPO outperforms other online policy gradient ...

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- 논문이 제안한 representation/method를 3D scene understanding과 robot decision-making 사이의 중간 표현으로 재해석할 수 있다.
- 핵심 단서를 그대로 쓰기보다 geometry, semantics, action constraint 중 무엇을 보강해야 하는지 확인하는 출발점으로 삼는다.

## 이 논문이 끝난 지점
- 논문이 도달한 지점: Our experiments test PPO on a collection of benchmark tasks, including simulated robotic locomotion and Atari game playing, and we show that PPO outperforms other online policy gradient ...
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
- Problem cue: Q-learning (with function approximation) fails on many simple problems1 and is poorly understood, vanilla policy gradient methods have poor data effiency and robustness; and trust region policy optimization ...
- Method cue: Whereas standard policy gradient methods perform one gradient update per data sample, we propose a novel objective function that enables multiple epochs of minibatch updates.
- Result cue: Our experiments test PPO on a collection of benchmark tasks, including simulated robotic locomotion and Atari game playing, and we show that PPO outperforms other online policy gradient ...
