# NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation

> Evidence maturity: `ABSTRACT_CHECKED`. 개요 전반은 초록 수준이며, 아래 요약과 두 기여에는 확인한 본문 위치를 표시했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / RSS
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
- Source audit: 2026-11-23 요약과 핵심 기여 두 개를 원문 본문에 대조했다. 나머지 세부 분석은 기존 초록·공식 자료에 근거한다.

## Problem and Importance

NaVid는 언어 지시와 로봇의 단안 RGB 영상 이력으로 다음 이동 행동을 결정하는 비디오 기반 내비게이션 모델이다. [PDF 1쪽](https://roboticsproceedings.org/rss20/p079.pdf#page=1)

## Core Idea and Contribution

- 과거와 현재 영상을 시공간 문맥으로 인코딩하고 연속 환경에서 수집한 행동 계획·지시 추론 예제와 웹 데이터를 함께 사용한다. [PDF 4쪽](https://roboticsproceedings.org/rss20/p079.pdf#page=4) · [PDF 5쪽](https://roboticsproceedings.org/rss20/p079.pdf#page=5)
- 처음 보는 R2R 환경, 다른 데이터셋, 실제 로봇에서 결과를 비교해 지도·깊이 입력 없이 가능한 전이를 평가했다. [PDF 7쪽](https://roboticsproceedings.org/rss20/p079.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss20/p079.pdf#page=8)

## Observation–State–Action Interface

Language instruction + 누적 RGB video → next-step navigation action; map·odometry·depth 입력 없이 동작하는 formulation을 제안한다.

## Evaluation Scope and Claim Boundary

RSS abstract는 continuous navigation simulation과 실제 환경의 cross-dataset/sim-to-real 평가를 명시한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss20/p079.html) · [저자 project/code](https://pku-epic.github.io/NaVid/). 그 밖의 수치, 기준선의 비교 조건, 실패 범위는 별도 대조가 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Foundation lineage. RGB video history에서 next action을 출력하는 navigation VLM이다. Uni-NaVid/StreamVLN을 비교할 때 선행 interface를 보충한다. **NaVILA 및 Uni-NaVid와 다른 논문**이다.

## Verification Boundary

Camera-only 가정, action discretization, history truncation, 실제 low-level controller을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문과 공개 자료

- 코드 — NaVid의 언어·영상 내비게이션 평가 · run.py [배포 파일](https://raw.githubusercontent.com/jzhzhang/NaVid-VLN-CE/ce2f804a43fb23f1d52431ec24be1acf74c3f4f4/run.py)
- 가중치 — R2R·RxR로 학습한 원래 NaVid 모델 · navid-7b-full-224-video-fps-1-grid-2-r2r-rxr-training-split/pytorch_model-00001-of-00002.bin [배포 파일](https://huggingface.co/Jzzhang/NaVid/blob/1f96dbdc5c24594220395beeb447cbee728a84a9/navid-7b-full-224-video-fps-1-grid-2-r2r-rxr-training-split/pytorch_model-00001-of-00002.bin)
