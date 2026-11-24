# RLVR-World: Training World Models with Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2025 / NeurIPS
- Authors: Jialong Wu, Shaofeng Yin, Ningya Feng, Mingsheng Long
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: world-model, RLVR, video-prediction
- Aliases: RLVR-World
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html
- Code/Project: https://thuml.github.io/RLVR-World/
- Code: https://github.com/thuml/RLVR-World
- Full-text retrieval: https://proceedings.neurips.cc/paper_files/paper/2025/file/b63a24a1832bd14fa945c71f535c0095-Paper-Conference.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

RLVR-World는 행동에 따른 다음 상태를 생성하는 세계 모델을, 디코딩된 예측의 품질로 계산한 검증 가능 보상으로 후학습한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/b63a24a1832bd14fa945c71f535c0095-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/b63a24a1832bd14fa945c71f535c0095-Paper-Conference.pdf#page=4)

## Core Idea and Contribution

- 토큰 시퀀스를 출력하는 언어·영상 세계 모델에서 완성된 예측을 과제별 지표로 채점해 모델의 정책 경사를 계산한다. [PDF 3쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/b63a24a1832bd14fa945c71f535c0095-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/b63a24a1832bd14fa945c71f535c0095-Paper-Conference.pdf#page=4)
- 텍스트 게임·웹 환경의 상태 예측과 RT-1 등 로봇 영상의 다음 관측 예측을 각각 평가하고, 생성 품질과 전이 정확도를 비교했다. [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/b63a24a1832bd14fa945c71f535c0095-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/b63a24a1832bd14fa945c71f535c0095-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/b63a24a1832bd14fa945c71f535c0095-Paper-Conference.pdf#page=8)

## Observation–State–Action Interface

Action-conditioned state prediction → decoded metric reward → world model update.

## Evaluation Scope and Claim Boundary

언어·영상 world model의 여러 도메인을 평가한다. RT-1 로봇 영상의 예측 품질을 로봇 제어 성공으로 해석하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html) · [저자 project/code](https://thuml.github.io/RLVR-World/) · [공식 code](https://github.com/thuml/RLVR-World).

## Why This Paper Is Here — Researcher Interpretation

VLA policy RL과 world model RL을 구분하며 예측 개선이 행동에 전달되는지 물을 비교 자료다.

## Verification Boundary

reward metric과 task 목표 정합성, planner의 model exploitation, 로봇 행동 평가 유무을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
