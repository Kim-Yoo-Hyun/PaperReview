# Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Authors: Asher J. Hancock, Xindi Wu, Lihan Zha, Olga Russakovsky, Anirudha Majumdar
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action representation, language generalization
- Aliases: VLM2VLA
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html
- Code/Project: https://vlm2vla.github.io/
- Code: https://github.com/irom-princeton/vlm2vla
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

VLM2VLA는 저수준 로봇 행동을 자연어로 표현하고 LoRA로 적응시켜 조작을 학습하면서 시각언어 능력을 보존한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 로봇 행동 라벨의 표현을 백본의 언어 출력 형식에 맞춰 로봇 데이터만으로 학습할 수 있게 했다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf#page=4)
- 시각 질의응답과 실제 로봇의 새 과제·다국어 지시 수행을 함께 평가해 조작 학습 후 남는 의미 이해 능력을 측정했다. [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf#page=6)

## Observation–State–Action Interface

영상·언어 → 언어형 action 표현 → robot 명령.

## Evaluation Scope and Claim Boundary

Robot manipulation과 VQA 능력 보존을 함께 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

의미 능력 보존이라는 넓은 방향의 직접 선행이며 action interface 비교에도 필요하다.

## Verification Boundary

action decoding, LoRA 범위, VQA/robot split과 robot controller을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문 대조

저자 표기와 순서는 이 판본의 표제면을 따른다. [표제면](https://proceedings.iclr.cc/paper_files/paper/2026/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf#page=1)

## 공개 자료

- 코드 — 행동의 언어 표현을 학습하는 VLM 미세조정 · src/vlm2vla/train.py [배포 파일](https://raw.githubusercontent.com/irom-princeton/vlm2vla/27da5ad142e9d92d027db84a2d2c520ceace91e2/src/vlm2vla/train.py)
- 가중치 — 행동 언어화용 LoRA 어댑터 · adapter_model.safetensors [배포 파일](https://huggingface.co/AasherH/vlm2vla/blob/d40f632269aa0d54159f7e07432ce794f3239f24/adapter_model.safetensors)
