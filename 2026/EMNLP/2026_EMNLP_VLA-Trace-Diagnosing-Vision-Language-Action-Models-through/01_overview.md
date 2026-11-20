# VLA-Trace: Diagnosing Vision-Language-Action Models through Representation and Behavior Tracing

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue
- Authors: Haoyuan Shi, Xiancong Ren, Yingji Zhang, Qinfan Zhang, Jiayu Hu, Haozhe Shan, Han Dong, Jinpeng Lu, Yinda Chen, Yi Zhang, Yong Dai, Xiaozhu Ju
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, representation, interpretability, behavioral-probing
- Official paper: https://aclanthology.org/2026.emnlp-main.2076/
- Venue verification: https://aclanthology.org/2026.emnlp-main.2076/
- Code/Project: https://vla-trace.github.io/
- Code: https://github.com/VLA-Trace/VLA-Trace
- Source audit: 2026-11-05: 공식 EMNLP metadata; arXiv v1 §3.1–3.3; code README. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD.

## Problem and Contribution

Robot adaptation에서 multimodal representation 변화가 행동의 grounding과 어떻게 이어지는지 분석한다.

Checkpoint CKA, attention knockout, region masking과 input editing을 단계적으로 연결한다.

## Scope and Limitation

읽은 arXiv v1과 EMNLP 최종본의 전체 동등성은 확인하지 않았다. 공개 toolkit의 존재와 우리 checkpoint adapter의 호환·실행은 별개다.

## Why This Paper Is Here — Researcher Interpretation

FEEDBACK의 표현/행동 연결 진단 도구로 REFERENCE에 보존한다. 기존 mechanistic NEXT와 중복되는 도구 축이며 현재 학습 메커니즘의 직접 검증은 아니다.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2605.30117v1), 공식 EMNLP metadata; arXiv v1 §3.1–3.3; code README.
