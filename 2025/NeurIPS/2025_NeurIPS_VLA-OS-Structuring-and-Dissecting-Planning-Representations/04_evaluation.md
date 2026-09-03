# Evaluation - VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=PQYazNKEYo; PDF retrieval source: https://arxiv.org/pdf/2506.17561. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (3.1 Preliminaries), p. 9 (3.1 Preliminaries), p. 10 (3.1 Preliminaries), p. 11 (1. Why are visually grounded representations better than language?)): Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the provided datasets and perform worse ...

## Evaluation Body Digest

- **p. 8 / 3.1 Preliminaries - extractive body cue:** 4.3 More Performance, Generalization, and Benefit from Planning Head Pretraining To further compare different planning paradigms, we perform additional experiments to explore their performance on: ...
- **p. 8 / 3.1 Preliminaries - extractive body cue:** L V IF L+V L+IF V+IF L+V+IF VLA-OS-I-I 68.0 (↑2.0) 71.0 (↑5.0) 72.5 (↑6.5) 66.7 (↑0.7) 73.3 (↑7.3) 71.0 (↑5.0) 71.7 (↑5.7) VLA-OS-I-E 60.5 (↓5.5) ...
- **p. 9 / 3.1 Preliminaries - extractive body cue:** For data scalability, we use LIBERO-LONG [51], a dataset with 10 tasks with a total of 500 demonstrations.
- **p. 9 / 3.1 Preliminaries - extractive body cue:** Here, we train them on LIBERO-90, a larger dataset with 90 manipulation tasks and 50 demonstrations for each task.
- **p. 11 / 1. Why are visually grounded representations better than language? - extractive body cue:** The limitations of this paper are: 1) despite the VLA-OS family encompassing a wide array of task planning paradigms for VLA, there remain several designs ...
- **p. 10 / 3.1 Preliminaries - extractive body cue:** 4.7 Continual Learning Experiments of Different VLA Paradigms Continual learning for robot imitation learning [51, 24] measures the degree to which the VLA model forgets ...
- **p. 11 / 1. Why are visually grounded representations better than language? - extractive body cue:** How to construct large-scale task planning datasets for VLA?
- **p. 10 / 3.1 Preliminaries - extractive body cue:** Success rates are calculated among 20 evaluation episodes among the 3 best checkpoints.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** A Benchmarks and Dataset Details (p. 19); A.1 VLM Pretraining Dataset (p. 19); A.2 LIBERO Dataset (p. 19); A.3 The COLOSSEUM Dataset (p. 19); A.4 The Real-World Deformable Manipulation Dataset (p. 20); A.5 The DexArt Dataset (p. 20); A.6 The FurnitureBench Dataset (p. 20); A.7 The PerAct2 Dataset (p. 20); A.8 The Real-World Rigid-Body Manipulation Dataset (p. 20); B Reasoning Dataset Annotation (p. 22); B.1 Language Reasoning Dataset (p. 22); B.2 Visual Reasoning Dataset (p. 23).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with ... | p. 2 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Sanity check. Success rates on four LIBERO benchmarks. Baseline results are from their papers [43, 8, 44]. Our results are the average ... | p. 7 (Figure/Table caption) |
| 3.1 Preliminaries | EMPIRICAL / REAL-ROBOT OR HARDWARE | Finding 11: The performance of all VLA paradigms improves as the amount of action-labeled demonstration data increases, i.e., all VLA paradigms have the data ... | p. 9 (3.1 Preliminaries) |
| 3.1 Preliminaries | EMPIRICAL / REAL-ROBOT OR HARDWARE | Finding 5: Integrated-VLA and Hierarchical-VLA outperform ActionOnly-VLA across a broad spectrum of tasks (2D, 3D, simulation, and real-world), with their performances largely comparable. | p. 9 (3.1 Preliminaries) |
| 3.1 Preliminaries | EMPIRICAL / REAL-ROBOT OR HARDWARE | Then, we find the earliest epoch e∗ i in which the agent achieves the best performance on task i (i.e., e∗ i = arg ... | p. 10 (3.1 Preliminaries) |

## Dataset / Benchmark Role

- **p. 8 / 3.1 Preliminaries - extractive body cue:** 4.3 More Performance, Generalization, and Benefit from Planning Head Pretraining To further compare different planning paradigms, we perform additional experiments to explore their performance on: ...
- **p. 8 / 3.1 Preliminaries - extractive body cue:** L V IF L+V L+IF V+IF L+V+IF VLA-OS-I-I 68.0 (↑2.0) 71.0 (↑5.0) 72.5 (↑6.5) 66.7 (↑0.7) 73.3 (↑7.3) 71.0 (↑5.0) 71.7 (↑5.7) VLA-OS-I-E 60.5 (↓5.5) ...
- **p. 9 / 3.1 Preliminaries - extractive body cue:** For data scalability, we use LIBERO-LONG [51], a dataset with 10 tasks with a total of 500 demonstrations.
- **p. 9 / 3.1 Preliminaries - extractive body cue:** Here, we train them on LIBERO-90, a larger dataset with 90 manipulation tasks and 50 demonstrations for each task.
- **p. 11 / 1. Why are visually grounded representations better than language? - extractive body cue:** The limitations of this paper are: 1) despite the VLA-OS family encompassing a wide array of task planning paradigms for VLA, there remain several designs ...
- **p. 10 / 3.1 Preliminaries - extractive body cue:** 4.7 Continual Learning Experiments of Different VLA Paradigms Continual learning for robot imitation learning [51, 24] measures the degree to which the VLA model forgets ...
- **p. 11 / 1. Why are visually grounded representations better than language? - extractive body cue:** How to construct large-scale task planning datasets for VLA?
- **p. 10 / 3.1 Preliminaries - extractive body cue:** Success rates are calculated among 20 evaluation episodes among the 3 best checkpoints.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: The VLA-OS model family. Left: the VLM and the composable heads. Our VLM has the same architecture with different numbers of parameters. Although ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: The formats and contents of the language reasoning dataset, the visual reasoning dataset, and the image foresight reasoning dataset in this work. We ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Benchmarks used in our evaluations, including LIBERO [51] and FurnitureBench [32] for 2D rigid body manipulation experiments, The COLOSSEUM [64] for 3D and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Sanity check. Success rates on four LIBERO benchmarks. Baseline results are from their papers [43, 8, 44]. Our results are the average of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Different planning representation comparison on LIBERO-Long. All results are the average of top-3 checkpoints averaged over 20 rollouts. Numbers in parentheses indicate the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: More results for different paradigms and inference time and training cost for different representations. Results of the right figure are calculated from the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Comparison between VLA- OS-I-E and VLA-OS-H with the same planning errors. The three planning rep- resentations shown in this figure all have small ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.3 More Performance, Generalization, and Benefit from Planning Head Pretraining To further compare different planning paradigms, we perform additional experiments to explore their performance ... | embodiment, simulator version and control stack | p. 8 (3.1 Preliminaries), p. 8 (3.1 Preliminaries) |
| Task/environment | L V IF L+V L+IF V+IF L+V+IF VLA-OS-I-I 68.0 (↑2.0) 71.0 (↑5.0) 72.5 (↑6.5) 66.7 (↑0.7) 73.3 (↑7.3) 71.0 (↑5.0) 71.7 (↑5.7) VLA-OS-I-E 60.5 ... | reset, timeout, object/scene variation | p. 8 (3.1 Preliminaries), p. 9 (3.1 Preliminaries) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 6 (3.1 Preliminaries), p. 8 (3.1 Preliminaries) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (3.1 Preliminaries), p. 4 (3.1 Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| L V IF L+V L+IF V+IF L+V+IF VLA-OS-I-I 68.0 (↑2.0) 71.0 (↑5.0) 72.5 (↑6.5) 66.7 (↑0.7) 73.3 (↑7.3) 71.0 (↑5.0) 71.7 (↑5.7) VLA-OS-I-E 60.5 ... | definition/direction/unit from same section | p. 8 (3.1 Preliminaries) |
| Table 1: Sanity check. Success rates on four LIBERO benchmarks. Baseline results are from their papers [43, 8, 44]. Our results are the average ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Finding 6: Both Integrated-VLA and Hierarchical-VLA benefit similarly from task-planning pretraining, exhibiting analogous gains in task success rate. | definition/direction/unit from same section | p. 9 (3.1 Preliminaries) |
| Then we compute the average planning correctness I (0 or 1) of the planning outcomes and execution success rate S (0 or 1) from ... | definition/direction/unit from same section | p. 9 (3.1 Preliminaries) |
| Success rates are calculated among 20 evaluation episodes among the 3 best checkpoints. | definition/direction/unit from same section | p. 10 (3.1 Preliminaries) |
| Let ci,i be the best success rate over all evaluated epochs e for the current task i (i.e., ci,i = maxe ci,i,e). | definition/direction/unit from same section | p. 10 (3.1 Preliminaries) |
| Visually grounded representations (visual and image foresight) are better than language planning representations in terms of success rates, low-level following, and continual learning. | definition/direction/unit from same section | p. 11 (3.1 Preliminaries) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1: Sanity check. Success rates on four LIBERO benchmarks. Baseline results are from their papers [43, 8, 44]. Our results are the average ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 2: The VLA-OS model family. Left: the VLM and the composable heads. Our VLM has the same architecture with different numbers of parameters. ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Finding 4: When employing multiple planning representations concurrently, Hierarchical-VLA outperforms Integrated-VLA paradigms. | comparison identity and matched condition | p. 8 (3.1 Preliminaries) |
| Finding 5: Integrated-VLA and Hierarchical-VLA outperform ActionOnly-VLA across a broad spectrum of tasks (2D, 3D, simulation, and real-world), with their performances largely comparable. | comparison identity and matched condition | p. 9 (3.1 Preliminaries) |
| Finding 13: VLA paradigms with task planning (Integrated-VLA and Hierarchical-VLA), compared to the non-planning paradigm (ActionOnly-VLA), achieve higher forward transfer but incur faster forgetting. | comparison identity and matched condition | p. 11 (3.1 Preliminaries) |
| Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For 3), a lot of literature [27, 48, 13, 72, 94, 91] claim that the primary advantage of using task planning in VLA rather ... | component/input/data sensitivity | p. 9 (3.1 Preliminaries) |
| The limitations of this paper are: 1) despite the VLA-OS family encompassing a wide array of task planning paradigms for VLA, there remain several ... | component/input/data sensitivity | p. 11 (1. Why are visually grounded representations better than language?) |
| Then we fine-tune the pretrained VLM and planning heads together with the action head on LIBERO-LONG with both the task reasoning and policy learning ... | component/input/data sensitivity | p. 9 (3.1 Preliminaries) |
| 4.3 More Performance, Generalization, and Benefit from Planning Head Pretraining To further compare different planning paradigms, we perform additional experiments to explore their performance ... | component/input/data sensitivity | p. 8 (3.1 Preliminaries) |
| L V IF L+V L+IF V+IF L+V+IF VLA-OS-I-I 68.0 (↑2.0) 71.0 (↑5.0) 72.5 (↑6.5) 66.7 (↑0.7) 73.3 (↑7.3) 71.0 (↑5.0) 71.7 (↑5.7) VLA-OS-I-E 60.5 ... | component/input/data sensitivity | p. 8 (3.1 Preliminaries) |
| This is because that our finding 6 shows that task planning pretraining is useful. | component/input/data sensitivity | p. 11 (1. Why are visually grounded representations better than language?) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, ... | Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with ... | PDF body cue; verify exact table/figure and matched conditions | p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (3.1 Preliminaries), p. 9 (3.1 Preliminaries), p. 10 (3.1 Preliminaries), p. 11 (1. Why are visually grounded representations better than language?) |
| Primary metric/result | Table 1: Sanity check. Success rates on four LIBERO benchmarks. Baseline results are from their papers [43, 8, 44]. Our results are the average ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 3.1 Preliminaries - extractive body cue:** All results are the average of top-3 checkpoints averaged over 20 rollouts.
- **p. 8 / 3.1 Preliminaries - extractive body cue:** All results are averaged over 20 rollouts among 3 best checkpoints.
- **p. 9 / 3.1 Preliminaries - extractive body cue:** Results are averaged from 20 episodes for each task in LIBERO-LONG.
- **p. 9 / 3.1 Preliminaries - extractive body cue:** Thus, for a given task trajectory, we can get Decomposition Score (DCS)= 1 T PT t=1 I(pt) and Instruction Following Score (IFS)= 1 T PT ...
- **p. 9 / 3.1 Preliminaries - extractive body cue:** For data scalability, we use LIBERO-LONG [51], a dataset with 10 tasks with a total of 500 demonstrations.
- **p. 9 / 3.1 Preliminaries - extractive body cue:** For model scalability, we use LIBERO-90, a dataset with 90 tasks and 4,500 demonstrations, for the experiment with all training data.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | L V IF DCS IFS DCS IFS DCS IFS VLA-OS-I-I 0.79 - 0.83 - 0.92 - VLA-OS-H 0.81 0.84 0.86 0.93 0.94 0.90 It ... | p. 9 (3.1 Preliminaries) |
| body limitation/failure cue | For qualitative comparisons, we show in Figure 5 an example that when VLA-OS-H uses the same planning heads as VLA-OS-I-E where there are some ... | p. 8 (3.1 Preliminaries) |
| body limitation/failure cue | 5 Conclusion and Limitation We provide a systematic investigation across different VLA paradigms and task planning representations through various kinds of manipulation tasks. | p. 11 (3.1 Preliminaries) |
| body limitation/failure cue | The limitations of this paper are: 1) despite the VLA-OS family encompassing a wide array of task planning paradigms for VLA, there remain several ... | p. 11 (1. Why are visually grounded representations better than language?) |
| body limitation/failure cue | Meanwhile, the action head does not receive raw visual or language inputs. | p. 8 (3.1 Preliminaries) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We believe that our findings (as well as source codes, annotated datasets, and checkpoints) will provide significant help and guidance for future research within ... | p. 3 (1 Introduction) |
| We select the best checkpoint before 100k steps. | p. 10 (3.1 Preliminaries) |
| (b) Training cost and inference time for different representations. | p. 8 (3.1 Preliminaries) |
| Different from end-to-end foundation models in computer vision [58, 45, 40] and natural language processing tasks [1, 30, 89], recent studies of VLAs have ... | p. 1 (1 Introduction) |
| First, a VLM encodes the visual and language inputs, where the vision encoder will encode input image patches and project them into language embedding ... | p. 4 (3.1 Preliminaries) |
| The action head is a transformer decoder that has the same number of layers as the LLM, and for each layer, the queries of ... | p. 4 (3.1 Preliminaries) |
| Although we only draw Qwen2.5 here, our code supports any kind of LLM backbone from HuggingFace. | p. 5 (3.1 Preliminaries) |
| Thus, we choose Qwen2.5 [89] LLM series with 0.5B, 1.5B, 3B, 7B pretrained checkpoints rather than the original PaliGamma [6]. | p. 5 (3.1 Preliminaries) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the ...
- **p. 9 / 3.1 Preliminaries - extractive body cue:** L V IF DCS IFS DCS IFS DCS IFS VLA-OS-I-I 0.79 - 0.83 - 0.92 - VLA-OS-H 0.81 0.84 0.86 0.93 0.94 0.90 It is ...
- **p. 8 / 3.1 Preliminaries - extractive body cue:** For qualitative comparisons, we show in Figure 5 an example that when VLA-OS-H uses the same planning heads as VLA-OS-I-E where there are some planning ...
- **p. 11 / 3.1 Preliminaries - extractive body cue:** 5 Conclusion and Limitation We provide a systematic investigation across different VLA paradigms and task planning representations through various kinds of manipulation tasks.
- **p. 11 / 1. Why are visually grounded representations better than language? - extractive body cue:** The limitations of this paper are: 1) despite the VLA-OS family encompassing a wide array of task planning paradigms for VLA, there remain several designs ...
- **p. 8 / 3.1 Preliminaries - extractive body cue:** Meanwhile, the action head does not receive raw visual or language inputs.

- **Evidence anchors reviewed:** datasets p. 8 (3.1 Preliminaries), p. 8 (3.1 Preliminaries), p. 9 (3.1 Preliminaries), p. 9 (3.1 Preliminaries), p. 11 (1. Why are visually grounded representations better than language?), p. 10 (3.1 Preliminaries), metrics p. 2 (Figure/Table caption), p. 8 (3.1 Preliminaries), p. 7 (Figure/Table caption), p. 9 (3.1 Preliminaries), p. 9 (3.1 Preliminaries), p. 10 (3.1 Preliminaries), baselines p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (3.1 Preliminaries), p. 9 (3.1 Preliminaries), p. 11 (3.1 Preliminaries), p. 2 (Figure/Table caption), results p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (3.1 Preliminaries), p. 9 (3.1 Preliminaries), p. 10 (3.1 Preliminaries), p. 11 (1. Why are visually grounded representations better than language?).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
