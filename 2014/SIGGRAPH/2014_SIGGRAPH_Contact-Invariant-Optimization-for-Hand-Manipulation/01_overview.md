# Contact-Invariant Optimization for Hand Manipulation

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2014 / SIGGRAPH
- Category: Robotics Foundations: Contact and Whole-Body Control
- Tags: Robotics, contact-rich manipulation, trajectory optimization, contact invariant
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Automated synthesis of complex human behaviors is one of the long-standing grand challenges in computer graphics, that would also have an impact on robotics, biomechanics, and movement neuroscience.
- Unlike prior work on walking where contact information was specified manually and left outside the scope of numerical optimization, discovering suitable contact sets is the central goal of ...
- 1.1 The key idea: Contact-Invariant Optimization (CIO) As with prior methods for automated behavior synthesis, our CIO method also comes down to exploiting domain-specific knowledge.

## Core Idea
- We present a motion synthesis framework capable of producing a wide variety of important human behaviors that have rarely been studied, including getting up from the ground, crawling, ...
- In this paper we present a step towards a more general yet fully automated framework for behavior synthesis, capable of produc- ing a wide variety of less commonly ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Interaction Between Characters Two characters also cooperate to achieve tasks impossible for one, such as `pos for one of the characters specifying a target location above character’s height.
- Because contacts can be made with the surfaces of other characters, the task is achieved by one character climbing on top of the other.
- The pattern of foot contacts typical of walking is not specified and emerges automatically from our optimization. `pos task is shown in the corresponding video with a white ...

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- We present a motion synthesis framework capable of producing a wide variety of important human behaviors that have rarely been studied, including getting up from the ground, crawling, ...
- At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.
- It also does not require pre-existing examples or motion capture data.

## Abstract Cue
- We present a motion synthesis framework capable of producing a wide variety of important human behaviors that have rarely been studied, including getting up from the ground, crawling, climbing, moving heavy objects, acrobatics (hand-stands in particular), and various cooperative actions involving two characters and their ...
