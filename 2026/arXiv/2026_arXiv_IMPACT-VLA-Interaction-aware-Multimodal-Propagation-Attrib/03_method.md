# Method — IMPACT-VLA: Interaction-aware Multimodal Propagation Attribution via Counterfactual Trajectories for Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-24에 확인한 저자 본문 §III–IV에 근거한다.

## 관측과 재실행

성공 경로의 행동 전환점을 8개 행동을 생성하는 정책 질의 경계에 맞춘다. 한 구간의 외부 영상, 손목 영상, 고유감각, 언어가 각각 개입 단위다. 지정된 입력을 대체하고 매 질의에서 그 경로의 후속 관측으로 다시 행동한다. 평균 영상·상태와 빈 언어를 기본 대체값으로 사용하며 영상에는 회색·흐림·잡음도 대조한다. [저자 §III-B·C, IV-A](https://arxiv.org/html/2609.15005v1#S3)

## 기여도와 회복

같은 정보 조합에 한 단위의 입력을 돌려줬을 때 성공에 생기는 차이를 순열 표본으로 평균내 Shapley 값을 추정한다. 앞 구간과 뒤 구간의 입력을 함께 복원할 때의 추가 효과도 계산한다. 앞선 개입 뒤 손끝이 참조 궤적에 가까워지는 정도와 과제 성공이 회복되는 정도를 별도로 측정한다. 정책 가중치는 고정한다. [저자 §III-C–E](https://arxiv.org/html/2609.15005v1#S3)
