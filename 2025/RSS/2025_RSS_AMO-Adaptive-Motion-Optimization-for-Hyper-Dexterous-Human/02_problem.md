# AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Source audit: 2026-11-16: RSS metadata·arXiv v1 §III–V/Table II–IV·공식 코드로 OCR/설명 교정. 과거2026-09-03 PDF review 기록은 보존; 사용자 reading status 변경 없음.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Problem and Assumptions

MoCap의 운동학적 pose가 target robot에서 실행 가능한 동역학을 보장하지 않는다. 상체 조작에 필요한 몸통 변화와 균형을 함께 다룬다. [§I–III](https://arxiv.org/html/2505.03738v1).

## Formulation and Closed Loop

Upper policy 명령→adaptation reference→RL lower policy→관절 제어. 이미 실행 가능한 reference가 주어진 순수 tracking과 구별한다. 논문은 G1에서 검증하며 unseen embodiment 일반화는 별도다.
