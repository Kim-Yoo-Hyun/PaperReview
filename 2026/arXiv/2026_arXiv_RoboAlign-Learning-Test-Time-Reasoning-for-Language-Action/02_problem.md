# RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

언어 추론 능력 개선이 low-level robot action 개선으로 항상 전이되지 않는다.

## Formulation and Robotics Loop

영상·언어 추론 → action-token 정렬 MLLM → diffusion action head → 조작 행동.

자연어 추론에서 action token을 생성하고 RL로 행동 정확도를 정렬한 MLLM 위에 diffusion action head를 학습한다.

## Assumptions to Verify

RL action token과 최종 행동 차이·head 학습 데이터·추론 비용·공유 weight 경로.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

VLM pretraining·OpenVLA → RoboAlign → VLA 내부 RL의 학습 단계 구분.

VLM의 RL 정렬과 배포 VLA의 직접 RL 갱신을 구분할 선행으로 단일 정책 연구의 기여 경계를 보완한다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/2603.21341). arXiv v1의 정확한 제목 사용. 저자 페이지의 이전 제목은 alias로 보존한다. 검색 색인의 ICLR 2026 표기는 공식 acceptance로 확인하지 못해 arXiv로 등록한다. RoboAlign-R1 world-model 논문과 다르다.
