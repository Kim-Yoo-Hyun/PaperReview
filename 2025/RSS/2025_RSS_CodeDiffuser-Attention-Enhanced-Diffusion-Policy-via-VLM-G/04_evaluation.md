# Evaluation - CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p072.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p072.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 10 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (B. Analysis of Existing Imitation Learning Algorithm)): While the performance of ACT and DP initially improves, they generally show diminishing returns while success rate is still low, and in some cases plateaus as the number of demonstrations ...

## Evaluation Body Digest

- **p. 2 / 3) We conduct extensive evaluations of individual modules - extractive body cue:** and the full system in both simulation and real-world tasks, including contact-rich 6-DoF manipulation with multi-object interactions, demonstrating the effectiveness of our approach, in handling ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For real-world robot experiments, we tse the ALOHA system for data collection and evaluation [6], along with four RealSense cameras positioned around the workspace to ...
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** In addition, we build a benchmark in the simulation to quantitatively evaluate the language-to-3D attention pipeline, which ‘can automatically generate scenes, prompts, and corresponding ground ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In addition to collecting real-world demonstrations, we design a lightweight labeling process to generate language instructions and 3D attention ‘maps for training the low-level policy.
- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** In addition, we evaluate the entire system on the Hang Mug, Pack Battery, and Stow Book tasks in the real world, We collect 150 demonstrations ...
- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** We note that while using 2D attention achieves similar performance to using 3D attention maps, we adopt 3D attention maps for real-world tasks due to ...
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** These results confirm that the 3D attention map is a robust representation for downstream isuomotor policy learning in ambiguous task scenarios. ‘Additionally, we stress-test our ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** For the Hang Mug task, we train and test on the scene with 2 mugs for picking and 3 branches for placing.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 3) We conduct extensive evaluations of individual modules (p. 2); IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| B. Analysis of Existing Imitation Learning Algorithm | EMPIRICAL / REAL-ROBOT OR HARDWARE | While the performance of ACT and DP initially improves, they generally show diminishing returns while success rate is still low, and in some cases ... | p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| B. Analysis of Existing Imitation Learning Algorithm | EMPIRICAL / REAL-ROBOT OR HARDWARE | In ‘contrast to Lang-DP (RGB), our method, which incorporates 2 similar pipeline from language instructions to 2D attention, achieves a performance improvement from 12% ... | p. 9 (B. Analysis of Existing Imitation Learning Algorithm) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 8: Evaluation of Entire System. (a) We qualitatively evaluate the entire pipeline from language instructions to low-level actions, ‘demonstrating how our system interprets ... | p. 10 (Figure/Table caption) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | For simple tasks with no ambiguity (Lop-left entry), the high success rate confirms the validity of the baseline methods. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | For method evaluation, we report the task success rate, where the success criteria are determined by the information provided to the method. | p. 6 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 2 / 3) We conduct extensive evaluations of individual modules - extractive body cue:** and the full system in both simulation and real-world tasks, including contact-rich 6-DoF manipulation with multi-object interactions, demonstrating the effectiveness of our approach, in handling ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For real-world robot experiments, we tse the ALOHA system for data collection and evaluation [6], along with four RealSense cameras positioned around the workspace to ...
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** In addition, we build a benchmark in the simulation to quantitatively evaluate the language-to-3D attention pipeline, which ‘can automatically generate scenes, prompts, and corresponding ground ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In addition to collecting real-world demonstrations, we design a lightweight labeling process to generate language instructions and 3D attention ‘maps for training the low-level policy.
- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** In addition, we evaluate the entire system on the Hang Mug, Pack Battery, and Stow Book tasks in the real world, We collect 150 demonstrations ...
- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** We note that while using 2D attention achieves similar performance to using 3D attention maps, we adopt 3D attention maps for real-world tasks due to ...
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** These results confirm that the 3D attention map is a robust representation for downstream isuomotor policy learning in ambiguous task scenarios. ‘Additionally, we stress-test our ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** For the Hang Mug task, we train and test on the scene with 2 mugs for picking and 3 branches for placing.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Codeitfuser leverages the code generated by Vision-Language Models (VLMSs) as an interpretable and executable representation to understand abstract and ambiguous language instructions. This ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Language Ambiguity for Task Speci
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Method Overview. CodeDitfuser consists of three primary components: code generation, 3D attention map computation, and low level policy. (a) CodeDitfuser first leverages the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Image Input to se1_name. After segmenting 3D instances and projecting them into 2D images, we concatenate the masked images ‘and overlay instance labels. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Analysis of Existing Imitation Learning Algorithms. (a) We first evaluate three SOTA imitation learning algorthms-ACT, DP (RGB), and DP (PCD)-on the Pack Battery ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: 3D Attention Maps Visualization, We visualize the 3D attention maps for corresponding instructions and scenarios. First, our 3D attention maps successfully highlight the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Analysis of Attention-Conditioned Policy. (a) We first ‘examine the performance of the aitention-conditioned policy under
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: Evaluation of Entire System. (a) We qualitatively evaluate the entire pipeline from language instructions to low-level actions, ‘demonstrating how our system interprets semantic ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | and the full system in both simulation and real-world tasks, including contact-rich 6-DoF manipulation with multi-object interactions, demonstrating the effectiveness of our approach, in ... | embodiment, simulator version and control stack | p. 2 (3) We conduct extensive evaluations of individual modules), p. 5 (IV. EXPERIMENTS) |
| Task/environment | For real-world robot experiments, we tse the ALOHA system for data collection and evaluation [6], along with four RealSense cameras positioned around the workspace ... | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (A. Problem Statement), p. 4 (A. Problem Statement) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (A. Problem Statement), p. 6 (B. Analysis of Existing Imitation Learning Algorithm) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased ... | definition/direction/unit from same section | p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| We find that adding additional demonstrations in these settings often shows diminishing returns at low success rates even with extensive demonstrations, indicating that additional ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| While the performance of ACT and DP initially improves, they generally show diminishing returns while success rate is still low, and in some cases ... | definition/direction/unit from same section | p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| For simple tasks with no ambiguity (Lop-left entry), the high success rate confirms the validity of the baseline methods. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| The training and testing scenarios coasist of a mixture of 1 10 4 picking optioas with 1 placing option, The success rate curve indicates ... | definition/direction/unit from same section | p. 9 (B. Analysis of Existing Imitation Learning Algorithm) |
| (0) Success Rate Under (c) Success Rate Under Increasing Ambigt Unseen Scenarios | definition/direction/unit from same section | p. 9 (B. Analysis of Existing Imitation Learning Algorithm) |
| (Section IV-B) (2) Does the 3D attention map generated by VLM-generated code align with the language instruction? | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| (Section 1V-C) (3) Is the 3D attention map a suitable representation for the downstream visuomotor policy to handle task ambiguity? | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We find that our policy consistently outperforms the baselines by leveraging VLMgenerated code as an interpretable and executable intermediate representation, effectively utilizing the visual-semantic ... | comparison identity and matched condition | p. 9 (B. Analysis of Existing Imitation Learning Algorithm) |
| Fig. 8: Evaluation of Entire System. (a) We qualitatively evaluate the entire pipeline from language instructions to low-level actions, ‘demonstrating how our system interprets ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| For methods conditioned on language ‘or attention, we consider a rollout successful if the task is completed in the desired manner, such as successfully ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| For simple tasks with no ambiguity (Lop-left entry), the high success rate confirms the validity of the baseline methods. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| + Ours without Residual Connection: In our policy, we incclude a residual connection in PointNet++ for visual feature extraction, This baseline ablates the residual ... | comparison identity and matched condition | p. 8 (B. Analysis of Existing Imitation Learning Algorithm) |
| Compared to Lang-DP (PCD), our method leverages VLM to interpret language instructions and compute | comparison identity and matched condition | p. 8 (B. Analysis of Existing Imitation Learning Algorithm) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For DP, we consider two variants - DP with RGB inputs, denoted as "DP (RGB)", and DP with point cloud inputs, denoted as "DP ... | component/input/data sensitivity | p. 6 (B. Analysis of Existing Imitation Learning Algorithm) |
| For methods conditioned on language ‘or attention, we consider a rollout successful if the task is completed in the desired manner, such as successfully ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| Furthermore, ‘even with ambiguous commands like "Hang a mug on a branch" (without specifying a particular mug or branch), ‘our system autonomously selects and ... | component/input/data sensitivity | p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| + Prompt without slackness: All objects are strictly specified, such as "Hang the left-most mug on the top branch." | component/input/data sensitivity | p. 8 (B. Analysis of Existing Imitation Learning Algorithm) |
| First, our 3D attention maps successfully highlight the correct object instances even under ambiguous instructions, such as "Hang a mug on a branch" for ... | component/input/data sensitivity | p. 8 (B. Analysis of Existing Imitation Learning Algorithm) |
| (4) ‘Our ablation study demonstrates that incorporating the residual ‘connection into PointNet++ improves performance from 61% to 86.5%. | component/input/data sensitivity | p. 9 (B. Analysis of Existing Imitation Learning Algorithm) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In contrast, our framework is capable of understanding potentially ambiguous natural language instructions by using visual-semantic reasoning capabilities of VLM and generated code as ... | While the performance of ACT and DP initially improves, they generally show diminishing returns while success rate is still low, and in some cases ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 10 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| Primary metric/result | In ‘contrast to Lang-DP (RGB), our method, which incorporates 2 similar pipeline from language instructions to 2D attention, achieves a performance improvement from 12% ... | numeric claim only at cited anchor | p. 9 (B. Analysis of Existing Imitation Learning Algorithm) |

