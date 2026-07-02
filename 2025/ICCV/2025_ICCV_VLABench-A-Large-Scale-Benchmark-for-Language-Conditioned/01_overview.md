# VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks

- Year/Venue: 2025 / ICCV
- Category: Benchmarks and Datasets
- Tags: VLA, Benchmark, long-horizon
- Paper link: ./2025/ICCV/2025_ICCV_VLABench-A-Large-Scale-Benchmark-for-Language-Conditioned/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Introduction Language-conditioned manipulation represents a fundamental challenge in embodied AI and a stepping stone toward Artificial General Intelligence .
- The experimental results indicate that both the current state-of-theart pretrained VLAs and the workflow based on VLMs face challenges in our tasks.

## Core Idea
- To better define such general-purpose tasks in the context of LLMs and advance the research in VLAs, we present VLABench, an open-source benchmark for evaluating universal LCM task ...
- To support the downstream finetuning, we provide high-quality training data collected via an automated framework incorporating heuristic skills and prior information.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We demonstrate the superiority of our data framework through comparative experiments.
- Subsequently, the selected skills generate trajectories using RRT , with quaternion interpolation achieved through spherical linear interpolation.
- The experimental results indicate that both the current state-of-theart pretrained VLAs and the workflow based on VLMs face challenges in our tasks.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To better define such general-purpose tasks in the context of LLMs and advance the research in VLAs, we present VLABench, an open-source benchmark for evaluating universal LCM task ...
- The experimental results indicate that both the current state-of-theart pretrained VLAs and the workflow based on VLMs face challenges in our tasks.
- To support the downstream finetuning, we provide high-quality training data collected via an automated framework incorporating heuristic skills and prior information.

## Abstract Cue
- General-purposed embodied agents are designed to understand the users’ natural instructions or intentions and act precisely to complete universal tasks.
