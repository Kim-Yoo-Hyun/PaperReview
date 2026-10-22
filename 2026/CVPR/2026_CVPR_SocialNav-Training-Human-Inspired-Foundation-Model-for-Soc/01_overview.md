# SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: social-navigation, flow-policy, RL
- Aliases: SocialNav
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html
- Code/Project: https://amap-eai.github.io/SocialNav/
- Code: project_only
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

짧은 경로와 collision avoidance만으로는 사회적 규범을 준수하는 embodied navigation을 충분히 설명하지 못한다.

## Core Idea and Contribution

VLM brain과 trajectory action module을 결합하고 imitation 이후 socially-aware flow-exploration GRPO로 정책을 개선한다.

## Observation–State–Action Interface

Visual/semantic context → social reasoning/traversability → flow trajectory policy → navigation.

## Evaluation Scope and Claim Boundary

CVF abstract는 SocNav dataset, navigation success와 social compliance 평가를 보고한다. 정확한 metric 정의와 실제 robot trial은 확인 필요.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html) · [저자 project/code](https://amap-eai.github.io/SocialNav/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / dataset. Semantic reasoning과 trajectory generation에 socially compliant reward를 연결한다. NaVILA/VLFM의 task success 중심 비교에 행동 제약을 더한다. 기존 **SocialNav-SUB는 별도 benchmark**다.

## Verification Boundary

Social label/reward 정의, 지역/환경별 규범 변화, reward hacking 및 evaluation split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
