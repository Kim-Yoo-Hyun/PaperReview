# Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Authors: Jai Bardhan, Patrik Drozdik, Josef Sivic, Vladimir Petrik
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: world-model, exposure-bias, visual-fidelity, Reinforcement Learning, video diffusion
- Aliases: PersistWorld
- Official paper: https://arxiv.org/abs/2603.25685
- Full-text retrieval: https://arxiv.org/pdf/2603.25685v2
- Venue verification: https://api.crossref.org/works/10.1007/978-3-032-37517-9_29
- Code/Project: https://jaibardhan.com/persistworld/
- Code: https://github.com/Jai2500/PersistWorld
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

이 연구는 로봇 행동에 조건화한 영상 세계 모형이 자신이 생성한 장면을 연이어 입력할 때 생기는 시각적 오차 누적을 줄이도록 후학습한다. [PDF 1쪽](https://arxiv.org/pdf/2603.25685v2#page=1)

## Core Idea and Contribution

- 같은 예측 이력에서 길이가 다른 여러 미래를 생성하고 실제 다중 시점 영상과의 일치도를 보상으로 삼아 확산 모형을 갱신한다. [PDF 5쪽](https://arxiv.org/pdf/2603.25685v2#page=5) · [PDF 7쪽](https://arxiv.org/pdf/2603.25685v2#page=7) · [PDF 9쪽](https://arxiv.org/pdf/2603.25685v2#page=9)
- 연속 생성에서 시점별 영상 품질 지표와 사람이 선호하는 영상을 비교해 오차가 시간에 따라 어떻게 변하는지 분석했다. [PDF 11쪽](https://arxiv.org/pdf/2603.25685v2#page=11) · [PDF 12쪽](https://arxiv.org/pdf/2603.25685v2#page=12) · [PDF 13쪽](https://arxiv.org/pdf/2603.25685v2#page=13) · [PDF 14쪽](https://arxiv.org/pdf/2603.25685v2#page=14)

## Observation–State–Action Interface

Robot action + predicted video history → future multi-view video; 최적화 대상은 robot policy가 아니라 world model이다.

## Evaluation Scope and Claim Boundary

공식 abstract/project는 DROID에서 LPIPS/SSIM/PSNR 기반 rollout fidelity와 human preference 평가를 설명한다. Downstream policy improvement는 별도 검증 대상이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2603.25685) · [저자 project/code](https://jaibardhan.com/persistworld/). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## 검색 태그 근거

로봇 행동과 이전 영상으로 여러 카메라의 다음 영상을 생성한다. 자기 예측 이력에서 갈라진 영상 후보에 시각적 보상을 매겨 비디오 확산 모델을 강화학습한다. 평가 대상은 연속 생성 영상의 품질이다. [원문 9쪽](https://arxiv.org/pdf/2603.25685v2#page=9) · [원문 13쪽](https://arxiv.org/pdf/2603.25685v2#page=13)

## Why This Paper Is Here — Researcher Interpretation

Current trend. RL로 개선하는 대상은 world model의 autoregressive prediction이다. DROID rollout fidelity 근거를 policy success 개선으로 간주하지 않는다. Ctrl-World/WMPO 기반 learned simulator를 직접 고도화할 때 NEXT 검토.

## Verification Boundary

Reward metric의 geometry/contact 민감도, rollout horizon, 실제 robot policy evidence 유무을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
