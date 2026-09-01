# Evaluation - SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p011.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p011.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (10 Ablations on Design), p. 9 (B. Adapting to New Robot Setups), p. 7 (10 Ablations on Design), p. 8 (B. Adapting to New Robot Setups), p. 6 (10 Ablations on Design), p. 8 (B. Adapting to New Robot Setups)): Spatial VLA achieves the highest average success rate, outperforming all generalist manipulation policies.

## Evaluation Body Digest

- **p. 4 / B. The Pre-training and Post-training Scheme - extractive body cue:** We train SpatialVLA from Paligemma2 backbone [62] on a cross-robot dataset mixture with 1.1 Million real robot demonstrations {615 Gu}> covering a diverse range of ...
- **p. 5 / 3) How well does SpatialVLA perform in scenarios that - extractive body cue:** Firstly, we evaluate SpatialVLA in both SimplerEnv [35] simulation and the real-world Widow robot platform (BridgeV2 [64] [64] setups), testing its outof-the-box control capabilities on ...
- **p. 5 / 3) How well does SpatialVLA perform in scenarios that - extractive body cue:** Second, we assess the fine-tuning efficacy of our method in both simulation and real-world settings, including LIBERO [36] and new Franka robot setups, to adapt ...
- **p. 7 / B. Adapting to New Robot Setups - extractive body cue:** We present the evaluation of SpatialVLA on the LIBERO simulation benchmark [36], which consists of a set of diverse robotic manipulation tasks in simulated environments.
- **p. 4 / B. The Pre-training and Post-training Scheme - extractive body cue:** Pre-training stage aims to learn generalizable knowledge across diverse tasks and robots from a large-scale dataset mixture, while the post-training stage adapts the pretrained model ...
- **p. 9 / B. Adapting to New Robot Setups - extractive body cue:** We select four tasks from the SimplerEiny benchmark [35], namely "Pick Coke Can" and "Move Near" ‘on the Google Robot, as well as "Put Carrot ...
- **p. 6 / 10 Ablations on Design - extractive body cue:** 5, we design seven task suites for the Widow robot, encompassing, language grounding, semantic understanding (unseen background and poses), and motion distractors (manually move the ...
- **p. 6 / 10 Ablations on Design - extractive body cue:** For a more comprehensive evaluation, we conduct expernts on a real-world WidowX robot platform from the BridgeData V2 evaluation [64].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** Dataset (p. 1).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 10 Ablations on Design | EMPIRICAL / REAL-ROBOT OR HARDWARE | Spatial VLA achieves the highest average success rate, outperforming all generalist manipulation policies. | p. 7 (10 Ablations on Design) |
| B. Adapting to New Robot Setups | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to 1026-resolution action grids (#ly.s:#4), where Maes = Muss = 512, Myip = 2, Spatial VLA with 8194resolution action grids (Mines = Mrans ... | p. 9 (B. Adapting to New Robot Setups) |
| 10 Ablations on Design | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, SpatialVLA achieves a higher average success rate, showcasing robust and generalizable operation capabilities in unseen scenarios, objects, language grounding, and dynamic motions. | p. 7 (10 Ablations on Design) |
| B. Adapting to New Robot Setups | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fine-tuned SpatialVLA models achieve the highest average success rate and ranking, followed by fine-tuned OpenVLA [30] and Octo [48] | p. 8 (B. Adapting to New Robot Setups) |
| 10 Ablations on Design | EMPIRICAL / REAL-ROBOT OR HARDWARE | On average, SpatialVLA achieves the highest overall visual matching and variant aggregation performance with a significant margin, Our SpatialVLA model yields 71.9% and 75.1% ... | p. 6 (10 Ablations on Design) |

## Dataset / Benchmark Role

- **p. 4 / B. The Pre-training and Post-training Scheme - extractive body cue:** We train SpatialVLA from Paligemma2 backbone [62] on a cross-robot dataset mixture with 1.1 Million real robot demonstrations {615 Gu}> covering a diverse range of ...
- **p. 5 / 3) How well does SpatialVLA perform in scenarios that - extractive body cue:** Firstly, we evaluate SpatialVLA in both SimplerEnv [35] simulation and the real-world Widow robot platform (BridgeV2 [64] [64] setups), testing its outof-the-box control capabilities on ...
- **p. 5 / 3) How well does SpatialVLA perform in scenarios that - extractive body cue:** Second, we assess the fine-tuning efficacy of our method in both simulation and real-world settings, including LIBERO [36] and new Franka robot setups, to adapt ...
- **p. 7 / B. Adapting to New Robot Setups - extractive body cue:** We present the evaluation of SpatialVLA on the LIBERO simulation benchmark [36], which consists of a set of diverse robotic manipulation tasks in simulated environments.
- **p. 4 / B. The Pre-training and Post-training Scheme - extractive body cue:** Pre-training stage aims to learn generalizable knowledge across diverse tasks and robots from a large-scale dataset mixture, while the post-training stage adapts the pretrained model ...
- **p. 9 / B. Adapting to New Robot Setups - extractive body cue:** We select four tasks from the SimplerEiny benchmark [35], namely "Pick Coke Can" and "Move Near" ‘on the Google Robot, as well as "Put Carrot ...
- **p. 6 / 10 Ablations on Design - extractive body cue:** 5, we design seven task suites for the Widow robot, encompassing, language grounding, semantic understanding (unseen background and poses), and motion distractors (manually move the ...
- **p. 6 / 10 Ablations on Design - extractive body cue:** For a more comprehensive evaluation, we conduct expernts on a real-world WidowX robot platform from the BridgeData V2 evaluation [64].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We present Spatial VLA, a spatial-enhanced
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of Spatial VLA, Given an image observati
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Illustration of adaptive action grids. (a) Statistics of translation and rotation action movements on the whole pre- training mixture, (b) grids are split ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Experiment Setup. We evaluate SpatialVLA across 7 robot learning scenarios, 16 real-robot tasks, and 48 simulation
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Zero-shot Robot Control Evaluation on WidowX Robot. We evaluate SpatialVLA across 7 task suites to explore the Ianguage grounding, semantic understanding, and motion ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Adapting to New Robot Setups on Franka Robot. Spatial VLA serves as a generalist robot control policy, achieving better performance across multiple setups, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Spatial Understanding Capability Evaluation. Ben- efiting from the proposed Ego3D Position Encoding, Spa- tialVLA exhibits superior performance in understanding spa: tial prompts and ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Cross-sectional features visualization in spatial grids ‘The proposed spatial embedding adaptation aligns the pre- trained spatial grid features with those of the target ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We train SpatialVLA from Paligemma2 backbone [62] on a cross-robot dataset mixture with 1.1 Million real robot demonstrations {615 Gu}> covering a diverse range ... | embodiment, simulator version and control stack | p. 4 (B. The Pre-training and Post-training Scheme), p. 5 (3) How well does SpatialVLA perform in scenarios that) |
| Task/environment | Firstly, we evaluate SpatialVLA in both SimplerEnv [35] simulation and the real-world Widow robot platform (BridgeV2 [64] [64] setups), testing its outof-the-box control capabilities ... | reset, timeout, object/scene variation | p. 5 (3) How well does SpatialVLA perform in scenarios that), p. 5 (3) How well does SpatialVLA perform in scenarios that) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (A. The SpatialVLA Model Architecture), p. 3 (A. The SpatialVLA Model Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We present the success rate (SR) and standard error for each method across four task suites, which are averaged over three random seeds with ... | definition/direction/unit from same section | p. 8 (B. Adapting to New Robot Setups) |
| Compared to 1026-resolution action grids (#ly.s:#4), where Maes = Muss = 512, Myip = 2, Spatial VLA with 8194resolution action grids (Mines = Mrans ... | definition/direction/unit from same section | p. 9 (B. Adapting to New Robot Setups) |
| Spatial VLA achieves the highest average success rate, outperforming all generalist manipulation policies. | definition/direction/unit from same section | p. 7 (10 Ablations on Design) |
| Finetuning on the BridgeV2 yields a remarkable 100% success rate in the "Put Eggplant in Yellow Basket" task, demonstrating the rmodel's exceptional zero-shot manipulation ... | definition/direction/unit from same section | p. 7 (10 Ablations on Design) |
| Similar results are observed in the LIBERO-Spatial task suite (88.2% success rate). | definition/direction/unit from same section | p. 8 (B. Adapting to New Robot Setups) |
| In contrast to the conventional linear 256-bin action space discretization (6, 13, 30] (#1vs.#2), the proposed adaprive spatial action grids exhibits significant advantages, particularly ... | definition/direction/unit from same section | p. 9 (B. Adapting to New Robot Setups) |
| On average, SpatialVLA achieves the highest overall visual matching and variant aggregation performance with a significant margin, Our SpatialVLA model yields 71.9% and 75.1% ... | definition/direction/unit from same section | p. 6 (10 Ablations on Design) |
| 7) into polar coordinates (¢,0,r) to disentangle movement direction (6, 0) and distance r. | definition/direction/unit from same section | p. 4 (A. The SpatialVLA Model Architecture) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In particular, SpatialVLA also matches or outperforms te latest SOTA model 7, Tab, I! summarizes the esults across different manipulation policies on the WidowX ... | comparison identity and matched condition | p. 7 (10 Ablations on Design) |
| Spatial VLA is compared to previous state-of-the-art robot foundation models and alternative designs in spatial representations. | comparison identity and matched condition | p. 5 (B. The Pre-training and Post-training Scheme) |
| In most tasks, SpatialVLA outperforms the state-of-the-art generalist ‘manipulation policies but struggles with long-horizon tasks in LIBERO-Long, due to the lack of architecture design ... | comparison identity and matched condition | p. 7 (B. Adapting to New Robot Setups) |
| We compare ‘our model with the latest state-of-the-art generalist manipulation policies, including RT-1 [6], RT-1-X [13], RE2-X [13], Octo [48], OpenVLA [30], HPT [65], ... | comparison identity and matched condition | p. 6 (10 Ablations on Design) |
| Compared to existing policies, SpaIVLA shows superior spatial understanding, achieving 73% accuracy in Franka task #1, which involves spatial prompts, and significantly improving manipulation ... | comparison identity and matched condition | p. 8 (B. Adapting to New Robot Setups) |
| Compared to 1026-resolution action grids (#ly.s:#4), where Maes = Muss = 512, Myip = 2, Spatial VLA with 8194resolution action grids (Mines = Mrans ... | comparison identity and matched condition | p. 9 (B. Adapting to New Robot Setups) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| On average, SpatialVLA achieves the highest overall visual matching and variant aggregation performance with a significant margin, Our SpatialVLA model yields 71.9% and 75.1% ... | component/input/data sensitivity | p. 6 (10 Ablations on Design) |
| In this section, we conduct ablation studies to investigate the effectiveness of the proposed 3D Spatial Presentation in both pre-training and post-rraining stages. | component/input/data sensitivity | p. 8 (B. Adapting to New Robot Setups) |
| a thorough ablation study on a mixed Fractal and Bridge dataset to verify our design decisions. | component/input/data sensitivity | p. 6 (10 Ablations on Design) |
| conditions, characterized by varying visual appearances, which is further supported by its superior performance in variant aggregation. | component/input/data sensitivity | p. 7 (10 Ablations on Design) |
| ‘TABLE V: Fine-tuning Ablations in Domain Datasets. | component/input/data sensitivity | p. 9 (B. Adapting to New Robot Setups) |
| Finally, we conduct comprehensive ablation studies on a mixture of Fractal (6] and BridgeV2 [64] datasets to verify our design decisions in Spatial VLA. | component/input/data sensitivity | p. 5 (3) How well does SpatialVLA perform in scenarios that) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the contributions of this work consist of a novel generalist robot policy that explores spatial representations for robot foundation models, sophisticated designs ... | Spatial VLA achieves the highest average success rate, outperforming all generalist manipulation policies. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (10 Ablations on Design), p. 9 (B. Adapting to New Robot Setups), p. 7 (10 Ablations on Design), p. 8 (B. Adapting to New Robot Setups), p. 6 (10 Ablations on Design), p. 8 (B. Adapting to New Robot Setups) |
| Primary metric/result | Compared to 1026-resolution action grids (#ly.s:#4), where Maes = Muss = 512, Myip = 2, Spatial VLA with 8194resolution action grids (Mines = Mrans ... | numeric claim only at cited anchor | p. 9 (B. Adapting to New Robot Setups) |

- Numeric sentences retained from the body:
- **p. 4 / A. The SpatialVLA Model Architecture - extractive body cue:** Moreover, itis worth noting that the model only needs 10 generate 3 tokens for one-step robot actions rather than 7 tokens as in RT-1 [6], ...
- **p. 5 / 3) How well does SpatialVLA perform in scenarios that - extractive body cue:** For output robot actions, the SpatialVLA policy predicts a chunk of T = 4 future actions (12 spatial action tokens from total V = 8194 ...
- **p. 5 / 3) How well does SpatialVLA perform in scenarios that - extractive body cue:** During inference, SpatialVLA requires 8.5GB of GPU memory and ins at approximately 20Hz on one NVIDIA RX 4090 GPU to run evaluations in both simulation ...
- **p. 6 / 10 Ablations on Design - extractive body cue:** We evaluate SpatialVLA across 7 robot learning scenarios, 16 real-robot tasks, and 48 simulation
- **p. 6 / 10 Ablations on Design - extractive body cue:** All generalist manipulation policies, including Octo, RT-1-X, OpenVLA, and RoboVLM, are evaluated across 7 task suites with 11 trials each, resulting in a total of ...
- **p. 7 / 10 Ablations on Design - extractive body cue:** We evaluate SpatialVLA across 7 task suites to explore the Ianguage grounding, semantic understanding, and motion sensing capabilities, with varying backgrounds, poses, and motion istractors.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, in moderately complex tasks (#3-7), ‘most policies, such as RT-1-X, Octo, and RoboVLM struggle with manipulation, frequently encountering issues like object nisidentfication and ... | p. 7 (10 Ablations on Design) |
| body limitation/failure cue | Compared to OpenVLA, ‘our method demonstrates superior robustness in handling motion disturbances (human-induced dynamic object movement in tasks #3 and #4), successfully tracking and ... | p. 7 (10 Ablations on Design) |
| body limitation/failure cue | To assess the robustness of Spatial VLA in diverse environmental variations, we employ the SimplerEnv simulation benchmark [35] to evaluate visual ‘matching and variant ... | p. 5 (3) How well does SpatialVLA perform in scenarios that) |
| body limitation/failure cue | Qualitatively, we find that SpatialVLA exhibits greater generalizability and robustness across diverse robotic manipulation tasks and environmental | p. 6 (10 Ablations on Design) |
| body limitation/failure cue | 1), including depth or point cloud, into the VLA framework to improve the model's adaptability and robustness in spatial layout variations. | p. 8 (B. Adapting to New Robot Setups) |
| body limitation/failure cue | Compared to existing policies, SpaIVLA shows superior spatial understanding, achieving 73% accuracy in Franka task #1, which involves spatial prompts, and significantly improving manipulation ... | p. 8 (B. Adapting to New Robot Setups) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation Details. ‘The SpatialVLA model is pre~ trained with 1.1 Million real-robot demonstrations from the OXE [15] and RH2OT dataset {18} on a cluster ... | p. 5 (3) How well does SpatialVLA perform in scenarios that) |
| All the models are trained from seratch on 8 A100 GPUs with 128 batch size for 120k steps. | p. 9 (B. Adapting to New Robot Setups) |
| initialized, and then they are optimized during training, as well as the parameters of vision encoder and LLM backbone. | p. 5 (B. The Pre-training and Post-training Scheme) |
| We present the success rate (SR) and standard error for each method across four task suites, which are averaged over three random seeds with ... | p. 8 (B. Adapting to New Robot Setups) |
| The ‘egocentric 3D positions P are then encoded into 3D position embeddings P< R**" through a sinusoidal function -y(-) following by a learnable MLP. | p. 4 (A. The SpatialVLA Model Architecture) |
| 2, we first employ SigLIP [68] visual encoder to extract 2D semantic visual features X ¢ R4**" to inherit the alignment between vision and ... | p. 4 (A. The SpatialVLA Model Architecture) |
| All generalist manipulation policies, including Octo, RT-1-X, OpenVLA, and RoboVLM, are evaluated across 7 task suites with 11 trials each, resulting in a total ... | p. 6 (10 Ablations on Design) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 10 Ablations on Design - extractive body cue:** However, in moderately complex tasks (#3-7), ‘most policies, such as RT-1-X, Octo, and RoboVLM struggle with manipulation, frequently encountering issues like object nisidentfication and grasp ...
- **p. 7 / 10 Ablations on Design - extractive body cue:** Compared to OpenVLA, ‘our method demonstrates superior robustness in handling motion disturbances (human-induced dynamic object movement in tasks #3 and #4), successfully tracking and grasping ...
- **p. 5 / 3) How well does SpatialVLA perform in scenarios that - extractive body cue:** To assess the robustness of Spatial VLA in diverse environmental variations, we employ the SimplerEnv simulation benchmark [35] to evaluate visual ‘matching and variant aggregation ...
- **p. 6 / 10 Ablations on Design - extractive body cue:** Qualitatively, we find that SpatialVLA exhibits greater generalizability and robustness across diverse robotic manipulation tasks and environmental
- **p. 8 / B. Adapting to New Robot Setups - extractive body cue:** 1), including depth or point cloud, into the VLA framework to improve the model's adaptability and robustness in spatial layout variations.
- **p. 8 / B. Adapting to New Robot Setups - extractive body cue:** Compared to existing policies, SpaIVLA shows superior spatial understanding, achieving 73% accuracy in Franka task #1, which involves spatial prompts, and significantly improving manipulation capabilities ...

- **PDF anchors reviewed:** datasets p. 4 (B. The Pre-training and Post-training Scheme), p. 5 (3) How well does SpatialVLA perform in scenarios that), p. 5 (3) How well does SpatialVLA perform in scenarios that), p. 7 (B. Adapting to New Robot Setups), p. 4 (B. The Pre-training and Post-training Scheme), p. 9 (B. Adapting to New Robot Setups), metrics p. 8 (B. Adapting to New Robot Setups), p. 9 (B. Adapting to New Robot Setups), p. 7 (10 Ablations on Design), p. 7 (10 Ablations on Design), p. 8 (B. Adapting to New Robot Setups), p. 9 (B. Adapting to New Robot Setups), baselines p. 7 (10 Ablations on Design), p. 5 (B. The Pre-training and Post-training Scheme), p. 7 (B. Adapting to New Robot Setups), p. 6 (10 Ablations on Design), p. 8 (B. Adapting to New Robot Setups), p. 9 (B. Adapting to New Robot Setups), results p. 7 (10 Ablations on Design), p. 9 (B. Adapting to New Robot Setups), p. 7 (10 Ablations on Design), p. 8 (B. Adapting to New Robot Setups), p. 6 (10 Ablations on Design), p. 8 (B. Adapting to New Robot Setups).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
