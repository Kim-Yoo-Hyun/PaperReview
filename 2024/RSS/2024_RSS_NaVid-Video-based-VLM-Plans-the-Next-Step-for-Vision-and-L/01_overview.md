# NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Jiazhao Zhang, Kunyu Wang, Rongtao Xu, Gengze Zhou, Yicong Hong, Xiaomeng Fang, Qi Wu, Zhizheng Zhang, He Wang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: video-memory, VLN-CE, sim-to-real
- Aliases: NaVid
- Official paper: https://roboticsproceedings.org/rss20/p079.html
- Venue verification: https://roboticsproceedings.org/rss20/p079.html
- Code/Project: https://pku-epic.github.io/NaVid/
- Code: https://github.com/jzhzhang/NaVid-VLN-CE
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

Language instruction을 따라 unseen environment를 이동할 때 scene generalization과 sim-to-real gap을 줄이는 문제다.

## Core Idea and Contribution

Monocular RGB video history를 VLM context로 처리하여 다음 navigation action을 출력한다.

## Observation–State–Action Interface

Language instruction + 누적 RGB video → next-step navigation action; map·odometry·depth 입력 없이 동작하는 formulation을 제안한다.

## Evaluation Scope and Claim Boundary

RSS abstract는 continuous navigation simulation과 실제 환경의 cross-dataset/sim-to-real 평가를 명시한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss20/p079.html) · [저자 project/code](https://pku-epic.github.io/NaVid/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Foundation lineage. RGB video history에서 next action을 출력하는 navigation VLM이다. Uni-NaVid/StreamVLN을 비교할 때 선행 interface를 보충한다. **NaVILA 및 Uni-NaVid와 다른 논문**이다.

## Verification Boundary

Camera-only 가정, action discretization, history truncation, 실제 low-level controller을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
