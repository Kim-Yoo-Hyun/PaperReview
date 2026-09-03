# Method - On Bringing Robots Home

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.16098; PDF retrieval source: https://arxiv.org/pdf/2311.16098. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (1 Introduction), p. 6 (C D), p. 6 (C D), p. 1 (Abstract), p. 1 (Abstract), p. 7 (C D)): This dataset serves to pretrain representation models for Dobb·E. • Models and algorithms: Given the pretraining dataset we train a streamlined vision model, called Home Pretrained Representations (HPR), employing cutting-edge ...

## Method Body Digest

- **p. 4 / 1 Introduction - extractive body cue:** This dataset serves to pretrain representation models for Dobb·E. • Models and algorithms: Given the pretraining dataset we train a streamlined vision model, called Home ...
- **p. 6 / C D - extractive body cue:** Behavior cloning involves training a model to mimic a demonstrated behavior or action, often through the use of labeled training data mapping observations to desired ...
- **p. 6 / C D - extractive body cue:** Our key experimental findings are: • Surprising effectiveness of simple methods: Dobb·E follows a simple behavior cloning recipe for visual imitation learning using a ResNet ...
- **p. 1 / Abstract - extractive body cue:** We use the Stick to collect 13 hours of data in 22 homes of New York City, and train Home Pretrained Representations (HPR).
- **p. 1 / Abstract - extractive body cue:** Then, in a novel home environment, with five minutes of demonstrations and fifteen minutes of adapting the HPR model, we show that Dobb·E can reliably ...
- **p. 7 / C D - extractive body cue:** a lightweight foundational vision model on a dataset of household demonstrations, and then in a new home, given a new task, we collect a handful ...
- **p. 4 / 1 Introduction - extractive body cue:** For novel tasks, a mere 24 demonstrations sufficed to finetune this vision model, incorporating both visual and depth information to account for 3D reasoning. • ...
- **p. 1 / Abstract - extractive body cue:** The concept of a "generalist machine" in homes - a domestic assistant that can adapt and learn from our needs, all while remaining cost-effective - ...

## Design Rationale

- **p. 4 / 1 Introduction - extractive body cue:** In this work we present Dobb·E, a framework for teaching robots in homes by embodying three core principles: efficiency, safety, and user comfort.
- **p. 1 / Abstract - extractive body cue:** Success 81% Pick up hat Open microwave door Pick up paper towel roll Place rag in laundry Open cabinet door Close cabinet door Open shower ...
- **p. 7 / C D - extractive body cue:** Our method can be divided into four broad stages: (a) designing a hardware setup that helps us in the collection of demonstrations and their seamless ...

## Source Evidence Cues

