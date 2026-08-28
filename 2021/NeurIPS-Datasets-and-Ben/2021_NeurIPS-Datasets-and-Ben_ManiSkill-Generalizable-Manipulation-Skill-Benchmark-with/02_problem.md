# Problem — ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / NeurIPS Datasets and Benchmarks
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, Dataset, manipulation, simulation
- Official paper: https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/eda80a3d5b344bc40f3bc04f65b7a357-Abstract-round2.html
- Code/Project: https://maniskill.ai/
- Source audit: official proceedings abstract and project page checked; task statistics and baseline tables remain UNVERIFIED.

## Target Problem and Assumptions

다양한 objects와 tasks에 generalize하는 manipulation skill을 대규모·재현 가능하게 평가한다.

## Closed-Loop Position

visual/state observations, continuous robot action, object/task variation과 success criteria를 정의한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
