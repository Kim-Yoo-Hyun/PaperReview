# Evaluation - Mastering Diverse Domains through World Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (40 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2301.04104; PDF retrieval source: https://arxiv.org/pdf/2301.04104. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 24 (Figure/Table caption), p. 2 (Abstract), p. 2 (Abstract), p. 9 (Abstract), p. 32 (Figure/Table caption), p. 39 (Figure/Table caption)): Figure 9: Item success rates as a percentage of episodes. Dreamer obtains items at substantially higher rates than the baselines and continues to improve until the 100M step budget. At ...

## Evaluation Body Digest

- **p. 9 / Abstract - extractive body cue:** Dreamer sets a new state-of-the-art on this benchmark, outperforming D4PG, DMPO, and MPO33. • Visual Control This benchmark consists of 20 continuous control tasks where ...
- **p. 9 / Abstract - extractive body cue:** Without this complexity, Dreamer outperforms the best remaining methods, including the transformer-based IRIS and TWM agents, the model-free SPR, and SimPLe45. • Proprio Control This ...
- **p. 1 / Abstract - extractive body cue:** 0 300 600 900 PPO Rainbow MuZero Dreamer 57 tasks, 200M steps Atari 10 30 50 70 PPO Rainbow PPG Dreamer 16 tasks, 50M steps ...
- **p. 2 / Abstract - extractive body cue:** However, applying reinforcement learning algorithms to sufficiently new tasks-such as moving from video games to robotics tasksrequires substantial effort, expertise, and computational resources for tweaking ...
- **p. 2 / Abstract - extractive body cue:** Dreamer succeeds across these domains, ranging from robot locomotion and manipulation tasks over Atari games, procedurally generated ProcGen levels, and DMLab tasks, that require spatial ...
- **p. 6 / Abstract - extractive body cue:** st)  (6) The return distribution can be multi-modal and include outliers, especially for randomized environments where some episodes have higher achievable returns than others.
- **p. 10 / Abstract - extractive body cue:** • BSuite This benchmark includes 23 environments with a total of 468 configurations that are specifically designed to test credit assignment, robustness to reward scale ...
- **p. 4 / Abstract - extractive body cue:** True Context Input Open Loop Prediction Model True T = 0 Model 5 10 15 20 25 30 35 40 45 50 Figure 4: Multi-step ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 9: Item success rates as a percentage of episodes. Dreamer obtains items at substantially higher rates than the baselines and continues to improve ... | p. 24 (Figure/Table caption) |
| Abstract | SYSTEM / EVALUATION SCOPE UNRESOLVED | Notably, larger model sizes not only achieve higher scores but also require less interaction to solve a task. | p. 2 (Abstract) |
| Abstract | SYSTEM / EVALUATION SCOPE UNRESOLVED | Although intuitively appealing, robustly learning and leveraging world models to achieve strong task performance has been an open problem17. | p. 2 (Abstract) |
| Abstract | SYSTEM / EVALUATION SCOPE UNRESOLVED | Together with model size, this allows practitioners to improve task performance and data-efficiency by employing more computational resources. • Atari100k This data-efficiency benchmark comntains ... | p. 9 (Abstract) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 10: Evaluation protocols for the Atari 100k benchmark. Computational resources are converted to A100 GPU days. EfficientMuZero44 achieves the highest scores but changed ... | p. 32 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 9 / Abstract - extractive body cue:** Dreamer sets a new state-of-the-art on this benchmark, outperforming D4PG, DMPO, and MPO33. • Visual Control This benchmark consists of 20 continuous control tasks where ...
- **p. 9 / Abstract - extractive body cue:** Without this complexity, Dreamer outperforms the best remaining methods, including the transformer-based IRIS and TWM agents, the model-free SPR, and SimPLe45. • Proprio Control This ...
- **p. 1 / Abstract - extractive body cue:** 0 300 600 900 PPO Rainbow MuZero Dreamer 57 tasks, 200M steps Atari 10 30 50 70 PPO Rainbow PPG Dreamer 16 tasks, 50M steps ...
- **p. 2 / Abstract - extractive body cue:** However, applying reinforcement learning algorithms to sufficiently new tasks-such as moving from video games to robotics tasksrequires substantial effort, expertise, and computational resources for tweaking ...
- **p. 2 / Abstract - extractive body cue:** Dreamer succeeds across these domains, ranging from robot locomotion and manipulation tasks over Atari games, procedurally generated ProcGen levels, and DMLab tasks, that require spatial ...
- **p. 6 / Abstract - extractive body cue:** st)  (6) The return distribution can be multi-modal and include outliers, especially for randomized environments where some episodes have higher achievable returns than others.
- **p. 10 / Abstract - extractive body cue:** • BSuite This benchmark includes 23 environments with a total of 468 configurations that are specifically designed to test credit assignment, robustness to reward scale ...
- **p. 4 / Abstract - extractive body cue:** True Context Input Open Loop Prediction Model True T = 0 Model 5 10 15 20 25 30 35 40 45 50 Figure 4: Multi-step ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Benchmark summary. a, Using fixed hyperparameters across all domains, Dreamer outperforms tuned expert algorithms across a wide range of benchmarks and data budgets. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Diverse visual domains used in the experiments. Dreamer succeeds across these domains, ranging from robot locomotion and manipulation tasks over Atari games, procedurally ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Training process of Dreamer. The world model encodes sensory inputs into discrete representations zt that are predicted by a sequence model with recurrent ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: Multi-step video predictions of a DMLab maze (top) and a quadrupedal robot (bottom). Given 5 context images and the full action sequence, the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Fraction of trained agents that discover each of the three latest items in the Minecraft Diamond task. Although previous algorithms progress up to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: Ablations and robust scaling of Dreamer. a, All individual robustness techniques contribute to the performance of Dreamer on average, although each individual technique ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 1: PPO hyperparameters used across all benchmarks. For Minecraft, we additionally tune and run the IMPALA and Rainbow algorithms because not successful end-to-end learning ...
- **p. 19 / Figure/Table caption - extractive body cue:** Table 2: Benchmark overview. All agents were trained on a single Nvidia A100 GPU each. Environment instances In earlier experiments, we observed that the performance ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Dreamer sets a new state-of-the-art on this benchmark, outperforming D4PG, DMPO, and MPO33. • Visual Control This benchmark consists of 20 continuous control tasks ... | embodiment, simulator version and control stack | p. 9 (Abstract), p. 9 (Abstract) |
| Task/environment | Without this complexity, Dreamer outperforms the best remaining methods, including the transformer-based IRIS and TWM agents, the model-free SPR, and SimPLe45. • Proprio Control ... | reset, timeout, object/scene variation | p. 9 (Abstract), p. 1 (Abstract) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (Abstract), p. 5 (Abstract) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (Abstract), p. 3 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 16: BSuite scores visualized by category48. Dreamer exceeds previous methods in the categories scale and memory. The scale category measure robustness to reward ... | definition/direction/unit from same section | p. 37 (Figure/Table caption) |
| Figure 6: Ablations and robust scaling of Dreamer. a, All individual robustness techniques contribute to the performance of Dreamer on average, although each individual ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| 0 50 100 Env steps (%) 0 50 100 Return (%) 14 task mean Dreamer No obs symlog No retnorm (advnorm) No symexp twohot ... | definition/direction/unit from same section | p. 9 (Abstract) |
| We observe that all robustness techniques contribute to performance, most notably the KL objective of the world model, followed by return normalization and symexp ... | definition/direction/unit from same section | p. 10 (Abstract) |
| Figure 9: Item success rates as a percentage of episodes. Dreamer obtains items at substantially higher rates than the baselines and continues to improve ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Normalizing rewards or returns by standard deviation can fail under sparse rewards where their standard deviation is near zero, drastically amplifying rewards regardless of ... | definition/direction/unit from same section | p. 6 (Abstract) |
| To estimate returns that consider rewards beyond the prediction horizon, we compute bootstrapped λ-returns29 that integrate the predicted rewards and the values. | definition/direction/unit from same section | p. 5 (Abstract) |
| To consider rewards beyond the prediction horizon T = 16, the critic learns to approximate the distribution of returns28 for each state under the ... | definition/direction/unit from same section | p. 5 (Abstract) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Dreamer establishes a new state-of-the-art on this benchmark, outperforming DrQ-v2 and CURL47, which are specialized to visual environments and leverage data augmentation. | comparison identity and matched condition | p. 9 (Abstract) |
| Dreamer sets a new state-of-the-art on this benchmark, outperforming D4PG, DMPO, and MPO33. • Visual Control This benchmark consists of 20 continuous control tasks ... | comparison identity and matched condition | p. 9 (Abstract) |
| Dreamer establishes a new state-of-the-art on this benchmark, outperforming Boot DQN and other methods49. | comparison identity and matched condition | p. 10 (Abstract) |
| Figure 9: Item success rates as a percentage of episodes. Dreamer obtains items at substantially higher rates than the baselines and continues to improve ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |
| While several strong baselines progress to advanced items such as the iron pickaxe, none of them discovers a diamond. | comparison identity and matched condition | p. 10 (Abstract) |
| We note that these baselines were not designed for data-efficiency but serve as a valuable comparison point for the performance previously achievable at scale. | comparison identity and matched condition | p. 8 (Abstract) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 0 50 100 Env steps (%) 0 50 100 Return (%) 14 task mean Dreamer No obs symlog No retnorm (advnorm) No symexp twohot ... | component/input/data sensitivity | p. 9 (Abstract) |
| This finding could allow for future algorithm variants that leverage pretraining on unsupervised data. | component/input/data sensitivity | p. 10 (Abstract) |
| To investigate the effect of the world model, we ablate the learning signals of Dreamer by stopping either the task-specific reward and value prediction ... | component/input/data sensitivity | p. 10 (Abstract) |
| Applied out of the box, Dreamer is the first algorithm to collect diamonds in Minecraft from scratch without human data or curricula. | component/input/data sensitivity | p. 1 (Abstract) |
| Our work allows solving challenging control problems without extensive experimentation, making reinforcement learning broadly applicable. | component/input/data sensitivity | p. 1 (Abstract) |
| Creating a general algorithm that learns to master new domains without having to be reconfigured has been a central challenge in artificial intelligence and ... | component/input/data sensitivity | p. 2 (Abstract) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present DreamerV3, a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration. | Figure 9: Item success rates as a percentage of episodes. Dreamer obtains items at substantially higher rates than the baselines and continues to improve ... | PDF body cue; verify exact table/figure and matched conditions | p. 24 (Figure/Table caption), p. 2 (Abstract), p. 2 (Abstract), p. 9 (Abstract), p. 32 (Figure/Table caption), p. 39 (Figure/Table caption) |
| Primary metric/result | Notably, larger model sizes not only achieve higher scores but also require less interaction to solve a task. | numeric claim only at cited anchor | p. 2 (Abstract) |

