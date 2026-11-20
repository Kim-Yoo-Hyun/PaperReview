# Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue
- Authors: Shuaijun Liu, Feiyang You, Chengyu Wu, Shuyang Hao, Chenglong Zhang, Jingyao Cai, Xingwei Chen, Li Sun, Ningxin Su
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, semantic-calibration, residual-policy, instruction-following
- Official paper: https://arxiv.org/abs/2609.23650
- Venue verification: https://neurips.cc/Downloads/2026
- Code/Project: https://nebulis-lab.com/BAS-VLA/
- Code: https://github.com/NEBULIS-Lab/BAS-VLA
- Source audit: 2026-11-05: §3–4, §5.1–5.3, Tables 6–7, Appendix A.2.1. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD.

## Problem and Contribution

외관만 변할 때의 안정성과 실제 목표가 바뀔 때의 행동 전환을 구분한다.

동결 VLA 행동에 instruction-conditioned residual을 더한다. Clean/control 모방·일관성과 semantic-break margin을 함께 학습하고 preserving 보조 경로는 evidence gate로 제한한다.

## Scope and Limitation

Break 열은 옛 목표 성공률이므로 낮다고 새 목표 성공이 아니다. Margin 분리만으로 물리적 성공이 보장되지 않는다. 최종 proceedings와 읽은 v1의 동일성·공개 구현은 미확인.

## Why This Paper Is Here — Researcher Interpretation

REVISION·FEEDBACK·residual 보정의 직접 충돌 선행. 변화에 반응하고 nuisance에 불변이라는 broad proposal의 재발명을 막는다.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2609.23650v1), §3–4, §5.1–5.3, Tables 6–7, Appendix A.2.1.
