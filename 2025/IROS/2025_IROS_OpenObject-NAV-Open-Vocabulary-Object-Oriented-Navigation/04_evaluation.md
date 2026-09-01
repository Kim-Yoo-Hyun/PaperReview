# Evaluation - OpenObject-NAV: Open-Vocabulary Object-Oriented Navigation Based on Dynamic Carrier-Relationship Scene Graph

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2409.18743; PDF retrieval source: https://arxiv.org/pdf/2409.18743. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 6 (1. Does the carrier-relationship scene graph (CRSG) im), p. 6 (1. Does the carrier-relationship scene graph (CRSG) im)): 4 illustrates an example of long-sequence navigation, where the efficiency of navigating to the target significantly improves as the number of navigated objects increases.

## Evaluation Body Digest

- **p. 6 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive PDF cue:** Real-World Validation We validated our algorithm using an Autolabor robot in a real scene, equipped with an industrial computer featuring an NVIDIA GeForce RTX 3080.
- **p. 3 / III. METHOD - extractive PDF cue:** St = (Lt, CRt, CTt, Ft) ∈S (6) In the initial state S0 = (L0, CR0, CT0, F0), L0 is the initial position of the ...
- **p. 4 / III. METHOD - extractive PDF cue:** Leveraging the LLM's commonsense understanding of object-carrier relationships (e.g., "a cup is unlikely to be placed on a toilet"), the LLM identifies the carrier object ...
- **p. 5 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive PDF cue:** Next, the robot is instructed to sequentially navigate to these objects in each scene.
- **p. 2 / III. METHOD - extractive PDF cue:** Additionally, T represents the number of exploration attempts the robot makes to navigate to the target object.
- **p. 2 / III. METHOD - extractive PDF cue:** Problem Definition In a daily environment, when given a navigation command, the robot queries the CRSG to determine the navigation endpoint and proceeds to the ...
- **p. 3 / III. METHOD - extractive PDF cue:** We model the exploration of a displaced object as a fixedpolicy Markov decision process (MDP) below. state space S: In the current step t, we ...
- **p. 4 / III. METHOD - extractive PDF cue:** As the robot navigates, it periodically captures RGB and depth images from the environment.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENTAL RESULTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 1. Does the carrier-relationship scene graph (CRSG) im | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4 illustrates an example of long-sequence navigation, where the efficiency of navigating to the target significantly improves as the number of navigated objects increases. | p. 5 (1. Does the carrier-relationship scene graph (CRSG) im) |
| 1. Does the carrier-relationship scene graph (CRSG) im | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report Success Rate(SR) and Success weighted by inverse Path Length (SPL) [39]. | p. 4 (1. Does the carrier-relationship scene graph (CRSG) im) |
| 1. Does the carrier-relationship scene graph (CRSG) im | EMPIRICAL / REAL-ROBOT OR HARDWARE | I, where our object query success rate averages 86% and is the highest in all three scenarios. | p. 4 (1. Does the carrier-relationship scene graph (CRSG) im) |
| 1. Does the carrier-relationship scene graph (CRSG) im | EMPIRICAL / REAL-ROBOT OR HARDWARE | Tasks SR(i) represents the success rate of correctly navigating to all i objects. | p. 5 (1. Does the carrier-relationship scene graph (CRSG) im) |
| 1. Does the carrier-relationship scene graph (CRSG) im | EMPIRICAL / REAL-ROBOT OR HARDWARE | III, our method achieves the highest SPL, followed by only-carriers LLM. | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im) |

## Dataset / Benchmark Role

