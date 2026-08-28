# Evaluation — ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / NeurIPS Datasets and Benchmarks
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, Dataset, manipulation, simulation
- Official paper: https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/eda80a3d5b344bc40f3bc04f65b7a357-Abstract-round2.html
- Code/Project: https://maniskill.ai/
- Source audit: official proceedings abstract and project page checked; task statistics and baseline tables remain UNVERIFIED.

## Protocol

imitation/RL baselines와 seen/unseen object/task generalization을 평가한다.

## Limitations and Reproducibility

simulation-to-real gap과 version별 task/protocol 변화는 명시적으로 관리해야 한다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
