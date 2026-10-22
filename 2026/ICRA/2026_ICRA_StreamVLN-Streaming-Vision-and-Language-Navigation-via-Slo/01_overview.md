# StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICRA
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
