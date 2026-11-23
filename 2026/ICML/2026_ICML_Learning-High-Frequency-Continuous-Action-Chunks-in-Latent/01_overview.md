# Learning High-Frequency Continuous Action Chunks in Latent Space

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICML
- Authors: Kunyun Wang, Yuhang Zheng, Yupeng Zheng, Jieru Zhao, Wenchao Ding
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-chunking, feedback, control-frequency
- Aliases: RTR
- Official paper: https://proceedings.mlr.press/v306/wang26lj.html
- Venue verification: https://proceedings.mlr.press/v306/wang26lj.html
- Code/Project: https://github.com/tars-robotics/RTR
- Code: https://github.com/tars-robotics/RTR
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 고주파 행동 묶음을 잠재 공간에서 학습하고 비동기 실행 중 인접한 두 묶음의 경계를 부드럽게 연결한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/wang26lj/wang26lj.pdf#page=1)

## Core Idea and Contribution

- VAE로 연속 행동을 잠재 표현으로 압축하고 Reuse-then-Refine으로 기존 묶음의 일부를 재사용해 다음 묶음을 보정한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/wang26lj/wang26lj.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/wang26lj/wang26lj.pdf#page=5)
- 데이터 기반 비교와 실제 접촉 조작 세 과제에서 움직임의 연속성 및 과제 수행을 평가했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/wang26lj/wang26lj.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/wang26lj/wang26lj.pdf#page=7)

## Observation–State–Action Interface

관측 → latent chunk → 고주파 action decoding·경계 보정.

## Evaluation Scope and Claim Boundary

실제 contact manipulation과 여러 policy backbone 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/wang26lj.html) · [저자 project/code](https://github.com/tars-robotics/RTR). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

E2에서 고주파 표현과 controller 변경을 분리할 직접 기준이다.

## Verification Boundary

controller mode, interpolation baseline, VAE 데이터, refinement timing을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
