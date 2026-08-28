# Problem — Behavior Transformers: Cloning k modes with one stone

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, Transformer, multimodal actions
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html
- Code/Project: https://mahis.life/bet/
- Source audit: official proceedings abstract and project page checked; detailed metrics remain UNVERIFIED.

## Target Problem and Assumptions

동일 observation에서 여러 유효 action mode가 존재할 때 단순 regression BC가 평균 행동을 내는 문제를 다룬다.

## Closed-Loop Position

observation history를 discrete action mode와 continuous action으로 매핑한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
