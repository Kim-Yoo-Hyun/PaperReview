# Can Vision-Language-Action Models Learn from Real-World Data Continually without Forgetting?

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Jiarun Zhu, Yijun Hong, Xiaoquan Sun, Zetian Xu, Qijun He, Haijier Chen, Zhiyong Wang, Mingqi Yuan, Wenjun Zeng, Jiayu Chen
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: continual-learning, replay, robot-learning
- Aliases: Real-world Continual VLA
- Official paper: https://arxiv.org/abs/2605.26820
- Venue verification: https://arxiv.org/abs/2605.26820
- Code/Project: https://github.com/Agentic-Intelligence-Lab/ContinualVLA
- Code: https://github.com/Agentic-Intelligence-Lab/ContinualVLA
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. arXiv v3를 확인했다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 단팔·양팔을 포함한 실제 조작 열 가지를 차례로 학습시켜 VLA의 새 기술 습득과 이전 기술 망각을 평가했다. [PDF 1쪽](https://arxiv.org/pdf/2605.26820v3#page=1)

## Core Idea and Contribution

- 순차 미세조정, 과거 경험 재생과 공동 학습을 실물 과제에서 비교하며 계산 예산을 통제했다. [PDF 3쪽](https://arxiv.org/pdf/2605.26820v3#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2605.26820v3#page=4)
- 재생 설정을 조정해 열 과제의 연속 학습에서 과거 기술 유지와 새 과제 적응을 함께 평가했다. [PDF 1쪽](https://arxiv.org/pdf/2605.26820v3#page=1) · [PDF 6쪽](https://arxiv.org/pdf/2605.26820v3#page=6)

## Observation–State–Action Interface

순차 task demonstration → VLA update → 기존/신규 task 실행.

## Evaluation Scope and Claim Boundary

단일 팔과 양팔 실환경 continual learning을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2605.26820). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

E1의 실환경 단순 baseline과 compute-matched 비교에 필요한 연구다.

## Verification Boundary

v3 변경점, normalization 범위, joint training compute, trial 수을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 연속 학습용 리플레이 버퍼 · src/openpi/training/replay_buffer.py [배포 파일](https://raw.githubusercontent.com/Agentic-Intelligence-Lab/ContinualVLA/d84ed7a811f95218e79ac5f0906465147ad7e1e3/src/openpi/training/replay_buffer.py)
- 데이터 — 단팔 PiPER 그릇 쌓기 시연 · data/chunk-000/episode_000000.parquet [배포 파일](https://huggingface.co/datasets/Ray0v0/cl-piper-single-stack-bowls/blob/f81ff5e07c31053b39e64aa621882d6d17705d52/data/chunk-000/episode_000000.parquet)
