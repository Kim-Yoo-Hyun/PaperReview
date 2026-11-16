# Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

Offline 정책이 online fine-tuning 시작 때 기존 능력을 잃는 현상을 다룬다.

## Formulation and Robotics Loop

Offline data → calibrated conservative critic·정책 → online fine-tuning.

Conservative value의 scale을 reference policy 가치와 정렬하여 online 갱신에 유용한 초기화를 학습한다.

## Assumptions to Verify

reference return·보수성·초기 탐색·데이터 혼합·성능 회복 비용.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

CQL → Cal-QL → AWAC/RLPD 및 VLA online 전환의 초기 손실 분석.

초기 성능 손실을 semantic forgetting으로만 설명하지 않게 하는 critic calibration baseline이다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
