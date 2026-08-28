# Behavior Transformers: Cloning k modes with one stone

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, Transformer, multimodal actions
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html
- Code/Project: https://mahis.life/bet/
- Source audit: official proceedings abstract and project page checked; detailed metrics remain UNVERIFIED.

## Why This Paper Is Here

multimodal demonstration behavior를 transformer policy로 복제하는 diffusion-policy 이전의 강한 generative/action-token IL baseline이다.

## Problem

동일 observation에서 여러 유효 action mode가 존재할 때 단순 regression BC가 평균 행동을 내는 문제를 다룬다.

## Core Idea

action clustering/tokenization과 transformer sequence modeling을 결합해 mode와 residual action을 예측한다.

## Interface

observation history를 discrete action mode와 continuous action으로 매핑한다.

## Evaluation Scope

simulation과 real-robot imitation tasks에서 multimodal behavior cloning을 비교하며 세부 task/metric은 정독 후 기록한다.
