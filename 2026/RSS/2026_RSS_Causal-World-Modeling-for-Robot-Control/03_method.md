# Causal World Modeling for Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

RSS abstract의 CauVA는 autoregressive MoT로 frame/action을 처리하고 KV history와 noisy latent augmentation을 사용한다.

## Observation, State, and Action

영상·행동 이력 → 인과적 생성 sequence → 미래 영상·robot action.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: 예측/행동 gradient 경로·추론 history·실제 피드백·버전별 모델 명칭.

## Method-Specific Comparison — Researcher Interpretation

동일 action head에서 예측 보조 loss와 value loss를 분리하여 표현·행동 효과를 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p016.html). 공식 RSS abstract만을 canonical scope로 사용한다. 같은 제목의 arXiv2601.21998은 LingBot-VA와 다른 저자 구성·설계를 표기하므로 version mapping을 확정하지 않았고 arXiv ID/code를 자동 합치지 않았다. 별도 중복 등록도 하지 않았다.