- Numeric sentences retained from the body:
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** The number of demonstrations is increased from 30 to 540 episodes.
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** The number of demonstrations is increased from 30 to 540 episodes.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased ... | p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| body limitation/failure cue | In our experiments, we first identify the key limitations of existing imitation learning algorithms. | p. 9 (V. ConcLusion) |
| body limitation/failure cue | (b) Failure Breakdown of Two Special Scenarios | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | We observe that failure primarily occurs at the task stage with the highest ambiguity, demonstrating a strong cconrelation between policy failure and task ambiguity. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Additional analysis and visualizations of 3D attention failure cases are provided in the | p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| body limitation/failure cue | In addition, we analyze the common failure cases of our ‘method, as shown in Figure 9. | p. 9 (B. Analysis of Existing Imitation Learning Algorithm) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Second, while training on a 1x1 scenario dloes not generalize to scenarios with multiple placing options, the generalization of CodeDiffuser quickly improves. after seeing ... | p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| (Section IV-B) (2) Does the 3D attention map generated by VLM-generated code align with the language instruction? | p. 5 (IV. EXPERIMENTS) |
| In contrast, our approach uses VLM-generated code to compute 3D attention map, which highlights task-relevant regions and possesses much lower dimension compared to 3D ... | p. 3 (B. Foundational Vision Model for Roboties) |
| In contrast, our framework is capable of understanding potentially ambiguous natural language instructions by using visual-semantic reasoning capabilities of VLM and generated code as ... | p. 3 (B. Foundational Vision Model for Roboties) |
| The VLM-generated, code can also perform zero-shot interpretation of language exhibiting more complicated logical structures, such as self repairing phrases such as "Hang the ... | p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| Compared to Lang-DP (PCD), our method leverages VLM to interpret language instructions and compute | p. 8 (B. Analysis of Existing Imitation Learning Algorithm) |
| + Lang-DP (RGB): This baseline extends DP (RGB) by conditioning the policy on language using a frozen CLIP encoder. | p. 8 (B. Analysis of Existing Imitation Learning Algorithm) |
| We observe that the majority of failure focuses on task execution, while the code generation and perception are relatively stable. | p. 9 (B. Analysis of Existing Imitation Learning Algorithm) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ...
- **p. 9 / V. ConcLusion - extractive body cue:** In our experiments, we first identify the key limitations of existing imitation learning algorithms.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** (b) Failure Breakdown of Two Special Scenarios
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We observe that failure primarily occurs at the task stage with the highest ambiguity, demonstrating a strong cconrelation between policy failure and task ambiguity.
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Additional analysis and visualizations of 3D attention failure cases are provided in the
- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** In addition, we analyze the common failure cases of our ‘method, as shown in Figure 9.

