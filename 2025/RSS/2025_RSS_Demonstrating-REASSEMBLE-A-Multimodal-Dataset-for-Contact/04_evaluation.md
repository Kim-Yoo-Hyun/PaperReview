# Evaluation - Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p059.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p059.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (V. BENCHMARKS), p. 11 (V. BENCHMARKS), p. 3 (2) A dataset with multi-task labels to support algorithm), p. 3 (2) A dataset with multi-task labels to support algorithm), p. 9 (Figure/Table caption), p. 10 (V. BENCHMARKS)): Preliminary results demonstrate improved performance through the integration of visual, auditory, force-torque (wrench), gripper, and pose information. ‘These findings are promising, and we plan 10 conduct a more comprehensive analysis ...

## Evaluation Body Digest

- **p. 2 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** In robotic manipulation, most simulated environments and datasets primarily focus on fundamental tasks such as picking, placing, in-hand manipulation, lifting, and stacking (15), (17), [24], ...
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** We compare several commonly used datasets based on the number of demonstrations, the number of verbs they contain, the sensors used during data collection, the ...
- **p. 10 / V. BENCHMARKS - extractive body cue:** More formally, TAS can be defined as follows: given a dataset of N' untrimmed task demonstrations D = {d,, si }o. where d, represents a ...
- **p. 2 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** 4) Introduction of the, to the best of our knowledge, first manipulation-focused dataset to include event camera data, providing low-latency and precise object and robot ...
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** For example, the 50Salads dataset is a widely used benchmark Where humans perform salad preparation tasks [20].
- **p. 10 / V. BENCHMARKS - extractive body cue:** One of our goals when developing the REASSEMBLE dataset was to include multi-task annotations t0 enable the development of robotic algorithms for addressing challenges encountered ...
- **p. 11 / V. BENCHMARKS - extractive body cue:** ‘The REASSEMBLE dataset presents new opportunities for advancing temporal action segmentation (TAS) in robotics. ‘One underexplored area is the proper fusion of multimodal data in ...
- **p. 8 / dataset - extractive body cue:** The higher failure rate for inserting objects like the Ethemet cable or USB cable arises for two reasons: first, both plugs are directional and ‘must ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 2) A dataset with multi-task labels to support algorithm (p. 2); dataset (p. 8); V. BENCHMARKS (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. BENCHMARKS | BENCHMARK / DATASET | Preliminary results demonstrate improved performance through the integration of visual, auditory, force-torque (wrench), gripper, and pose information. ‘These findings are promising, and we plan ... | p. 11 (V. BENCHMARKS) |
| V. BENCHMARKS | BENCHMARK / DATASET | We hypothesize that the lower performance of DiffAct on the REASSEMBLE dataset is due to the increased challenges it presents, Firstly, the REASSEMBLE dataset ... | p. 11 (V. BENCHMARKS) |
| 2) A dataset with multi-task labels to support algorithm | BENCHMARK / DATASET | For instance, force-torque sensing plays a pivotal role in assembly tasks involving a NIST assembly board, where precise measurements are essential to detect and ... | p. 3 (2) A dataset with multi-task labels to support algorithm) |
| 2) A dataset with multi-task labels to support algorithm | BENCHMARK / DATASET | ‘The increasing prevalence of automation in robotic manipulation tasks highlights the necessity of effective skill assess- ‘ment, task monitoring, and summarization to enhance system ... | p. 3 (2) A dataset with multi-task labels to support algorithm) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 7: Number of successful and unsuccessful demonstrations for success of each action demonstration. This can serve as a proxy for the the highest ... | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 2 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** In robotic manipulation, most simulated environments and datasets primarily focus on fundamental tasks such as picking, placing, in-hand manipulation, lifting, and stacking (15), (17), [24], ...
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** We compare several commonly used datasets based on the number of demonstrations, the number of verbs they contain, the sensors used during data collection, the ...
- **p. 10 / V. BENCHMARKS - extractive body cue:** More formally, TAS can be defined as follows: given a dataset of N' untrimmed task demonstrations D = {d,, si }o. where d, represents a ...
- **p. 2 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** 4) Introduction of the, to the best of our knowledge, first manipulation-focused dataset to include event camera data, providing low-latency and precise object and robot ...
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** For example, the 50Salads dataset is a widely used benchmark Where humans perform salad preparation tasks [20].
- **p. 10 / V. BENCHMARKS - extractive body cue:** One of our goals when developing the REASSEMBLE dataset was to include multi-task annotations t0 enable the development of robotic algorithms for addressing challenges encountered ...
- **p. 11 / V. BENCHMARKS - extractive body cue:** ‘The REASSEMBLE dataset presents new opportunities for advancing temporal action segmentation (TAS) in robotics. ‘One underexplored area is the proper fusion of multimodal data in ...
- **p. 8 / dataset - extractive body cue:** The higher failure rate for inserting objects like the Ethemet cable or USB cable arises for two reasons: first, both plugs are directional and ‘must ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of the REASSEMBLE dataset, In REASSEMBLE, we focus on cteating a dataset for contact-rich manipulation tasks. We leverage the well-established NIST Assembly ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of the sensor placement. We use two external and fone wrist-mounted RGB cameras (marked in orange). Additionally, We use an externally mounted ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Visualization of event camera data. In this example, @ pee becomes stuck after insertion, and the robot applies a midge 10 properly insert ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. The haptic feedback allows the operator to perceive the robot's interaction forces with the environment, enabling them to adjust the motion accordingly.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Overview of the teleoperation control system. The operator controls the robot's motion through the haptic device, which simul- taneously feeds back forces measured ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Sankey diagram showing the hierarchical structure and how skills are distributed within actions. The REASSEMBLE dataset contains 121 unique skll-object pairs.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Number of demonstrations of each action-object pair. n REASSEMBLE, we have 4 actions: pick, insert, remove, and place, and 17 objects, resulting in ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Number of successful and unsuccessful demonstrations for success of each action demonstration. This can serve as a proxy for the the highest precision ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In robotic manipulation, most simulated environments and datasets primarily focus on fundamental tasks such as picking, placing, in-hand manipulation, lifting, and stacking (15), (17), ... | embodiment, simulator version and control stack | p. 2 (2) A dataset with multi-task labels to support algorithm), p. 3 (2) A dataset with multi-task labels to support algorithm) |
| Task/environment | We compare several commonly used datasets based on the number of demonstrations, the number of verbs they contain, the sensors used during data collection, ... | reset, timeout, object/scene variation | p. 3 (2) A dataset with multi-task labels to support algorithm), p. 10 (V. BENCHMARKS) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 4 (B. Sensors), p. 1 (1 Seraies) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 2 (2) A dataset with multi-task labels to support algorithm), p. 2 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| + FI scores at 10%, 25%, and S0% overlap: Measure | definition/direction/unit from same section | p. 10 (V. BENCHMARKS) |
| + Frame-evel accuracy: Measures the proportion of cor rectly annotated frames relative to the total number of frames. | definition/direction/unit from same section | p. 10 (V. BENCHMARKS) |
| the precision and recall of action segments, with the overlap indicating the required temporal overlap between, predicted and ground truth segments for them to ... | definition/direction/unit from same section | p. 11 (V. BENCHMARKS) |
| Preliminary results demonstrate improved performance through the integration of visual, auditory, force-torque (wrench), gripper, and pose information. ‘These findings are promising, and we plan ... | definition/direction/unit from same section | p. 11 (V. BENCHMARKS) |
| For instance, force-torque sensing plays a pivotal role in assembly tasks involving a NIST assembly board, where precise measurements are essential to detect and ... | definition/direction/unit from same section | p. 3 (2) A dataset with multi-task labels to support algorithm) |
| Fig. 7: Number of successful and unsuccessful demonstrations for success of each action demonstration. This can serve as a proxy for the the highest ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Fig. 1: Overview of the REASSEMBLE dataset, In REASSEMBLE, we focus on cteating a dataset for contact-rich manipulation tasks. We leverage the well-established NIST ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| ‘and disassembly, which require stringent tolerances, demand accurate and high-resolution contact information, including force-torque data, that visual sensing alone cannot reliably ‘capture. | definition/direction/unit from same section | p. 3 (2) A dataset with multi-task labels to support algorithm) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For benchmarking purposes, we evaluate the performance of a state-of-the-art visual TAS model, DiffAct [37]. | comparison identity and matched condition | p. 10 (V. BENCHMARKS) |
| Additionally, the REASSEMBLE dataset has almost twice the median number of actions per video (36 compared 10 19 in SOSalads). | comparison identity and matched condition | p. 11 (V. BENCHMARKS) |
| We hypothesize that the lower performance of DiffAct on the REASSEMBLE dataset is due to the increased challenges it presents, Firstly, the REASSEMBLE dataset ... | comparison identity and matched condition | p. 11 (V. BENCHMARKS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Failures in the "Remove" action (Figure 7, bottom left) often result from improper alignment of the gripper with the object during removal, causing the ... | component/input/data sensitivity | p. 8 (dataset) |
| Fig. 6: Number of demonstrations of each action-object pair. n REASSEMBLE, we have 4 actions: pick, insert, remove, and place, and 17 objects, resulting ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Diffusion processes work by progressively adding noise to the ground truth information and learning how t0 iteratively remove this noise. | component/input/data sensitivity | p. 10 (V. BENCHMARKS) |
| Furthermore, REASSEMBLE often includes sequences where very long actions (e.g., Insert and Remove) are separated by very short actions (eg., Pick and Place). | component/input/data sensitivity | p. 11 (V. BENCHMARKS) |
| Fig. 11: Large Gear assembly & disassembly The figure illustrates the trajectories generated by the DMP framework for robotic assembly and disassembly of the ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To. bridge this gap, we present REASSEMBLE (Robotic assEmbly disASSEMBLy datasEt), a 1 new dataset designed specifically for contact-rich manipalation | Preliminary results demonstrate improved performance through the integration of visual, auditory, force-torque (wrench), gripper, and pose information. ‘These findings are promising, and we plan ... | PDF body cue; verify exact table/figure and matched conditions | p. 11 (V. BENCHMARKS), p. 11 (V. BENCHMARKS), p. 3 (2) A dataset with multi-task labels to support algorithm), p. 3 (2) A dataset with multi-task labels to support algorithm), p. 9 (Figure/Table caption), p. 10 (V. BENCHMARKS) |
| Primary metric/result | We hypothesize that the lower performance of DiffAct on the REASSEMBLE dataset is due to the increased challenges it presents, Firstly, the REASSEMBLE dataset ... | numeric claim only at cited anchor | p. 11 (V. BENCHMARKS) |

