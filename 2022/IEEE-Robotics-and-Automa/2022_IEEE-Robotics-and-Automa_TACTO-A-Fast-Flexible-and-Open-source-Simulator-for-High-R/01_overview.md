# TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / IEEE Robotics and Automation Letters
- Category: Benchmarks and Datasets
- Tags: Robotics, tactile sensing, simulation, contact
- Official paper: https://doi.org/10.1109/LRA.2022.3146945
- Code/Project: https://github.com/facebookresearch/tacto
- Source audit: publisher metadata, abstract, and official code repository checked; fidelity results remain UNVERIFIED.

## Why This Paper Is Here

GelSight/DIGIT류 vision-based tactile sensor를 빠르게 simulate해 tactile policy 학습과 sim-to-real 연구를 가능하게 하는 기반 도구다.

## Problem

고해상도 tactile rendering의 계산 비용과 sensor configuration 재사용 문제를 다룬다.

## Core Idea

physics simulator contact와 graphics rendering을 결합해 여러 vision-based tactile sensor output을 생성한다.

## Interface

simulated contact state를 tactile RGB/image observation으로 변환한다.

## Evaluation Scope

rendering speed, sensor variants와 learning applications가 보고되며 real-sensor fidelity 범위는 원문 확인이 필요하다.
