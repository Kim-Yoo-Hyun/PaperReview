# SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

짧은 경로와 collision avoidance만으로는 사회적 규범을 준수하는 embodied navigation을 충분히 설명하지 못한다.

## Bottleneck and Changed Formulation

VLM brain과 trajectory action module을 결합하고 imitation 이후 socially-aware flow-exploration GRPO로 정책을 개선한다.

## System and Robotics Loop

Visual/semantic context → social reasoning/traversability → flow trajectory policy → navigation.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Social label/reward 정의, 지역/환경별 규범 변화, reward hacking 및 evaluation split.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

CVF abstract는 SocNav dataset, navigation success와 social compliance 평가를 보고한다. 정확한 metric 정의와 실제 robot trial은 확인 필요.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html) · [저자 project/code](https://amap-eai.github.io/SocialNav/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
