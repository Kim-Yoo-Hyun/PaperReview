# Is Your Imitation Learning Policy Better than Mine? Policy Comparison with Near-Optimal Stopping

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / RSS
- Authors: David Snyder, Asher James Hancock, Apurva Badithela, Emma Dixon, Patrick Miller, Rares Andrei Ambrus, Anirudha Majumdar, Masha Itkina, Haruki Nishimura
- Category: Benchmarks and Datasets
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: robot-evaluation, Benchmark, policy-comparison
- Aliases: STEP
- Official paper: https://roboticsproceedings.org/rss21/p077.html
- Venue verification: https://roboticsproceedings.org/rss21/p077.html
- Code/Project: https://tri-ml.github.io/step/
- Code: https://github.com/TRI-ML/sequentialized_barnard_tests
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 로봇 조작 정책 두 개를 비교할 때 중간 결과를 보고 시행을 종료해도 통계적 오류를 통제할 수 있는 순차 검정을 제안한다. [PDF 1쪽](https://roboticsproceedings.org/rss21/p077.pdf#page=1)

## Core Idea and Contribution

- 두 정책 사이의 구별 난이도에 맞춰 비교에 필요한 시행 수를 조절하는 정지 기준을 구성했다. [PDF 3쪽](https://roboticsproceedings.org/rss21/p077.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss21/p077.pdf#page=4)
- 수치 시뮬레이션과 실제 조작에서 비교 결론의 정확도와 검정력을 유지하면서 요구되는 시행 수를 기존 방법과 비교했다. [PDF 6쪽](https://roboticsproceedings.org/rss21/p077.pdf#page=6) · [PDF 8쪽](https://roboticsproceedings.org/rss21/p077.pdf#page=8)

## Observation–State–Action Interface

Policy별 binary success trial → sequential evidence → 중단/선택.

## Evaluation Scope and Claim Boundary

Simulation 및 실제 policy 비교를 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss21/p077.html). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

C6의 trial budget·통계적 중단에 대한 표준 직접 기준이다.

## Verification Boundary

독립성, indifference region, 오류 확률, 다중 비교 처리을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 순차적 정책 비교 검정 · sequentialized_barnard_tests/step.py [배포 파일](https://raw.githubusercontent.com/TRI-ML/sequentialized_barnard_tests/3ae1623906f82fe472a352ed4a6b8e4a712f1f3d/sequentialized_barnard_tests/step.py)
- 데이터 — 쏟은 액체 청소 정책의 시행별 비교 예제 · data/example_clean_spill/TRI_CLEAN_SPILL_v4.npy [배포 파일](https://raw.githubusercontent.com/TRI-ML/sequentialized_barnard_tests/3ae1623906f82fe472a352ed4a6b8e4a712f1f3d/data/example_clean_spill/TRI_CLEAN_SPILL_v4.npy)
