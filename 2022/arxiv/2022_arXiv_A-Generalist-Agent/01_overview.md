# A Generalist Agent

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / arXiv
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, Generalist Agent, Transformer, Multimodal Learning, Google DeepMind
- Official paper: https://arxiv.org/abs/2205.06175
- Code/Project: https://deepmind.google/discover/blog/a-generalist-agent/
- Source audit: arXiv abstract and official DeepMind article checked; dataset and result details remain UNVERIFIED.

## Why This Paper Is Here

Gato는 text·vision·control을 단일 token sequence model로 통합한 generalist-agent 계보의 대표작으로 PaLM-E/VLA 배경을 보강한다.

## Problem

서로 다른 modality, embodiment와 task를 각각 별도 모델이 아닌 하나의 policy로 수행한다.

## Core Idea

observations와 actions를 공통 token sequence로 직렬화해 autoregressive transformer를 multi-domain data에 학습한다.

## Interface

text/image/state history를 task별 discrete/continuous action token으로 매핑한다.

## Evaluation Scope

Atari, language, vision, simulated/real robot control 등 다수 domain을 하나의 모델로 평가한다.
