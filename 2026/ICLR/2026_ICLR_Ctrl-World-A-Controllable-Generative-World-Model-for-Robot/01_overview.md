# Ctrl-World: A Controllable Generative World Model for Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://iclr.cc/virtual/2026/poster/10011332.
> PDF retrieval source: https://arxiv.org/pdf/2510.10125. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, robot manipulation, controllable generation
- Official paper: https://iclr.cc/virtual/2026/poster/10011332
- Full-text retrieval: https://arxiv.org/pdf/2510.10125
- Code/Project: https://ctrl-world.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Moreover, existing models typically lack the fine-grained control required to capture the 1 를 문제로 두고, In this paper, we introduce Ctrl-World, a Controllable, multi-view generative world model designed for policy-in-the-loop interaction, enabling multi-step rollouts entirely within imagination space, as illustrated in Figure 1.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Generalist robot policies can now perform a wide range of manipulation skills, but evaluating and improving their ability with unfamiliar objects and instructions remains a ...
- **p. 1 / ABSTRACT - extractive body cue:** Rigorous evaluation requires a large number of realworld rollouts, while systematic improvement demands additional corrective data with expert labels.
- **p. 1 / ABSTRACT - extractive body cue:** Both of these processes are slow, costly, and difficult to scale.
- **p. 1 / ABSTRACT - extractive body cue:** World models offer a promising, scalable alternative by enabling policies to rollout within imagination space.
- **p. 1 / ABSTRACT - extractive body cue:** However, a key challenge is building a controllable world model that can handle multi-step interactions with generalist robot policies.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Moreover, existing models typically lack the fine-grained control required to capture the 1.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Equally critical is policy improvement: once weaknesses are revealed, existing methods offer few ways to strengthen policies on failure cases beyond collecting more expert data.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Ctrl-World, a Controllable, multi-view generative world model designed for policy-in-the-loop interaction, enabling multi-step rollouts entirely within imagination space, as illustrated ...
- **p. 1 / ABSTRACT - extractive body cue:** We show that our method can accurately rank policy performance without real-world robot rollouts.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Building on early works (Finn & Levine, 2017; Ebert et al., 2018; Xie et al., 2019; Dasari et al., 2019; Yang et al., 2023; Wu ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** To explore a larger search space, we introduce structured perturbations to encourage diversity in rollouts.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The core contribution of this work is a controllable world model for robot manipulation.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Specifically, robot observation ot = [I1 t , . . . , In t , qt] includes n camera views [I1 t , . . ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** 1: for i = 0 to M do 2: τ = [oi 0] 3: for j = 0 to N do 4: Current observation: ot ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Some works leverage video prediction models to synthesize robotic trajectories with fake action labels, and these synthetic trajectories can then be used for policy learning ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Specifically, robot observation ot = [I1 t , . . . , In t , qt] includes n camera views [I1 t , . . . , In t ] and robot ... | observation, uncertainty/risk estimate와 task command | p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| State/latent | Specifically, robot, observation, includes, camera, views, pose, policy, outputs, H-step, action, chunk | safe set, recovery state 또는 constraint margin | p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (1 INTRODUCTION) |
| Output/action | A modern generalist policy π typically maps multi-view observations and language instructions into a sequence of actions (Zhao et al., 2023; Black et al., 2025). | shielded, recovery 또는 safe action | p. 3 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 4 (1 INTRODUCTION) |
| Objective/outcome | A complementary line of research integrates future-prediction objectives into generalist policies via co-training (Zhao et al., 2025; Li et al., 2025a; Zhu et al., 2025; Guo et al., 2024; Gao et al., ... | task return과 violation/failure probability | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 4 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Ctrl-World, a Controllable, multi-view generative world model designed for policy-in-the-loop interaction, enabling multi-step rollouts entirely within imagination space, as illustrated ...
- **p. 1 / ABSTRACT - extractive body cue:** We show that our method can accurately rank policy performance without real-world robot rollouts.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Building on early works (Finn & Levine, 2017; Ebert et al., 2018; Xie et al., 2019; Dasari et al., 2019; Yang et al., 2023; Wu ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** To explore a larger search space, we introduce structured perturbations to encourage diversity in rollouts.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The core contribution of this work is a controllable world model for robot manipulation.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Spatial Shape Towel-Dir Novel-Obj Average 0.0 0.2 0.4 0.6 0.8 1.0 Success rate 0.29 0.44 0.57 0.25 0.39 0.88 0.91 0.80 0.75 0.83 Base Policy ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** While the pretrained π0.5 policy achieves low success rates on unfamiliar objects and novel instructions, post-training aligns the model with new instructions and boosts the ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** As shown in Table 1, Ctrl-World-third-view outperforms these prior models, and multi-view joint prediction further improves generation quality.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Embodiment/environment | The DROID dataset (Khazatsky et al., 2024) contains 95,599 diverse trajectories collected from 564 scenes, providing dense coverage of the workspace. | hardware/simulator version and reset protocol | p. 5 (5 EXPERIMENTS), p. 5 (5 EXPERIMENTS) |
| Dataset/benchmark | Consistent with observations from prior work (Quevedo et al., 2025; Zhu et al., 2024), we also find that these baselines struggle to capture robot-object interactions and often generate hallucinated predictions. | role, split, size and leakage | p. 5 (5 EXPERIMENTS), p. 5 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Metric | Table 3: Comparison of instruction-following and success rate across methods and tasks. Breakdown for policy evaluation. We present the instruction-following and low-level execution success rates in Table 3. Task details and criterion. ... | definition, denominator, direction and uncertainty | p. 17 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Baseline/ablation | Consistent with observations from prior work (Quevedo et al., 2025; Zhu et al., 2024), we also find that these baselines struggle to capture robot-object interactions and often generate hallucinated predictions. | fair input/data/compute/action matching | p. 6 (5 EXPERIMENTS), p. 5 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 5 EXPERIMENTS - extractive body cue:** The inclusion of diverse actions and failure data is crucial, as it allows us to train a controllable world model that can simulate a wide ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Although some failure trajectories are included in the DROID dataset, there are still many failure modes outside the data distribution.
- **p. 17 / Figure/Table caption - extractive body cue:** Table 3: Comparison of instruction-following and success rate across methods and tasks. Breakdown for policy evaluation. We present the instruction-following and low-level execution success rates ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** We also observe that generalist policies tend to keep retrying in the real world after failed attempts, which the world model sometimes does not capture.
- **p. 5 / 5 EXPERIMENTS - extractive body cue:** This includes about 76k successful and about 19k failed trajectories.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Prior models rely on single-view prediction, suffering from partial observability and hallucinations (e.g., failing to move the green towel or grasp the red bowl).
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Prediction highlighted in the green box are inferred from other camera views, while those in the red box are retrieved from memory. methods WPE, IRASim ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Moreover, existing models typically lack the fine-grained control required to capture the 1 를 문제로 두고, In this paper, we introduce Ctrl-World, a Controllable, multi-view generative world model designed for policy-in-the-loop interaction, enabling multi-step rollouts entirely within imagination space, as illustrated in Figure 1.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Moreover, existing models typically lack the fine-grained control required to capture the ... (p. 1, 1 INTRODUCTION).
- **Actual contribution:** Building on early works (Finn & Levine, 2017; Ebert et al., 2018; Xie et al., 2019; Dasari et al., 2019; Yang et al., 2023; Wu et al., 2024) as well ... (p. 3, 1 INTRODUCTION).
- **Evaluation boundary:** Table 2: Ablations on key components in Ctrl-World. Removing memory mechanisms, frame-level action conditioning or multi-view joint predictions all lead to a performance drop. 2025) and IRASim (Zhu et al., ... (p. 6, Figure/Table caption).
- **Explicit failure boundary:** We also observe that generalist policies tend to keep retrying in the real world after failed attempts, which the world model sometimes does not capture. (p. 9, 5 EXPERIMENTS).
