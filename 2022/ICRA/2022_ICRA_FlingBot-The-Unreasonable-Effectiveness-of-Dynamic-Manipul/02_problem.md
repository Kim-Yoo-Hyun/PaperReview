# Problem

- Year/Venue: 2022 / ICRA
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, deformable object, cloth manipulation, dynamic manipulation, vision-based control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://flingbot.cs.columbia.edu/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Yet, most prior works have tackled cloth manipulation using exclusively single-arm quasi-static actions, which requires a large number of interactions for challenging initial cloth configurations and strictly limits ...

## 해결하려는 문제
- Our approach learns how to unfold a piece of fabric from arbitrary initial configurations using a pick, stretch, and fling primitive for a dual-arm setup from visual observations.
- The final system achieves over 80% coverage within 3 actions on novel cloths, can unfold cloths larger than the system’s reach range, and generalizes to T-shirts despite being ...
- In this work, we demonstrate the effectiveness of dynamic flinging actions for cloth unfolding with our proposed self-supervised learning framework, FlingBot.

## 선행 연구 / 배경 단서
- From goal-conditioned folding to fabric smoothing , prior works have achieved success using exclusively single-arm quasistatic interactions (e.g., pick & place) for cloth manipulation.
- In summary: • Our main contribution is in demonstrating the effectiveness of dynamic manipulation for cloth unfolding through our self-supervised learning framework, FlingBot. • We propose a parameterization ...
- To achieve this goal, we present FlingBot, a self-supervised algorithm that learns how to unfold cloths from arbitrary initial configurations using a pick, stretch, and fling primitive for ...
