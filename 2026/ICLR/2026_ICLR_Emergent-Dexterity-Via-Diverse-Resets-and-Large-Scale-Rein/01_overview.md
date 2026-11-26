# Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Authors: Patrick Yin, Tyler Westenbroek, Zhengyu Zhang, Ignacio Dagnino, Eeshani Shilamkar, Numfor Mbiziwo-Tiapo, Simran Bagaria, Xinlei Liu, Galen Mullins, Andrey Kolobov, Abhishek Gupta
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: dexterous-manipulation, reset-distribution, sim-to-real, reinforcement-learning
- Aliases: OmniReset
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/8e3e3488623d64c493a7f11cf1f2e49f-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/8e3e3488623d64c493a7f11cf1f2e49f-Abstract-Conference.html
- Code/Project: https://weirdlabuw.github.io/omnireset/
- Code: https://github.com/UW-Lab/UWLab
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

OmniReset은 시뮬레이션에서 조작을 시작하는 상태를 다양하게 만들어 긴 접촉 과제의 여러 단계에서 강화학습 정책이 경험을 얻도록 한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8e3e3488623d64c493a7f11cf1f2e49f-Paper-Conference.pdf#page=1) · [PDF 2쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8e3e3488623d64c493a7f11cf1f2e49f-Paper-Conference.pdf#page=2)

## Core Idea and Contribution

- 물체에 접근하기 전, 이미 파지한 상태, 목표에 가까운 상태 등 물리적으로 가능한 시작 조건을 생성해 단일 보상으로 훈련한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8e3e3488623d64c493a7f11cf1f2e49f-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8e3e3488623d64c493a7f11cf1f2e49f-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8e3e3488623d64c493a7f11cf1f2e49f-Paper-Conference.pdf#page=6)
- 시뮬레이션에서 배운 정책을 영상 기반 정책으로 증류한 뒤 실제 핀 삽입에서 추가 실물 학습 없이 성공률과 재시도 행동을 평가했다. [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8e3e3488623d64c493a7f11cf1f2e49f-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8e3e3488623d64c493a7f11cf1f2e49f-Paper-Conference.pdf#page=10)

## Observation–State–Action Interface

다양한 simulator reset → RL 정책 → 시각 정책 증류 → 실제 로봇.

## Evaluation Scope and Claim Boundary

장기 dexterous manipulation과 넓은 초기 조건, zero-shot 실로봇 전이를 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8e3e3488623d64c493a7f11cf1f2e49f-Abstract-Conference.html) · [저자 project/code](https://omnireset.github.io/). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA-RL의 탐색 개선이 정책 방법보다 reset coverage에서 오는지 분리할 중요한 대조군이다.

## Verification Boundary

reset 생성의 물리 유효성·특권 정보, 증류 비용, 초기 조건 분할을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · OmniReset의 UR5e·Robotiq 조립 시작 상태 설정 · source/uwlab_tasks/uwlab_tasks/manager_based/manipulation/omnireset/config/ur5e_robotiq_2f85/reset_states_cfg.py [배포 파일](https://raw.githubusercontent.com/UW-Lab/UWLab/2b40afb9693d46bc1b1a91c7ba95e03c04daa60d/source/uwlab_tasks/uwlab_tasks/manager_based/manipulation/omnireset/config/ur5e_robotiq_2f85/reset_states_cfg.py)
