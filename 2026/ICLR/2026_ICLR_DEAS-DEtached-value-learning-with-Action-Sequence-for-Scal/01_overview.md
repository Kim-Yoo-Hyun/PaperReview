# DEAS: DEtached value learning with Action Sequence for Scalable Offline RL

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Authors: Changyeon Kim, Haeone Lee, Younggyo Seo, Kimin Lee, Yuke Zhu
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-RL, action-chunk, value-learning, VLA
- Aliases: DEAS
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/68b7f71467c83d5d32275c5acbf6b588-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/68b7f71467c83d5d32275c5acbf6b588-Abstract-Conference.html
- Code/Project: https://changyeon.site/deas/
- Code: https://github.com/csmile-1006/DEAS-Isaac-GR00T
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

DEAS는 긴 과제에서 여러 행동을 하나의 묶음으로 평가하면서 오프라인 자료 바깥 행동의 가치를 과대평가하는 문제를 줄인다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/68b7f71467c83d5d32275c5acbf6b588-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 행위자와 가치 학습을 분리해 데이터에 기록된 행동 묶음의 할인 수익과 후속 상태 가치로 비평가를 갱신한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/68b7f71467c83d5d32275c5acbf6b588-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/68b7f71467c83d5d32275c5acbf6b588-Paper-Conference.pdf#page=5)
- OGBench의 장기 과제와 RoboCasa·실물 조작에서 행동 묶음을 쓰는 오프라인 학습과 VLA 미세조정의 성능을 평가했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/68b7f71467c83d5d32275c5acbf6b588-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/68b7f71467c83d5d32275c5acbf6b588-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/68b7f71467c83d5d32275c5acbf6b588-Paper-Conference.pdf#page=9)

## Observation–State–Action Interface

Offline observation/action sequence → value estimation → sequence policy; VLA action chunk와 연결한다.

## Evaluation Scope and Claim Boundary

OGBench, RoboCasa Kitchen과 실세계 조작의 VLA 확장을 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/68b7f71467c83d5d32275c5acbf6b588-Abstract-Conference.html) · [저자 project/code](https://changyeon.site/deas/) · [공식 code](https://github.com/csmile-1006/DEAS-Isaac-GR00T). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Chunk-aware actor-critic과 공유 표현 연구에서 반드시 넘어야 하는 직접 offline RL 선행이다.

## Verification Boundary

value target gradient 경계, OOD action 처리, 실로봇 데이터·환경 예산을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · GR00T에 연결한 DEAS 비평가 · gr00t/model/action_head/deas_critic.py [배포 파일](https://raw.githubusercontent.com/csmile-1006/DEAS-Isaac-GR00T/1bfc8464c4d28574cbd2e699342791c7e4d80028/gr00t/model/action_head/deas_critic.py)
- 데이터 · RoboCasa CoffeeSetupMug 시연 궤적 · demos/CoffeeSetupMug/data/chunk-000/episode_000000.parquet [배포 파일](https://huggingface.co/datasets/changyeon/deas_robocasa/resolve/b929891bd6e18ec5cec46d20e793f78e5d4d0359/demos/CoffeeSetupMug/data/chunk-000/episode_000000.parquet)
