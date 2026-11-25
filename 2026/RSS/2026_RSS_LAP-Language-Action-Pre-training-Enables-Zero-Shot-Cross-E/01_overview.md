# LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Lihan Zha, Asher J. Hancock, Mingtong Zhang, Tenny Yin, Yixuan Huang, Dhruv Shah, Allen Z. Ren, Anirudha Majumdar
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-interface, cross-embodiment
- Aliases:
- Official paper: https://www.roboticsproceedings.org/rss22/p203.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p203.html
- Code/Project: https://lap-vla.github.io/
- Code: https://github.com/lihzha/lap
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

LAP는 저수준 행동을 자연어로 표현해 여러 로봇의 데이터를 사전학습하고 처음 보는 단팔 로봇에서 추가 학습 없는 전이를 시험한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p203.pdf#page=1)

## Core Idea and Contribution

- 별도 학습형 행동 토크나이저 없이 행동과 질의응답을 같은 언어 형식으로 표현해 공동 학습이 가능하게 했다. [PDF 2쪽](https://www.roboticsproceedings.org/rss22/p203.pdf#page=2) · [PDF 3쪽](https://www.roboticsproceedings.org/rss22/p203.pdf#page=3)
- 새 조작기에서 실행한 성공률과 학습에서 제외한 데이터의 행동 예측 오차를 구분해 교차 로봇 전이를 평가했다. [PDF 5쪽](https://www.roboticsproceedings.org/rss22/p203.pdf#page=5) · [PDF 8쪽](https://www.roboticsproceedings.org/rss22/p203.pdf#page=8)

## Observation–State–Action Interface

영상·지시 → 언어 action → 로봇별 실행.

## Evaluation Scope and Claim Boundary

새 embodiment 전이와 robot adaptation 평가를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p203.html). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Cross-embodiment VLA interface를 비교할 최신 직접 선행이다.

## Verification Boundary

zero-shot 정의, robot-specific mapping, pretraining 중복을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문 대조

저자 표기와 순서는 이 판본의 표제면을 따른다. [표제면](https://www.roboticsproceedings.org/rss22/p203.pdf#page=1)

## 공개 자료

- 코드 — 언어 행동 예측 정책 학습 · scripts/train.py [배포 파일](https://raw.githubusercontent.com/lihzha/lap/3958d1466d5b92445b67de7d4202c19608ad4d56/scripts/train.py)
- 가중치 — LAP-3B 파라미터 샤드 · params/ocdbt.process_0/d/2a547295477492a7426cdd99bfd9c7a8 [배포 파일](https://huggingface.co/lihzha/LAP-3B/blob/601db9c1ab4bcaf6dddb160c7b2dec589a67b730/params/ocdbt.process_0/d/2a547295477492a7426cdd99bfd9c7a8)
