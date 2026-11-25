# IMPACT-VLA: Interaction-aware Multimodal Propagation Attribution via Counterfactual Trajectories for Vision-Language-Action Policies

> Evidence maturity: `FULL_TEXT_CHECKED`.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tags: Vision-Language-Action, robot-manipulation, counterfactual-evaluation, interpretability, closed-loop-control
- Code/Project: 논문 전용 저자 공개 구현 확인 필요.
- Source audit: 2026-11-24, arXiv v1 §III–IV와 표 I·III·VI. [서지와 저자](https://arxiv.org/abs/2609.15005) · [본문](https://arxiv.org/html/2609.15005v1)

## Why This Paper Is Here

특정 순간의 영상이 명령을 바꿨어도 과제의 마지막 성공에 그 정보가 필요했는지는 별도의 질문이다. 이 논문은 둘을 직접 비교한 선행으로, 시각 피드백 평가를 설계할 때 참조한다. [연구 후보의 판단](../../../work/research_topics/RESULTS.md#visual-feedback)

## 문제와 기여

저자들은 성공 시연의 행동 전환으로 시간 구간을 정하고, 정책 질의 시점에 영상·고유감각·언어 중 일부를 바꾼 뒤 로봇을 끝까지 실행한다. 이때 입력 조합별 최종 성공으로 구간별 정보 기여를 추정한다. LIBERO의 고정 OpenVLA-OFT에서 어느 입력을 제거할 때 성공을 잃는지 순위를 매기는 능력이 즉시 명령 변화 기준보다 높았다. 과제마다 성공 기준 경로가 필요하며, [평가 노트](./04_evaluation.md)에 비교 조건을 기록했다.
