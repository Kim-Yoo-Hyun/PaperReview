# DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Hanxiang Ren, Pei Zhou, Xunzhe Zhou, Yanchao Yang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, hypernetwork, instruction grounding, multitask manipulation
- Aliases:
- Official paper: https://www.roboticsproceedings.org/rss22/p147.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p147.html
- Code/Project: https://github.com/ReNginx/DISC
- Code: https://github.com/ReNginx/DISC
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

DISC는 언어 지시만으로 과제별 정책의 가중치를 생성하고, 그 정책이 시각 관측으로 조작 행동을 결정하게 한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p147.pdf#page=1)

## Core Idea and Contribution

- 두 단계 하이퍼네트워크가 정책 파라미터를 생성·정제하도록 설계해 지시 해석과 현재 상태의 제어를 분리했다. [PDF 3쪽](https://www.roboticsproceedings.org/rss22/p147.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss22/p147.pdf#page=4)
- LIBERO·Meta-World에서 여러 과제를 평가하고, 실제 로봇에서는 장면이 같고 지시만 다른 조합으로 언어 의존성을 시험했다. [PDF 6쪽](https://www.roboticsproceedings.org/rss22/p147.pdf#page=6) · [PDF 9쪽](https://www.roboticsproceedings.org/rss22/p147.pdf#page=9)

## Observation–State–Action Interface

언어 → policy weights; 생성된 policy는 관측 → action.

## Evaluation Scope and Claim Boundary

LIBERO-90, Meta-World 및 동일 visual context의 실제 로봇 비교를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p147.html) · [저자 project/code](https://github.com/ReNginx/DISC). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

OpenVLA 이후 language-conditioned 행동 여부를 확인할 직접 비교군이므로 NEXT다.

## Verification Boundary

generated parameter 수, training budget, 동일 장면 통제을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 지시 조건부 하이퍼네트워크 · model/hylap/hypogen2_impl/hypernetworks.py [배포 파일](https://raw.githubusercontent.com/ReNginx/DISC/4979e1516246a2e5a2fc7c3cae7511c5f17e5f6d/model/hylap/hypogen2_impl/hypernetworks.py)
- 가중치 — LIBERO-90 DISC 정책 · DISC-libero90.ckpt [배포 파일](https://huggingface.co/ReNginx/DISC/blob/36b98d7496553df98e9e2150a502d99b190b6d11/DISC-libero90.ckpt)
