# Method

- Year/Venue: 2022 / ICLR
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, deformable object, tool use, differentiable physics, skill abstraction, Planning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://diffskill.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Given an initial state s0 , a goal state sg and the transition dynamics p of a differentiable simulator, we use gradient-based trajectory optimization to solve for an ...

## 원리적 동기
- 2.2 C OLLECTING D EMONSTRATION T RAJECTORIES WITH D IFFERENTIABLE P HYSICS Previous work has shown that differentiable physics solvers can acquire short-horizon skills for deformable object manipulation ...
- Given an initial state s0 , a goal state sg and the transition dynamics p of a differentiable simulator, we use gradient-based trajectory optimization to solve for an ...

## 핵심 방법론
- Trajectory Opt (Oracle) Behavior Cloning Model-free RL (TD3) Model-free RL (SAC) Trajectory Opt (Oracle) Behavior Cloning Model-free RL (TD3) Model-free RL (SAC) Trajectory Opt (Oracle) Model-free RL (TD3) ...
- Each entry shows the normalized improvement / success rate.
- The top bar shows H, the planning horizon for each environment.
- 3.5 A BLATION A NALYSIS We perform two ablations on DiffSkill.
- First, we try removing the planning over the discrete variables that decides which tool to use at each step.