- **p. 6 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive PDF cue:** Real-World Validation We validated our algorithm using an Autolabor robot in a real scene, equipped with an industrial computer featuring an NVIDIA GeForce RTX 3080.
- **p. 3 / III. METHOD - extractive PDF cue:** St = (Lt, CRt, CTt, Ft) ∈S (6) In the initial state S0 = (L0, CR0, CT0, F0), L0 is the initial position of the ...
- **p. 4 / III. METHOD - extractive PDF cue:** Leveraging the LLM's commonsense understanding of object-carrier relationships (e.g., "a cup is unlikely to be placed on a toilet"), the LLM identifies the carrier object ...
- **p. 5 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive PDF cue:** Next, the robot is instructed to sequentially navigate to these objects in each scene.
- **p. 2 / III. METHOD - extractive PDF cue:** Additionally, T represents the number of exploration attempts the robot makes to navigate to the target object.
- **p. 2 / III. METHOD - extractive PDF cue:** Problem Definition In a daily environment, when given a navigation command, the robot queries the CRSG to determine the navigation endpoint and proceeds to the ...
- **p. 3 / III. METHOD - extractive PDF cue:** We model the exploration of a displaced object as a fixedpolicy Markov decision process (MDP) below. state space S: In the current step t, we ...
- **p. 4 / III. METHOD - extractive PDF cue:** As the robot navigates, it periodically captures RGB and depth images from the environment.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. The robot executes long-sequence, multi-modal, and multi-type daily object navigation commands based on a dynamic carrier-relationship scene graph. First, it successfully navigates to ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. The OpenObject-NAV system framework consists of two main modules. The Scene Graph Construction module focuses on constructing the carrier-relationship scene graph. The Graph ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3. Static Object Query Experiment: Comparison of Target Object Query Results on the Offline Map.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4. The visualization of a long-sequence instance navigation result in scene 2 is shown, where "Point to Point" represents the shortest path navigation. for ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 5. The first figure presents the SPL results in Sec. IV-B, while the second and third figures show the results of the ablation experiments ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6. The robot queries the CRSG for the position of the red book at the chair and navigates there. It then discovers that the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Real-World Validation We validated our algorithm using an Autolabor robot in a real scene, equipped with an industrial computer featuring an NVIDIA GeForce RTX ... | embodiment, simulator version and control stack | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im), p. 3 (III. METHOD) |
| Task/environment | St = (Lt, CRt, CTt, Ft) ∈S (6) In the initial state S0 = (L0, CR0, CT0, F0), L0 is the initial position of ... | reset, timeout, object/scene variation | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (III. METHOD), p. 4 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report Success Rate(SR) and Success weighted by inverse Path Length (SPL) [39]. | definition/direction/unit from same section | p. 4 (1. Does the carrier-relationship scene graph (CRSG) im) |
| I, where our object query success rate averages 86% and is the highest in all three scenarios. | definition/direction/unit from same section | p. 4 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Tasks SR(i) represents the success rate of correctly navigating to all i objects. | definition/direction/unit from same section | p. 5 (1. Does the carrier-relationship scene graph (CRSG) im) |
| The object with the highest similarity score is selected as the target object, Otarget. | definition/direction/unit from same section | p. 3 (III. METHOD) |
| The mathematical expression for this is as follows. sim(T Fi, ˜T) = T Fi · ˜T //T Fi// //˜T// (2) Next, we select the ... | definition/direction/unit from same section | p. 3 (III. METHOD) |
| 5, the SPL for the first object is noticeably lower, while the SPL for the remaining objects shows significant improvement. | definition/direction/unit from same section | p. 5 (1. Does the carrier-relationship scene graph (CRSG) im) |
| The first figure presents the SPL results in Sec. | definition/direction/unit from same section | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im) |
| III, our method achieves the highest SPL, followed by only-carriers LLM. | definition/direction/unit from same section | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The resulting feature is then compared with the SBERT or CLIP features of each object in the CRSG S G using cosine similarity, similar ... | comparison identity and matched condition | p. 3 (III. METHOD) |
| The previously carried objects on Ocr match are then compared with Ocrd. | comparison identity and matched condition | p. 4 (III. METHOD) |
| IV-B, while the second and third figures show the results of the ablation experiments with and without CRSG updates in Sec. | comparison identity and matched condition | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Ablation Study To further investigate the role of CRSG updates in efficient navigation to everyday objects, we conducted ablation experiments on one long-sequence navigation ... | comparison identity and matched condition | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im) |
| If the input command is an image, an LLM-based image comparison is also performed. | comparison identity and matched condition | p. 4 (III. METHOD) |
| Static Object Query Experiment: Comparison of Target Object Query Results on the Offline Map. | comparison identity and matched condition | p. 5 (1. Does the carrier-relationship scene graph (CRSG) im) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| IV-B, while the second and third figures show the results of the ablation experiments with and without CRSG updates in Sec. | component/input/data sensitivity | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Ablation Study To further investigate the role of CRSG updates in efficient navigation to everyday objects, we conducted ablation experiments on one long-sequence navigation ... | component/input/data sensitivity | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Since some candidates in CTt may be carried by objects in CRobserved, CTt is updated to CTt ∗after these candidates are removed. | component/input/data sensitivity | p. 4 (III. METHOD) |
| After the comparison, the carried objects on Ocr match are updated accordingly: they are either added, removed, or left unchanged. | component/input/data sensitivity | p. 4 (III. METHOD) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We present an adaptable carrier relationship scene graph (CRSG) that primarily describes the dynamic carrier and ... | 4 illustrates an example of long-sequence navigation, where the efficiency of navigating to the target significantly improves as the number of navigated objects increases. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 6 (1. Does the carrier-relationship scene graph (CRSG) im), p. 6 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Primary metric/result | We report Success Rate(SR) and Success weighted by inverse Path Length (SPL) [39]. | numeric claim only at cited anchor | p. 4 (1. Does the carrier-relationship scene graph (CRSG) im) |

