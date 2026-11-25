# Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue: 2026 / NeurIPS
- Authors: Shuaijun Liu, Feiyang You, Chengyu Wu, Shuyang Hao, Chenglong Zhang, Jingyao Cai, Xingwei Chen, Li Sun, Ningxin Su
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, semantic-calibration, residual-policy, instruction-following
- Official paper: https://arxiv.org/abs/2609.23650
- Venue verification: https://neurips.cc/Downloads/2026
- Code/Project: https://nebulis-lab.com/BAS-VLA/
- Code: https://github.com/NEBULIS-Lab/BAS-VLA
- Source audit: 2026-11-05: §3–4, §5.1–5.3, Tables 6–7, Appendix A.2.1. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

BAS-VLA는 목표와 무관한 외형 변화에서는 기본 행동을 유지하고 과제의 의미가 바뀌면 새 목표에 맞춰 고정 VLA의 행동을 수정한다. [PDF 2쪽](https://arxiv.org/pdf/2609.23650v2#page=2)

## Core Idea and Contribution

- 원래 지시·의미를 유지한 지시·의미가 바뀐 지시로 행동 잔차를 학습하고, 시각적 방해와 의미 보존의 증거가 있을 때 선택적으로 보조 경로를 작동시킨다. [PDF 5쪽](https://arxiv.org/pdf/2609.23650v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.23650v2#page=6)
- 시뮬레이션의 네 목표 교체 과제에서 새 목표 성공률은 기본 정책 2.3%와 보정 정책 68.5%였고, 옛 목표 실행 및 그 밖의 실패를 별도로 집계했다. [PDF 9쪽](https://arxiv.org/pdf/2609.23650v2#page=9) · [PDF 10쪽](https://arxiv.org/pdf/2609.23650v2#page=10)

## Scope and Limitation

저자판 v2 표 5의 Break는 옛 목표 성공률이다. 새 목표 달성 여부는 실물 표 6과 시뮬레이션 표 7에서 확인할 수 있다. 네 가지 쉬운 교체 과제와 어려운 교체 과제의 결과도 구분해 읽어야 한다. [실물 표 6](https://arxiv.org/pdf/2609.23650v2#page=9) · [시뮬레이션 표 7](https://arxiv.org/pdf/2609.23650v2#page=10)

## Why This Paper Is Here — Researcher Interpretation

REVISION·FEEDBACK·residual 보정의 직접 충돌 선행. 변화에 반응하고 nuisance에 불변이라는 broad proposal의 재발명을 막는다.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2609.23650v1), §3–4, §5.1–5.3, Tables 6–7, Appendix A.2.1.

## 공개 자료

- 코드 — 지시의 의미 변화에 대응하는 보정 모듈 · bas_vla/breaking/residual_adapter.py [배포 파일](https://raw.githubusercontent.com/NEBULIS-Lab/BAS-VLA/51f0dab5b2edab6539f3bccda7a04b3cb1d52a6c/bas_vla/breaking/residual_adapter.py)
- 가중치·학습 파라미터 — 반대 의미 지시에 적용하는 행동 보정 어댑터 · adapter/residual_adapter.pt [배포 파일](https://huggingface.co/Shuaijun/BAS-VLA/resolve/d5e05c8b74bc8d8f1a831151a432f73158831f85/adapter/residual_adapter.pt)
