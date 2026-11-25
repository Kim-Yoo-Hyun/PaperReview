# Policy Decorator: Model-Agnostic Online Refinement for Large Policy Model

> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

- Year/Venue: 2025 / ICLR
- Authors: Xiu Yuan, Tongzhou Mu, Stone Tao, Yunhao Fang, Mengke Zhang, Hao Su
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: residual-RL, Imitation Learning, controlled-exploration, manipulation
- Aliases: Policy Decorator
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html
- Code/Project: https://policydecorator.github.io/
- Code: https://github.com/tongzhoumu/policy_decorator
- Source audit: 2026-11-03 공식 venue/서지 재확인; 기존 GAP-VRL 검토의 지정 본문 final paper §4.1–4.3, selected Appendix B.5; project/code README를 반영. 선택 절 검토이며 전체 논문 정독·native 실행은 아님. Final paper의 지정 절만 검토했고 전체 36쪽 정독은 아니다. 공식 code 링크/README 확인과 실행 검증을 구분한다. 사용자 읽기 상태는 UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Policy Decorator는 사전학습 정책의 출력에 작은 보정을 더하는 강화학습으로 서로 다른 종류의 조작 정책을 개선한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 잔차 행동의 범위를 제한하고 학습 초기 탐색을 제약해 기본 정책의 유용한 동작을 보존하며 보정을 학습한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf#page=4)
- ManiSkill과 Adroit 시뮬레이션에서 Behavior Transformer와 Diffusion Policy 등을 기본 정책으로 사용해 조작 성공과 표본 효율을 비교했다. [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf#page=7)

## Observation–State–Action Interface

Base 행동 + 제한된 residual → 환경. Base 모델 계열별 적용 가능성과 학습된 residual weights의 전이는 서로 다른 주장이다.

## Evaluation Scope and Limitations

ManiSkill·Adroit의 8개 task, Behavior Transformer·Diffusion Policy에 적용한다. 보고된 성능 향상은 해당 설정이며 같은 residual의 base 교체 전이를 뜻하지 않는다.

Final paper의 지정 절만 검토했고 전체 36쪽 정독은 아니다. 공식 code 링크/README 확인과 실행 검증을 구분한다.

근거: [지정 본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf) — final paper §4.1–4.3, selected Appendix B.5; project/code README.

## Why This Paper Is Here — Researcher Interpretation

Frozen large policy+bounded residual의 핵심 비교 선행이다. 현재 후보의 scalar gain·탐색 schedule이라는 단순 대안을 놓치지 않도록 NEXT에 추가한다.

## 공개 자료

- 코드 — ManiSkill2에서 확산 기본 정책의 잔차 학습 · online/pi_dec_diffusion_maniskill2.py [배포 파일](https://raw.githubusercontent.com/tongzhoumu/policy_decorator/92ba9ba442587ae5989c286355ace2200a0537fb/online/pi_dec_diffusion_maniskill2.py)
- 가중치·학습 파라미터 — PegInsertionSide의 사전학습 Behavior Transformer · best.pt [배포 파일](https://drive.google.com/file/d/1w702JogWkpdb83W4fwVLFLc9dxjFqbSS/view)
- 데이터 — PegInsertionSide 전문가 시연 · trajectory.h5 [배포 파일](https://drive.google.com/file/d/1ZxqKdDr1D5ns92R7tKJhvJL5GN2zS73q/view)

## 판본과 출처

저자 표기·순서는 표제면 기준이다. [표제면](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf#page=1)