- **p. 4 / 1 Introduction - extractive body cue:** This dataset serves to pretrain representation models for Dobb·E. • Models and algorithms: Given the pretraining dataset we train a streamlined vision model, called Home ...
- **p. 6 / C D - extractive body cue:** Behavior cloning involves training a model to mimic a demonstrated behavior or action, often through the use of labeled training data mapping observations to desired ...
- **p. 6 / C D - extractive body cue:** Our key experimental findings are: • Surprising effectiveness of simple methods: Dobb·E follows a simple behavior cloning recipe for visual imitation learning using a ResNet ...
- **p. 1 / Abstract - extractive body cue:** We use the Stick to collect 13 hours of data in 22 homes of New York City, and train Home Pretrained Representations (HPR).
- **p. 1 / Abstract - extractive body cue:** Then, in a novel home environment, with five minutes of demonstrations and fifteen minutes of adapting the HPR model, we show that Dobb·E can reliably ...
- **p. 7 / C D - extractive body cue:** a lightweight foundational vision model on a dataset of household demonstrations, and then in a new home, given a new task, we collect a handful ...
- **p. 4 / 1 Introduction - extractive body cue:** For novel tasks, a mere 24 demonstrations sufficed to finetune this vision model, incorporating both visual and depth information to account for 3D reasoning. • ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | This dataset serves to pretrain representation models for Dobb·E. • Models and algorithms: Given the pretraining dataset we train a streamlined vision ... | p. 4 (1 Introduction), p. 6 (C D) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | Behavior cloning involves training a model to mimic a demonstrated behavior or action, often through the use of labeled training data mapping ... | p. 6 (C D), p. 6 (C D) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | Our key experimental findings are: • Surprising effectiveness of simple methods: Dobb·E follows a simple behavior cloning recipe for visual imitation learning ... | p. 6 (C D), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** The concept of a "generalist machine" in homes - a domestic assistant that can adapt and learn from our needs, all while remaining cost-effective - ...
- **p. 6 / C D - extractive body cue:** Ease of collecting demonsrations also makes iterating on research problems with the Stick much faster and easier (see Section 3.4). • Remaining challenges: Hardware constraints ...
- **p. 6 / C D - extractive body cue:** Our key experimental findings are: • Surprising effectiveness of simple methods: Dobb·E follows a simple behavior cloning recipe for visual imitation learning using a ResNet ...
- **p. 8 / C D - extractive body cue:** One of the main advantages of collecting our data using this setup is that, from the camera's point of view, the Stick gripper and the ...
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 6 (C D).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Behavior, cloning, involves, training, model, mimic, demonstrated, action, often, through, labeled, data, mapping, observations | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | Behavior, cloning, involves, training, model, mimic, demonstrated, action, often, through | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | present, Dobb, framework, teaching, robots, homes, embodying, three, core, principles | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | concept, generalist, machine, homes, domestic, assistant, adapt, learn, needs, while | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / C D - extractive body cue:** Behavior cloning involves training a model to mimic a demonstrated behavior or action, often through the use of labeled training data mapping observations to desired ...
- **p. 6 / C D - extractive body cue:** On average, only using 91 seconds of data on each task collected over five minutes, Dobb·E can achieve a 81% success rate in homes (see ...
- **p. 7 / C D - extractive body cue:** However, augmenting these controllers with force feedback is nearly impossible, often leading users to inadvertently apply extra force or torque on the robot.
- **p. 7 / C D - extractive body cue:** Generally, the hardware controller approach suffers from inefficiency because the human demonstrators have to map the controller input to the robot motion.
- **p. 1 / Abstract - extractive body cue:** In this work, we initiate a large-scale effort towards this goal by introducing Dobb·E, an affordable yet versatile general-purpose system for learning robotic manipulation within ...
- **p. 1 / Abstract - extractive body cue:** The concept of a "generalist machine" in homes - a domestic assistant that can adapt and learn from our needs, all while remaining cost-effective - ...
- **p. 4 / 1 Introduction - extractive body cue:** Our goal is to build robots that perform a wide-range of simple domestic tasks across diverse realworld households.
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | Demo Robot run: Without Shadows Robot run: With Shadows Frame Step 0 5 10 15 20 25 30 20 50 70 90 ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | 4.1 Scaling to Long Horizon Tasks We primarily focused on short-horizon tasks in this work, but intuitively, our framework should be easily ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | Turning on light switch Figure 10: A small subset of 8 robot rollouts from the 109 tasks that we tried in homes. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 1 Introduction - extractive body cue:** This dataset serves to pretrain representation models for Dobb·E. • Models and algorithms: Given the pretraining dataset we train a streamlined vision model, called Home ...
- **p. 6 / C D - extractive body cue:** Behavior cloning involves training a model to mimic a demonstrated behavior or action, often through the use of labeled training data mapping observations to desired ...
- **p. 1 / Abstract - extractive body cue:** We use the Stick to collect 13 hours of data in 22 homes of New York City, and train Home Pretrained Representations (HPR).
- **p. 7 / C D - extractive body cue:** a lightweight foundational vision model on a dataset of household demonstrations, and then in a new home, given a new task, we collect a handful ...
- **p. 18 / 3 Experiments - extractive body cue:** Demo Robot run: Without Shadows Robot run: With Shadows Frame Step 0 5 10 15 20 25 30 20 50 70 90 100 110 125 ...
- **p. 19 / 3 Experiments - extractive body cue:** A secondary problem with reflective surfaces like mirrors is that we collect demonstrations using the Stick but run the trained policies on the robot.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** dataset, serves, pretrain, representation, models, Dobb, algorithms, Given, pretraining, train, streamlined, vision, model, called, Home, Pretrained, Representations, HPR, employing, cutting-edge.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | 25 4.4 Robustifying Robot Hardware . . . . . . . . . . . . . . . . . ... | p. 3 (3 Experiments), p. 20 (3 Experiments) |
| Base-arm task decision | Alongside these household experiments, we also set up a "home" area in our lab, with a benchmark suite with 10 tasks that ... | p. 12 (3 Experiments), p. 17 (3 Experiments) |
| Execution / correction | Figure 1: We present Dobb·E, a simple framework to train robots, which is then field tested in homes across New York City. ... | p. 1 (Figure/Table caption), p. 22 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 21 / 3 Experiments - extractive body cue:** The failure modes for tasks without depth are generally concentrated around cases where the robot end-effector (and thus the camera) is very close to some ...
- **p. 21 / 3 Experiments - extractive body cue:** These ablation experiments evaluate different components of our system and how they contribute to our performance.
- **p. 12 / 3 Experiments - extractive body cue:** Alongside these household experiments, we also set up a "home" area in our lab, with a benchmark suite with 10 tasks that we use to ...
- **p. 18 / 3 Experiments - extractive body cue:** Rollout With Shadows Demo Without Shadows Figure 15: First person view from the iPhone from the (top row) Stick during demonstration collection and (bottom row) ...
- **p. 18 / 3 Experiments - extractive body cue:** Demo Robot run: Without Shadows Robot run: With Shadows Frame Step 0 5 10 15 20 25 30 20 50 70 90 100 110 125 ...
- **p. 19 / 3 Experiments - extractive body cue:** Rollout With Depth Rollout Without Depth Depth Image Demo Figure 18: Opening an outward facing window blind (top row) both without depth (second row) and ...
- **p. 20 / 3 Experiments - extractive body cue:** Knob turning, another low performing task, had 65% success rate because of the fine manipulation required: if the robot's grasp is not perfectly centered on ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (1 Introduction), p. 6 (C D), p. 6 (C D), p. 1 (Abstract), p. 1 (Abstract), p. 7 (C D), objective p. 1 (Abstract), p. 6 (C D), p. 6 (C D), p. 8 (C D), temporal p. 18 (3 Experiments), p. 23 (3 Experiments), p. 20 (3 Experiments), p. 23 (3 Experiments), p. 3 (3 Experiments), p. 15 (3 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