- Numeric sentences retained from the body:
- **p. 1 / Abstract - extractive body cue:** 0 300 600 900 PPO Rainbow MuZero Dreamer 57 tasks, 200M steps Atari 10 30 50 70 PPO Rainbow PPG Dreamer 16 tasks, 50M steps ...
- **p. 2 / Abstract - extractive body cue:** We observe robust learning not only across over 150 tasks from the domains summarized in Figure 2, but also across model sizes and training budgets, ...
- **p. 3 / Abstract - extractive body cue:** x1 x2 x3 x̂1 x̂2 x̂3 a1 a2 z1 z2 z3 h3 h2 h1 enc enc enc dec dec dec (a) World Model Learning h3 ...
- **p. 4 / Abstract - extractive body cue:** Given 5 context images and the full action sequence, the model predicts 45 frames into the future without access to intermediate images.
- **p. 8 / Abstract - extractive body cue:** Results We evaluate the generality of Dreamer across 8 domains-with over 150 tasks-under fixed hyperparameters.
- **p. 8 / Abstract - extractive body cue:** Our PPO agent with fixed hyperparameters matches the published score of the highly tuned official PPO implementation37. • DMLab This suite of 30 tasks features ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Importantly, the network can output any continuous value in the interval because the weighted average can fall between the buckets: ˆy .= softmax(f(x))TB B ... | p. 7 (Abstract) |
| body limitation/failure cue | In practice, substracting an offset from the returns does not change the actor gradient and thus dividing by the range S is sufficient. | p. 6 (Abstract) |
| body limitation/failure cue | The symlog function approximates the identity around the origin so that it does not affect learning of targets that are already small enough. | p. 7 (Abstract) |
| body limitation/failure cue | In comparison, Dreamer masters a diverse range of environments with fixed hyperparameters, does not require expert data, and its implementation is open source. | p. 11 (Abstract) |
| body limitation/failure cue | Robustness techniques based on normalization, balancing, and transformations enable stable learning across domains. | p. 1 (Abstract) |
| body limitation/failure cue | Dreamer overcomes this challenge through a range of robustness techniques based on normalization, balancing, and transformations. | p. 2 (Abstract) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 0 300 600 900 PPO Rainbow MuZero Dreamer 57 tasks, 200M steps Atari 10 30 50 70 PPO Rainbow PPG Dreamer 16 tasks, 50M ... | p. 1 (Abstract) |
| We run PPO with fixed hyperparameters chosen to maximize performance across domains and that reproduce strong published results of PPO on ProcGen37. | p. 8 (Abstract) |
| Our PPO agent with fixed hyperparameters matches the published score of the highly tuned official PPO implementation37. • DMLab This suite of 30 tasks ... | p. 8 (Abstract) |
| In comparison, Dreamer masters a diverse range of environments with fixed hyperparameters, does not require expert data, and its implementation is open source. | p. 11 (Abstract) |
| Because of the training time in this complex domain, extensive tuning would be difficult for Minecraft. | p. 10 (Abstract) |
| Dreamer also substantially outperforms a high-quality implementation of the widely applicable PPO algorithm. b, Applied out of the box, Dreamer learns to obtain diamonds ... | p. 1 (Abstract) |
| Introduction Reinforcement learning has enabled computers to solve tasks through interaction, such as surpassing humans in the games of Go and Dota1,2. | p. 2 (Abstract) |
| We present Dreamer, a general algorithm that outperforms specialized expert algorithms across a wide range of domains while using fixed hyperparameters, making reinforcement learning ... | p. 2 (Abstract) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Abstract - extractive body cue:** Importantly, the network can output any continuous value in the interval because the weighted average can fall between the buckets: ˆy .= softmax(f(x))TB B .= ...
- **p. 6 / Abstract - extractive body cue:** In practice, substracting an offset from the returns does not change the actor gradient and thus dividing by the range S is sufficient.
- **p. 7 / Abstract - extractive body cue:** The symlog function approximates the identity around the origin so that it does not affect learning of targets that are already small enough.
- **p. 11 / Abstract - extractive body cue:** In comparison, Dreamer masters a diverse range of environments with fixed hyperparameters, does not require expert data, and its implementation is open source.
- **p. 1 / Abstract - extractive body cue:** Robustness techniques based on normalization, balancing, and transformations enable stable learning across domains.
- **p. 2 / Abstract - extractive body cue:** Dreamer overcomes this challenge through a range of robustness techniques based on normalization, balancing, and transformations.

- **PDF anchors reviewed:** datasets p. 9 (Abstract), p. 9 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 6 (Abstract), metrics p. 37 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (Abstract), p. 10 (Abstract), p. 24 (Figure/Table caption), p. 6 (Abstract), baselines p. 9 (Abstract), p. 9 (Abstract), p. 10 (Abstract), p. 24 (Figure/Table caption), p. 10 (Abstract), p. 8 (Abstract), results p. 24 (Figure/Table caption), p. 2 (Abstract), p. 2 (Abstract), p. 9 (Abstract), p. 32 (Figure/Table caption), p. 39 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
