# Method — ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / NeurIPS Datasets and Benchmarks
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, Dataset, manipulation, simulation
- Official paper: https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/eda80a3d5b344bc40f3bc04f65b7a357-Abstract-round2.html
- Code/Project: https://maniskill.ai/
- Source audit: official proceedings abstract and project page checked; task statistics and baseline tables remain UNVERIFIED.

## Pipeline

physics simulation, task suite, demonstration trajectories와 standardized learning tracks를 제공한다.

## Interface

visual/state observations, continuous robot action, object/task variation과 success criteria를 정의한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
