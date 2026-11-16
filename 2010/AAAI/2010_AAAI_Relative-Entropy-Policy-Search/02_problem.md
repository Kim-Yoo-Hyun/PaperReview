# Relative Entropy Policy Search

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

큰 정책 변경에 따른 정보 손실과 조기 수렴을 줄인다.

## Formulation and Robotics Loop

정책 분포·return → 정보 제약 최적화 → 새 정책 분포.

Relative entropy 제약으로 정책 개선을 제한하고 명시적 갱신을 도출한다.

## Assumptions to Verify

KL 방향·분포 제약·sample 추정·실제 행동 변화.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

정보 제약 policy search → REPS·MPO/TRPO → VLA 보존 regularization 비교.

TRPO·MPO·KL 제약의 개념 계보를 보완할 원전이며 현재 공통 정독은 GAE/PPO를 우선한다.

## Evidence Boundary

[공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/7727). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
