# Autonomous Improvement of Instruction Following Skills via Foundation Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CoRL
- Authors: Zhiyuan Zhou, Pranav Atreya, Abraham Lee, Homer Rich Walke, Oier Mees, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: autonomous-data, instruction-following, goal-conditioned-policy, hindsight-learning
- Aliases: SOAR
- Official paper: https://proceedings.mlr.press/v270/zhou25b.html
- Venue verification: https://proceedings.mlr.press/v270/zhou25b.html
- Code/Project: https://soar-autonomous-improvement.github.io/
- Code: https://github.com/soar-autonomous-improvement/code-release
- Source audit: 2026-11-07: 공식 metadata/abstract·저자 project/README 확인. CoRL 행사 연도 2024, PMLR270 발행 연도 2025를 구분. 공식 proceedings와 저자 project/code 확인; OpenReview forum은 challenge로 본문 접근 실패. Project의 Data Coming Soon과 abstract의 공개 주장을 구분하여 data_status는 미확인으로 둔다. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 로봇이 자율 수집한 상호작용을 시각언어 모델로 평가해 새로운 장면에서 지시 이행 능력을 개선한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25b/zhou25b.pdf#page=1)

## Core Idea and Contribution

- 언어에서 목표 영상을 만드는 단계와 로봇이 영상 목표를 달성하는 단계를 나눠 사람의 궤적별 주석 없이 자율 자료를 활용한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25b/zhou25b.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25b/zhou25b.pdf#page=4)
- 실제 탁상 환경에서 자율 자료 사용 전후의 성공을 비교하고 다섯 환경에서 수집한 약 3만 500개 궤적의 구성을 제시했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25b/zhou25b.pdf#page=6) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25b/zhou25b.pdf#page=8) · [PDF 20쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25b/zhou25b.pdf#page=20)

## Observation–State–Action Interface

언어 → image subgoal → goal-conditioned robot action. 학습 데이터 수집/평가와 배포 정책의 역할을 분리한다.

## Evaluation Scope and Claim Boundary

공식 abstract는 새로운 실세계 환경의 정책 개선과 5개 tabletop 환경에서 수집한 25K trajectory 데이터 공개를 설명한다. Project는 9개 평가 scene을 설명하므로 두 숫자의 분모를 합치지 않는다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/zhou25b.html) · [저자 project/code](https://soar-autonomous-improvement.github.io/) · [공식 code](https://github.com/soar-autonomous-improvement/code-release). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

자율 수집·hindsight 학습의 시스템 선행. 단일 VLA 내부 RL과 분해된 image-goal 정책을 비교할 대조이며 fleet를 cross-embodiment로 오인하지 않게 한다.

## Verification Boundary

수집 scene과 평가 scene의 분리, 데이터 release의 실제 접근성, 의미 이해와 운동 능력 개선의 기여, 서로 다른 정책 정보량을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
