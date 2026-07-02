# Benchmarking Knowledge Transfer for Lifelong Robot Learning

- Year/Venue: 2023 / NeurIPS
- Category: Benchmarks and Datasets
- Tags: Robotics, Imitation Learning, Benchmark
- Paper link: ./2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/paper.pdf
- Code/Project: https://libero-project.github.io/main.html
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Consider a scenario where a robot, initially trained to retrieve juice from a fridge, fails ∗
- Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...
- Unlike traditional lifelong learning problems in image and text domains, which primarily involve the transfer of declarative knowledge of entities and concepts, lifelong learning in decision-making (LLDM) also ...

## Core Idea
- Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...
- Specifically, LIBERO highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how to design effective ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...
- We first introduce the evaluation metric used in experiments, and present analysis of empirical results in LIBERO.
- Then, we find the earliest epoch e∗i in which the agent achieves the best performance on task i (i.e., e∗i = arg mine ci,i,ei = ci,i ), and ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...
- Specifically, LIBERO highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how to design effective ...
- To advance research in LLDM, we introduce LIBERO, a novel benchmark of lifelong learning for robot manipulation.

## Abstract Cue
- Lifelong learning offers a promising paradigm of building a generalist agent that learns and adapts over its lifespan.
