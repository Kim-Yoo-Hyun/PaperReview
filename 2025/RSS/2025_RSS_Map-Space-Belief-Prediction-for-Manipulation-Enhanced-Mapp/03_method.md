# Method - Map Space Belief Prediction for Manipulation-Enhanced Mapping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p039.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p039.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 13 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details), p. 13 (B. CNABU Implementation Details), p. 2 (A. Next Best Viewpoint Planning), p. 15 (B. CNABU Implementation Details)): Ultimately, we learn om = om (A, RobotOccupancy (04 (t.)), RobotOccupancy (a (te))) ‘We use network architectures Similar to Georgakis et al.

## Method Body Digest

- **p. 13 / B. CNABU Implementation Details - extractive body cue:** Ultimately, we learn om = om (A, RobotOccupancy (04 (t.)), RobotOccupancy (a (te))) ‘We use network architectures Similar to Georgakis et al.
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** To evaluate the performance of the trained CNABUs, we use the unseen test set of the dataset used for their training.
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** The dataset for training o,, consists of 30,000 randomly sampled scenes, while the dataset for training a, consists of 11.700 pushes.
- **p. 13 / B. CNABU Implementation Details - extractive body cue:** Each CNABU implements a preprocessing step to encode actions and observations in a representation aligned to the ‘map grid.
- **p. 2 / A. Next Best Viewpoint Planning - extractive body cue:** In this work, we build upon existing concepts of BV planing, but enhance them by incorporating manipulation actions to interactively shape and explore the environment, ...
- **p. 15 / B. CNABU Implementation Details - extractive body cue:** Summary of baseline features We summarize the considered baselines in ‘Tab.
- **p. 15 / B. CNABU Implementation Details - extractive body cue:** pringles cans, milk cartons and cans. ‘They also differ from the geometries used during training.
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** ‘The networks are trained using backpropagation in PyTorch [32], with grid search-optimized learning rates and ADAM ‘optimizer, as well as early stopping based on the ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** Therefore, we propose Calibrated Neural-Accelerated Belief Updates (CNABUs) to learn a belief propagation model that generalizes to novel scenarios and provides confidence: calibrated predictions for ...
- **p. 2 / 2. The proticted elit map is visualized - extractive body cue:** An implementation of our method can be found on Github!.
- **p. 2 / A. Next Best Viewpoint Planning - extractive body cue:** Generally, NBV consists of two steps: First sampling view candidates, then evaluating which candidate is the best.

## Source Evidence Cues

