# SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

VLM brain과 trajectory action module을 결합하고 imitation 이후 socially-aware flow-exploration GRPO로 정책을 개선한다.

## Observation–State–Action Interface

Visual/semantic context → social reasoning/traversability → flow trajectory policy → navigation.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Social label/reward 정의, 지역/환경별 규범 변화, reward hacking 및 evaluation split.

Source가 명시한 evaluation 범위: CVF abstract는 SocNav dataset, navigation success와 social compliance 평가를 보고한다. 정확한 metric 정의와 실제 robot trial은 확인 필요.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Task-only reward와 social reward를 같은 policy로 비교하고 success·규범 위반·경로 길이·collision을 함께 보고한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html) · [저자 project/code](https://amap-eai.github.io/SocialNav/). 수식·세부 구현·코드 실행은 미검증이다.
