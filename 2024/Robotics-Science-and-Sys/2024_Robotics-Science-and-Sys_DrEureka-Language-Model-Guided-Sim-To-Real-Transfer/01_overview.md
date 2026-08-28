# DrEureka: Language Model Guided Sim-To-Real Transfer

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / Robotics: Science and Systems
- Category: Robot Learning and Data
- Tags: Robotics, sim-to-real, Reinforcement Learning, Large Language Model, NVIDIA
- Official paper: https://www.roboticsproceedings.org/rss20/p094.html
- Code/Project: https://eureka-research.github.io/dr-eureka/
- Source audit: official RSS proceedings abstract and project page checked; hardware trial details remain UNVERIFIED.

## Why This Paper Is Here

Eureka의 reward synthesis를 domain-randomization 설계와 실로봇 transfer까지 확장한 NVIDIA sim-to-real lineage의 핵심이다.

## Problem

simulation에서 학습한 policy를 실제 robot에 옮길 때 reward와 dynamics randomization을 수작업으로 조정하는 병목을 다룬다.

## Core Idea

LLM이 reward와 physics randomization 범위를 제안하고 simulator feedback을 이용해 transfer configuration을 구성한다.

## Interface

task/environment description와 simulation diagnostics를 reward/randomization code 및 deployable policy training으로 연결한다.

## Evaluation Scope

quadruped locomotion 및 dexterous manipulation의 sim-to-real demonstrations가 보고된다.
