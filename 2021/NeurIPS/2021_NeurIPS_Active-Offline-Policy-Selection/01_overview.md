# Active Offline Policy Selection

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2021 / NeurIPS
- Authors: Ksenia Konyushkova, Yutian Chen, Tom Le Paine, Caglar Gulcehre, Cosmin Paduraru, Daniel J Mankowitz, Misha Denil, Nando de Freitas
- 저자 판본: 학회 서지에는 Ksenia Konyushova, Thomas Paine, Daniel J. Mankowitz로 실려 있다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2021/file/cec2346566ba8ecd04bfd992fd193fb3-Paper.pdf#page=1) · [학회 서지](https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html)
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: RL, evaluation, learning-foundation
- Aliases: AOPS
- Official paper: https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html
- Venue verification: https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://proceedings.neurips.cc/paper_files/paper/2021/file/cec2346566ba8ecd04bfd992fd193fb3-Paper.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

A-OPS는 고정 로그가 있고 새 시행 예산은 적을 때, 후보 정책 중 어느 것을 다음으로 실행해야 좋은 정책을 찾을지 결정한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2021/file/cec2346566ba8ecd04bfd992fd193fb3-Paper.pdf#page=1) · [PDF 3쪽](https://proceedings.neurips.cc/paper_files/paper/2021/file/cec2346566ba8ecd04bfd992fd193fb3-Paper.pdf#page=3)

## Core Idea and Contribution

- 오프폴리시 가치 추정치를 가우시안 과정에 반영하고 관측 상태에서의 행동 차이로 정책 간 유사도를 계산해 새 평가 결과를 다른 후보에도 반영한다. [PDF 3쪽](https://proceedings.neurips.cc/paper_files/paper/2021/file/cec2346566ba8ecd04bfd992fd193fb3-Paper.pdf#page=3) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2021/file/cec2346566ba8ecd04bfd992fd193fb3-Paper.pdf#page=4)
- 연속제어와 Atari 등을 대상으로 로그만 쓰는 선택, 온라인 평가, 두 정보를 함께 쓰는 선택의 정책 선택 성능을 비교했다. [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2021/file/cec2346566ba8ecd04bfd992fd193fb3-Paper.pdf#page=6) · [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2021/file/cec2346566ba8ecd04bfd992fd193fb3-Paper.pdf#page=7) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2021/file/cec2346566ba8ecd04bfd992fd193fb3-Paper.pdf#page=8)

## Observation–State–Action Interface

Logged data·policy 후보·평가 결과 → 다음 policy 선택.

## Evaluation Scope and Claim Boundary

여러 benchmark와 다수 후보 정책의 selection 효율을 보고한다.

근거: [공식 paper/abstract](https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html).

## Why This Paper Is Here — Researcher Interpretation

C6에서 OPE+능동 online 평가라는 넓은 방법의 직접 선행이다.

## Verification Boundary

kernel 입력, adaptive reuse, candidate chronology, online budget을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
