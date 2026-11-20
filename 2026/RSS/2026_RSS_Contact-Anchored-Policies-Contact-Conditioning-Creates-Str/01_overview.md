# Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

추상 언어만으로 구체적 접촉 목표를 전달하기 어려운 문제를 다룬다.

## Core Idea and Contribution

Contact point로 조건화한 modular utility policies와 EgoGym 반복 평가를 제안한다.

## Observation–State–Action Interface

접촉 anchor·관측 → skill action; language-conditioned VLA 자체는 아니다.

## Evaluation Scope and Claim Boundary

Pick/Open/Close와 새 환경·embodiment 평가를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p141.html) · [저자 project/code](https://cap-policy.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA의 이득이 task specification 차이인지 가릴 강한 non-VLA baseline이므로 NEXT다.

## Verification Boundary

anchor 획득 비용, embodiment split, 실제 checkpoint release을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