- Numeric sentences retained from the body:
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** (1S) 601k 14 4-RGB Cameras / Dep Widow VR tcleoperation MPL Camera, Robot" Proprio= ception RoboSet 98Sk 1s STRGHD Comers, Robot Franks Emika Pands Kinestheic, ...
- **p. 10 / V. BENCHMARKS - extractive body cue:** The video is downsampled from 30 to 10 frames per second to reduce computational time.
- **p. 10 / V. BENCHMARKS - extractive body cue:** We extract the visual features in windows of 21 frames, and with 4 stride of 1, resulting in one feature for each corresponding frame in ...
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** (1S) 601k 14 4-RGB Cameras / Dep Widow VR tcleoperation MPL Camera, Robot" Proprio= ception RoboSet 98Sk 1s STRGHD Comers, Robot Franks Emika Pands Kinestheic, ...
- **p. 8 / B. Action difficulty and failure modes - extractive body cue:** 6: Number of demonstrations of each action-object pair. n REASSEMBLE, we have 4 actions: pick, insert, remove, and place, and 17 objects, resulting in 68 ...
- **p. 12 / B. Motion Policy Learning - extractive body cue:** The pick action was successfully executed in 8 out of 10 trials, with failures occurring due to the gear slipping from the gripper.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | ‘The majority of failures in the ition (Figure 7, top left) occur because the gripper either misses the object or the ‘object slips out ... | p. 8 (dataset) |
| body limitation/failure cue | failures in this action do occur if the object slips prematurely from the gripper and lands on the task board, which we classify as ... | p. 8 (dataset) |
| body limitation/failure cue | From the figure, we observe that the most difficult action in the dataset is the "Insert" action, which has the highest number of total ... | p. 7 (B. Action difficulty and failure modes) |
| body limitation/failure cue | (Crucially, it incorporates failure data to train models that can effectively learn to detect, understand, and respond to failures, in real time. | p. 4 (2) A dataset with multi-task labels to support algorithm) |
| body limitation/failure cue | ‘and disassembly, which require stringent tolerances, demand accurate and high-resolution contact information, including force-torque data, that visual sensing alone cannot reliably ‘capture. | p. 3 (2) A dataset with multi-task labels to support algorithm) |
| body limitation/failure cue | To address these limitations, REASSEMBLE introduces a novel dataset incorporating high-resolution force-torque sensing specifically tailored for tight-tolerance, high-precision, and ong-horizon tasks. | p. 3 (2) A dataset with multi-task labels to support algorithm) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| involves multiple steps: approaching the target, executing a search pattern to align the object with its socket, and finally applying downward force to insert ... | p. 8 (dataset) |
| To ensure high diversity in the collected data, we instructed the operator t0 randomize the board and object poses for each trial during data ... | p. 8 (C. Interaction point diversity) |
| To analyze the temporal evolution of each action, we normalize all demonstrations by their duration and compute the average wrench profile over the action ... | p. 10 (C. Interaction point diversity) |
| In the computer vision community, ‘TAS is typically posed as a supervised learning problem [37], Where the model is trained using both data and ... | p. 10 (V. BENCHMARKS) |
| The place motion was successful in all trials. | p. 12 (B. Motion Policy Learning) |
| The pick action was successfully executed in 8 out of 10 trials, with failures occurring due to the gear slipping from the gripper. | p. 12 (B. Motion Policy Learning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / dataset - extractive body cue:** ‘The majority of failures in the ition (Figure 7, top left) occur because the gripper either misses the object or the ‘object slips out of ...
- **p. 8 / dataset - extractive body cue:** failures in this action do occur if the object slips prematurely from the gripper and lands on the task board, which we classify as a ...
- **p. 7 / B. Action difficulty and failure modes - extractive body cue:** From the figure, we observe that the most difficult action in the dataset is the "Insert" action, which has the highest number of total failures ...
- **p. 4 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** (Crucially, it incorporates failure data to train models that can effectively learn to detect, understand, and respond to failures, in real time.
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** ‘and disassembly, which require stringent tolerances, demand accurate and high-resolution contact information, including force-torque data, that visual sensing alone cannot reliably ‘capture.
- **p. 3 / 2) A dataset with multi-task labels to support algorithm - extractive body cue:** To address these limitations, REASSEMBLE introduces a novel dataset incorporating high-resolution force-torque sensing specifically tailored for tight-tolerance, high-precision, and ong-horizon tasks.

- **Evidence anchors reviewed:** datasets p. 2 (2) A dataset with multi-task labels to support algorithm), p. 3 (2) A dataset with multi-task labels to support algorithm), p. 10 (V. BENCHMARKS), p. 2 (2) A dataset with multi-task labels to support algorithm), p. 3 (2) A dataset with multi-task labels to support algorithm), p. 10 (V. BENCHMARKS), metrics p. 10 (V. BENCHMARKS), p. 10 (V. BENCHMARKS), p. 11 (V. BENCHMARKS), p. 11 (V. BENCHMARKS), p. 3 (2) A dataset with multi-task labels to support algorithm), p. 9 (Figure/Table caption), baselines p. 10 (V. BENCHMARKS), p. 11 (V. BENCHMARKS), p. 11 (V. BENCHMARKS), results p. 11 (V. BENCHMARKS), p. 11 (V. BENCHMARKS), p. 3 (2) A dataset with multi-task labels to support algorithm), p. 3 (2) A dataset with multi-task labels to support algorithm), p. 9 (Figure/Table caption), p. 10 (V. BENCHMARKS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Preliminary results demonstrate improved performance through the integration of visual, auditory, force-torque (wrench), gripper, and pose information. ‘These findings are promising, and we plan 10 conduct a more comprehensive analysis ... (p. 11, V. BENCHMARKS).
- **Metric evidence:** + FI scores at 10%, 25%, and S0% overlap: Measure (p. 10, V. BENCHMARKS).
- **Baseline/ablation evidence:** For benchmarking purposes, we evaluate the performance of a state-of-the-art visual TAS model, DiffAct [37]. (p. 10, V. BENCHMARKS).
- **Failure/negative evidence:** ‘The number of failed demonstrations per action can serve as ‘4 metric for task difficulty, as operators are more likely to fail ‘when the motion is complex. (p. 7, B. Action difficulty and failure modes).
