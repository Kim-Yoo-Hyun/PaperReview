# What Can RL Bring to VLA Generalization? An Empirical Study

> Evidence maturity: `ABSTRACT_CHECKED`. 개요 전반은 초록 수준이며, 아래 요약과 두 기여에는 확인한 본문 위치를 표시했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Authors: Jijia Liu, Feng Gao, Bingwen Wei, Xinlei Chen, Qingmin Liao, YI WU, Chao Yu, Yu Wang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: RL-finetuning, generalization, evaluation
- Aliases: RL4VLA
- Official paper: https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html
- Venue verification: https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html
- Code/Project: https://rlvla.github.io/
- Code: https://github.com/gen-robot/RL4VLA
- Source audit: 2026-11-23 요약과 핵심 기여 두 개를 원문 본문에 대조했다. 나머지 세부 분석은 기존 초록·공식 자료에 근거한다.

## Problem and Importance

이 연구는 VLA의 강화학습 미세조정과 지도 미세조정을 비교해 시각 변화·지시 의미·행동 실행 중 어느 축의 일반화가 달라지는지 측정했다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf#page=1) · [PDF 2쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf#page=2)

## Core Idea and Contribution

- 시각·의미·실행 변화를 분리한 평가 조건을 만들고 PPO 등 여러 학습 방법을 같은 조작 설정에서 비교했다. [PDF 3쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf#page=3) · [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf#page=7)
- 실험 조건에서는 PPO가 의미 이해와 실행 강건성에서 지도 미세조정보다 개선됐고 시각 변화에 대한 성능은 비슷했다. [PDF 2쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf#page=2) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf#page=8)

## Observation–State–Action Interface

Image/language-conditioned VLA → action; 학습 방식과 평가 시 입력 perturbation을 분리한다.

## Evaluation Scope and Claim Boundary

공식 NeurIPS abstract는 visual, semantic, execution generalization 및 PPO/DPO/GRPO 비교를 설명한다.

근거: [공식 paper/abstract](https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html) · [저자 project/code](https://rlvla.github.io/). 그 밖의 수치, 기준선의 비교 조건, 실패 범위는 별도 대조가 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Benchmark / empirical study. Visual·semantic·execution generalization을 나누어 SFT와 RL을 비교한다. OpenVLA/OFT 이후 RL의 효과를 주장할 때 필요한 평가 기준이다. 해당 실험에서의 PPO 결과를 모든 VLA에 대한 우열로 일반화하지 않는다.

## Verification Boundary

Generalization split 생성, pretrained overlap, RL별 budget 및 real-robot 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문과 공개 자료

- 코드 — OpenVLA 일반화 비교용 강화학습 구현 · SimplerEnv/simpler_env/train_ms3_ppo.py [배포 파일](https://raw.githubusercontent.com/gen-robot/RL4VLA/de46e0174e7ac310255a2836718fcefab28b8963/SimplerEnv/simpler_env/train_ms3_ppo.py)
- 가중치 — 일반화 실험의 RL 미세조정 OpenVLA · model-00001-of-00004.safetensors [배포 파일](https://huggingface.co/gen-robot/openvla-7b-rlvla-rl/blob/93c54b036cc90ee394731fc73788406d7e65f057/model-00001-of-00004.safetensors)
