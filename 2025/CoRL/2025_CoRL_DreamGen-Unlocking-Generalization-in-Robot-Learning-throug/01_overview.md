# DreamGen: Unlocking Generalization in Robot Learning through Video World Models

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2025 / CoRL
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, Video Generation, robot data, NVIDIA
- Official paper: https://research.nvidia.com/labs/lpr/publication/jang2025neural/
- Code/Project: https://research.nvidia.com/labs/gear/dreamgen/
- Source audit: official NVIDIA publication/project pages checked; generation and policy result details remain UNVERIFIED.

## Why This Paper Is Here

video world model로 diverse synthetic robot experience를 생성해 policy generalization을 높이는 NVIDIA의 robot-data/world-model lineage를 대표한다.

## Problem

real robot demonstration의 task·scene coverage 부족 때문에 policy가 새로운 조건에 일반화하지 못하는 문제를 다룬다.

## Core Idea

video generative world model을 robot-domain data에 adaptation하고 generated trajectories/observations를 policy learning에 사용한다.

## Interface

task/context와 visual trajectory generation을 robot policy training data 및 actions로 연결한다.

## Evaluation Scope

robot manipulation generalization에서 real-only와 generated-data policies를 비교하며 exact setup은 정독 후 기록한다.
