# Evaluation - ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=72UR53jN7T; PDF retrieval source: https://arxiv.org/pdf/2507.16815. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Quantitative Evaluation), p. 10 (4.5. Analysis of ThinkAct), p. 10 (4.4. Ablation Study), p. 7 (4.2. Quantitative Evaluation), p. 9 (4.4. Ablation Study), p. 6 (4.1. Experimental Setup)): On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA Zhao et al.

## Evaluation Body Digest

- **p. 8 / 4.2. Quantitative Evaluation - extractive body cue:** Okay, I'm ready to give the final trajectory: move to eggplant, lift it, and place it in basket. </think> "Pick up the book and place ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Training Datasets and Evaluation Benchmarks For SFT cold-start, we fine-tune the MLLM using trajectories from the subset of OXE, and QA tasks from RoboVQA Sermanet ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We evaluate ThinkAct on two robot manipulation and three embodied reasoning benchmarks.
- **p. 10 / 4.5. Analysis of ThinkAct - extractive body cue:** We focus on two key aspects: (1) how reasoning facilitates effective few-shot adaptation to new tasks and environments, and (2) how it enables the robot ...
- **p. 8 / 4.2. Quantitative Evaluation - extractive body cue:** Dataset Split / Metric GPT-4V LLaVA-Video InternVL2.5 InternVL3 NVILA Qwen2.5-VL Qwen2.5-VL* Magma ThinkAct (Ours) EgoPlanBench2 Daily life 36.7 38.0 36.2 38.5 35.8 31.4 47.9 32.1 ...
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** Robot Manipulation To assess the effectiveness of ThinkAct on robot manipulation task, we evaluate on SimplerEnv Li et al.
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** The enhanced reasoning ability of ThinkAct enables better generalization and scene comprehension, resulting in strong performance on this benchmark.
- **p. 9 / 4.3. Qualitative Results - extractive body cue:** That seems clear now.</think> <answer>The carpet on the floor is rectangular.</answer> (a) RoboVQA (b) OpenEQA ThinkAct w/o RL ThinkAct ThinkAct Figure 4: Qualitative comparison of ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiment (p. 6); 4.1. Experimental Setup (p. 6); 4.2. Quantitative Evaluation (p. 7); 4.3. Qualitative Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Quantitative Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA Zhao et al. | p. 7 (4.2. Quantitative Evaluation) |
| 4.5. Analysis of ThinkAct | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5, ThinkAct consistently outperforms state-of-the-art methods, achieving the highest success rates across all tasks. | p. 10 (4.5. Analysis of ThinkAct) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | Method SimplerEnv EgoPlan RoboVQA ThinkAct (Ours) 60.1 48.2 59.8 Ours w/o 𝑟traj 59.2 47.9 58.5 Ours w/o 𝑟goal 59.1 47.6 58.9 Ours w/o 𝑟traj, ... | p. 10 (4.4. Ablation Study) |
| 4.2. Quantitative Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | ThinkAct outperforms the second-best method by 2.5% and 4.1 BLEU score on these two benchmarks, demonstrating its strength in long-horizon and multi-step planning. | p. 7 (4.2. Quantitative Evaluation) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | We start from the full version of ThinkAct, which achieves the best performance across all benchmarks. | p. 9 (4.4. Ablation Study) |

## Dataset / Benchmark Role

