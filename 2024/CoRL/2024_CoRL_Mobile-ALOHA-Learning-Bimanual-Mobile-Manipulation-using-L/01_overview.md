# Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2401.02117.
> PDF retrieval source: https://arxiv.org/pdf/2401.02117. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: CORE
- Tags: Robotics, mobile manipulation, bimanual manipulation, teleoperation
- Official paper: https://arxiv.org/abs/2401.02117
- Full-text retrieval: https://arxiv.org/pdf/2401.02117
- Code/Project: https://mobile-aloha.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 (1) We lack accessible, plug-and-play hardware for whole-body teleoperation.를 문제로 두고, On the hardware front, we present Mobile ALOHA, a low-cost and whole-body teleoperation system for collecting bimanual mobile manipulation data.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Imitation learning from human demonstrations has shown impressive performance in robotics.
- **p. 1 / Abstract - extractive body cue:** However, most results focus on table-top manipulation, lacking the mobility and dexterity necessary for generally useful tasks.
- **p. 1 / Abstract - extractive body cue:** In this work, we develop a system for imitating mobile manipulation tasks that are bimanual and require whole-body control.
- **p. 1 / Abstract - extractive body cue:** We first present Mobile ALOHA, a low-cost and whole-body teleoperation system for data collection.
- **p. 1 / Abstract - extractive body cue:** It augments the ALOHA system [104] with a mobile base, and a whole-body teleoperation interface.
- **p. 2 / 1. Introduction - extractive body cue:** (1) We lack accessible, plug-and-play hardware for whole-body teleoperation.
- **p. 2 / 1. Introduction - extractive body cue:** We seek to tackle the challenges of applying imitation learning to bimanual mobile manipulation in this paper.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** On the hardware front, we present Mobile ALOHA, a low-cost and whole-body teleoperation system for collecting bimanual mobile manipulation data.
- **p. 2 / 1. Introduction - extractive body cue:** The main contribution of this paper is a system for learning complex mobile bimanual manipulation tasks.
- **p. 1 / 1. Introduction - extractive body cue:** Imitation learning from human-provided demonstrations is a promising tool for developing generalist robots, as it allows people to teach arbitrary skills to robots.
- **p. 4 / 3. Mobile ALOHA Hardware - extractive body cue:** Connecting the operator to the mobile manipulator directly also enables coarse haptic feedback when the robot collides with objects.
- **p. 1 / Abstract - extractive body cue:** In this work, we develop a system for imitating mobile manipulation tasks that are bimanual and require whole-body control.
- **p. 5 / 3. Mobile ALOHA Hardware - extractive body cue:** The training objective for a mobile manipulation policy πm for a task m is E(oi,aiarms,ai base)∼Dm mobile  L(ai arms, ai base, πm(oi))  + ...
- **p. 2 / 1. Introduction - extractive body cue:** While many recent works demonstrate that highly expressive policy classes such as diffusion models and transformers can perform well on fine-grained, multi-modal manipulation tasks, it ...
- **p. 5 / 3. Mobile ALOHA Hardware - extractive body cue:** In this work, we use a co-training pipeline that leverages the existing static ALOHA datasets to improve the performance of imitation learning for mobile manipulation, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This observation is also consistent across different class of state-of-the-art imitation learning methods, including ACT [104] and Diffusion Policy [18]. | egocentric RGB-D, language/task goal, base-arm proprioception | p. 2 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware) |
| State/latent | observation, consistent, across, different, class, state-of-the-art, imitation, learning, methods, including, ACT, Diffusion | map/object/contact state와 base-arm coordination decision | p. 2 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction) |
| Output/action | We also record the joint positions of all 4 robot arms to be used as policy observations and actions. | base motion plus arm/gripper action | p. 4 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware) |
| Objective/outcome | The training objective for a mobile manipulation policy πm for a task m is E(oi,aiarms,ai base)∼Dm mobile  L(ai arms, ai base, πm(oi))  + E(oi,aiarms)∼Dstatic  L(ai arms, [0, 0], πm(oi)) ... | long-horizon task success, reachability, collision과 recovery | p. 5 (3. Mobile ALOHA Hardware), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Abstract) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** On the hardware front, we present Mobile ALOHA, a low-cost and whole-body teleoperation system for collecting bimanual mobile manipulation data.
- **p. 2 / 1. Introduction - extractive body cue:** The main contribution of this paper is a system for learning complex mobile bimanual manipulation tasks.
- **p. 1 / 1. Introduction - extractive body cue:** Imitation learning from human-provided demonstrations is a promising tool for developing generalist robots, as it allows people to teach arbitrary skills to robots.
- **p. 4 / 3. Mobile ALOHA Hardware - extractive body cue:** Connecting the operator to the mobile manipulator directly also enables coarse haptic feedback when the robot collides with objects.
- **p. 1 / Abstract - extractive body cue:** In this work, we develop a system for imitating mobile manipulation tasks that are bimanual and require whole-body control.
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** Co-training improves the whole-task success rate in 5 out of the 7 tasks, with a boost of 45%, 20%, 80%, 95% and 80% respectively.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Co-training improves ACT performance. Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ACT. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Co-train vs. Pre-train. Co-train outperforms pre-train on the Wipe Wine task. For pre-train, we first train ACT on the static ALOHA data and ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (6.1. Co-training Improves Performance), p. 7 (Figure/Table caption) |
| Embodiment/environment | We then evaluate each policy in the real-world, with randomization of robot and objects configurations as described in Figure 3. | hardware/simulator version and reset protocol | p. 8 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance) |
| Dataset/benchmark | In Table 2, we report co-training and no cotraining success rates on 2 real-world tasks: Wipe Wine and Push Chairs. | role, split, size and leakage | p. 8 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance), p. 9 (6.1. Co-training Improves Performance), p. 9 (6.1. Co-training Improves Performance) |
| Metric | Table 1: Co-training improves ACT performance. Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ACT. It is particularly important for sub-tasks like ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 8 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance) |
| Baseline/ablation | Co-train outperforms pre-train on the Wipe Wine task. | fair input/data/compute/action matching | p. 9 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 8. User Studies - extractive body cue:** Despite Mobile ALOHA's simplicity and performance, there are still limitations that we hope to address in future works.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Hardware Details. Left: Mobile ALOHA has two wrist cameras and one top camera, with onboard power and compute. Middle: The teleoperation setup can ...
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** In all of these cases, compounding errors appear to be the main source of failure, either from the stochasticity of robot base velocity control or ...
- **p. 9 / 6.1. Co-training Improves Performance - extractive body cue:** The main failure modes are imprecise grasping on Lift Glass and Wipe as well as jerky motion when switching between chunks.
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** The only task that falls below 80% success is Cook Shrimp (40%), which is a 75-second long-horizon task for which we only collected 20 demonstrations.
- **p. 10 / 8. User Studies - extractive body cue:** Conclusion, Limitations and Future Directions In summary, our paper tackles both the hardware and the software aspects of bimanual mobile manipulation.
- **p. 9 / 6.1. Co-training Improves Performance - extractive body cue:** Only the representations of VINN are cotrained, while the action prediction mechanism of VINN does not have a way to leverage the out-ofdomain static ALOHA ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 (1) We lack accessible, plug-and-play hardware for whole-body teleoperation.를 문제로 두고, On the hardware front, we present Mobile ALOHA, a low-cost and whole-body teleoperation system for collecting bimanual mobile manipulation data.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction), p. 5 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** (1) We lack accessible, plug-and-play hardware for whole-body teleoperation. (p. 2, 1. Introduction).
- **Actual contribution:** The main contribution of this paper is a system for learning complex mobile bimanual manipulation tasks. (p. 2, 1. Introduction).
- **Evaluation boundary:** Table 1: Co-training improves ACT performance. Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ACT. It is particularly important for ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** In all of these cases, compounding errors appear to be the main source of failure, either from the stochasticity of robot base velocity control or from rich contacts such as ... (p. 8, 6.1. Co-training Improves Performance).
