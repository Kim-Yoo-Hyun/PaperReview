# Evaluation - WorldGym: World Model as An Environment for Policy Evaluation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10008029; PDF retrieval source: https://arxiv.org/pdf/2506.00613. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 17 (Figure/Table caption), p. 6 (Figure/Table caption), p. 23 (Figure/Table caption), p. 22 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption)): Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground truth task success labels. GPT-4o achieves ...

## Evaluation Body Digest

- **p. 8 / 1 INTRODUCTION - extractive body cue:** We suspect that OpenVLA consistently outperforms Octo and RT-1-X on OOD language tasks due to its strong VLM backbone and richer robot pretraining dataset (Kim ...
- **p. 8 / 1 INTRODUCTION - extractive body cue:** Put orange on plate Image Model Put orange on plate Legend Image Edit Prompt Robot Policy Instruction (a) add an orange Put orange on plate ...
- **p. 9 / 1 INTRODUCTION - extractive body cue:** Task RT-1-X Octo OpenVLA Move Pot Into Drying Rack 3 0 7 Move The Pot To The Counter 0 0 1 Put Plate On Drying ...
- **p. 9 / 1 INTRODUCTION - extractive body cue:** We use Nano Banana (Google, 2025) to add distractions to every image of the OpenVLA Bridge task suite.
- **p. 17 / Figure/Table caption - extractive body cue:** Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground truth ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6: Success Rates of different model versions in WorldGym. We evaluate different generations of Octo and OpenVLA in the world model, showing that WorldGym ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Success rates of modern VLAs, as evaluated within WorldGym and the real world. control policy by only moving one action dimension at once ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 7: Success Rate within WorldGym throughout training. We train a video-based policy and a diffusion policy from scratch and evaluate it within our world ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground ... | p. 17 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: Success Rates of different model versions in WorldGym. We evaluate different generations of Octo and OpenVLA in the world model, showing that ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5: Detailed Bridge Evaluation Results comparing RT-1-X (O'Neill et al., 2023), Octo (Octo Model Team et al., 2024), and OpenVLA (Kim et al.) ... | p. 23 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Policy rollouts on Google Robot (RT-1 subset). OpenVLA outperforms RT-1-X and Octo, but by a smaller margin than on the Bridge dataset. ... | p. 22 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Success rates of modern VLAs, as evaluated within WorldGym and the real world. control policy by only moving one action dimension at ... | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 1 INTRODUCTION - extractive body cue:** We suspect that OpenVLA consistently outperforms Octo and RT-1-X on OOD language tasks due to its strong VLM backbone and richer robot pretraining dataset (Kim ...
- **p. 8 / 1 INTRODUCTION - extractive body cue:** Put orange on plate Image Model Put orange on plate Legend Image Edit Prompt Robot Policy Instruction (a) add an orange Put orange on plate ...
- **p. 9 / 1 INTRODUCTION - extractive body cue:** Task RT-1-X Octo OpenVLA Move Pot Into Drying Rack 3 0 7 Move The Pot To The Counter 0 0 1 Put Plate On Drying ...
- **p. 9 / 1 INTRODUCTION - extractive body cue:** We use Nano Banana (Google, 2025) to add distractions to every image of the OpenVLA Bridge task suite.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of WorldGym. Given an initial frame and an action sequence predicted by a policy, WorldGym uses a world model to interactively predict ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Qualitative evaluation of the world model on Bridge, RT-1, VIOLA, and Berkeley UR5. In each group, top row shows the ground truth video ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Results on end-effector control across action dimensions. Generated videos closely follow the gripper controls such as open and close the gripper as well ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Success rates of modern VLAs, as evaluated within WorldGym and the real world. control policy by only moving one action dimension at once ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative policy rollouts on Bridge and Google Robot for RT-1-X, Octo, and OpenVLA. OpenVLA rollouts often lead to more visual successes than the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6: Success Rates of different model versions in WorldGym. We evaluate different generations of Octo and OpenVLA in the world model, showing that WorldGym ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 7: Success Rate within WorldGym throughout training. We train a video-based policy and a diffusion policy from scratch and evaluate it within our world ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 8: OOD: Color Classification. We add red and blue pieces of paper to a table, and ask the policies to "pick red" or "pick ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We suspect that OpenVLA consistently outperforms Octo and RT-1-X on OOD language tasks due to its strong VLM backbone and richer robot pretraining dataset ... | embodiment, simulator version and control stack | p. 8 (1 INTRODUCTION), p. 8 (1 INTRODUCTION) |
| Task/environment | Put orange on plate Image Model Put orange on plate Legend Image Edit Prompt Robot Policy Instruction (a) add an orange Put orange on ... | reset, timeout, object/scene variation | p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Figure 6: Success Rates of different model versions in WorldGym. We evaluate different generations of Octo and OpenVLA in the world model, showing that ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 4: Success rates of modern VLAs, as evaluated within WorldGym and the real world. control policy by only moving one action dimension at ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 7: Success Rate within WorldGym throughout training. We train a video-based policy and a diffusion policy from scratch and evaluate it within our ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| We can then easily obtain success rates for these unseen tasks by rolling them out within WorldGym, finding that OpenVLA generalizes best (see Table ... | definition/direction/unit from same section | p. 8 (1 INTRODUCTION) |
| The resulting change in mean success rates can be seen in Figure 13. | definition/direction/unit from same section | p. 9 (1 INTRODUCTION) |
| RT-1-X Octo OpenVLA 0 10 20 30 40 50 60 70 Success Rate (%) 15.6% 23.8% 67.4% 7.6% 4.1% 39.4% Effect of OOD Distractors ... | definition/direction/unit from same section | p. 9 (1 INTRODUCTION) |
| Table 5: Detailed Bridge Evaluation Results comparing RT-1-X (O'Neill et al., 2023), Octo (Octo Model Team et al., 2024), and OpenVLA (Kim et al.) ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We suspect that OpenVLA consistently outperforms Octo and RT-1-X on OOD language tasks due to its strong VLM backbone and richer robot pretraining dataset ... | comparison identity and matched condition | p. 8 (1 INTRODUCTION) |
| Table 4: Policy rollouts on Google Robot (RT-1 subset). OpenVLA outperforms RT-1-X and Octo, but by a smaller margin than on the Bridge dataset. ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |
| Additionally, even without access to an image editing model, we demonstrate that WorldGym can be used to evaluate policies' performance on OOD language instructions. | comparison identity and matched condition | p. 8 (1 INTRODUCTION) |
| Table 7: Policy rollout performance comparison in the presence of unrelated distractions. OpenVLA is more robust to distractions over RT-1-X and Octo. However, all ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |
| Table 8: Dataset ablation. Larger training dataset improves all three metrics comparing generated videos and ground-truth validation videos. ↑means higher the better. Subset (Bridge ... | comparison identity and matched condition | p. 25 (Figure/Table caption) |
| Table 9: Parallelism efficiency comparison. Inference time for generating 40-frame video rollouts on an A100 GPU with different horizon lengths, demonstrating the efficiency gains ... | comparison identity and matched condition | p. 25 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| RT-1-X Octo OpenVLA 0 10 20 30 40 50 60 70 Success Rate (%) 15.6% 23.8% 67.4% 7.6% 4.1% 39.4% Effect of OOD Distractors ... | component/input/data sensitivity | p. 9 (1 INTRODUCTION) |
| Figure 13: Effect of OOD Distractors. We use an image editing model to add distractor objects to the Bridge evaluation suite, finding that RT-1- ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Additionally, even without access to an image editing model, we demonstrate that WorldGym can be used to evaluate policies' performance on OOD language instructions. | component/input/data sensitivity | p. 8 (1 INTRODUCTION) |
| Future research could be prioritized to address these issues, all without spending extra effort to set up additional experiments in the real world or ... | component/input/data sensitivity | p. 8 (1 INTRODUCTION) |
| Table 8: Dataset ablation. Larger training dataset improves all three metrics comparing generated videos and ground-truth validation videos. ↑means higher the better. Subset (Bridge ... | component/input/data sensitivity | p. 25 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Key contributions of this paper include: • We propose to use video world model to evaluate robot policies across different robot morphologies, and perform ... | Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground ... | PDF body cue; verify exact table/figure and matched conditions | p. 17 (Figure/Table caption), p. 6 (Figure/Table caption), p. 23 (Figure/Table caption), p. 22 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Primary metric/result | Figure 6: Success Rates of different model versions in WorldGym. We evaluate different generations of Octo and OpenVLA in the world model, showing that ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 9 / 1 INTRODUCTION - extractive body cue:** We use an image editing model to add distractor objects to the Bridge evaluation suite, finding that RT-1X drops in performance by 51%, Octo by ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** For each task and each policy, Kim et al. perform 10 trials, each with randomized initial object locations.
- **p. 7 / 1 INTRODUCTION - extractive body cue:** First, we average success rates across all 17 tasks and find that the relative performance rankings between RT-1-X, Octo, and OpenVLA are the same (Figure ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Pick Carrot Pick Carrot Pick Carrot Pick Cat Pick Cat Pick Taylor Swift Pick Square Figure 10: OOD: Failure modes. | p. 8 (1 INTRODUCTION) |
| body limitation/failure cue | Figure 10: OOD: Failure modes. Left: We add a laptop to the scene, which displays an image of a carrot. In 15% of trials, ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Table 1: Policy Evaluations Results on Bridge OOD Language Tasks. "Move the pot to the counter" is perhaps the most challenging because the Bridge ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | We use an image editing model to add distractor objects to the Bridge evaluation suite, finding that RT-1X drops in performance by 51%, Octo ... | p. 9 (1 INTRODUCTION) |
| body limitation/failure cue | Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground ... | p. 17 (Figure/Table caption) |
| body limitation/failure cue | Table 6: Detailed Bridge OOD Image task results. OpenVLA appears to be more robust across the different OOD settings of object generalization, distractions and ... | p. 24 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 0 5k 10k 20k 40k 60k Checkpoint (training steps) 0 5 10 15 20 25 30 35 Success Rate (%) Mean Success Rate Across ... | p. 6 (1 INTRODUCTION) |
| We evaluate checkpoints of the video prediction policy at 2K, 8K, 12K, and 18K steps, and the diffusion policy at 10K, 20K, 40K, and ... | p. 7 (1 INTRODUCTION) |
| To examine whether WorldGym provides meaningful signals for policy training, hyperparameter tuning, and checkpoint selections, we train two robot policies from scratch. | p. 7 (1 INTRODUCTION) |
| To enable efficient rollouts of policies which predict different-length action chunks, WorldGym aligns its diffusion horizon length with policies' chunk sizes at inference time. | p. 2 (1 INTRODUCTION) |
| By virtue of being trained with Diffusion Forcing, as well as our usage of a causal temporal attention mask, we can flexibly control how ... | p. 4 (1 INTRODUCTION) |
| Moreoever, we show that WorldGym is able to preserve relative policy rankings across different policy versions, sizes, and training checkpoints. | p. 1 (ABSTRACT) |
| Key contributions of this paper include: • We propose to use video world model to evaluate robot policies across different robot morphologies, and perform ... | p. 2 (1 INTRODUCTION) |
| See Appendix A for additional implementation details. | p. 3 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 1 INTRODUCTION - extractive body cue:** Pick Carrot Pick Carrot Pick Carrot Pick Cat Pick Cat Pick Taylor Swift Pick Square Figure 10: OOD: Failure modes.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 10: OOD: Failure modes. Left: We add a laptop to the scene, which displays an image of a carrot. In 15% of trials, OpenVLA ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Policy Evaluations Results on Bridge OOD Language Tasks. "Move the pot to the counter" is perhaps the most challenging because the Bridge dataset ...
- **p. 9 / 1 INTRODUCTION - extractive body cue:** We use an image editing model to add distractor objects to the Bridge evaluation suite, finding that RT-1X drops in performance by 51%, Octo by ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground truth ...
- **p. 24 / Figure/Table caption - extractive body cue:** Table 6: Detailed Bridge OOD Image task results. OpenVLA appears to be more robust across the different OOD settings of object generalization, distractions and classification. ...

- **PDF anchors reviewed:** datasets p. 8 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION), p. 9 (1 INTRODUCTION), metrics p. 17 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION), baselines p. 8 (1 INTRODUCTION), p. 22 (Figure/Table caption), p. 8 (1 INTRODUCTION), p. 24 (Figure/Table caption), p. 25 (Figure/Table caption), p. 25 (Figure/Table caption), results p. 17 (Figure/Table caption), p. 6 (Figure/Table caption), p. 23 (Figure/Table caption), p. 22 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
