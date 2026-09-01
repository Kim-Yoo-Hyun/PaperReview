# Evaluation - Volumetric Environment Representation for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 7 (4.2. Diagnostic Experiment), p. 8 (4.3. Analysis on 3D Representation Learning), p. 6 (4.1. Performance on VLN), p. 6 (4.1. Performance on VLN), p. 8 (4.3. Analysis on 3D Representation Learning)): Table 3. Quantitative results on R4R [39] (more details in §4.1). (RGS), and Remote Grounding Success weighted by Path Length (RGSPL) are also employed for object grounding. For R4R, Coverage ...

## Evaluation Body Digest

- **p. 6 / 4.1. Performance on VLN - extractive body cue:** The dataset is split into train, val seen, val unseen, and test unseen sets, which mainly focus on the generalization capability in unseen environments.
- **p. 8 / 4.3. Analysis on 3D Representation Learning - extractive body cue:** This suggests these 3D perception tasks are complementary to each other in capturing geometric and semantic properties of scenes, further facilitating the decision-making.
- **p. 6 / 4.1. Performance on VLN - extractive body cue:** The experiments are conducted on three datasets.
- **p. 7 / 4.1. Performance on VLN - extractive body cue:** Compared with the recent stateof-the-art VLN agent [55], our agent improves SR and SPL by 3.86% and 4.07% on the val unseen split.
- **p. 7 / 4.2. Diagnostic Experiment - extractive body cue:** To thoroughly test the efficacy of crucial components of our model, we conduct a series of diagnostic studies on val unseen split of REVERIE and ...
- **p. 8 / 4.3. Analysis on 3D Representation Learning - extractive body cue:** Ablation study of Multi-task Learning on occupancy prediction (mIoU), 3D detection (mAP), room layout estimation (3D IoU), and val unseen set of R2R [3] (see ...
- **p. 6 / 4.1. Performance on VLN - extractive body cue:** For R2R, Success Rate (SR), Trajectory Length (TL), Oracle Success Rate (OSR), Success rate weighted by Path Length (SPL), and Navigation Error (NE) are used.
- **p. 7 / 4.1. Performance on VLN - extractive body cue:** For R4R, Coverage weighted by Length Score (CLS), normalized Dynamic Time Warping (nDTW), and Success rate weighted nDTW (SDTW) are used.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 3.5. Implementation Details (p. 6); 4. Experiment (p. 6); 4.2. Diagnostic Experiment (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3. Quantitative results on R4R [39] (more details in §4.1). (RGS), and Remote Grounding Success weighted by Path Length (RGSPL) are also employed ... | p. 7 (Figure/Table caption) |
| 4.2. Diagnostic Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | After using Episodic Memory, a higher score (i.e., 31.36% →33.71% on RGS) is achieved. | p. 7 (4.2. Diagnostic Experiment) |
| 4.3. Analysis on 3D Representation Learning | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our approach improves the performance by solid margins (e.g., 11.03%→ 12.93% for 3D occupancy, 75.14% →75.80% on SR of R2R). | p. 8 (4.3. Analysis on 3D Representation Learning) |
| 4.1. Performance on VLN | EMPIRICAL / SOURCE-REPORTED EVALUATION | For REVERIE, Remote Grounding Success rate 16322 | p. 6 (4.1. Performance on VLN) |
| 4.1. Performance on VLN | EMPIRICAL / SOURCE-REPORTED EVALUATION | For R2R, Success Rate (SR), Trajectory Length (TL), Oracle Success Rate (OSR), Success rate weighted by Path Length (SPL), and Navigation Error (NE) are ... | p. 6 (4.1. Performance on VLN) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Performance on VLN - extractive body cue:** The dataset is split into train, val seen, val unseen, and test unseen sets, which mainly focus on the generalization capability in unseen environments.
- **p. 8 / 4.3. Analysis on 3D Representation Learning - extractive body cue:** This suggests these 3D perception tasks are complementary to each other in capturing geometric and semantic properties of scenes, further facilitating the decision-making.
- **p. 6 / 4.1. Performance on VLN - extractive body cue:** The experiments are conducted on three datasets.
- **p. 7 / 4.1. Performance on VLN - extractive body cue:** Compared with the recent stateof-the-art VLN agent [55], our agent improves SR and SPL by 3.86% and 4.07% on the val unseen split.
- **p. 7 / 4.2. Diagnostic Experiment - extractive body cue:** To thoroughly test the efficacy of crucial components of our model, we conduct a series of diagnostic studies on val unseen split of REVERIE and ...
- **p. 8 / 4.3. Analysis on 3D Representation Learning - extractive body cue:** Ablation study of Multi-task Learning on occupancy prediction (mIoU), 3D detection (mAP), room layout estimation (3D IoU), and val unseen set of R2R [3] (see ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The agent observes its surroundings with correspond- ing perspective features of different candidate views ( ). Previous methods construct the topological graph or ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of our model. Given the perspective features of candidate views, a group of 3D queries are used to sample and aggregate them ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Our coarse-to-fine VER representation extraction (§3.1) adopts cascade up-sampling operations with 3D deconvolutions (Eq. 2) and 3D queries (Eq. 1). The training process ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results on R2R [3] (more details in §4.1). at each mini-batch with the same sampling ratio. Finetuning. Following the standard protocol [1, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison results on REVERIE [64]. ‘-': unavailable statistics (see §4.1 for more details). R4R val unseen Models NE↓ SR↑ CLS↑ nDTW↑ SDTW↑
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Quantitative results on R4R [39] (more details in §4.1). (RGS), and Remote Grounding Success weighted by Path Length (RGSPL) are also employed for ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Ablation study of overall design on val unseen of REVERIE [64] and R2R [3] (see §4.2 for more details). diction at the key ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. A representative visual result on val unseen of R2R [3]. We first visualize the 3D occupancy prediction at the key steps. In addition, ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset is split into train, val seen, val unseen, and test unseen sets, which mainly focus on the generalization capability in unseen environments. | embodiment, simulator version and control stack | p. 6 (4.1. Performance on VLN), p. 8 (4.3. Analysis on 3D Representation Learning) |
| Task/environment | This suggests these 3D perception tasks are complementary to each other in capturing geometric and semantic properties of scenes, further facilitating the decision-making. | reset, timeout, object/scene variation | p. 8 (4.3. Analysis on 3D Representation Learning), p. 6 (4.1. Performance on VLN) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 4 (3.2. Volume State Estimation) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (3.4. Annotation Generation), p. 6 (3.5. Implementation Details) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For R2R, Success Rate (SR), Trajectory Length (TL), Oracle Success Rate (OSR), Success rate weighted by Path Length (SPL), and Navigation Error (NE) are ... | definition/direction/unit from same section | p. 6 (4.1. Performance on VLN) |
| For R4R, Coverage weighted by Length Score (CLS), normalized Dynamic Time Warping (nDTW), and Success rate weighted nDTW (SDTW) are used. | definition/direction/unit from same section | p. 7 (4.1. Performance on VLN) |
| Room. mIoU↑ mAP↑ 3D IoU↑ SR↑ SPL↑ ✓ 12.09 - - 74.90 63.82 ✓ ✓ 12.14 32.64 - 75.21 64.79 ✓ ✓ - 33.11 ... | definition/direction/unit from same section | p. 8 (4.3. Analysis on 3D Representation Learning) |
| 3D Perception R2R Up-Sampling mIoU↑ mAP↑ 3D IoU↑ SR↑ SPL↑ w/o Coarse-to-Fine 12.39 32.95 66.57 - - Trilinear Interpolation 11.03 29.42 63.45 75.14 64.30 ... | definition/direction/unit from same section | p. 8 (4.3. Analysis on 3D Representation Learning) |
| For REVERIE, Remote Grounding Success rate 16322 | definition/direction/unit from same section | p. 6 (4.1. Performance on VLN) |
| After using Episodic Memory, a higher score (i.e., 31.36% →33.71% on RGS) is achieved. | definition/direction/unit from same section | p. 7 (4.2. Diagnostic Experiment) |
| Figure 1. The agent observes its surroundings with correspond- ing perspective features of different candidate views ( ). Previous methods construct the topological graph ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 3. Our coarse-to-fine VER representation extraction (§3.1) adopts cascade up-sampling operations with 3D deconvolutions (Eq. 2) and 3D queries (Eq. 1). The training ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For R2R, Success Rate (SR), Trajectory Length (TL), Oracle Success Rate (OSR), Success rate weighted by Path Length (SPL), and Navigation Error (NE) are ... | comparison identity and matched condition | p. 6 (4.1. Performance on VLN) |
| Our approach outperforms others in most metrics with a promising gain on nDTW (i.e., 1%). | comparison identity and matched condition | p. 7 (4.1. Performance on VLN) |
| Compared with the recent stateof-the-art VLN agent [55], our agent improves SR and SPL by 3.86% and 4.07% on the val unseen split. | comparison identity and matched condition | p. 7 (4.1. Performance on VLN) |
| In Table 6, our network (§3.1) outperforms other methods [51, 78] by a significant margin (2.19% on IoU of occupancy, 3.66% on mAP of ... | comparison identity and matched condition | p. 8 (4.3. Analysis on 3D Representation Learning) |
| Ablation study of neighborhood range on val unseen of REVERIE [64] and R2R [3] (see §4.2 for more details). | comparison identity and matched condition | p. 8 (4.3. Analysis on 3D Representation Learning) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study of overall design on val unseen of REVERIE [64] and R2R [3] (see §4.2 for more details). diction at the key steps, ... | component/input/data sensitivity | p. 7 (4.1. Performance on VLN) |
| Ablation study of Coarse-to-Fine Extraction on occupancy prediction (mIoU), 3D detection (mAP), room layout (3D IoU), and val unseen set of R2R [3] (see ... | component/input/data sensitivity | p. 8 (4.3. Analysis on 3D Representation Learning) |
| Table 5. Ablation study of neighborhood range on val unseen of REVERIE [64] and R2R [3] (see §4.2 for more details). Occupancy Detection Layout ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| To thoroughly test the efficacy of crucial components of our model, we conduct a series of diagnostic studies on val unseen split of REVERIE ... | component/input/data sensitivity | p. 7 (4.2. Diagnostic Experiment) |
| For the multiview images, we adopt ViT-B/16 [20] pretrained on ImageNet to extract features. | component/input/data sensitivity | p. 6 (3.5. Implementation Details) |
| Following recent VLN practice [14, 16, 33], both offline pretraining and finetuning are adopted. | component/input/data sensitivity | p. 6 (3.5. Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this article, we propose a Volumetric Environment Representation (VER) that quantizes the physical world into structured 3D cells (Fig. | Table 3. Quantitative results on R4R [39] (more details in §4.1). (RGS), and Remote Grounding Success weighted by Path Length (RGSPL) are also employed ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 7 (4.2. Diagnostic Experiment), p. 8 (4.3. Analysis on 3D Representation Learning), p. 6 (4.1. Performance on VLN), p. 6 (4.1. Performance on VLN), p. 8 (4.3. Analysis on 3D Representation Learning) |
| Primary metric/result | After using Episodic Memory, a higher score (i.e., 31.36% →33.71% on RGS) is achieved. | numeric claim only at cited anchor | p. 7 (4.2. Diagnostic Experiment) |

- Numeric sentences retained from the body:
- **p. 6 / 3.5. Implementation Details - extractive body cue:** MLT with 4 layers is initialized from [73] for state estimation (Eq.
- **p. 6 / 3.5. Implementation Details - extractive body cue:** Our model is implemented in PyTorch and trained on eight RTX 4090 GPUs with a 24GB memory per-card.
- **p. 6 / 4.1. Performance on VLN - extractive body cue:** R2R [3] contains 7,189 trajectories sampled from 90 realworld indoor scenes.
- **p. 3 / 3. Approach - extractive body cue:** The local action space At∈RNt+1 is defined by Nt candidate views, which correspond to neighboring navigable nodes {v∗ t,n}Nt n=1, as well as a [STOP] ...
- **p. 5 / 3.3. Action Prediction - extractive body cue:** As our agent navigates on the horizontal plane to reach the adjacent candidate viewpoints {v∗ n}Nt n=1, we map the volume state space into 2D ...
- **p. 5 / 3.3. Action Prediction - extractive body cue:** Then we sum probability values in the neighborhood of {v∗ t,n}Nt n=0 (v∗ 0 for the current viewpoint, i.e., [STOP]), and normalize them as the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In this stage, we set the learning rate to 1e-5 and batch size to 8 with 20k iterations. | p. 6 (3.5. Implementation Details) |
| Initially, the environment encoder (§3.1) is introduced for VER through coarse-to-fine extraction. | p. 6 (3.5. Implementation Details) |
| Ablation study of overall design on val unseen of REVERIE [64] and R2R [3] (see §4.2 for more details). diction at the key steps, ... | p. 7 (4.1. Performance on VLN) |
| We first visualize the 3D occupancy prediction at the key steps. | p. 8 (4.3. Analysis on 3D Representation Learning) |
| To encode VER, we devise coarse-to-fine extraction with multiple 3D perception tasks supervised by multi-resolution annotations (§3.4). | p. 3 (3. Approach) |
| At step t, an environment encoder is proposed to sample multi-view features (F 2d t of each view) into the volumetric space of VER, ... | p. 3 (3. Approach) |
| For 3D occupancy prediction, the decoder is implemented as MLPs with the focal loss [52]. | p. 4 (3.1. Environment Encoder) |
| As such, the state transition within the locally observed 3D environment, computed by Eq. | p. 4 (3.2. Volume State Estimation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **PDF anchors reviewed:** datasets p. 6 (4.1. Performance on VLN), p. 8 (4.3. Analysis on 3D Representation Learning), p. 6 (4.1. Performance on VLN), p. 7 (4.1. Performance on VLN), p. 7 (4.2. Diagnostic Experiment), p. 8 (4.3. Analysis on 3D Representation Learning), metrics p. 6 (4.1. Performance on VLN), p. 7 (4.1. Performance on VLN), p. 8 (4.3. Analysis on 3D Representation Learning), p. 8 (4.3. Analysis on 3D Representation Learning), p. 6 (4.1. Performance on VLN), p. 7 (4.2. Diagnostic Experiment), baselines p. 6 (4.1. Performance on VLN), p. 7 (4.1. Performance on VLN), p. 7 (4.1. Performance on VLN), p. 8 (4.3. Analysis on 3D Representation Learning), p. 8 (4.3. Analysis on 3D Representation Learning), results p. 7 (Figure/Table caption), p. 7 (4.2. Diagnostic Experiment), p. 8 (4.3. Analysis on 3D Representation Learning), p. 6 (4.1. Performance on VLN), p. 6 (4.1. Performance on VLN), p. 8 (4.3. Analysis on 3D Representation Learning).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
