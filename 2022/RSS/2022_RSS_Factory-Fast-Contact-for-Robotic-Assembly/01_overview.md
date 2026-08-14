# Factory: Fast Contact for Robotic Assembly

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2022 / RSS
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, assembly, contact-rich manipulation, simulation, Reinforcement Learning, sim-to-real
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/NVIDIA-Omniverse/IsaacGymEnvs
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- However, accurately, efficiently, and robustly simulating the range of contact-rich interactions in assembly remains a longstanding challenge.
- However, assembly has been exceptionally difficult to automate due to physical complexity, part variability, and strict reliability requirements .
- Custom tooling and part-specific engineering are also cost-prohibitive for high-mix, low-volume settings .

## Core Idea
- In this work, we present Factory, a set of physics simulation methods and robot learning tools for such applications.
- We provide 60 carefullydesigned part models, 3 robotic assembly environments, and 7 robot controllers for training and testing virtual robots.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We achieve real-time or faster simulation of a wide range of contact-rich scenes, including simultaneous simulation of 1000 nut-and-bolt interactions.
- In industry, robotic assembly methods may achieve high precision, accuracy, and reliability .
- In research, methods for robotic assembly often use lessexpensive equipment, require fewer custom fixtures, achieve increased robustness to variation, and may recover from failure .

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- In this work, we present Factory, a set of physics simulation methods and robot learning tools for such applications.
- In research, methods for robotic assembly often use lessexpensive equipment, require fewer custom fixtures, achieve increased robustness to variation, and may recover from failure .
- We provide 60 carefullydesigned part models, 3 robotic assembly environments, and 7 robot controllers for training and testing virtual robots.

## Abstract Cue
- —Robotic assembly is one of the oldest and most challenging applications of robotics.
