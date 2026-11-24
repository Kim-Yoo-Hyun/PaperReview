# Dichotomous Diffusion Policy Optimization

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / ICLR
- Authors: Ruiming Liang, Yinan Zheng, Kexin ZHENG, Tianyi Tan, Jianxiong Li, Liyuan Mao, Zhihao Wang, Guang Chen, Hangjun Ye, Jingjing Liu, Jinqiao Wang, Xianyuan Zhan
- 저자 판본: 학회 서지와 표기가 다른 저자의 인쇄명은 Kexin Zheng이다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/64a0192102e1421a2b2c15ae0bdb9f3a-Paper-Conference.pdf#page=1) · [학회 서지](https://proceedings.iclr.cc/paper_files/paper/2026/hash/64a0192102e1421a2b2c15ae0bdb9f3a-Abstract-Conference.html)
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: diffusion-policy, offline-RL, offline-to-online-RL
- Aliases: DIPOLE
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/64a0192102e1421a2b2c15ae0bdb9f3a-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/64a0192102e1421a2b2c15ae0bdb9f3a-Abstract-Conference.html
- Code/Project: https://lrmbbj.github.io/DIPOLE/
- Code: https://github.com/LRMbbj/DIPOLE
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/64a0192102e1421a2b2c15ae0bdb9f3a-Paper-Conference.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

DIPOLE은 보상이 높은 행동과 낮은 행동을 나타내는 두 확산 정책을 학습해, 추론 중 어느 쪽을 얼마나 선호할지 조절한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/64a0192102e1421a2b2c15ae0bdb9f3a-Paper-Conference.pdf#page=1) · [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/64a0192102e1421a2b2c15ae0bdb9f3a-Paper-Conference.pdf#page=3)

## Core Idea and Contribution

- 정규화된 정책 개선 문제를 두 가중 회귀 문제로 바꾸고, 추론 시 두 정책의 점수를 선형 결합해 행동을 생성한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/64a0192102e1421a2b2c15ae0bdb9f3a-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/64a0192102e1421a2b2c15ae0bdb9f3a-Paper-Conference.pdf#page=5)
- ExORL과 OGBench에서 오프라인 및 오프라인에서 온라인으로 전환하는 학습을 평가하고 점수 결합 강도의 영향을 비교했다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/64a0192102e1421a2b2c15ae0bdb9f3a-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/64a0192102e1421a2b2c15ae0bdb9f3a-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/64a0192102e1421a2b2c15ae0bdb9f3a-Paper-Conference.pdf#page=8)

## Observation–State–Action Interface

Offline transition → 두 diffusion score → 결합된 action generation.

## Evaluation Scope and Claim Boundary

ExORL·OGBench의 offline 및 offline-to-online RL과 NAVSIM 자율주행 VLA를 평가한다. 주행 VLA 결과를 조작 VLA의 근거로 확대하지 않는다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/64a0192102e1421a2b2c15ae0bdb9f3a-Abstract-Conference.html) · [저자 project/code](https://lrmbbj.github.io/DIPOLE/) · [공식 code](https://github.com/LRMbbj/DIPOLE).

## Why This Paper Is Here — Researcher Interpretation

Diffusion RL 안정화의 알고리즘 대안으로 참고하며 로봇 조작 효과는 별도 검증한다.

## Verification Boundary

두 모델의 추가 계산량, 추론 결합 계수 선택, manipulation 전이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
