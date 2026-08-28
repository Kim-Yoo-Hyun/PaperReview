# Evaluation — Behavior Transformers: Cloning k modes with one stone

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, Transformer, multimodal actions
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html
- Code/Project: https://mahis.life/bet/
- Source audit: official proceedings abstract and project page checked; detailed metrics remain UNVERIFIED.

## Protocol

simulation과 real-robot imitation tasks에서 multimodal behavior cloning을 비교하며 세부 task/metric은 정독 후 기록한다.

## Limitations and Reproducibility

clustering choice, long-horizon error accumulation과 online feedback/recovery는 별도 검증이 필요하다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
