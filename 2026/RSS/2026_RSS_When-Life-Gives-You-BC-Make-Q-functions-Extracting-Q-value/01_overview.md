# When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Lakshita Dodeja, Ondrej Biza, Shivam Vats, Stephen Hart, Stefanie Tellex, Robin Walters, Karl Schmeckpeper, Thomas Weng
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-to-online-RL, behavior-cloning, Q-learning, contact
- Aliases: Q2RL
- Official paper: https://roboticsproceedings.org/rss22/p153.html
- Venue verification: https://roboticsproceedings.org/rss22/p153.html
- Code/Project: https://pages.rai-inst.com/q2rl_website/
- Code: https://github.com/rai-opensource/q2rl
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Q2RL은 행동 복제 정책으로부터 소량의 환경 상호작용을 통해 가치 함수를 추정하고 이를 이용해 온라인 학습 중 실행할 행동을 고른다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p153.pdf#page=1)

## Core Idea and Contribution

- 행동 복제와 강화학습 정책이 각각 제안한 행동을 Q값으로 비교해 자료 수집에서 기존 정책의 유용한 행동을 유지한다. [PDF 3쪽](https://roboticsproceedings.org/rss22/p153.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p153.pdf#page=4)
- 시뮬레이션과 실제 파이프 조립·부품 배치에서 기본 행동 복제 및 오프라인-온라인 학습 기준선과 성공률·학습 시간을 비교했다. [PDF 6쪽](https://roboticsproceedings.org/rss22/p153.pdf#page=6) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p153.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p153.pdf#page=8)

## Observation–State–Action Interface

BC 정책·학습 정책 → Q-Gating → 실제 상호작용·RL 갱신.

## Evaluation Scope and Claim Boundary

D4RL·robomimic과 실제 pipe assembly·kitting을 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p153.html) · [저자 project/code](https://pages.rai-inst.com/q2rl_website/) · [공식 code](https://github.com/rai-opensource/q2rl). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

BC prior 보존을 새 unified objective 없이 달성하는 강한 대안이다.

## Verification Boundary

Q 초기화에 필요한 상호작용, 두 정책 유지 비용, gating의 행동 분포 변화을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · BC·RL 후보의 Q값을 이용하는 학습 에이전트 · backend/agents/q2rl_gym.py [배포 파일](https://raw.githubusercontent.com/rai-opensource/q2rl/d565ab09f5ae88546f2dec43445fe8701ee3de65/backend/agents/q2rl_gym.py)
- 가중치 · robomimic Can의 영상 기반 BC 초기 정책 · gmm.pth [배포 파일](https://huggingface.co/theaiinstitute/gmm_robomimic_can_img/resolve/0174f1f1214e326ccc2a6cd7410cc55837a6212a/gmm.pth)
- 데이터 · Q2RL 배포처에서 제공한 robomimic Can 영상 시연 · can/ph/image_v141.hdf5 [배포 파일](https://huggingface.co/datasets/theaiinstitute/q2rl_robomimic_datasets/resolve/ba3b72ac9f372634a1b7293f140bc3bd0f3acf89/can/ph/image_v141.hdf5)
