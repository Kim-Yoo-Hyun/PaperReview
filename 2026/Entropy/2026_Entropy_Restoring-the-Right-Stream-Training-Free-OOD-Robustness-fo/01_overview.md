# Restoring the Right Stream: Training-Free OOD Robustness for Vision–Language–Action Policies

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / Entropy
- Authors: Zhiyin Yan, Gang Shen
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, proprioception, robustness
- Aliases:
- Official paper: https://api.crossref.org/works/10.3390/e28090975
- Full-text retrieval: https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf
- Venue verification: https://www.mdpi.com/1099-4300/28/9/975
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다. 평가 노트의 측정 조건도 해당 표·절에서 확인했다.

## Problem and Importance

이 연구는 고정된 VLA의 입력을 영상과 고유수용감각으로 나누고 시점 변화와 로봇 초기 자세 변화에 맞춰 입력을 보정한다. [PDF 1쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=1)

## Core Idea and Contribution

- 영상의 불확실성으로 시각 보정 여부를 정하고 초기 방향 편차를 조건부로 보정해 이후 에피소드 안의 상대 방향 변화를 보존한다. [PDF 4쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=4) · [PDF 6쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=6) · [PDF 8쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=8)
- LIBERO-Plus의 대응 시행과 별도로 확보한 새 인스턴스에서 시각 보정, 상태 보정 및 결합 보정의 결과를 비교했다. [PDF 9쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=9) · [PDF 10쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=10) · [PDF 11쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=11)

## Observation–State–Action Interface

영상·proprioception·언어 → gated restoration → frozen policy.

## Evaluation Scope and Claim Boundary

1,120개 새 인스턴스에서 상태 입력 보정 후 초기 자세 교란의 성공률은 23.8%에서 28.7%로 변했다(Holm 보정 p=0.287). 보정이 활성화되는 별도의 600개 확인 표본에서는 26.3%에서 32.2%로 변했다. [PDF 10쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=10) · [PDF 12쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=12)

## 검색 태그 근거

고정한 OpenVLA-OFT 앞에서 여러 영상 간 일치도와 에피소드 시작 대비 자세를 점검해 관측을 선택적으로 보정한다. LIBERO-Plus의 카메라·고유수용 교란이 평가 조건이다. [원문 4쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=4) · [원문 9쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=9)

## Why This Paper Is Here — Researcher Interpretation

Top-tier 선정 논문은 아니지만 D1의 stream diagnosis·correction 주장과 직접 겹쳐 REFERENCE로 등록한다.

## Verification Boundary

native state interface, gate oracle leakage, code·trial manifest 공개을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
