# TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Matthew M. Hong, Jesse Zhang, Anusha Nagabandi, Abhishek Gupta
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: exploration, Diffusion, policy-finetuning, VLA
- Aliases: TMRL
- Official paper: https://roboticsproceedings.org/rss22/p208.html
- Venue verification: https://roboticsproceedings.org/rss22/p208.html
- Code/Project: https://weirdlabuw.github.io/tmrl/
- Code: https://github.com/matthewh6/tmrl
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

TMRL은 모방 사전학습에서 관측에 섞는 확산 잡음의 단계를 이용해 이후 강화학습에서 탐색할 행동의 폭을 조절한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p208.pdf#page=1)

## Core Idea and Contribution

- 여러 잡음 단계에 조건화해 정확한 모방부터 넓은 행동 분포까지 학습한 뒤 강화학습 정책이 상황에 맞는 단계를 선택하게 한다. [PDF 3쪽](https://roboticsproceedings.org/rss22/p208.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p208.pdf#page=4) · [PDF 5쪽](https://roboticsproceedings.org/rss22/p208.pdf#page=5)
- 상태·점군·영상 입력의 정책에서 표본 효율을 평가하고 실제 로봇의 조작에서 온라인 미세조정 결과를 보고했다. [PDF 7쪽](https://roboticsproceedings.org/rss22/p208.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p208.pdf#page=8) · [PDF 9쪽](https://roboticsproceedings.org/rss22/p208.pdf#page=9)

## Observation–State–Action Interface

관측·noise 수준 → 사전학습 정책의 행동; RL이 timestep을 조절.

## Evaluation Scope and Claim Boundary

항법·조작 평가를 보고하며 project는 실제 VLA 후학습도 설명한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p208.html) · [저자 project/code](https://weirdlabuw.github.io/tmrl/) · [공식 code](https://github.com/matthewh6/tmrl). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA 내부 학습을 제안할 때 비교해야 할 사전학습 coverage·탐색 조절 대안이다.

## Verification Boundary

pretraining 추가 비용, high-level action 주기, baseline 탐색 분산, 로봇별 학습 시간을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · LIBERO에서 탐색 단계를 미세조정하는 RL 학습 · sac_libero.py [배포 파일](https://raw.githubusercontent.com/matthewh6/tmrl/a881748b612460cba8194aa7da10bc8bac51ae09/sac_libero.py)
- 가중치 · LIBERO 문맥 평활화 사전학습 정책 · model.safetensors [배포 파일](https://huggingface.co/matthewh6/cspi0_libero/resolve/5092ecb529ac17057ce3b96cd8ac7bca97f4a906/model.safetensors)
