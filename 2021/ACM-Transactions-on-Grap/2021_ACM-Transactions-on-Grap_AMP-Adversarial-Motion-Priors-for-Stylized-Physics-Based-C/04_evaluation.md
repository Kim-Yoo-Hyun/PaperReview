# Evaluation - AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1145/3450626.3459670; PDF retrieval source: https://doi.org/10.1145/3450626.3459670. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (8 RESULTS), p. 10 (8 RESULTS), p. 9 (8 RESULTS), p. 11 (8 RESULTS), p. 12 (8 RESULTS), p. 18 (Figure/Table caption)): Training the motion prior with a diverse dataset results in more flexible and optimal policies that are able to achieve a wider range of target speeds.

## Evaluation Body Digest

- **p. 8 / 8 RESULTS - extractive body cue:** Each environment is denoted by "Character: Task (Dataset)".
- **p. 9 / 8 RESULTS - extractive body cue:** To determine whether the transitions between distinct gaits are a product of the motion prior or a result of the task objective, we train policies ...
- **p. 9 / 8 RESULTS - extractive body cue:** Policies trained using the larger Locomotion dataset is able to more closely follow the various target speeds by imitating different gaits. our policies can in ...
- **p. 12 / 8 RESULTS - extractive body cue:** Performance statistics of imitating individual motion clips without task objectives. "Dataset Size" records the total length of motion data used for each skill.
- **p. 7 / 8 RESULTS - extractive body cue:** First, we demonstrate that our approach can readily scale to large unstructured datasets containing diverse motion clips, which then enables our characters to perform challenging ...
- **p. 8 / 8 RESULTS - extractive body cue:** The character can be trained to perform tasks in a variety of distinct styles by providing the motion prior with different datasets.
- **p. 11 / 8 RESULTS - extractive body cue:** But as shown in the previous sections, this lack of synchronization is precisely what allows AMP to easily leverage large datasets of diverse motion clips ...
- **p. 11 / 8 RESULTS - extractive body cue:** 8.4 Single-Clip Imitation Although our goal is to train characters with large motion datasets, to evaluate the effectiveness of our framework for imitating behaviors from ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 8 RESULTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 8 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Training the motion prior with a diverse dataset results in more flexible and optimal policies that are able to achieve a wider range of ... | p. 9 (8 RESULTS) |
| 8 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves comparable performance across the various tasks, while also producing higher fidelity motions. order to fulfill the high-level task objectives. | p. 10 (8 RESULTS) |
| 8 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | As a result, these policies are not able to achieve the faster target speeds. | p. 9 (8 RESULTS) |
| 8 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Since the tracking-based policies are synchronized with their respective reference motions, they are generally able to learn faster and achieve lower errors than policies ... | p. 11 (8 RESULTS) |
| 8 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The addition of the gradient penalty not only improves stability during training, but also leads to substantially faster learning across a large set of ... | p. 12 (8 RESULTS) |

## Dataset / Benchmark Role

