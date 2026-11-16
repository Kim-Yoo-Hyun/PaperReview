# RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

자연어 추론에서 action token을 생성하고 RL로 행동 정확도를 정렬한 MLLM 위에 diffusion action head를 학습한다.

## Observation, State, and Action

영상·언어 추론 → action-token 정렬 MLLM → diffusion action head → 조작 행동.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: RL action token과 최종 행동 차이·head 학습 데이터·추론 비용·공유 weight 경로.

## Method-Specific Comparison — Researcher Interpretation

고정 head와 재학습 head를 분리하고 같은 RL 데이터·계산에서 alignment 이득을 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/2603.21341). arXiv v1의 정확한 제목 사용. 저자 페이지의 이전 제목은 alias로 보존한다. 검색 색인의 ICLR 2026 표기는 공식 acceptance로 확인하지 못해 arXiv로 등록한다. RoboAlign-R1 world-model 논문과 다르다.
