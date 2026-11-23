# Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Zichen Jeff Cui, Omar Rayyan, Haritheja Etukuru, Bowen Tan, Zavier Andrianarivo, Zicheng Teng, Yihang Zhou, Krish Mehta, Nicholas Wojno, Kevin Yuanbo Wu, Manan H. Anjaria, Ziyuan Wu, Manrong Mao, Guangxun Zhang, Binit Shah, Yejin Kim, Soumith Chintala, Lerrel Pinto, Nur Muhammad Mahi Shafiullah
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: contact, manipulation, representation
- Aliases:
- Official paper: https://www.roboticsproceedings.org/rss22/p141.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p141.html
- Code/Project: https://cap-policy.github.io/
- Code availability: CAP 저자 저장소의 모방학습 손실 구현. imitation-in-homes/loss_fns/diffusion_policy_loss_fn.py [근거](https://raw.githubusercontent.com/jeffacce/cap-policy/8ab11176ecb61a5e88f290958877ab17a6f3e8e2/imitation-in-homes/loss_fns/diffusion_policy_loss_fn.py)
- Code: https://github.com/jeffacce/cap-policy
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Contact-Anchored Policies는 실행 시 접촉할 공간 지점을 지정해 여러 환경과 로봇에서 기본 조작 기술을 수행한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p141.pdf#page=1)

## Core Idea and Contribution

- 기술별 정책을 접촉점으로 조건화하고 EgoGym 시뮬레이션에서 실패를 찾아 정책과 학습 데이터를 수정한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss22/p141.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss22/p141.pdf#page=4)
- 기본 조작 세 가지에서 새로운 환경·로봇으로의 추가 학습 없는 전이를 비교했다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p141.pdf#page=1) · [PDF 5쪽](https://www.roboticsproceedings.org/rss22/p141.pdf#page=5)

## Observation–State–Action Interface

접촉 anchor·관측 → skill action; language-conditioned VLA 자체는 아니다.

## Evaluation Scope and Claim Boundary

Pick/Open/Close와 새 환경·embodiment 평가를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p141.html) · [저자 project/code](https://cap-policy.github.io/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA의 이득이 task specification 차이인지 가릴 강한 non-VLA baseline이므로 NEXT다.

## Verification Boundary

anchor 획득 비용, embodiment split, 실제 checkpoint release을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
