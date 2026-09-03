# Insights — Goal-VLA: Image-Generative VLMs As Object-Centric World Models Empowering Zero-Shot Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2506.23919. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize, our key contributions are: • We introduce Goal-VLA, a decoupled hierarchical framework that leverages an Image-Generative VLM as a world model to generate ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To this end, we propose a decoupled architecture that leverages the VLM as an objectcentric world model.
- **p. 3 / III. METHOD - extractive body cue:** The overall workflow of our framework is illustrated conceptually in Figure 2 and detailed procedurally in Algorithm 1.
- **p. 4 / III. METHOD - extractive body cue:** This overlay is crucial as it provides an in-context visualization of the goal, which mitigates the semantic gap and enables a more robust evaluation. • ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These models are either developed by finetuning existing Vision-Language Models (VLMs) [7]-[9]
- **p. 3 / III. METHOD - extractive body cue:** Algorithm 1 Goal-VLA Execution Framework Require: Initial observation O = (I, D), Language instruction L, Initial End-effector pose Pinit Ensure: Action sequence {a}i 1: procedure ...
- **p. 4 / III. METHOD - extractive body cue:** The Low-level Policy takes the current observation O = (I, D) and the mask M as input, then outputs a sequence of actions {a}i to ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** This generalization gap is the primary barrier hindering the practical deployment of autonomous robots in unstructured environments.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Foundation models, pre-trained on vast datasets, have emerged as a promising direction to address this challenge.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Sparse or symbolic representations, such as language descriptions and keypoints [14], [17]-[19], lack the precise geometric detail required for complex manipulation.
- **p. 2 / I. INTRODUCTION - extractive body cue:** While their architectures differ, both approaches share a common and significant challenge: their performance is contingent on massive paired instructionvision-action data.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** Reflection's Necessary: Figure 3 highlights a typical failure mode of image generation.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Failures originating from the Spatial Grounding module are the primary obstacle in several precision-demanding tasks.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Failure Cases Analysis In our real-world experiments, we observe several typical failure modes as different tasks place varying demands on each module of our framework.
- **Boundary to test:** Reflection's Necessary: Figure 3 highlights a typical failure mode of image generation.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To summarize, our key contributions are: • We introduce Goal-VLA, a decoupled hierarchical framework that leverages an Image-Generative VLM as a world model to generate goal object states, serving as the bridge ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Our method, Goal-VLA, achieves a remarkable average success rate of 59.9%, significantly outperforming all baselines across a diverse set of eight manipulation tasks. | p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Failure/limitation | Reflection's Necessary: Figure 3 highlights a typical failure mode of image generation. | p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Algorithm 1 Goal-VLA Execution Framework Require: Initial observation O = (I, D), Language instruction L, Initial End-effector pose Pinit Ensure: Action sequence {a}i 1: procedure GOAL-VLA(O, L) Stage 1: Goal State Reasoning ...를 "Place tomato in pan" Task Description Initial Image (a) Goal State Reasoning World Model Goal Image Goal Depth Synthesized Image Reflector Failure Success Depth-Anything Initial Mask Goal Mask Segmentation (b) Spatial Grounding ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Reflection's Necessary: Figure 3 highlights a typical failure mode of image generation.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To summarize, our key contributions are: • We introduce Goal-VLA, a decoupled hierarchical framework that leverages an Image-Generative VLM as a world model to generate goal object states, serving as the bridge ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Reflection's Necessary: Figure 3 highlights a typical failure mode of image generation.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Q3: Can our framework generalize across diverse environments, tasks, object categories, and robot embodiments?.
3. Compare against the body-reported baseline or a matched simpler baseline: In this section, we conduct comprehensive experiments and analyses to answer the following key questions: Q1: How well does our proposed method perform compared to existing baselines?.
4. Report the body metric and its denominator/aggregation: Our method, Goal-VLA, achieves a remarkable average success rate of 59.9%, significantly outperforming all baselines across a diverse set of eight manipulation tasks..
5. Re-run the body-reported ablation/failure condition: Fig. 4: Ablation Study. The performance of our full model ("World Model w/ Instruction & max 3 Reflection"), shown by the purple line, surpasses all ablated variants. alter non-target elements (e.g., moving ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD); the primary result is directionally consistent at p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summarize, contributions, introduce mechanism이 In this section, we conduct comprehensive experiments and analyses to answer the following key questions: Q1: ... 대비 Our method, Goal-VLA, achieves a remarkable average success rate of 59.9%, significantly outperforming all baselines across a diverse ...을 개선하고, Reflection's Necessary: Figure 3 highlights a typical failure mode of image generation. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
