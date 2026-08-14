# Control Barrier Function Based Quadratic Programs for Safety Critical Systems

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2017 / TAC
- Category: World Models, Safety, and Recovery
- Tags: Robotics, control barrier function, safety-critical control, quadratic programming
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://coogan.ece.gatech.edu/papers/pdf/ames2017control.pdf
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- In contrast, the approach developed here will pose a feedback design problem that mediates the safety and stabilization requirements, in the sense that safety is always guaranteed, and ...
- Motivated by the use of Lyapunov functions to certify stability properties of a set without calculating the exact solution of a system, the underlying concept in this paper ...
- The mediation of safety and performance through a QP is demonstrated on adaptive cruise control and lane keeping, two automotive control problems that present both safety and performance ...

## Core Idea
- —Safety critical systems involve the tight coupling between potentially conflicting control objectives and safety constraints.
- As a means of creating a formal framework for controlling systems of this form, and with a view toward automotive applications, this paper develops a methodology that allows ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Through these constructions, CBFs can naturally be unified with control Lyapunov functions (CLFs) in the context of a quadratic program (QP); this allows for the achievement of control ...
- Prior work in incorporates into a single feedback law the conditions required to simultaneously achieve asymptotic stability of an equilibrium point, while avoiding an unsafe set.
- The mediation of safety and performance through a QP is demonstrated on adaptive cruise control and lane keeping, two automotive control problems that present both safety and performance ...

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- Prior work in incorporates into a single feedback law the conditions required to simultaneously achieve asymptotic stability of an equilibrium point, while avoiding an unsafe set.
- The mediation of safety and performance through a QP is demonstrated on adaptive cruise control and lane keeping, two automotive control problems that present both safety and performance ...
- Through these constructions, CBFs can naturally be unified with control Lyapunov functions (CLFs) in the context of a quadratic program (QP); this allows for the achievement of control ...

## Abstract Cue
- —Safety critical systems involve the tight coupling between potentially conflicting control objectives and safety constraints.
