# π0.5: a Vision-Language-Action Model with Open-World Generalization

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v305/black25a.html.
> PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/black25a/black25a.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CoRL
- Authors: Kevin Black, Noah Brown, James Darpinian, Karan Dhabalia, Danny Driess, Adnan Esmail, Michael Robert Equi, Chelsea Finn, Niccolo Fusai, Manuel Y. Galliker, Dibya Ghosh, Lachy Groom, Karol Hausman, brian ichter, Szymon Jakubczak, Tim Jones, Liyiming Ke, Devin LeBlanc, Sergey Levine, Adrian Li-Bell, Mohith Mothukuri, Suraj Nair, Karl Pertsch, Allen Z. Ren, Lucy Xiaoyang Shi, Laura Smith, Jost Tobias Springenberg, Kyle Stachowicz, James Tanner, Quan Vuong, Homer Walke, Anna Walling, Haohuan Wang, Lili Yu, Ury Zhilinsky
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: VLA, open-world, Robotics
- Official paper: https://proceedings.mlr.press/v305/black25a.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v305/main/assets/black25a/black25a.pdf
- Code/Project: https://www.physicalintelligence.company/blog/pi05
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

π0.5는 여러 로봇의 행동, 웹 데이터, 의미 단위 하위 작업을 함께 학습해 새로운 장소에서 조작하는 능력을 평가한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab.
- **p. 1 / Abstract - extractive body cue:** While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the ...
- **p. 1 / Abstract - extractive body cue:** We describe π0.5, a new model based on π0 that uses co-training on heterogeneous tasks to enable broad generalization. π0.5 uses data from multiple robots, ...
- **p. 1 / Abstract - extractive body cue:** Our system uses a combination of cotraining and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions.
- **p. 1 / Abstract - extractive body cue:** Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled ...
- **p. 2 / 1 Introduction - extractive body cue:** A person can draw on a lifetime of experience to synthesize appropriate solutions to each of these challenges.
- **p. 1 / 1 Introduction - extractive body cue:** Open-world generalization represents one of the biggest open problems in physical intelligence, and scalable learning systems offer a path to enable such generalization, as they ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our central contribution is a system for training a highly generalizable VLA, π0.5, together with a proof of concept that generalization can emerge from this ...
- **p. 1 / Abstract - extractive body cue:** Our system uses a combination of cotraining and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions.
- **p. 2 / 1 Introduction - extractive body cue:** Given general tasks (close the cabinets, put the items in the drawer, wipe the spill, and put the dishes in the sink), the model predicts ...
- **p. 1 / Abstract - extractive body cue:** While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our system uses a combination of cotraining and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions. | image/video, language instruction, proprioception과 history | p. 1 (Abstract), p. 1 (Abstract) |
| State/latent | system, uses, combination, cotraining, hybrid, multi-modal, examples, combine, image, observations, language, commands | language-grounded task state와 action-policy context | p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/action | Instruction Low-Level Action Expert Subtask Commands Multimodal Web Data Detection In-the-wild Mobile Robot In-the-wild Static Robot In-Lab Static Robot Shirt in basket Item in drawer Q: Detect and label | continuous action, pose 또는 action chunk | p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | instruction following, task success, generalization과 latency | instruction following, task success, generalization과 latency | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 관측 영상·언어·물체 검출·하위 작업 예측·저수준 행동을 결합한 학습 예제를 구성한다.
- 훈련 장소와 다른 실제 가정에서 물체 정리처럼 여러 단계가 필요한 조작을 평가한다.

[저자 원문](https://proceedings.mlr.press/v305/black25a.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | We describe π0.5, a new model based on π0 that uses co-training on heterogeneous tasks to enable broad generalization. π0.5 uses data from multiple robots, highlevel semantic prediction, web data, and other ... | hardware/simulator version and reset protocol | p. 1 (Abstract), p. 2 (1 Introduction) |
| Dataset/benchmark | A: Chocolate Deploy in new homes out-of-the-box Fold laundry Figure 1: The π0.5 model transfers knowledge from a heterogeneous range of data sources, including other robots, high-level subtask prediction, verbal instructions, and ... | role, split, size and leakage | p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Metric | Figure 7: Evaluating language following with dif- ferent numbers of training locations. We evalu- ate language following rate and success rate for pick- ing up user-indicated items and placing them into drawers ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 24 (Figure/Table caption), p. 1 (Abstract) |
| Baseline/ablation | Figure 6: Evaluating performance with different numbers of locations. Performance over the four test tasks - "dishes in sink", "items in drawer", "laundry basket", "make bed" - improves with more training environments. ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 24 (Figure/Table caption), p. 22 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 2 Related Work - extractive body cue:** Web data (WD) does not make a significant difference, but we will see in Figures 9, 16 that it impacts object generalization and high-level performance.
- **p. 7 / 2 Related Work - extractive body cue:** As expected, the performance on indistribution objects improves more quickly than that of out-of-distribution objects.
- **p. 7 / 2 Related Work - extractive body cue:** Performance increases steadily as we increase the number of training locations. standard rubric in Appendix C and (2) a more fine-grained evaluation of each model's ...
- **p. 8 / 2 Related Work - extractive body cue:** For both experiments we see in the results that excluding either of the two cross-embodiment data sources significantly degrades performance, indicating that π0.5 benefits considerably ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 17: Per-task performance breakdown for training recipe ablations. We evaluate each training mix- ture variant on four representative household tasks: Items in Drawer, Dishes ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 A person can draw on a lifetime of experience to synthesize appropriate solutions to each of these challenges.를 문제로 두고, Our central contribution is a system for training a highly generalizable VLA, π0.5, together with a proof of concept that generalization can emerge from this model when it is trained on appropriately ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Open-world generalization represents one of the biggest open problems in physical intelligence, and scalable learning systems offer a path to enable such generalization, as they have in domains ranging from ... (p. 1, 1 Introduction).
- **Actual contribution:** Given general tasks (close the cabinets, put the items in the drawer, wipe the spill, and put the dishes in the sink), the model predicts subtasks (e.g., pick up the ... (p. 2, 1 Introduction).
- **Evaluation boundary:** Figure 18: Per-task performance breakdown for high-level inference methods. We evaluate the full π0.5 model and various high-level inference baselines across four representative household tasks. For Items in Drawer and ... (p. 24, Figure/Table caption).
- **Explicit failure boundary:** Some evaluations include cancelled episodes due to robot failures, time limitations or other causes, which are removed. (p. 20, 3 DoF holonomic base).
