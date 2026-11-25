# Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Justin Tien-Smith, Matthew Pidden, Rolandos Alexandros Potamias
- Category: Benchmarks and Datasets
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: manipulation, VLA, spatial-grounding, counting, real-robot-benchmark
- Aliases: Spa-Bench (robotics)
- Official paper: https://arxiv.org/abs/2610.12696
- Venue verification: https://arxiv.org/abs/2610.12696
- Code/Project: https://justintiensmith.github.io/Spa-Bench/
- Code: not_identified
- Source audit: 2026-11-01 공식 서지/abstract·project/code 소개 확인. arXiv v1 및 저자 project 확인. Robotics 논문이며 동명 ICLR 2025 smartphone-agent benchmark와 다르다. 학회 채택은 확인되지 않아 arXiv로 등록. 신규 노트는 보수적으로 abstract/project 범위이며, 기존 SET의 지정 본문/code 감사는 별도 source ledger를 따른다. 정독·native 실행을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Spa-Bench는 익숙한 구성 요소를 낯선 배치로 옮겨 실제 로봇 정책의 공간 관계 이해를 검사한다. [PDF 1쪽](https://arxiv.org/pdf/2610.12696v1#page=1)

## Core Idea and Contribution

- SO-101의 여섯 과제에서 물체와 관계의 조합을 통제하고 직접적인 행동 지시를 따르는 조건을 두어 물리 실행 능력을 비교했다. [PDF 3쪽](https://arxiv.org/pdf/2610.12696v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2610.12696v1#page=4)
- 평가를 모두 마친 세 정책에서는 같은 조작을 직접 지시했을 때 성공률이 28.3~40.0%포인트 높아져 공간 관계 해석과 물리 실행을 구분할 근거를 얻었다. [PDF 6쪽](https://arxiv.org/pdf/2610.12696v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2610.12696v1#page=7)

## Observation–State–Action Interface

실제 로봇의 관측·공간 언어 지시 → VLA 행동 → 목표별 채점. Counting과 no-action을 별도 진단으로 포함한다.

## Evaluation Scope and Claim Boundary

저자는 여섯 tabletop task와 여러 VLA의 실제 rollout을 보고한다. 전체 protocol을 수행한 모델과 부분 baseline이 다르므로 분모를 섞지 않는다. 공개 project의 model/data 링크는 확인했으나 독립 실행 code URL은 확인하지 못했다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.12696) · [저자 project/code](https://justintiensmith.github.io/Spa-Bench/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

집합·수량 후보의 가장 직접적인 counting/직접 지시 비교 선행이다. 알려진 공간 grounding 실패를 새 공백으로 과장하지 않도록 NEXT에 등록하며 preprint 경계를 유지한다.

## Verification Boundary

ID/OOD support, 모델별 완료 범위와 trial 분모, 직접 지시의 정보량, 최종 수량·무행동 채점, 공개 data/코드의 실제 가용 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 가중치·학습 파라미터 — 언어 백본을 고정한 GR00T 평가 모델 · model.safetensors [배포 파일](https://huggingface.co/Spa-Bench/spa-bench-model-groot-n1-7-frozen-llm-epoch-12/resolve/decd6df3bfebc6dff80150fc7d0bfd0bc794cf35/model.safetensors)
- 데이터 — 실제 SO-101에서 수집한 π0.5 평가 궤적 · data/chunk-000/file-000.parquet [배포 파일](https://huggingface.co/datasets/Spa-Bench/spa-bench-eval-rollouts-pi-0-5-full/resolve/b04f54b130ea84f25ab711b6dece329b3eaa8245/data/chunk-000/file-000.parquet)
