# SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 개요 전반은 초록 수준이며, 아래 요약과 두 기여에는 확인한 본문 위치를 표시했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Authors: Haozhan Li, Yuxin Zuo, Jiale Yu, Yuhao Zhang, Yang Zhaohui, Kaiyan Zhang, Xuekai Zhu, Yuchen Zhang, Tianxing Chen, Ganqu Cui, Dehui Wang, Dingxiang Luo, Yuchen Fan, Youbang Sun, Jia Zeng, Jiangmiao Pang, Shanghang Zhang, Yu Wang, Yao Mu, Bowen Zhou, Ning Ding
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: online-RL, sparse-reward, distributed-training
- Aliases: SimpleVLA-RL
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html
- Code/Project: https://github.com/PRIME-RL/SimpleVLA-RL
- Code: https://github.com/PRIME-RL/SimpleVLA-RL
- Source audit: 2026-11-23 요약과 핵심 기여 두 개를 원문 본문에 대조했다. 나머지 세부 분석은 기존 초록·공식 자료에 근거한다.

## Problem and Importance

SimpleVLA-RL은 시뮬레이터의 결과 보상으로 VLA를 미세조정하기 위한 병렬 실행·학습 체계를 제공한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cbfbcb4da14235bd69b134070898ae9d-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- veRL에 로봇 궤적 표본화와 다중 환경 렌더링, VLA 출력에 맞춘 손실 계산을 결합했다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cbfbcb4da14235bd69b134070898ae9d-Paper-Conference.pdf#page=1) · [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cbfbcb4da14235bd69b134070898ae9d-Paper-Conference.pdf#page=3)
- OpenVLA-OFT를 RoboTwin·LIBERO에서 평가하고 시뮬레이션에서 학습한 정책의 실제 로봇 전이도 별도로 비교했다. [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cbfbcb4da14235bd69b134070898ae9d-Paper-Conference.pdf#page=5) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cbfbcb4da14235bd69b134070898ae9d-Paper-Conference.pdf#page=8)

## Observation–State–Action Interface

OpenVLA-OFT의 observation/language → action rollout → outcome reward → policy update.

## Evaluation Scope and Claim Boundary

ICLR abstract는 LIBERO, RoboTwin 1.0/2.0 및 real-world task 결과를 보고한다. Real-world 평가와 실제 online training은 구분해야 한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html) · [저자 project/code](https://github.com/PRIME-RL/SimpleVLA-RL). 그 밖의 수치, 기준선의 비교 조건, 실패 범위는 별도 대조가 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / system. OpenVLA-OFT에서 outcome reward와 scalable rollout/training을 다룬다. 현재 OFT → ConRFT 경로에 대규모 simulator RL의 비교 지점을 추가한다. Real-world 결과와 real-world online training의 범위는 구분해서 정독해야 한다.

## Verification Boundary

실제 robot online training 범위, sparse reward 생성, data leakage 및 compute accounting을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
