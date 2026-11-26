# A process-centric manipulation taxonomy for the organization, classification and synthesis of tactile robot skills

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2025 / Nature Machine Intelligence
- Authors: Lars Johannsmeier, Samuel Schneider, Yanan Li, Etienne Burdet, Sami Haddadin
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, skill-composition, process-specification, force control
- Aliases: TMS
- Official paper: https://www.nature.com/articles/s42256-025-01045-3
- Venue verification: https://www.nature.com/articles/s42256-025-01045-3
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://www.nature.com/articles/s42256-025-01045-3.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다.

## Problem and Importance

전문가가 명시한 조작 공정의 요구 조건에서 필요한 촉각 로봇 스킬을 선택하고 조합하는 공정 중심 분류법을 제안했다. [PDF 1쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=1) · [PDF 2쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=2)

## Core Idea and Contribution

- 요구하는 힘·모멘트의 시간 변화, 물체 사이의 공간 관계, 필요한 공정 동작에 따라 분류를 좁혀 스킬을 선택한다. [PDF 2쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=2) · [PDF 3쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=3) · [PDF 4쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=4)
- 산업 응용의 서로 다른 스킬 28개에 분류를 적용하고, 목표 자세를 교란한 조건에서 과제별 실행 시간과 접촉 토크 등의 결과를 보고했다. [PDF 5쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=5) · [PDF 6쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=6) · [PDF 7쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=7)

## Observation–State–Action Interface

공정 요구 → skill specification → policy/controller → 접촉 feedback.

## Evaluation Scope and Claim Boundary

28은 구현한 조작 스킬 수다. 표 1은 작업별 실행 시간과 접촉 토크의 강건성을 따로 싣는다. 원통 삽입의 두 열은 각각 94%와 92%다. [PDF 5쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=5) · [PDF 6쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=6) · [PDF 7쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=7)

근거: [공식 paper/abstract](https://www.nature.com/articles/s42256-025-01045-3).

## 검색 태그 근거

과정을 힘·모멘트의 변화와 물체 간 공간 관계로 기술해 조작 기술을 선택한다. 실물 평가에서는 힘·임피던스 제어와 접촉 토크를 다룬다. 이 논문의 tactile skill이라는 용어만으로 피부형 촉각 센서를 정책 입력으로 지정할 수 없다. [원문 2쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=2) · [원문 9쪽](https://www.nature.com/articles/s42256-025-01045-3.pdf#page=9)

## Why This Paper Is Here — Researcher Interpretation

언어 기반 skill 조합과 전문가가 명시한 물리적 요구·종료 조건을 비교할 참조다.

## Verification Boundary

전문가 specification 비용, grasp/접촉 가정, skill 선택과 저수준 controller 기여을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
