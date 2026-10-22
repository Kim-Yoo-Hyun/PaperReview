# SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: online-RL, sparse-reward, distributed-training
- Aliases: SimpleVLA-RL
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html
- Code/Project: https://github.com/PRIME-RL/SimpleVLA-RL
- Code: https://github.com/PRIME-RL/SimpleVLA-RL
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

VLA SFT에 필요한 robot trajectory 비용과 distribution shift에서의 낮은 task 성능을 줄인다.

## Core Idea and Contribution

Outcome reward 기반 VLA RL에 trajectory sampling, parallel rollout/rendering 및 loss 계산 최적화를 결합한다.

## Observation–State–Action Interface

OpenVLA-OFT의 observation/language → action rollout → outcome reward → policy update.

## Evaluation Scope and Claim Boundary

ICLR abstract는 LIBERO, RoboTwin 1.0/2.0 및 real-world task 결과를 보고한다. Real-world 평가와 실제 online training은 구분해야 한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html) · [저자 project/code](https://github.com/PRIME-RL/SimpleVLA-RL). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / system. OpenVLA-OFT에서 outcome reward와 scalable rollout/training을 다룬다. 현재 OFT → ConRFT 경로에 대규모 simulator RL의 비교 지점을 추가한다. Real-world 결과와 real-world online training의 범위는 구분해서 정독해야 한다.

## Verification Boundary

실제 robot online training 범위, sparse reward 생성, data leakage 및 compute accounting을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