- **p. 8 / 8 RESULTS - extractive body cue:** Each environment is denoted by "Character: Task (Dataset)".
- **p. 9 / 8 RESULTS - extractive body cue:** To determine whether the transitions between distinct gaits are a product of the motion prior or a result of the task objective, we train policies ...
- **p. 9 / 8 RESULTS - extractive body cue:** Policies trained using the larger Locomotion dataset is able to more closely follow the various target speeds by imitating different gaits. our policies can in ...
- **p. 12 / 8 RESULTS - extractive body cue:** Performance statistics of imitating individual motion clips without task objectives. "Dataset Size" records the total length of motion data used for each skill.
- **p. 7 / 8 RESULTS - extractive body cue:** First, we demonstrate that our approach can readily scale to large unstructured datasets containing diverse motion clips, which then enables our characters to perform challenging ...
- **p. 8 / 8 RESULTS - extractive body cue:** The character can be trained to perform tasks in a variety of distinct styles by providing the motion prior with different datasets.
- **p. 11 / 8 RESULTS - extractive body cue:** But as shown in the previous sections, this lack of synchronization is precisely what allows AMP to easily leverage large datasets of diverse motion clips ...
- **p. 11 / 8 RESULTS - extractive body cue:** 8.4 Single-Clip Imitation Although our goal is to train characters with large motion datasets, to evaluate the effectiveness of our framework for imitating behaviors from ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Our framework enables physically simulated character to solve challenging tasks while adopting stylistic behaviors specified by unstructured motion data. Left: A character learns ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. Schematic overview of the system. Given a motion dataset defining a desired motion style for the character, the system trains a motion prior ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 3. The motion prior can be trained with large datasets of diverse motions, enabling simulated characters to perform complex tasks by composing a wider ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1. Performance statistics of combining AMP with additional task objectives. Performance is recorded as the average normalized task return, with 0 being the minimum ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2. Summary statistics of the different datasets used to train the motion priors. We record the total length of motion clips in each dataset, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4. Performance of Target Heading policies trained with different datasets. Left: Learning curves comparing the normalized task returns of policies trained with a large ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 5. Learning curves comparing the task performance of AMP to latent space models (Latent Space) and policies trained from scratch without motion data (No ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6. Snapshots of behaviors learned by the Humanoid on the single-clip imitation tasks. Top-to-bottom: back-flip, side-flip, cartwheel, spin, spin- kick, roll. AMP enables the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Each environment is denoted by "Character: Task (Dataset)". | embodiment, simulator version and control stack | p. 8 (8 RESULTS), p. 9 (8 RESULTS) |
| Task/environment | To determine whether the transitions between distinct gaits are a product of the motion prior or a result of the task objective, we train ... | reset, timeout, object/scene variation | p. 9 (8 RESULTS), p. 9 (8 RESULTS) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 7 (4 BACKGROUND), p. 4 (4 BACKGROUND) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 5 (4 BACKGROUND), p. 4 (4 BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Since AMP does not use a phase variable to synchronize the policy with the reference motion, the motions may progress at different rates, resulting ... | definition/direction/unit from same section | p. 11 (8 RESULTS) |
| Performance is evaluated using the average pose error, where the pose error 𝑒pose 𝑡 at each time step 𝑡is computed between the pose of ... | definition/direction/unit from same section | p. 11 (8 RESULTS) |
| Table 6. Performance of policies trained using different dataset on a spatial compositional task that combines following a target heading and waving the character's ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| The weights for the task-reward and style-reward are set to 𝑤𝐺= 0.5 and 𝑤𝑆= 0.5 for all tasks. | definition/direction/unit from same section | p. 8 (8 RESULTS) |
| AMP enforces a motion style directly through the reward function, and is therefore able to better mitigate some of these artifacts. | definition/direction/unit from same section | p. 10 (8 RESULTS) |
| AMP is able to closely imitate a diverse repertoire of complex motions, without manual reward engineering. | definition/direction/unit from same section | p. 12 (8 RESULTS) |
| The pose error is averaged across 3 models initialized with different random seeds, with 32 episodes recorded per model. | definition/direction/unit from same section | p. 12 (8 RESULTS) |
| Performance is recorded as the average normalized task return, with 0 being the minimum possible return per episode and 1 being the maximum possible ... | definition/direction/unit from same section | p. 9 (8 RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| AMP produces results of comparable quality when compared to prior tracking-based methods, without requiring a manually designed reward function or synchronization between the policy ... | comparison identity and matched condition | p. 12 (8 RESULTS) |
| Both AMP and the latent space models are able to produce substantially more life-like behaviors than the baseline models. | comparison identity and matched condition | p. 10 (8 RESULTS) |
| The characters automatically learn to compose and generalize different skills from the motion data in order to fulfill high-level task objectives, without requiring mechanisms ... | comparison identity and matched condition | p. 7 (8 RESULTS) |
| Right: Comparison of the target speed with the average speed achieved by the different policies. | comparison identity and matched condition | p. 9 (8 RESULTS) |
| These intricate behaviors arise naturally from the motion prior, without requiring a motion planner to explicitly select which motion the character should execute in ... | comparison identity and matched condition | p. 9 (8 RESULTS) |
| A qualitative comparison of the behaviors learned using AMP and the latent space model is available in the supplementary video. | comparison identity and matched condition | p. 10 (8 RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The characters automatically learn to compose and generalize different skills from the motion data in order to fulfill high-level task objectives, without requiring mechanisms ... | component/input/data sensitivity | p. 7 (8 RESULTS) |
| These intricate behaviors arise naturally from the motion prior, without requiring a motion planner to explicitly select which motion the character should execute in ... | component/input/data sensitivity | p. 9 (8 RESULTS) |
| Learning curves comparing the task performance of AMP to latent space models (Latent Space) and policies trained from scratch without motion data (No Data). | component/input/data sensitivity | p. 10 (8 RESULTS) |
| Again, this composition of different skills emerges automatically from the motion prior, without requiring a motion planner or other mechanisms for motion selection. | component/input/data sensitivity | p. 10 (8 RESULTS) |
| In this setting, the character's objective is to imitate a single motion clip at a time, without additional task objectives. | component/input/data sensitivity | p. 11 (8 RESULTS) |
| Nonetheless, our method is able to produce results of comparable quality without the need to manually design or tune reward functions for different motions. | component/input/data sensitivity | p. 11 (8 RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The central contribution of this work is an adversarial learning approach for physics-based character animation that combines goalconditioned reinforcement with an adversarial motion prior, ... | Training the motion prior with a diverse dataset results in more flexible and optimal policies that are able to achieve a wider range of ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (8 RESULTS), p. 10 (8 RESULTS), p. 9 (8 RESULTS), p. 11 (8 RESULTS), p. 12 (8 RESULTS), p. 18 (Figure/Table caption) |
| Primary metric/result | Our method achieves comparable performance across the various tasks, while also producing higher fidelity motions. order to fulfill the high-level task objectives. | numeric claim only at cited anchor | p. 10 (8 RESULTS) |

- Numeric sentences retained from the body:
- **p. 8 / 8 RESULTS - extractive body cue:** The policy is queried at 30Hz, and each action specifies target positions for PD controllers positioned at the character's joints.
- **p. 8 / 8 RESULTS - extractive body cue:** Depending on the task and character, each policy is trained with 100-300 million samples, requiring approximately 30-140 hours on 16 CPU cores.
- **p. 8 / 8 RESULTS - extractive body cue:** 8.2 Tasks In this section, we demonstrate AMP's effectiveness for controlling the style of a character's motions as it performs other high-level tasks.
- **p. 8 / 8 RESULTS - extractive body cue:** AMP can accommodate large unstructured datasets, with the largest dataset containing 56 clips from 8 different human actors, for a total of 434s of motion ...
- **p. 9 / 8 RESULTS - extractive body cue:** The return is averaged across 3 models initialized with different random seeds, with 32 episodes recorded per model.
- **p. 9 / 8 RESULTS - extractive body cue:** Character Task Dataset Task Return Humanoid Target Locomotion 0.90 ± 0.01 Heading Walk 0.46 ± 0.01 Run 0.63 ± 0.01 Stealthy 0.89 ± 0.02 Zombie ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | These additional motion clips then enable our character to recover from a fall and continue to perform a given task (Figure 3(c)). | p. 9 (8 RESULTS) |
| body limitation/failure cue | When the character falls forward, it tucks its body into a roll during the fall in order to more quickly transition into a getup ... | p. 9 (8 RESULTS) |
| body limitation/failure cue | However, for some motions, such as the Front-Flip, AMP is prone to converging to locally optimal behaviors, where instead of performing a flip, the ... | p. 11 (8 RESULTS) |
| body limitation/failure cue | 9 DISCUSSION AND LIMITATIONS In this work, we presented an adversarial learning system for physicsbased character animation that enables characters to imitate diverse behaviors ... | p. 12 (8 RESULTS) |
| body limitation/failure cue | Unlike previous motion tracking methods, our approach does not require a manually designed tracking objective or a phase-based synchronization of the reference motion and ... | p. 11 (8 RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Synthesizing graceful and life-like behaviors for physically simulated characters has been a fundamental challenge in computer animation. | p. 1 (Body text (section boundary not confidently recovered)) |
| Developing control strategies that are able to replicate the properties of naturalistic behaviors is also of interest for robotic systems, as natural motions implicitly ... | p. 1 (1 INTRODUCTION) |
| The 3D rotation of each spherical joint is encoded using two 3D vectors corresponding to the normal and tangent in the coordinate frame. | p. 6 (4 BACKGROUND) |
| The policy is updated using advantages computed using GAE(𝜆) [Schulman et al. | p. 7 (4 BACKGROUND) |
| The value function is updated with target values computed using TD(𝜆) [Sutton and Barto 1998]. | p. 7 (4 BACKGROUND) |
| Detailed hyperparameter settings are available in Appendix B. | p. 8 (8 RESULTS) |
| Code for our system will be released upon publication of this paper. | p. 8 (8 RESULTS) |
| But when the target is further away, the character automatically transitions into a run. | p. 9 (8 RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 8 RESULTS - extractive body cue:** These additional motion clips then enable our character to recover from a fall and continue to perform a given task (Figure 3(c)).
- **p. 9 / 8 RESULTS - extractive body cue:** When the character falls forward, it tucks its body into a roll during the fall in order to more quickly transition into a getup behavior.
- **p. 11 / 8 RESULTS - extractive body cue:** However, for some motions, such as the Front-Flip, AMP is prone to converging to locally optimal behaviors, where instead of performing a flip, the character ...
- **p. 12 / 8 RESULTS - extractive body cue:** 9 DISCUSSION AND LIMITATIONS In this work, we presented an adversarial learning system for physicsbased character animation that enables characters to imitate diverse behaviors from ...
- **p. 11 / 8 RESULTS - extractive body cue:** Unlike previous motion tracking methods, our approach does not require a manually designed tracking objective or a phase-based synchronization of the reference motion and the ...

- **Evidence anchors reviewed:** datasets p. 8 (8 RESULTS), p. 9 (8 RESULTS), p. 9 (8 RESULTS), p. 12 (8 RESULTS), p. 7 (8 RESULTS), p. 8 (8 RESULTS), metrics p. 11 (8 RESULTS), p. 11 (8 RESULTS), p. 18 (Figure/Table caption), p. 8 (8 RESULTS), p. 10 (8 RESULTS), p. 12 (8 RESULTS), baselines p. 12 (8 RESULTS), p. 10 (8 RESULTS), p. 7 (8 RESULTS), p. 9 (8 RESULTS), p. 9 (8 RESULTS), p. 10 (8 RESULTS), results p. 9 (8 RESULTS), p. 10 (8 RESULTS), p. 9 (8 RESULTS), p. 11 (8 RESULTS), p. 12 (8 RESULTS), p. 18 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Training the motion prior with a diverse dataset results in more flexible and optimal policies that are able to achieve a wider range of target speeds. (p. 9, 8 RESULTS).
- **Metric evidence:** Performance is recorded as the average normalized task return, with 0 being the minimum possible return per episode and 1 being the maximum possible return. (p. 9, 8 RESULTS).
- **Baseline/ablation evidence:** AMP produces results of comparable quality when compared to prior tracking-based methods, without requiring a manually designed reward function or synchronization between the policy and reference motion. (p. 12, 8 RESULTS).
- **Failure/negative evidence:** 9 DISCUSSION AND LIMITATIONS In this work, we presented an adversarial learning system for physicsbased character animation that enables characters to imitate diverse behaviors from large unstructured datasets, without the ... (p. 12, 8 RESULTS).
