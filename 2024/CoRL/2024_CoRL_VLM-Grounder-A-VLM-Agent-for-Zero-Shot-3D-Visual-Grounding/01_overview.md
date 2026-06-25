# VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding

- Year/Venue: 2024 / CoRL
- Category: 3D Vision-Language Grounding
- Tags: 3D visual grounding, VLM, zero-shot
- Authors: not extracted
- Paper: https://proceedings.mlr.press/v270/xu25c.html
- PDF status: downloaded
- GitHub/Project: https://github.com/InternRobotics/VLM-Grounder

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: 3D visual grounding is crucial for robots, requiring integration of natural language and 3D scene understanding.
- Method cue: In this work, we present VLM-Grounder, a novel framework using vision-language models (VLMs) for zero-shot 3D visual grounding based solely on 2D images.
- Result cue: Experiments on ScanRefer and Nr3D datasets show VLM-Grounder outperforms previous zero-shot methods, achieving 51.6% Acc@0.25 on ScanRefer and 48.0% Acc on Nr3D, without relying ...

## Input / Output
Input: 3D scene representation plus free-form natural language. Output: target object, 3D box, mask, or referring expression result.

## Main Claims
- 논문은 `vision-language alignment and multimodal reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- vision-language alignment and multimodal reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D visual grounding, VLM, zero-shot.
- 초록에서 확인되는 주요 cue: Traditional, Recently, LLMs, While, VLM-Grounder, VLMs, Experiments, ScanRefer.