- **p. 13 / B. CNABU Implementation Details - extractive body cue:** Ultimately, we learn om = om (A, RobotOccupancy (04 (t.)), RobotOccupancy (a (te))) ‘We use network architectures Similar to Georgakis et al.
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** To evaluate the performance of the trained CNABUs, we use the unseen test set of the dataset used for their training.
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** The dataset for training o,, consists of 30,000 randomly sampled scenes, while the dataset for training a, consists of 11.700 pushes.
- **p. 13 / B. CNABU Implementation Details - extractive body cue:** Each CNABU implements a preprocessing step to encode actions and observations in a representation aligned to the ‘map grid.
- **p. 2 / A. Next Best Viewpoint Planning - extractive body cue:** In this work, we build upon existing concepts of BV planing, but enhance them by incorporating manipulation actions to interactively shape and explore the environment, ...
- **p. 15 / B. CNABU Implementation Details - extractive body cue:** Summary of baseline features We summarize the considered baselines in ‘Tab.
- **p. 15 / B. CNABU Implementation Details - extractive body cue:** pringles cans, milk cartons and cans. ‘They also differ from the geometries used during training.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Ultimately, we learn om = om (A, RobotOccupancy (04 (t.)), RobotOccupancy (a (te))) ‘We use network architectures Similar to Georgakis et al. | p. 13 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | To evaluate the performance of the trained CNABUs, we use the unseen test set of the dataset used for their training. | p. 14 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The dataset for training o,, consists of 30,000 randomly sampled scenes, while the dataset for training a, consists of 11.700 pushes. | p. 14 (B. CNABU Implementation Details), p. 13 (B. CNABU Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 14 / B. CNABU Implementation Details - extractive body cue:** ‘The networks are trained using backpropagation in PyTorch [32], with grid search-optimized learning rates and ADAM ‘optimizer, as well as early stopping based on the ...
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** Their losses and training are described in Sec.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 14 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | solve, POMDP, agent, should, perform, belief, update, about, state, after, manipulation, observation, actions, task | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | solve, POMDP, agent, should, perform, belief, update, about, state, after | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Therefore, Calibrated, Neural-Accelerated, Belief, Updates, CNABUs, learn, propagation, model, generalizes | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | networks, trained, backpropagation, PyTorch, grid, search-optimized, learning, rates, ADAM, optimizer | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / A. Overview - extractive body cue:** To solve this POMDP, the agent should perform a belief update about the state of the map after both manipulation and observation actions.
- **p. 3 / B. Mechanical Search in Shelves and Piles - extractive body cue:** The task is to ‘output the most informative sequence of actions ¢ such that the robot's predicted map or. at the last step of the ...
- **p. 4 / B. Neural Map Belief Dynamics - extractive body cue:** The fist, called observation CNABU, computes a map belief update after a observation action Boy ag('bs, na).
- **p. 13 / B. CNABU Implementation Details - extractive body cue:** Each CNABU implements a preprocessing step to encode actions and observations in a representation aligned to the ‘map grid.
- **p. 2 / A. Next Best Viewpoint Planning - extractive body cue:** In this work, we build upon existing concepts of BV planing, but enhance them by incorporating manipulation actions to interactively shape and explore the environment, ...
- **p. 4 / B. Neural Map Belief Dynamics - extractive body cue:** ‘obusinable Uyough a manipulation action followed by an observation action
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** Consider now a greedy clairvoyant oracle policy, which, at every time step, has access to all possible observations that could be taken and selects the ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Consider now a greedy clairvoyant oracle policy, which, at every time step, has access to all possible observations that could be taken ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | For evaluating the performance of the manipulation CNABU. om, we also choose 10 viewpoints at random and ‘obtain the pre-manipulation beliefs at ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | For each model, we report the total quantity of each detection at time step 20 summed over all 10 trials, Results in ... | hardware, batch and throughput |

## Training vs Inference

- **p. 14 / B. CNABU Implementation Details - extractive body cue:** To evaluate the performance of the trained CNABUs, we use the unseen test set of the dataset used for their training.
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** The dataset for training o,, consists of 30,000 randomly sampled scenes, while the dataset for training a, consists of 11.700 pushes.
- **p. 15 / B. CNABU Implementation Details - extractive body cue:** pringles cans, milk cartons and cans. ‘They also differ from the geometries used during training.
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** ‘The networks are trained using backpropagation in PyTorch [32], with grid search-optimized learning rates and ADAM ‘optimizer, as well as early stopping based on the ...
- **p. 7 / B. Simulation Experiments - extractive body cue:** and fine-tuned the network weights provided by the authors for only 5,000 action steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Ultimately, learn, RobotOccupancy, network, architectures, Similar, Georgakis, evaluate, performance, trained, CNABUs, unseen, test, dataset, training, consists, randomly, sampled, scenes, while.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | The dataset for training o,, consists of 30,000 randomly sampled scenes, while the dataset for training a, consists of 11.700 pushes. | p. 14 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details) |
| Global / local decision | We perform four core experiments to evaluate our approach, First, we test in simulation to highlight our pipeline's improvements in map completeness ... | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Motion execution / recovery | The mfoU serves as a measure of the correctness of the predicitons, while the mECE measures the confidence calibration of these predictions, ... | p. 14 (B. CNABU Implementation Details), p. 8 (B. Simulation Experiments) |

## Failure and Ablation Link

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Next, we present a series of ablations of our method and evaluate several interactive baselines.
- **p. 7 / B. Simulation Experiments - extractive body cue:** We also compare an ablation of our pipeline that does not use manipulation, Ours ‘wo pushing.
- **p. 7 / B. Simulation Experiments - extractive body cue:** "Moreover, we observe that belief prediction is a powerful approach, leading to excellent scene coverage in low occlusion scenes even without pushing, In highly occhided ...
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** Consider the pure ‘Viewpoint Planning task, i, we must survey the environment without manipulating it, which is a submodular optimization.
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** We compare our agent without pushing to this privileged information agent in the high-occlusion set of scenes and report the resulting ‘mean map occupancy entropies ...
- **p. 9 / VI. LIMITATIONS - extractive body cue:** Limitations of our method include the need for represen: tative simulation training data or ground truth segmented maps, It also relies on high-quality semantic segmentation, ...
- **p. 7 / B. Simulation Experiments - extractive body cue:** We generate 100 low occlusion scenarios via rejection sampling, using our sampling method described in Appendix A, but keeping only scenarios for which at least ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 13 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details), p. 13 (B. CNABU Implementation Details), p. 2 (A. Next Best Viewpoint Planning), p. 15 (B. CNABU Implementation Details), objective p. 14 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details), temporal p. 14 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details), p. 4 (B. Neural Map Belief Dynamics), p. 6 (B. Neural Map Belief Dynamics), p. 9 (C. Push Selection Alternatives), p. 2 (2. The proticted elit map is visualized).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
