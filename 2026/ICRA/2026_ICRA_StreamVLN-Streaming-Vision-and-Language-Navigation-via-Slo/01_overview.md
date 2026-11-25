# StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICRA
- Authors: Meng Wei, Chenyang Wan, Xiqian Yu, Tai Wang, Xiaohan Mao, Chenming Zhu, Wenzhe Cai, Hanqing Wang, Yilun Chen, Xihui Liu, Jiangmiao Pang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: streaming-memory, VLN, latency
- Aliases: StreamVLN
- Official paper: https://arxiv.org/abs/2507.05240
- Venue verification: https://github.com/InternRobotics/StreamVLN
- Code/Project: https://streamvln.github.io/
- Code: https://github.com/InternRobotics/StreamVLN
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. ICRA 2026 status는 저자 공식 자료 확인; IEEE proceedings 직접 검증 미완료.

## Problem and Importance

긴 navigation video history를 처리하면서 action generation의 latency와 context 크기를 제한하는 문제다.

## Core Idea and Contribution

Fast streaming dialogue context와 slow-updating memory를 결합하고 3D-aware token pruning으로 history를 압축한다.

## Observation–State–Action Interface

Interleaved vision/language/action stream → bounded context memory → navigation action.

## Evaluation Scope and Claim Boundary

저자 공식 project는 VLN-CE benchmark와 여러 실제 환경의 장기 navigation을 설명한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2507.05240) · [저자 project/code](https://streamvln.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. Fast action context와 slow history memory를 결합한다. NaVid/Uni-NaVid 이후 긴 video history를 제한된 inference budget으로 처리하는 비교 대상이다. RL 자체의 논문으로 분류하지 않는다.

## Verification Boundary

3D pruning에 필요한 입력, KV-cache 갱신, 실제 sensor/controller 지연을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문과 공개 자료

- 코드 — StreamVLN의 동영상·행동 문맥 모델 · streamvln/model/stream_video_vln.py [배포 파일](https://raw.githubusercontent.com/InternRobotics/StreamVLN/e48f6ff7e9201d93aae003e8f64b04c00cec13bc/streamvln/model/stream_video_vln.py)
- 가중치 — StreamVLN 항법 정책 배포본 · model-00001-of-00004.safetensors [배포 파일](https://huggingface.co/mengwei0427/StreamVLN_Video_qwen_1_5_r2r_rxr_envdrop_scalevln_v1_3/blob/f1f76c66083c362ddfcd2610167f9c4e4a46c027/model-00001-of-00004.safetensors)
- 데이터 — ScaleVLN에서 선정한 학습 궤적 주석 · ScaleVLN/scalevln_subset_150k.json.gz [배포 파일](https://huggingface.co/datasets/cywan/StreamVLN-Trajectory-Data/blob/dc61ee9b4e90aa7ba63c1163b2134df5610dccb9/ScaleVLN/scalevln_subset_150k.json.gz)
- IEEE 게재 서지에는 저자 11명이 등재됐다. 현재 arXiv 원고는 Tai Wang 다음에 Yuqiang Yang을 추가로 기재한다. 게재본 저자와 공개 원고 소속 근거를 따로 기록했다. [원문](https://api.crossref.org/works/10.1109/icra57385.2026.11696190)
