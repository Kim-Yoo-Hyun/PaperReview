# Evaluation - SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=anSWDvJm8v; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/168185. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 7 (5.2. Performances Across 18 RLBench Tasks), p. 7 (Figure/Table caption), p. 15 (Figure/Table caption), p. 8 (5.5. Real-robot Evaluations), p. 14 (Figure/Table caption)): Table 3. Performance on MemoryBench. We report the success rates for the three spatial memory tasks in MemoryBench. Our method, SAM2Act+, significantly outperforms all baseline meth- ods that lack an ...

## Evaluation Body Digest

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We benchmark SAM2Act in both simulated and real-world environments.
- **p. 6 / 5. Experiments - extractive body cue:** Specifically, we are interested in answering the following questions: § 5.2 How does SAM2Act compare with state-of-the-art 3D manipulation policies? § 5.3 Can SAM2Act generalize ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** We validate SAM2Act in real-world scenarios using a Franka Emika Panda robot with a Robotiq 2F-85 gripper and a exocentric Intel RealSense D455 depth sensor ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** In both benchmarks, each task is defined by a language instruction with 2-60 variations (e.g., handling objects, locations, and colors).
- **p. 8 / 5.5. Real-robot Evaluations - extractive body cue:** We compare RVT2 against SAM2Act for the first three tasks and SAM2Act+ on the last real-world tasks (indicated with *), evaluating performance both in-distribution and ...
- **p. 8 / 5.3. Semantic Generalization across Tasks - extractive body cue:** SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation Table 2.
- **p. 8 / 5.3. Semantic Generalization across Tasks - extractive body cue:** Task-average success rate percentage change for SAM2Act and other baselines across 13 perturbation factors from The Colosseum, relative to evaluations without perturbations.
- **p. 7 / 5.2. Performances Across 18 RLBench Tasks - extractive body cue:** Overall, SAM2Act achieves an average success rate of 86.8%±0.5, surpassing the previous best (RVT-2) by 5.4%.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Experimental Setup (p. 6); 5.5. Real-robot Evaluations (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3. Performance on MemoryBench. We report the success rates for the three spatial memory tasks in MemoryBench. Our method, SAM2Act+, significantly outperforms all ... | p. 8 (Figure/Table caption) |
| 5.2. Performances Across 18 RLBench Tasks | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, SAM2Act achieves an average success rate of 86.8%±0.5, surpassing the previous best (RVT-2) by 5.4%. | p. 7 (5.2. Performances Across 18 RLBench Tasks) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Multi-Task Performance on RLBench. We evaluate 18 RLBench tasks (James et al., 2020), reporting success rates across all tasks among 3D keyframe-based ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 9. SAM2Act Abaltion Performance on RLBench. We report the success rates for 18 RLBench tasks (James et al., 2020), along with the average ... | p. 15 (Figure/Table caption) |
| 5.5. Real-robot Evaluations | EMPIRICAL / REAL-ROBOT OR HARDWARE | Here, SAM2Act achieves 70% success, while RVT2, relying on random guessing, scores 40%. | p. 8 (5.5. Real-robot Evaluations) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We benchmark SAM2Act in both simulated and real-world environments.
- **p. 6 / 5. Experiments - extractive body cue:** Specifically, we are interested in answering the following questions: § 5.2 How does SAM2Act compare with state-of-the-art 3D manipulation policies? § 5.3 Can SAM2Act generalize ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** We validate SAM2Act in real-world scenarios using a Franka Emika Panda robot with a Robotiq 2F-85 gripper and a exocentric Intel RealSense D455 depth sensor ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** In both benchmarks, each task is defined by a language instruction with 2-60 variations (e.g., handling objects, locations, and colors).
- **p. 8 / 5.5. Real-robot Evaluations - extractive body cue:** We compare RVT2 against SAM2Act for the first three tasks and SAM2Act+ on the last real-world tasks (indicated with *), evaluating performance both in-distribution and ...
- **p. 8 / 5.3. Semantic Generalization across Tasks - extractive body cue:** SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation Table 2.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. SAM2Act is a multi-view, language-conditioned behavior cloning policy trained with fewer demonstrations. Given a language instruction, it can execute high-precision tasks, such as ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Simulation and Real Tasks. We demonstrate the effectiveness of SAM2Act+ in solving memory-based tasks by evaluating it against baselines on the three benchmark ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Overview of the SAM2Act (top) and SAM2Act+ (bottom) architectures. The SAM2Act architecture leverages the SAM2 image encoder to generate prompt-conditioned, multi-resolution embeddings, fine-tuned ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. SAM2Act Module and multi-resolution upsampling mechanism. A cascade of three convex upsamplers processes feature maps at increasing resolutions, integrating multi-resolution embeddings from the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. After pretraining SAM2Act in Stage 1, we freeze the SAM2 image encoder and the multi-view transformer in the coarse branch, as these components ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Multi-Task Performance on RLBench. We evaluate 18 RLBench tasks (James et al., 2020), reporting success rates across all tasks among 3D keyframe-based behavior ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. The Colosseum results. Task-average success rate percentage change for SAM2Act and other baselines across 13 perturbation factors from The Colosseum, relative to evaluations ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Performance on MemoryBench. We report the success rates for the three spatial memory tasks in MemoryBench. Our method, SAM2Act+, significantly outperforms all baseline ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We benchmark SAM2Act in both simulated and real-world environments. | embodiment, simulator version and control stack | p. 6 (5.1. Experimental Setup), p. 6 (5. Experiments) |
| Task/environment | Specifically, we are interested in answering the following questions: § 5.2 How does SAM2Act compare with state-of-the-art 3D manipulation policies? § 5.3 Can SAM2Act ... | reset, timeout, object/scene variation | p. 6 (5. Experiments), p. 7 (5.1. Experimental Setup) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (4. Method), p. 4 (4. Method) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (4. Method), p. 6 (4. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Task-average success rate percentage change for SAM2Act and other baselines across 13 perturbation factors from The Colosseum, relative to evaluations without perturbations. | definition/direction/unit from same section | p. 8 (5.3. Semantic Generalization across Tasks) |
| Overall, SAM2Act achieves an average success rate of 86.8%±0.5, surpassing the previous best (RVT-2) by 5.4%. | definition/direction/unit from same section | p. 7 (5.2. Performances Across 18 RLBench Tasks) |
| We evaluate 18 RLBench tasks (James et al., 2020), reporting success rates across all tasks among 3D keyframe-based behavior cloning (BC) policies. | definition/direction/unit from same section | p. 7 (5.1. Experimental Setup) |
| We report the success rates for the three spatial memory tasks in MemoryBench. | definition/direction/unit from same section | p. 8 (5.4. Performance on MemoryBench) |
| Table 9. SAM2Act Abaltion Performance on RLBench. We report the success rates for 18 RLBench tasks (James et al., 2020), along with the average ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Figure 1. SAM2Act is a multi-view, language-conditioned behavior cloning policy trained with fewer demonstrations. Given a language instruction, it can execute high-precision tasks, such ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| The real-world experiments demonstrate the applicability 6 | definition/direction/unit from same section | p. 6 (5.1. Experimental Setup) |
| Figure 4. SAM2Act Module and multi-resolution upsampling mechanism. A cascade of three convex upsamplers processes feature maps at increasing resolutions, integrating multi-resolution embeddings from ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method, SAM2Act, outperforms all baselines, achieving a significant performance margin of 5.8% over RVT-2 (Goyal et al., 2024), the prior state-of-the-art 3D keyframe-based ... | comparison identity and matched condition | p. 7 (5.1. Experimental Setup) |
| Specifically, we are interested in answering the following questions: § 5.2 How does SAM2Act compare with state-of-the-art 3D manipulation policies? § 5.3 Can SAM2Act ... | comparison identity and matched condition | p. 6 (5. Experiments) |
| SAM2Act significantly outperforms the baseline in high-precision tasks (60% vs 0%). | comparison identity and matched condition | p. 8 (5.5. Real-robot Evaluations) |
| SAM2Act exhibits the smallest performance drop compared to the baselines, with an average decrease of 4.3% (standard deviation of 3.59%). | comparison identity and matched condition | p. 8 (5.3. Semantic Generalization across Tasks) |
| Against all existing approaches, SAM2Act remains the state-of-the-art. | comparison identity and matched condition | p. 7 (5.1. Experimental Setup) |
| Figure 2. Simulation and Real Tasks. We demonstrate the effectiveness of SAM2Act+ in solving memory-based tasks by evaluating it against baselines on the three ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 3. After pretraining SAM2Act in Stage 1, we freeze the SAM2 image encoder and the multi-view transformer in the coarse branch, as these ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Ablation studies are performed on SAM2Act in Appendix E. | component/input/data sensitivity | p. 7 (5.2. Performances Across 18 RLBench Tasks) |
| It outperforms SAM2Act (without memory) by a huge margin of 39.3% on MemoryBench, highlighting the significant impact of explicit memory modeling. | component/input/data sensitivity | p. 8 (5.4. Performance on MemoryBench) |
| Task-average success rate percentage change for SAM2Act and other baselines across 13 perturbation factors from The Colosseum, relative to evaluations without perturbations. | component/input/data sensitivity | p. 8 (5.3. Semantic Generalization across Tasks) |
| Figure 3. Overview of the SAM2Act (top) and SAM2Act+ (bottom) architectures. The SAM2Act architecture leverages the SAM2 image encoder to generate prompt-conditioned, multi-resolution embeddings, ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method, SAM2Act, enables precise 3D manipulation with strong generalization across environmental and objectlevel variations. | Table 3. Performance on MemoryBench. We report the success rates for the three spatial memory tasks in MemoryBench. Our method, SAM2Act+, significantly outperforms all ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 7 (5.2. Performances Across 18 RLBench Tasks), p. 7 (Figure/Table caption), p. 15 (Figure/Table caption), p. 8 (5.5. Real-robot Evaluations), p. 14 (Figure/Table caption) |
| Primary metric/result | Overall, SAM2Act achieves an average success rate of 86.8%±0.5, surpassing the previous best (RVT-2) by 5.4%. | numeric claim only at cited anchor | p. 7 (5.2. Performances Across 18 RLBench Tasks) |

- Numeric sentences retained from the body:
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** To evaluate the general performance of SAM2Act and the memory capabilities of SAM2Act+, we conducted simulation experiments on two benchmarks: a subset of 18 tasks ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** RLBench is a standard multi-task manipulation benchmark, from which we selected 18 tasks well-studied in prior work.
- **p. 7 / 5.2. Performances Across 18 RLBench Tasks - extractive body cue:** A closer look at individual tasks reveals that SAM2Act ranks first in 9 out of 18 tasks and remains highly competitive in 7 others, coming ...
- **p. 7 / 5.3. Semantic Generalization across Tasks - extractive body cue:** We therefore trained SAM2Act and the baseline methods on 20 tasks from The Colosseum 7
- **p. 8 / 5.3. Semantic Generalization across Tasks - extractive body cue:** Our approach, SAM2Act, demonstrates the lowest average percentage change across all perturbations, with a minimal drop of -4.3±3.6%, highlighting its robustness in handling various environmental ...
- **p. 8 / 5.4. Performance on MemoryBench - extractive body cue:** Success ↑ (a) Reopen Drawer (b) Put Block Back (c) Rearrange Block RVT-2 54.0 ± 5.3 60.0 ± 0.0 50.0 ± 2.3 52.0 ± 3.3 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In Table 3, we evaluate SAM2Act+ against SoTA 3D BC model, RVT-2 on MemoryBench, training all models in a single-task setting to isolate memory-related ... | p. 8 (5.4. Performance on MemoryBench) |
| body limitation/failure cue | Specifically, we are interested in answering the following questions: § 5.2 How does SAM2Act compare with state-of-the-art 3D manipulation policies? § 5.3 Can SAM2Act ... | p. 6 (5. Experiments) |
| body limitation/failure cue | Figure 2. Simulation and Real Tasks. We demonstrate the effectiveness of SAM2Act+ in solving memory-based tasks by evaluating it against baselines on the three ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 3. After pretraining SAM2Act in Stage 1, we freeze the SAM2 image encoder and the multi-view transformer in the coarse branch, as these ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Each task undergoes 10 in-distribution and 10 out-of-distribution trials, including environmental perturbations, measuring total success. | p. 7 (5.1. Experimental Setup) |
| body limitation/failure cue | However, to truly assess generalization performance, policies must remain robust against both environmental and objectlevel perturbations. | p. 7 (5.3. Semantic Generalization across Tasks) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each task undergoes 10 in-distribution and 10 out-of-distribution trials, including environmental perturbations, measuring total success. | p. 7 (5.1. Experimental Setup) |
| The memory components function similarly to their implementation in SAM2 for object tracking, with one key distinction: the input to the Memory Encoder. | p. 6 (4. Method) |
| SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation Algorithm 1 Forward Pass of SAM2Act+ Module Initialize: Number of steps N, ... | p. 6 (4. Method) |
| These include Memory Bank, Memory Encoder, and Memory Attention, enabling the model to encode historical actions and condition current observations. | p. 4 (4. Method) |
| Additionally, to fully leverage the multi-resolution embeddings produced by the SAM2 image encoder, we introduce a multi-resolution upsampling method. | p. 4 (4. Method) |
| SAM2Act+ extends this architecture by incorporating memory-based components, including the Memory Encoder, Memory Attention, and Memory Bank, into the coarse branch. | p. 5 (4. Method) |
| The SAM2Act architecture leverages the SAM2 image encoder to generate prompt-conditioned, multi-resolution embeddings, fine-tuned with LoRA for efficient adaptation to manipulation tasks. | p. 5 (4. Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5.4. Performance on MemoryBench - extractive body cue:** In Table 3, we evaluate SAM2Act+ against SoTA 3D BC model, RVT-2 on MemoryBench, training all models in a single-task setting to isolate memory-related challenges ...
- **p. 6 / 5. Experiments - extractive body cue:** Specifically, we are interested in answering the following questions: § 5.2 How does SAM2Act compare with state-of-the-art 3D manipulation policies? § 5.3 Can SAM2Act generalize ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Simulation and Real Tasks. We demonstrate the effectiveness of SAM2Act+ in solving memory-based tasks by evaluating it against baselines on the three benchmark ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. After pretraining SAM2Act in Stage 1, we freeze the SAM2 image encoder and the multi-view transformer in the coarse branch, as these components ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** Each task undergoes 10 in-distribution and 10 out-of-distribution trials, including environmental perturbations, measuring total success.
- **p. 7 / 5.3. Semantic Generalization across Tasks - extractive body cue:** However, to truly assess generalization performance, policies must remain robust against both environmental and objectlevel perturbations.

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Experimental Setup), p. 6 (5. Experiments), p. 7 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup), p. 8 (5.5. Real-robot Evaluations), p. 8 (5.3. Semantic Generalization across Tasks), metrics p. 8 (5.3. Semantic Generalization across Tasks), p. 7 (5.2. Performances Across 18 RLBench Tasks), p. 7 (5.1. Experimental Setup), p. 8 (5.4. Performance on MemoryBench), p. 15 (Figure/Table caption), p. 2 (Figure/Table caption), baselines p. 7 (5.1. Experimental Setup), p. 6 (5. Experiments), p. 8 (5.5. Real-robot Evaluations), p. 8 (5.3. Semantic Generalization across Tasks), p. 7 (5.1. Experimental Setup), p. 4 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 7 (5.2. Performances Across 18 RLBench Tasks), p. 7 (Figure/Table caption), p. 15 (Figure/Table caption), p. 8 (5.5. Real-robot Evaluations), p. 14 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
