# STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

의미 있는 단계로 trajectory를 나누고 stage-aware TPO/PPO 및 imitation–preference–interaction 후학습을 구성한다.

## Observation, State, and Action

상태·action trajectory → 단계별 강화/선호 신호 → VLA 후학습.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: stage label·geometric/contact predicate·potential 경계·TPO/PPO 비용.

## Method-Specific Comparison — Researcher Interpretation

동일 stage 정보에서 단순 potential shaping과 STARE식 갱신을 원 sparse 성공 지표로 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/2512.05107). arXiv v2 및 저자 project 확인. 검색 색인의 ICLR 표기는 공식 proceedings/forum으로 확인하지 못해 arXiv 2025로 유지한다. 공개 구현 URL은 식별하지 못했다.
