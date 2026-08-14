# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: To handle the heterogeneity common in robotics, we propose HPT, a modular architecture and framework to embrace this heterogeneity through pre-training.
- 출발 문제 단서: Recent progress in open-source large-scale data collection has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) present in large-scale robotic data ...
- 주장된 효과 단서: HPTs outperform several baselines and enhance the fine-tuned policy performance by over 20% on unseen tasks in multiple simulator benchmarks and real-world settings.

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- Language-conditioned perception을 바로 action/policy token으로 연결하는 방식을 3D object state, affordance, contact-aware manipulation으로 확장할 수 있다.
- 2D image 중심 VLA가 놓치는 pose, metric distance, occlusion을 3D representation이나 scene memory로 보강하는 연구 질문으로 이어진다.

## 이 논문이 끝난 지점
- 논문이 도달한 지점: HPTs outperform several baselines and enhance the fine-tuned policy performance by over 20% on unseen tasks in multiple simulator benchmarks and real-world settings.
- 논문 내 한계/논의 단서: See Appendix §C for some failure modes.
- robot action까지 보인 경우에도 3D state grounding, closed-loop correction, force/tactile feedback, unseen embodiment generalization은 별도 검증이 필요하다.

## 다음 연구 질문
- 3D geometry token을 VLA policy에 넣을 때 action success와 language following 중 어느 부분이 실제로 개선되는가?
- open-vocabulary instruction과 metric manipulation constraint를 같은 representation에서 안정적으로 맞출 수 있는가?
- long-horizon task에서 memory/action token이 누적될 때 failure recovery를 어떻게 설계할 수 있는가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: 자동 추출에서 명확한 dataset 단서 없음 / mAP, success rate
- 내 연구 확장 benchmark 후보: CALVIN, LIBERO, RLBench, Open X-Embodiment
- 내 연구 확장 metric 후보: success rate, task completion, generalization gap, collision
- 검증 초점: language-conditioned manipulation success, unseen object/task generalization, closed-loop recovery를 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Problem cue: Recent progress in open-source large-scale data collection has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) present in large-scale robotic data ...
- Method cue: To handle the heterogeneity common in robotics, we propose HPT, a modular architecture and framework to embrace this heterogeneity through pre-training.
- Result cue: HPTs outperform several baselines and enhance the fine-tuned policy performance by over 20% on unseen tasks in multiple simulator benchmarks and real-world settings.
