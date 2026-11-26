# ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Authors: Puhao Li, Yingying Wu, Ziheng Xi, Wanlin Li, Yuzhe Huang, Zhiyuan Zhang, Yinghan Chen, Jianan Wang, Song-Chun Zhu, Tengyu Liu, Siyuan Huang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, few-shot-adaptation, object-centric, Imitation Learning
- Aliases: ControlVLA
- Official paper: https://proceedings.mlr.press/v305/li25c.html
- Venue verification: https://proceedings.mlr.press/v305/li25c.html
- Code/Project: https://controlvla.github.io/
- Code: https://github.com/ControlVLA/ControlVLA
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. 학회 웹 초록은 6개, 게재본 §5 표 1은 단기 6개와 장기 2개를 열거한다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

소수 시연으로 generalist VLA를 특정 물체·과제에 적응시키기 어렵다.

## Core Idea and Contribution

Zero-initialized projection을 가진 ControlNet 형태로 object-centric 조건을 주입한다.

## Observation–State–Action Interface

장면·객체 중심 표현 → 사전학습 VLA → 조작 행동.

## Evaluation Scope and Claim Boundary

게재본 §5와 표 1은 단기 과제 6개와 장기 과제 2개를 열거한다. 표 2의 평균 성공률 76.7%는 단기 과제 6개에서 집계했다. 학회 웹 초록의 과제 수는 6개다. [게재본 §5](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/li25c/li25c.pdf#page=5) · [게재본 표 1·2](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/li25c/li25c.pdf#page=6) · [학회 웹 초록](https://proceedings.mlr.press/v305/li25c.html)

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/li25c.html) · [저자 project/code](https://controlvla.github.io/) · [공식 code](https://github.com/ControlVLA/ControlVLA). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

RL이 반드시 필요한지를 판단할 저데이터 SFT·표현 적응 비교다.

## Verification Boundary

객체 mask 감독 비용, base model 학습 데이터, 표준·장기 task 구분을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · 객체 조건부 정책 평가 · eval_controlvla.py [배포 파일](https://raw.githubusercontent.com/ControlVLA/ControlVLA/0355e7614530c5e4e582c5465d609d677be7b1a8/eval_controlvla.py)
- 가중치 · 저자가 사전학습 ControlVLA로 명시한 묶음 · rgb_propri_10Hz-droid.zip [배포 파일](https://drive.google.com/file/d/1VcJle5Ooem7PHMU494qWWa-agMUj6hAE/view)
- 데이터 · UMI 수집 파이프라인의 예제 시연 · picknplace_toy.d10.zarr.zip [배포 파일](https://drive.google.com/file/d/1VtpxxzMw-tMH4IV7yLHdFPXWzn6vNzSS/view)
