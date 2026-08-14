# HumanPlus: Humanoid Shadowing and Imitation from Humans

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, humanoid, human-to-humanoid, Imitation Learning, teleoperation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://humanoid-ai.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Prior works use motion capture systems, first-person-view (FPV) virtual reality (VR) headsets and exoskeletons to teleoperate humanoids , which are expensive and restricted in operation locations.
- We first train a low-level policy in simulation via reinforcement learning using existing 40-hour human motion datasets.
- Additionally, we lack an accessible data pipeline for whole-body teleoperation of humanoids, preventing researchers from leveraging imitation learning as a tool to teach humanoids arbitrary skills.

## Core Idea
- In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.
- In this paper, we introduce a full-stack system for humanoids to learn motion and autonomous skills from human data.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We demonstrate the system on our customized 33-DoF 180cm humanoid, autonomously completing tasks such as wearing a shoe to stand up and walk, unloading objects from warehouse racks, ...
- Humanoids developed by multiple companies have demonstrated the potential of this data pipeline and subsequent imitation learning from the data collected, but details aren’t publicly available, and autonomous ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.
- In this paper, we introduce a full-stack system for humanoids to learn motion and autonomous skills from human data.
- This policy transfers to the real world and allows humanoid robots to follow hu- One of the key arguments for building robots that have similar form factors to ...

## Abstract Cue
- and lack of a data pipeline for humanoids to learn autonomous skills from egocentric vision.
