# Evaluation - GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/deng25a.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 24 (Figure/Table caption), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption)): Table 14: Impact of number of input views. Comparison of GraspVLA with different numbers of input views. The results demonstrate that while multiple views significantly improve performance, our single-view implementation ...

## Evaluation Body Digest

- **p. 6 / 5 Experiments - extractive body cue:** We define synthetic categories as those present in our SynGrasp-1B dataset, while web categories refer to those exclusively present in Internet grounding dataset. b) Synthetic ...
- **p. 7 / 5 Experiments - extractive body cue:** LIBERO [13] is a widely used simulation benchmark for robotic manipulation, encompassing diverse tasks and object categories.
- **p. 6 / 5 Experiments - extractive body cue:** For generalists, we use π0 [7], OpenVLA [6], and Octo [26], three transformer-based policies pre-trained on large-scale real-world datasets.
- **p. 7 / 5 Experiments - extractive body cue:** that cross-embodiment pre-training may not be optimal for this specific grasping task on the given robotic arm.
- **p. 6 / 5 Experiments - extractive body cue:** For each object group, we also report the average Success weighted by Path Length (SPL) [76], a widely used metric that weights success rate with ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5: We give a detailed abla- tion study of our models. With all the design choices enabled the per- formance boosts significantly. As shown ...
- **p. 19 / Figure/Table caption - extractive body cue:** Table 8: Success rate of GraspVLA on new robotic arms and camera configurations. E Details of Main Experiments Metrics. In each trial, the model is ...
- **p. 6 / 5 Experiments - extractive body cue:** Our approach achieves the highest grasping success rate on items from both synthetic and web categories using short trajectories.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 14: Impact of number of input views. Comparison of GraspVLA with different numbers of input views. The results demonstrate that while multiple views ... | p. 24 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As illustrated in Table 1, GraspVLA achieves around 90% on all test sets and significantly outperforms all baselines, demonstrating strong zero-shot generalizability. | p. 6 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our approach achieves the highest grasping success rate on items from both synthetic and web categories using short trajectories. | p. 6 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We also observe that the format of task captions significantly affects the performance of fine-tuned models and provide detailed results in the supplementary. | p. 7 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5: We give a detailed abla- tion study of our models. With all the design choices enabled the per- formance boosts significantly. As ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5 Experiments - extractive body cue:** We define synthetic categories as those present in our SynGrasp-1B dataset, while web categories refer to those exclusively present in Internet grounding dataset. b) Synthetic ...
- **p. 7 / 5 Experiments - extractive body cue:** LIBERO [13] is a widely used simulation benchmark for robotic manipulation, encompassing diverse tasks and object categories.
- **p. 6 / 5 Experiments - extractive body cue:** For generalists, we use π0 [7], OpenVLA [6], and Octo [26], three transformer-based policies pre-trained on large-scale real-world datasets.
- **p. 7 / 5 Experiments - extractive body cue:** that cross-embodiment pre-training may not be optimal for this specific grasping task on the given robotic arm.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: GraspVLA is a grasping foundation model pre-trained exclusively on billion-scale syn- thetic action data and co-trained with Internet semantics data. It exhibits direct ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Data generation pipeline: We first curated over 10,680 object meshes from Objaverse [63] that are suitable for tabletop grasping and randomly selected and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. The VLM takes observation images and a text instruction for vision-language joint per- ception. It comprises a trainable large language model (InternLM2 1.8B ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: GraspVLA consists of an autoregressive vision-language backbone and a flow-matching based action expert. It exploits the synergy between Internet grounding data and synthetic ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Zero-shot comparisons in real-world. We compare our method against state-of-the-art imitation learning specialists and large VLA models. All models are fine-tuned on SynGrasp-1B ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: We show our real-world setup in (a), objects used in experiments in (b,c), and 5 test sets corresponding to ba- sic, light, background, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Comparisons with baselines in LIBERO. The zero-shot performance of GraspVLA surpasses the fine-tuned perfor- mance of strong baselines π0 and OpenVLA. Setup. LIBERO ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Comparison with AnyGrasp. GraspVLA performs consistently well in both language-guided and arbitrary grasping tasks. In contrast, AnyGrasp is faster and excels at grasping ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We define synthetic categories as those present in our SynGrasp-1B dataset, while web categories refer to those exclusively present in Internet grounding dataset. b) ... | embodiment, simulator version and control stack | p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Task/environment | LIBERO [13] is a widely used simulation benchmark for robotic manipulation, encompassing diverse tasks and object categories. | reset, timeout, object/scene variation | p. 7 (5 Experiments), p. 6 (5 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (Body text (section boundary not confidently recovered)), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For each object group, we also report the average Success weighted by Path Length (SPL) [76], a widely used metric that weights success rate ... | definition/direction/unit from same section | p. 6 (5 Experiments) |
| Table 5: We give a detailed abla- tion study of our models. With all the design choices enabled the per- formance boosts significantly. As ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 8: Success rate of GraspVLA on new robotic arms and camera configurations. E Details of Main Experiments Metrics. In each trial, the model ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Our approach achieves the highest grasping success rate on items from both synthetic and web categories using short trajectories. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| Figure 9: GraspVLA supports fast adaptation to new robotic arms and camera configurations. Wrist camera UR5e arm with Robotiq gripper Success Rate 76.6 82.1 | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| As shown in Table 2, GraspVLA demonstrates satisfactory performance when zeroshot evaluated on LIBERO. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Table 13: Impact of instruction format. Fine-tuned baselines exhibit performance drops when the original instructions are simplified. H Details about Comparison with AnyGrasp Setup. ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| (3) How much do our design choices contribute to GraspVLA's performance? | definition/direction/unit from same section | p. 5 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Additionally, the SPL metric reveals that GraspVLA grasps objects with shorter path lengths compared to π0 baselines which often exhibit hesitation. | comparison identity and matched condition | p. 6 (5 Experiments) |
| As illustrated in Table 1, GraspVLA achieves around 90% on all test sets and significantly outperforms all baselines, demonstrating strong zero-shot generalizability. | comparison identity and matched condition | p. 6 (5 Experiments) |
| Table 14: Impact of number of input views. Comparison of GraspVLA with different numbers of input views. The results demonstrate that while multiple views ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |
| The zero-shot performance of GraspVLA surpasses the fine-tuned performance of strong baselines π0 and OpenVLA. | comparison identity and matched condition | p. 7 (5 Experiments) |
| 5.2 Zero-Shot Comparison with VLAs in LIBERO Benchmark Long Goal Object OpenVLA (fine-tuned) 33.7 56.6 65.4 π0 (fine-tuned) 62.7 79.4 93.8 Ours (zero-shot) 82.0 ... | comparison identity and matched condition | p. 7 (5 Experiments) |
| Table 4: Efficient post-training. GraspVLA shows superior adaptability to novel tasks, surpassing the model without pre- training and all baselines. As shown in Table ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Additionally, to assess the effectiveness of pre-training on SynGrasp-1B, we report results of direct fine-tuning π0 from its VLM weights [77], without its cross-embodiment ... | component/input/data sensitivity | p. 6 (5 Experiments) |
| Interestingly, the π0 baseline without cross-embodiment pre-training performs better than its pre-trained counterpart, suggesting 6 | component/input/data sensitivity | p. 6 (5 Experiments) |
| Figure 10: Scaling laws different training regimes. (a) Performance scaling with number of train- ing frames in both simulation and real-world environments. (b) Impact ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| Table 4: Efficient post-training. GraspVLA shows superior adaptability to novel tasks, surpassing the model without pre- training and all baselines. As shown in Table ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 13: Impact of instruction format. Fine-tuned baselines exhibit performance drops when the original instructions are simplified. H Details about Comparison with AnyGrasp Setup. ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |
| It surpasses π0 and OpenVLA fine-tuned on the LIBERO dataset, demonstrating strong generalizability. | component/input/data sensitivity | p. 7 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the ... | Table 14: Impact of number of input views. Comparison of GraspVLA with different numbers of input views. The results demonstrate that while multiple views ... | PDF body cue; verify exact table/figure and matched conditions | p. 24 (Figure/Table caption), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | As illustrated in Table 1, GraspVLA achieves around 90% on all test sets and significantly outperforms all baselines, demonstrating strong zero-shot generalizability. | numeric claim only at cited anchor | p. 6 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 5 Experiments - extractive body cue:** Each test set contains 15 objects from distinct categories randomly sampled from each group, with 2 trials per object.
- **p. 6 / 5 Experiments - extractive body cue:** In other words, we test each method for 15 × 2 × 5 × 2 = 300 trials in total.
- **p. 7 / 5 Experiments - extractive body cue:** To concentrate on grasping capabilities, we omit non-prehensile tasks (e.g., ‘turn on the stove') and reformulate task captions as ‘pick up {object}', selecting 7-10 tasks ...
- **p. 7 / 5 Experiments - extractive body cue:** In line with standard evaluation protocols, each task is rigorously tested with 50 randomized initial configurations, resulting in 350-500 trials per suite.
- **p. 7 / 5 Hz - extractive body cue:** To isolate grasping performance, we design two additional test sets (30 trials each): one with common household objects and another with transparent objects, where the ...
- **p. 8 / 5 Hz - extractive body cue:** We conduct 10 trials per task and report the overall success rate (task completion) and the grasping success rate (grasping any object).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 7 Limitations and Future Work Currently, our data generation and evaluation are conducted exclusively on the Franka Panda arm with front and side views. | p. 9 (6 Conclusion) |
| body limitation/failure cue | Like most grasping policies, we synthesize grasp labels using force-closure, which do not account for deformability-a limitation common to all such methods. | p. 9 (6 Conclusion) |
| body limitation/failure cue | We provide failure analysis in the supplementary. | p. 7 (5 Experiments) |
| body limitation/failure cue | We evaluate on three LIBERO suites (Long, Goal, Object), excluding Spatial, as its focus on spatial reasoning falls outside our scope. | p. 7 (5 Experiments) |
| body limitation/failure cue | Figure 11: Examples of LIBERO Benchmark. We visualize both front and side views side by side. is considered a success. Similarly, if the target ... | p. 22 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| It is computed as: 1 N PN i=1 Si li max(pi,li), where Si is a binary indicator of success (1 if successful), li is ... | p. 6 (5 Experiments) |
| In other words, we test each method for 15 × 2 × 5 × 2 = 300 trials in total. | p. 6 (5 Experiments) |
| In line with standard evaluation protocols, each task is rigorously tested with 50 randomized initial configurations, resulting in 350-500 trials per suite. | p. 7 (5 Experiments) |
| The fields of Natural Language Processing (NLP) and Computer Vision (CV) have undergone a paradigm shift with the advent of foundation models. | p. 2 (1 Introduction) |
| PAG treats perception tasks, i.e., visual grounding and grasping pose prediction, as intermediate steps in action generation, forming a CoT process that causally infers ... | p. 2 (1 Introduction) |
| To isolate grasping performance, we design two additional test sets (30 trials each): one with common household objects and another with transparent objects, where ... | p. 7 (5 Hz) |
| Introducing 2D bounding boxes as intermediate action steps (PAG-2D) yields significant improvements for web categories. | p. 8 (5 Hz) |
| We conduct 10 trials per task and report the overall success rate (task completion) and the grasping success rate (grasping any object). | p. 8 (5 Hz) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6 Conclusion - extractive body cue:** 7 Limitations and Future Work Currently, our data generation and evaluation are conducted exclusively on the Franka Panda arm with front and side views.
- **p. 9 / 6 Conclusion - extractive body cue:** Like most grasping policies, we synthesize grasp labels using force-closure, which do not account for deformability-a limitation common to all such methods.
- **p. 7 / 5 Experiments - extractive body cue:** We provide failure analysis in the supplementary.
- **p. 7 / 5 Experiments - extractive body cue:** We evaluate on three LIBERO suites (Long, Goal, Object), excluding Spatial, as its focus on spatial reasoning falls outside our scope.
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 11: Examples of LIBERO Benchmark. We visualize both front and side views side by side. is considered a success. Similarly, if the target is ...

- **Evidence anchors reviewed:** datasets p. 6 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), metrics p. 6 (5 Experiments), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption), p. 6 (5 Experiments), p. 19 (Figure/Table caption), p. 7 (5 Experiments), baselines p. 6 (5 Experiments), p. 6 (5 Experiments), p. 24 (Figure/Table caption), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (Figure/Table caption), results p. 24 (Figure/Table caption), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 14: Impact of number of input views. Comparison of GraspVLA with different numbers of input views. The results demonstrate that while multiple views significantly improve performance, our single-view implementation ... (p. 24, Figure/Table caption).
- **Metric evidence:** (3) How much do our design choices contribute to GraspVLA's performance? (p. 5, 5 Experiments).
- **Baseline/ablation evidence:** Interestingly, the π0 baseline without cross-embodiment pre-training performs better than its pre-trained counterpart, suggesting 6 (p. 6, 5 Experiments).
- **Failure/negative evidence:** Finally, the remaining failures (7%) include minor errors such as early gripper closure or collisions with the environment, which reinforcement learning could potentially address. (p. 26, C Details about Data Generation).