- Numeric sentences retained from the body:
- **p. 4 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive PDF cue:** A total of 50 queries with different types of navigation instructions (semantic, instance and requirementdriven) were conducted across 3 scenes in Gibson [40].
- **p. 5 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive PDF cue:** Long-sequence Navigation Task for Frequently Used Everyday Items We conducted a series of long-sequence frequently used daily items navigation experiments (4 or 5 objects as ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | If the robot fails to reach the target, the SPL score is zero. | p. 4 (1. Does the carrier-relationship scene graph (CRSG) im) |
| body limitation/failure cue | VLMap Ours ConceptGraph Result: Success Result: Success Result: Failed ---Find a chair Result: Failed ---Find yellow bottle Result: Failed ---Find chairs Task 1: black ... | p. 5 (1. Does the carrier-relationship scene graph (CRSG) im) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Real-World Validation We validated our algorithm using an Autolabor robot in a real scene, equipped with an industrial computer featuring an NVIDIA GeForce RTX ... | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Unlike ConceptGraph [19], each instance object Oi ∈O (O is the set of all objects) not only contains a CLIP feature V Fi but ... | p. 2 (III. METHOD) |
| Carrier layer: We calculate the similarity between the text features T Fi of each object Oi and the SBERT-encoded text feature ˜T for "furniture ... | p. 3 (III. METHOD) |
| Navigation Strategy for a Displaced Object Let the input navigation command for the target object be either a text, or an image. text or ... | p. 3 (III. METHOD) |
| The RGB images are processed through CropFormer [38], Tokenize Anything model [35], CLIP [22] and SBERT [36] to obtain instance masks, captions, encoded CLIP ... | p. 4 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive PDF cue:** If the robot fails to reach the target, the SPL score is zero.
- **p. 5 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive PDF cue:** VLMap Ours ConceptGraph Result: Success Result: Success Result: Failed ---Find a chair Result: Failed ---Find yellow bottle Result: Failed ---Find chairs Task 1: black bottle ...

- **PDF anchors reviewed:** datasets p. 6 (1. Does the carrier-relationship scene graph (CRSG) im), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 2 (III. METHOD), p. 2 (III. METHOD), metrics p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), baselines p. 3 (III. METHOD), p. 4 (III. METHOD), p. 6 (1. Does the carrier-relationship scene graph (CRSG) im), p. 6 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (III. METHOD), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), results p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 6 (1. Does the carrier-relationship scene graph (CRSG) im), p. 6 (1. Does the carrier-relationship scene graph (CRSG) im).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
