# Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`.
> Source audit: 2026-11-16: arXiv abstract·공식 project/repository 확인. abstract 기반 — 본문 수동 확인 필요. ICRA 게재는 공식 근거 확인 대기.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Data Pipeline and Interface

[공식 repository](https://github.com/physical-superintelligence-lab/Humanoid-Everyday)는 G1/H1 데이터와 RGB·depth·LiDAR·tactile·상태 등 modality 및30Hz schema를 안내한다. 모든 episode에서 모든 modality가 완전하다고 가정하지 않는다.

G1 arm/hand action28D, H1 26D를 구별하고 H1 hand 전처리를 확인한다. Leg state의 존재만으로 Ψ₀의 하체 명령8D가 원본에 모두 제공된다고 추론하지 않는다.

## Training / Inference Boundary

Dataset interface와 downstream policy architecture는 별개다. 구체적 학습 objective·controller·timing은 사용하는 모델의 본문과 release를 확인해야 한다.