- **p. 8 / 4.2. Quantitative Evaluation - extractive body cue:** Okay, I'm ready to give the final trajectory: move to eggplant, lift it, and place it in basket. </think> "Pick up the book and place ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Training Datasets and Evaluation Benchmarks For SFT cold-start, we fine-tune the MLLM using trajectories from the subset of OXE, and QA tasks from RoboVQA Sermanet ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We evaluate ThinkAct on two robot manipulation and three embodied reasoning benchmarks.
- **p. 10 / 4.5. Analysis of ThinkAct - extractive body cue:** We focus on two key aspects: (1) how reasoning facilitates effective few-shot adaptation to new tasks and environments, and (2) how it enables the robot ...
- **p. 8 / 4.2. Quantitative Evaluation - extractive body cue:** Dataset Split / Metric GPT-4V LLaVA-Video InternVL2.5 InternVL3 NVILA Qwen2.5-VL Qwen2.5-VL* Magma ThinkAct (Ours) EgoPlanBench2 Daily life 36.7 38.0 36.2 38.5 35.8 31.4 47.9 32.1 ...
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** Robot Manipulation To assess the effectiveness of ThinkAct on robot manipulation task, we evaluate on SimplerEnv Li et al.
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** The enhanced reasoning ability of ThinkAct enables better generalization and scene comprehension, resulting in strong performance on this benchmark.
- **p. 9 / 4.3. Qualitative Results - extractive body cue:** That seems clear now.</think> <answer>The carpet on the floor is rectangular.</answer> (a) RoboVQA (b) OpenEQA ThinkAct w/o RL ThinkAct ThinkAct Figure 4: Qualitative comparison of ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: We introduce ThinkAct, a reasoning VLA framework capable of thinking before acting. Through reasoning reinforced by our action-aligned visual feedback, ThinkAct enables capabilities ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of our ThinkAct. (a) Given observation 𝑜𝑡and instruction 𝑙, ThinkAct advances action- aligned rewards derived from visual trajectory 𝜏to incentivize embodied reasoning ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Quantitative comparisons of robot manipulation tasks on SimplerEnv Li et al. (2024) and LIBERO Liu et al. (2023) benchmarks. Bold denotes the best ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Quantitative comparisons of embodied reasoning tasks on EgoPlan-Bench2, RoboVQA, and OpenEQA benchmarks. Note that, Qwen2.5-VL* indicates fine-tuning the original Qwen2.5-VL using EgoPlan-IT Chen ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Qualitative results of intermediate reasoning steps and visualized trajectory for robot manipulation tasks on SimplerEnv and LIBERO benchmarks.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative comparison of reasoning process and the derived answer for our ThinkAct with and without RL for embodied reasoning tasks on RoboVQA and ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 3: Quantitative ablation study for our proposed RL rewards in ThinkAct on SimplerEnv, EgoPlan-Bench2, and RoboVQA benchmarks.
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5: Few-shot adaptation results on LIBERO. We use 10 demonstrations per task for fine-tuning. Dropped!! <think>Let's start by examining the scene and the task. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Okay, I'm ready to give the final trajectory: move to eggplant, lift it, and place it in basket. </think> "Pick up the book and ... | embodiment, simulator version and control stack | p. 8 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup) |
| Task/environment | Training Datasets and Evaluation Benchmarks For SFT cold-start, we fine-tune the MLLM using trajectories from the subset of OXE, and QA tasks from RoboVQA ... | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (3.3. Reasoning-Enhanced Action Adaptation), p. 3 (3.1. Problem Formulation) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.1. Problem Formulation), p. 6 (3.4. Learning Strategy and Inference) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| (2023) with long-horizon tasks are evaluated using task success rate. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA Zhao et al. | definition/direction/unit from same section | p. 7 (4.2. Quantitative Evaluation) |
| 5, ThinkAct consistently outperforms state-of-the-art methods, achieving the highest success rates across all tasks. | definition/direction/unit from same section | p. 10 (4.5. Analysis of ThinkAct) |
| Method SimplerEnv EgoPlan RoboVQA ThinkAct (Ours) 60.1 48.2 59.8 Ours w/o 𝑟traj 59.2 47.9 58.5 Ours w/o 𝑟goal 59.1 47.6 58.9 Ours w/o 𝑟traj, ... | definition/direction/unit from same section | p. 10 (4.4. Ablation Study) |
| (2024) are free-form QA tasks evaluated using BLEU score Papineni et al. | definition/direction/unit from same section | p. 7 (4.1. Experimental Setup) |
| Without the goal reward, performance also declines, suggesting that 𝑟goal plays a key role in incentivizing long-horizon reasoning. | definition/direction/unit from same section | p. 9 (4.4. Ablation Study) |
| The robot then successfully completes the task, demonstrating ThinkAct's ability to reflect on errors and self-correct through structured reasoning. | definition/direction/unit from same section | p. 11 (4.5. Analysis of ThinkAct) |
| Figure 1: We introduce ThinkAct, a reasoning VLA framework capable of thinking before acting. Through reasoning reinforced by our action-aligned visual feedback, ThinkAct enables ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA Zhao et al. | comparison identity and matched condition | p. 7 (4.2. Quantitative Evaluation) |
| 1, on the SimplerEnv, incorporating our reasoning-guided visual plan latents allows ThinkAct to outperform our baseline action model, DiT-Policy, by 15.5%, 16.9%, and 11.4% ... | comparison identity and matched condition | p. 7 (4.2. Quantitative Evaluation) |
| 5, ThinkAct consistently outperforms state-of-the-art methods, achieving the highest success rates across all tasks. | comparison identity and matched condition | p. 10 (4.5. Analysis of ThinkAct) |
| When both 𝑟traj and 𝑟goal are removed, leaving only QA-style reward from QA datasets, the model shows only marginal improvements over the SFT baseline, ... | comparison identity and matched condition | p. 9 (4.4. Ablation Study) |
| That seems clear now.</think> <answer>The carpet on the floor is rectangular.</answer> (a) RoboVQA (b) OpenEQA ThinkAct w/o RL ThinkAct ThinkAct Figure 4: Qualitative comparison ... | comparison identity and matched condition | p. 9 (4.3. Qualitative Results) |
| ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning Table 2: Quantitative comparisons of embodied reasoning tasks on EgoPlan-Bench2, RoboVQA, and OpenEQA benchmarks. | comparison identity and matched condition | p. 8 (4.2. Quantitative Evaluation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Finally, the SFT cold-start model without RL yields the lowest scores, verifying the effectiveness of our RL fine-tuning for eliciting the reasoning capability in ... | component/input/data sensitivity | p. 9 (4.4. Ablation Study) |
| When both 𝑟traj and 𝑟goal are removed, leaving only QA-style reward from QA datasets, the model shows only marginal improvements over the SFT baseline, ... | component/input/data sensitivity | p. 9 (4.4. Ablation Study) |
| (2024) includes Google-VM (Visual Matching), Google-VA (Variant Aggregation), and Bridge-VM setups, introducing variations in color, material, lighting, and camera pose to evaluate model robustness. | component/input/data sensitivity | p. 7 (4.2. Quantitative Evaluation) |
| ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning Table 3: Quantitative ablation study for our proposed RL rewards in ThinkAct on SimplerEnv, EgoPlan-Bench2, and ... | component/input/data sensitivity | p. 10 (4.4. Ablation Study) |
| (2023) tasks are further fine-tuned for 75K iterations with batch size 128. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| (2023) as the latent projector with 32 queries and fine-tune on 100K OXE samples for 120K iterations using batch size 256 and learning rate ... | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are summarized as follows: • We propose ThinkAct, a dual-system framework that mutually enhances action execution and visualgrounded embodied reasoning connected ... | On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA Zhao et al. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Quantitative Evaluation), p. 10 (4.5. Analysis of ThinkAct), p. 10 (4.4. Ablation Study), p. 7 (4.2. Quantitative Evaluation), p. 9 (4.4. Ablation Study), p. 6 (4.1. Experimental Setup) |
| Primary metric/result | 5, ThinkAct consistently outperforms state-of-the-art methods, achieving the highest success rates across all tasks. | numeric claim only at cited anchor | p. 10 (4.5. Analysis of ThinkAct) |

