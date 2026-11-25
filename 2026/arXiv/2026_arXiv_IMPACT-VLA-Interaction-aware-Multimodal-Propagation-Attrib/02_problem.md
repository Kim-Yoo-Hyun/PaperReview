# Problem — IMPACT-VLA: Interaction-aware Multimodal Propagation Attribution via Counterfactual Trajectories for Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-24에 확인한 저자 본문 §III–IV에 근거한다.

## 문제와 가정

언어 지시에 맞는 물체를 찾을 때와 집은 물체를 놓을 때는 다른 센서가 유용할 수 있다. 한 번의 행동 편차를 관측하면 후속 시각·자세 피드백으로 회복한 경로도 실패 위험으로 분류할 수 있다. 저자들은 시간 구간별 센서 입력을 유지하거나 대체했을 때의 최종 성공을 질문으로 삼았다.

출발점은 성공한 참조 경로와 재실행할 수 있는 초기 상태다. 참조 경로에서 정한 시간 경계를 모든 분기에 적용하므로 개입으로 물체 접근이나 파지가 지연되면 같은 시간의 비교 대상이 서로 다른 행동일 수 있다. [저자 §III-B·E](https://arxiv.org/html/2609.15005v1#S3)