- **Evidence anchors reviewed:** datasets p. 2 (3) We conduct extensive evaluations of individual modules), p. 5 (IV. EXPERIMENTS), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 5 (IV. EXPERIMENTS), p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 9 (B. Analysis of Existing Imitation Learning Algorithm), metrics p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 6 (IV. EXPERIMENTS), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 6 (IV. EXPERIMENTS), p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 9 (B. Analysis of Existing Imitation Learning Algorithm), baselines p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 10 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 8 (B. Analysis of Existing Imitation Learning Algorithm), p. 8 (B. Analysis of Existing Imitation Learning Algorithm), results p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 10 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (B. Analysis of Existing Imitation Learning Algorithm).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Fig. 8: Evaluation of Entire System. (a) We qualitatively evaluate the entire pipeline from language instructions to low-level actions, ‘demonstrating how our system interprets semantic meanings from abstract instructions. Given ... (p. 10, Figure/Table caption).
- **Metric evidence:** We find that adding additional demonstrations in these settings often shows diminishing returns at low success rates even with extensive demonstrations, indicating that additional training data alone may oot resolve ... (p. 6, IV. EXPERIMENTS).
- **Baseline/ablation evidence:** For methods conditioned on language ‘or attention, we consider a rollout successful if the task is completed in the desired manner, such as successfully following the language instruction or picking ... (p. 6, IV. EXPERIMENTS).
- **Failure/negative evidence:** Similarly, as the number of placement options increases, most failures occur during the placement stage of the task. ‘The observed correlation between (i) increased task ambiguity and (ii) declining task ... (p. 7, B. Analysis of Existing Imitation Learning Algorithm).
