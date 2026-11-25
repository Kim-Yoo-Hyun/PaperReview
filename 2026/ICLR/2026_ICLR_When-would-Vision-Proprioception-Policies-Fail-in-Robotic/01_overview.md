# When would Vision-Proprioception Policies Fail in Robotic Manipulation?

> Evidence maturity: `ABSTRACT_CHECKED`. 아래의 요약·기여는 인용한 원문 쪽에서 추가 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Authors: Jingxian Lu, Wenke Xia, Yuxuan Wu, Zhiwu Lu, Di Hu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Imitation Learning, proprioception, modality imbalance, manipulation
- Aliases: GAP
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/2b3bb2c95195130977a51b3bb251c40a-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/2b3bb2c95195130977a51b3bb251c40a-Abstract-Conference.html
- Code/Project: https://gewu-lab.github.io/GAP/
- Code: https://github.com/GeWu-Lab/GAP
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

조작 과정을 나눠 시각과 고유수용 상태에 대한 정책의 의존성을 측정하고 모달리티 불균형을 완화한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2b3bb2c95195130977a51b3bb251c40a-Paper-Conference.pdf#page=3)

## Core Idea and Contribution

- 물체와의 상대운동이 달라지는 단계에서 입력별 기여도를 분석하고 학습 시 기울기를 조정한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2b3bb2c95195130977a51b3bb251c40a-Paper-Conference.pdf#page=4)
- 시뮬레이션 조작과 실물 단팔·양팔에서 기존 시각운동 정책과 비교했다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2b3bb2c95195130977a51b3bb251c40a-Paper-Conference.pdf#page=6)

## Observation–State–Action Interface

영상·proprioception → manipulation action; 학습 중 phase-guided gradient 조정.

## Evaluation Scope and Claim Boundary

Simulation·실제 single/dual-arm 및 Octo 적용을 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2b3bb2c95195130977a51b3bb251c40a-Abstract-Conference.html) · [저자 project/code](https://gewu-lab.github.io/GAP/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D1에서 modality dominance를 새 발견으로 주장하지 않도록 추가한 직접 NEXT다.

## Verification Boundary

phase 추정 신호, task split, native Octo 코드·checkpoint을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 모달리티별 기울기 조정 · gap/gap.py [배포 파일](https://raw.githubusercontent.com/GeWu-Lab/GAP/2f605436c68eedf328c05520d52877604af730d3/gap/gap.py)
