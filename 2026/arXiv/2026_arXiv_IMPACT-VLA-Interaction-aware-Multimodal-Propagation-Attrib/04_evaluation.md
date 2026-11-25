# Evaluation — IMPACT-VLA: Interaction-aware Multimodal Propagation Attribution via Counterfactual Trajectories for Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-24에 확인한 저자 본문 §III–IV에 근거한다.

- **Evaluation type:** `Simulation`

## 평가와 결과

LIBERO Spatial·Object·Goal의 각 10개 시뮬레이션 과제를 고정 OpenVLA-OFT로 평가했다. 각 과제에서 성공 경로 하나가 구간을 정한다. 입력을 중요도 순으로 지우거나 돌려주면서 실제 성공 곡선의 부분 면적을 비교하고 과제 단위로 불확실성을 산출했다. [저자 §IV-A·D, 표 I·III](https://arxiv.org/html/2609.15005v1#S4)

| 입력 순위 기준 | 제거 부분 AUC | 복원 부분 AUC |
|---|---:|---:|
| IMPACT-VLA | 0.810 | 0.104 |
| 즉시 명령 변화 | 0.670 | 0.030 |
| 입력 하나씩 제거 | 0.780 | 0.017 |

복원 절대값은 작았다. 한 단위씩 빼는 대조와 비교한 제거 지표 차이, 구간 안에서만 Shapley를 계산한 대조와의 차이에는 명확한 통계적 근거가 없었다. 결과 범위는 사용한 정책, 입력 대체 방식과 시뮬레이션 과제다. [저자 §IV-D](https://arxiv.org/html/2609.15005v1#S4.SS4)

회복 비교에는 조건별로 짝지은 32개 rollout seed를 썼다. 통계 단위는 과제이며 과제 단위 bootstrap으로 95% 구간을 구했다. 입력을 대체한 뒤 손끝의 참조 경로 복귀와 과제 성공 복귀를 별도로 기록했다. [저자 §III-E·IV-A, 표 I·VI](https://arxiv.org/html/2609.15005v1#S4)
