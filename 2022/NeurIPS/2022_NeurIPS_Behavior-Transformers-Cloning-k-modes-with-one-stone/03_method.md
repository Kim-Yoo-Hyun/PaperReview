# Method — Behavior Transformers: Cloning k modes with one stone

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, Transformer, multimodal actions
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html
- Code/Project: https://mahis.life/bet/
- Source audit: official proceedings abstract and project page checked; detailed metrics remain UNVERIFIED.

## Pipeline

action clustering/tokenization과 transformer sequence modeling을 결합해 mode와 residual action을 예측한다.

## Interface

observation history를 discrete action mode와 continuous action으로 매핑한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
