# Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p059.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p059.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, Dataset, contact-rich manipulation, assembly, force-torque, event camera, failure data
- Official paper: https://www.roboticsproceedings.org/rss21/p059.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p059.pdf
- Code/Project: https://tuwien-asl.github.io/REASSEMBLE_page/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-02 (17 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 robot_data 문제를 이해하기 위해 읽는다. 본문은 ‘To bridge the gap between these pressing challenges, we introduce REASSEMBLE, a comprehensive dataset tailored to long-horizon and contact-rich manipulation tasks.를 문제로 두고, To. bridge this gap, we present REASSEMBLE (Robotic assEmbly disASSEMBLy datasEt), a 1 new dataset designed specifically for contact-rich manipalation를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotic manipulation remains a core challenge in robotics, particularly for contact-rich tasks such as industrial
- **p. 1 / Abstract - extractive body cue:** condi dcnieaion, ation segmentation, and tsk Inversion learning.
- **p. 1 / Abstract - extractive body cue:** The REASSEMBLE will be a valuable resource for advancing robotic manipulation in complex, real-world scenarios. ‘The dataset is publicly available on our project website'.
- **p. 1 / Abstract - extractive body cue:** To. bridge this gap, we present REASSEMBLE (Robotic assEmbly disASSEMBLy datasEt), a 1 new dataset designed specifically for contact-rich manipalation
- **p. 1 / Abstract - extractive body cue:** Built around the NIST Assembly Task Board 1 benchmark, REASSEMBLE includes four actions (pick, insert, remove, and place) involving 17 objects.
- **p. 2 / Abstract - extractive body cue:** ‘To bridge the gap between these pressing challenges, we introduce REASSEMBLE, a comprehensive dataset tailored to long-horizon and contact-rich manipulation tasks.
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** However, such datasets primarily focus on human activity and often lack relevance to robotic manipulation tasks.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** To. bridge this gap, we present REASSEMBLE (Robotic assEmbly disASSEMBLy datasEt), a 1 new dataset designed specifically for contact-rich manipalation
- **p. 2 / Abstract - extractive body cue:** By offering a rich, multi modal dataset, REASSEMBLE fosters the development of adaptive and versatile robotic systems capable of tackling the challenges of long-horizon, contact-rich ...
- **p. 2 / Abstract - extractive body cue:** ‘To bridge the gap between these pressing challenges, we introduce REASSEMBLE, a comprehensive dataset tailored to long-horizon and contact-rich manipulation tasks.
- **p. 11 / B. Motion Policy Learning - extractive body cue:** ‘The primary objective of this study is to introduce a novel robot manipulation dataset specifically designed for contactrich manipulation tasks, rather than t0 develop a ...
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** Numerous datasets have been developed to support temporal action segmentation [20], (27), [28].
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** This dataset provides temporally labelled actions for long-duration videos, facilitating the training and evaluation of models for action segmentation.
- **p. 2 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** development in various robot learning fields, like hicrarchical temporal action segmentation, motion policy learning, and anomaly detection.
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** The tasks include TAS (Temporal Action Segmentation), MPL (Motion Policy Learning), AD (Anomaly Detection), and TIL (Task Inversion Learning).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Interaction forces and torques are measured using a wrist-mounted 6-axis force-torque (FT) sensor (AIDIN ROBOTICS AFT200-D80-C), as shown in Figure 2. | multi-view observation, language/task label과 action trajectory | p. 4 (B. Sensors), p. 1 (1 Seraies) |
| State/latent | Interaction, forces, torques, measured, wrist-mounted, axis, force-torque, sensor, AIDIN, ROBOTICS, AFT200-D80-C, Figure | shared representation, embodiment/task identity와 data distribution | p. 4 (B. Sensors), p. 1 (1 Seraies), p. 2 (2) A dataset with multi-task labels to support algorithm) |
| Output/action | We annotate the data for three different tasks: Hierarchical Temporal Action Segmentation (high-level actions and low-level skills), Motion Policy Learning, and Succes Anomaly Detection, | dataset sample 또는 learned policy action | p. 1 (1 Seraies), p. 2 (2) A dataset with multi-task labels to support algorithm), p. 2 (Abstract) |
| Objective/outcome | ‘The increasing prevalence of automation in robotic manipulation tasks highlights the necessity of effective skill assess- ‘ment, task monitoring, and summarization to enhance system performance and reliability. ‘Temporal action segment ... | coverage, cross-embodiment transfer, data efficiency와 task success | p. 3 (2) A dataset with multi-task labels to support algorithm), p. 11 (B. Motion Policy Learning), p. 11 (B. Motion Policy Learning) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** To. bridge this gap, we present REASSEMBLE (Robotic assEmbly disASSEMBLy datasEt), a 1 new dataset designed specifically for contact-rich manipalation
- **p. 2 / Abstract - extractive body cue:** By offering a rich, multi modal dataset, REASSEMBLE fosters the development of adaptive and versatile robotic systems capable of tackling the challenges of long-horizon, contact-rich ...
- **p. 2 / Abstract - extractive body cue:** ‘To bridge the gap between these pressing challenges, we introduce REASSEMBLE, a comprehensive dataset tailored to long-horizon and contact-rich manipulation tasks.
- **p. 11 / B. Motion Policy Learning - extractive body cue:** ‘The primary objective of this study is to introduce a novel robot manipulation dataset specifically designed for contactrich manipulation tasks, rather than t0 develop a ...
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** Numerous datasets have been developed to support temporal action segmentation [20], (27), [28].
- **p. 11 / V. BENCHMARKS - extractive body cue:** Preliminary results demonstrate improved performance through the integration of visual, auditory, force-torque (wrench), gripper, and pose information. ‘These findings are promising, and we plan 10 ...
- **p. 11 / V. BENCHMARKS - extractive body cue:** We hypothesize that the lower performance of DiffAct on the REASSEMBLE dataset is due to the increased challenges it presents, Firstly, the REASSEMBLE dataset contains ...
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** For instance, force-torque sensing plays a pivotal role in assembly tasks involving a NIST assembly board, where precise measurements are essential to detect and respond ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 11 (V. BENCHMARKS), p. 11 (V. BENCHMARKS) |
| Embodiment/environment | In robotic manipulation, most simulated environments and datasets primarily focus on fundamental tasks such as picking, placing, in-hand manipulation, lifting, and stacking (15), (17), [24], [25], as shown in Table I. | hardware/simulator version and reset protocol | p. 2 (2) A dataset with multi-task labels to support algorithm), p. 3 (2) A dataset with multi-task labels to support algorithm) |
| Dataset/benchmark | More formally, TAS can be defined as follows: given a dataset of N' untrimmed task demonstrations D = {d,, si }o. where d, represents a demonstration of varying length containing modalities such ... | role, split, size and leakage | p. 2 (2) A dataset with multi-task labels to support algorithm), p. 3 (2) A dataset with multi-task labels to support algorithm), p. 10 (V. BENCHMARKS), p. 2 (2) A dataset with multi-task labels to support algorithm) |
| Metric | + FI scores at 10%, 25%, and S0% overlap: Measure | definition, denominator, direction and uncertainty | p. 10 (V. BENCHMARKS), p. 10 (V. BENCHMARKS), p. 11 (V. BENCHMARKS) |
| Baseline/ablation | For benchmarking purposes, we evaluate the performance of a state-of-the-art visual TAS model, DiffAct [37]. | fair input/data/compute/action matching | p. 10 (V. BENCHMARKS), p. 11 (V. BENCHMARKS), p. 11 (V. BENCHMARKS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / dataset - extractive body cue:** ‘The majority of failures in the ition (Figure 7, top left) occur because the gripper either misses the object or the ‘object slips out of ...
- **p. 8 / dataset - extractive body cue:** failures in this action do occur if the object slips prematurely from the gripper and lands on the task board, which we classify as a ...
- **p. 7 / B. Action difficulty and failure modes - extractive body cue:** From the figure, we observe that the most difficult action in the dataset is the "Insert" action, which has the highest number of total failures ...
- **p. 4 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** (Crucially, it incorporates failure data to train models that can effectively learn to detect, understand, and respond to failures, in real time.
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** ‘and disassembly, which require stringent tolerances, demand accurate and high-resolution contact information, including force-torque data, that visual sensing alone cannot reliably ‘capture.
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** To address these limitations, REASSEMBLE introduces a novel dataset incorporating high-resolution force-torque sensing specifically tailored for tight-tolerance, high-precision, and ong-horizon tasks.
- **p. 4 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** Building ‘on these limitations, REASSEMBLE is designed to address the gaps in existing resources.

## Why Read It

Manipulation, contact, tactile, and dexterity의 robot_data 문제를 이해하기 위해 읽는다. 본문은 ‘To bridge the gap between these pressing challenges, we introduce REASSEMBLE, a comprehensive dataset tailored to long-horizon and contact-rich manipulation tasks.를 문제로 두고, To. bridge this gap, we present REASSEMBLE (Robotic assEmbly disASSEMBLy datasEt), a 1 new dataset designed specifically for contact-rich manipalation를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (Abstract), p. 3 (2) A dataset with multi-task labels to support algorithm), p. 3 (2) A dataset with multi-task labels to support algorithm), p. 2 (Abstract), p. 4 (2) A dataset with multi-task labels to support algorithm), p. 3 (2) A dataset with multi-task labels to support algorithm) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
