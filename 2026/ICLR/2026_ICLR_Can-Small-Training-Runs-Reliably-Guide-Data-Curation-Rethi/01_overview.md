# Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / ICLR
- Authors: Jiachen (Tianhao) Wang, Tong Wu, Kaifeng Lyu, James Y Zou, Dawn Song, Ruoxi Jia, Prateek Mittal
- 저자 판본: 학회 서지와 표기가 다른 저자의 인쇄명은 Jiachen T. Wang, James Zou이다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/c7d04ce5e71efdfc7a4a78f7161238a9-Paper-Conference.pdf#page=1) · [학회 서지](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html)
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, evaluation, data-selection
- Aliases:
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/c7d04ce5e71efdfc7a4a78f7161238a9-Paper-Conference.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

언어 모델 사전학습 자료를 고르는 소규모 대리 실험에서 모든 자료에 같은 학습 설정을 쓰면 대규모 학습에서의 자료 순위를 잘못 예측할 수 있음을 보였다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/c7d04ce5e71efdfc7a4a78f7161238a9-Paper-Conference.pdf#page=1) · [PDF 2쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/c7d04ce5e71efdfc7a4a78f7161238a9-Paper-Conference.pdf#page=2)

## Core Idea and Contribution

- 데이터 조합에 따라 적절한 학습률이 달라지는 현상을 측정하고, 대리 모델의 학습률을 낮춰 자료 순위를 비교하는 절차를 제안했다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/c7d04ce5e71efdfc7a4a78f7161238a9-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/c7d04ce5e71efdfc7a4a78f7161238a9-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/c7d04ce5e71efdfc7a4a78f7161238a9-Paper-Conference.pdf#page=6)
- 무작위 특징 모델에서 순위 보존 조건을 분석하고 23개 사전학습 자료 조합에서 대리 실험과 대규모 학습의 순위 일치도를 확인했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/c7d04ce5e71efdfc7a4a78f7161238a9-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/c7d04ce5e71efdfc7a4a78f7161238a9-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/c7d04ce5e71efdfc7a4a78f7161238a9-Paper-Conference.pdf#page=9)

## Observation–State–Action Interface

Data recipe·proxy 학습 설정 → 상대 loss 순위; 로봇 행동 평가는 아니다.

## Evaluation Scope and Claim Boundary

LLM pretraining recipe와 random-feature model 이론을 다룬다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html).

## Why This Paper Is Here — Researcher Interpretation

GAP-N1에서 관측 정보 효과와 optimizer 설정 효과를 분리하는 필수 방법론 참조다.

## Verification Boundary

이론 적용 범위, loss와 task success 차이, tuning 총비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