- Numeric sentences retained from the body:
- **p. 10 / 4.5. Analysis of ThinkAct - extractive body cue:** We fine-tune the action model on just 10 demonstrations per task and evaluate performance over 100 trials.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Through extensive experiments across embodied reasoning and robot manipulation benchmarks, we demonstrated strong long-horizon planning, few-shot adaptation, and emergent behaviors such as failure detection ... | p. 11 (5. Conclusion) |
| body limitation/failure cue | (2023) The RoboFail dataset captures robot manipulation failures in both simulation and real-world scenarios. | p. 12 (5. Conclusion) |
| body limitation/failure cue | It includes 100 simulated failure cases in the AI2THOR environment and 30 real-world cases collected via UR5e teleoperation. | p. 12 (5. Conclusion) |
| body limitation/failure cue | The MLLM detects the failure and replans the pickup, leading to successful completion. | p. 15 (5. Conclusion) |
| body limitation/failure cue | Reasoning Elicit Self-Correction Failure detection and self-correction are critical for robust robot manipulation Liu et al. | p. 11 (4.5. Analysis of ThinkAct) |
| body limitation/failure cue | A8(a), the robot fails to grasp a mug. | p. 15 (5. Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| (2024) for 6K iterations, using batch size 64, learning rate 1e-6, and rollout size 5. | p. 6 (4.1. Experimental Setup) |
| (2023) tasks are further fine-tuned for 75K iterations with batch size 128. | p. 6 (4.1. Experimental Setup) |
| Okay, I'm ready to give the final trajectory: move to eggplant, lift it, and place it in basket. </think> "Pick up the book and ... | p. 8 (4.2. Quantitative Evaluation) |
| (2024) example, the SFT cold-start model focuses only on the current state and fails to reason over future steps, while the RL-tuned model successfully ... | p. 9 (4.3. Qualitative Results) |
| We fine-tune the action model on just 10 demonstrations per task and evaluate performance over 100 trials. | p. 10 (4.5. Analysis of ThinkAct) |
| Reward acts at every step (a) (b) Latent Projector State Encoder reasons every N steps Figure 2: Overview of our ThinkAct. | p. 4 (3.1. Problem Formulation) |
| 2(a), given an observation 𝑜𝑡at timestep 𝑡and a task instruction 𝑙, the MLLM ℱ𝜃autoregressively generates a sequence of latent embeddings for reasoning 𝑣𝑡∈R/𝑣𝑡/×𝑑and visual ... | p. 4 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning) |
| Thus, we solely update the state encoder, latent projector, and action 5 | p. 5 (3.3. Reasoning-Enhanced Action Adaptation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 11 / 5. Conclusion - extractive body cue:** Through extensive experiments across embodied reasoning and robot manipulation benchmarks, we demonstrated strong long-horizon planning, few-shot adaptation, and emergent behaviors such as failure detection and ...
- **p. 12 / 5. Conclusion - extractive body cue:** (2023) The RoboFail dataset captures robot manipulation failures in both simulation and real-world scenarios.
- **p. 12 / 5. Conclusion - extractive body cue:** It includes 100 simulated failure cases in the AI2THOR environment and 30 real-world cases collected via UR5e teleoperation.
- **p. 15 / 5. Conclusion - extractive body cue:** The MLLM detects the failure and replans the pickup, leading to successful completion.
- **p. 11 / 4.5. Analysis of ThinkAct - extractive body cue:** Reasoning Elicit Self-Correction Failure detection and self-correction are critical for robust robot manipulation Liu et al.
- **p. 15 / 5. Conclusion - extractive body cue:** A8(a), the robot fails to grasp a mug.

- **Evidence anchors reviewed:** datasets p. 8 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 10 (4.5. Analysis of ThinkAct), p. 8 (4.2. Quantitative Evaluation), p. 7 (4.2. Quantitative Evaluation), metrics p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Evaluation), p. 10 (4.5. Analysis of ThinkAct), p. 10 (4.4. Ablation Study), p. 7 (4.1. Experimental Setup), p. 9 (4.4. Ablation Study), baselines p. 7 (4.2. Quantitative Evaluation), p. 7 (4.2. Quantitative Evaluation), p. 10 (4.5. Analysis of ThinkAct), p. 9 (4.4. Ablation Study), p. 9 (4.3. Qualitative Results), p. 8 (4.2. Quantitative Evaluation), results p. 7 (4.2. Quantitative Evaluation), p. 10 (4.5. Analysis of ThinkAct), p. 10 (4.4. Ablation Study), p. 7 (4.2. Quantitative Evaluation), p. 9 (4.4. Ablation Study), p. 6 (4.1. Experimental Setup).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
