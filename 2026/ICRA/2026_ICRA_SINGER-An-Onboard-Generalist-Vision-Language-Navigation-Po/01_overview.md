# SINGER: An Onboard Generalist Vision-Language Navigation Policy for Drones

- Year/Venue: 2026 / ICRA
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Navigation
- Paper link: ./2026/ICRA/2026_ICRA_SINGER-An-Onboard-Generalist-Vision-Language-Navigation-Po/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Despite these successes, open-vocabulary autonomous drone navigation remains an unsolved challenge due to the scarcity of largescale demonstrations, real-time control demands of drones for stabilization, and lack of ...

## Core Idea
- In this work, we present SINGER for language-guided autonomous drone navigation in the open world using only onboard sensing and compute.
- In this work, we ask the question: “Can we train a visionlanguage drone navigation policy to reach previously unseen goal objects in a previously unseen environment using only ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Through extensive hardware flight experiments, we demonstrate superior zero-shot sim-to-real transfer of our policy to unseen environments and unseen language-conditioned goal objects.
- When trained on ∼700k-1M observation action pairs of language conditioned visuomotor data and deployed on hardware, SINGER outperforms a velocity-controlled semantic guidance baseline by reaching the query 23.33% ...
- I NTRODUCTION Everyday, humans demonstrate notable semantic and physical understanding of their environments.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, we present SINGER for language-guided autonomous drone navigation in the open world using only onboard sensing and compute.
- Through extensive hardware flight experiments, we demonstrate superior zero-shot sim-to-real transfer of our policy to unseen environments and unseen language-conditioned goal objects.
- In this work, we ask the question: “Can we train a visionlanguage drone navigation policy to reach previously unseen goal objects in a previously unseen environment using only ...

## Abstract Cue
- — Large vision-language models have driven remarkable progress in open-vocabulary robot policies, e.g., generalist robot manipulation policies, that enable robots to complete complex tasks specified in natural language.
