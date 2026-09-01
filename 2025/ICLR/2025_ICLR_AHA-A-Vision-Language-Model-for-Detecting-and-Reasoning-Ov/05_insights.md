# Insights — AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=JVkdSi7Ekg; PDF retrieval source: https://openreview.net/pdf/baa69f167306f963174767be4974c69528aa6379.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce FailGen, a data generation pipeline for the procedural generation of failure demonstration data for robotic manipulation tasks across simulators.
- **p. 7 / 4 Method - extractive body cue:** This structured input enables consistent handling of data across different tasks and viewpoints.
- **p. 10 / 4 Method - extractive body cue:** AHA enables efficient reward synthesis for reinforcement learning.
- **p. 7 / 4 Method - extractive body cue:** To achieve this, we developed FailGen, an environment wrapper that can be easily applied to any robot manipulation simulator.
- **p. 7 / 4 Method - extractive body cue:** 2, our model architecture includes an image encoder, a linear projector, a language tokenizer, and a transformerbased language model.
- **p. 10 / 4 Method - extractive body cue:** The PRoC3S system solves tasks specified in natural language by prompting an LLM for a Language-Model Program (LMP) that generates plans, and then testing a ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 7 (4 Method), p. 10 (4 Method), p. 7 (4 Method), p. 7 (4 Method)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** While these models excel at task execution, they often face challenges in detecting and reasoning over failures-skills that are crucial for navigating dynamic and complex ...
- **p. 2 / 1 Introduction - extractive body cue:** Unlike prior work that treats failure reasoning as a binary detection problem, we frame it as a free-form reasoning task, offering deeper insights into failure ...
- **p. 1 / 1 Introduction - extractive body cue:** However, despite these advancements, key challenges remain-particularly with hallucinations, where models generate responses that deviate from truth.
- **p. 1 / 1 Introduction - extractive body cue:** Unlike humans, who can intuitively detect and adjust for such errors, these models often lack the mechanisms for recognizing their own mistakes[6, 7, 8]. ∗Equal ...
- **p. 3 / 1 Introduction - extractive body cue:** 21.4% higher than GPT-4 models, highlighting AHA's effectiveness in delivering accurate natural language failure feedback to improve task performance through error correction.
- **p. 10 / 4 Method - extractive body cue:** Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: AHA datasets for instruction-tuning. We combined the AHA dataset, our large-scale robotic manipulation failure dataset, with VQA and object detection data. By incorporating ...
- **Boundary to test:** Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, and returns any sampled plan that does not ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Figure 3: (Left) Scaling law with the AHA dataset. Scaling of effect of model performance with varying domain specific fine-tuning data. (Right) Downstream Robotic Application Performance. AHA-13B outperforms GPT-4o in reasoning about ... | p. 9 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Failure/limitation | Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, and returns any sampled plan that does not ... | p. 10 (4 Method), p. 3 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 To capture the temporal relationships within the action sequence, the input image was constructed by selecting a single frame that represents the robot's trajectory up to the current sub-task and concatenating it ...를 For the input formulation in VLMs for instruction fine-tuning and evaluation, we required a query prompt 6로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, and returns any sampled plan that does not ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, and returns any sampled plan that does not ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Lastly, we adapted a failure benchmark from the RoboFail dataset [48], which features real-world robot failures in seven UR5 robot tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 2: Quantitative Evaluation on Failure Detection and Reasoning. AHA-13B was evaluated and benchmarked against three open and three proprietary VLMs and one visual prompting baseline across three evaluation datasets. AHA-13B outperf ....
4. Report the body metric and its denominator/aggregation: Comparing the evaluated policy success rates using different failure feedback VLMs, we observed that AHA-13B provided intuitive, human-level failure reasoning that aided in modifying and improving generated dense reward functions..
5. Re-run the body-reported ablation/failure condition: Scaling of effect of model performance with varying domain specific fine-tuning data..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (4 Method), p. 10 (4 Method), p. 7 (4 Method); the primary result is directionally consistent at p. 9 (Figure/Table caption), p. 3 (Figure/Table caption), p. 10 (4 Method); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, AHA, open-source mechanism이 Table 2: Quantitative Evaluation on Failure Detection and Reasoning. AHA-13B was evaluated and benchmarked against three ... 대비 Comparing the evaluated policy success rates using different failure feedback VLMs, we observed that AHA-13B provided intuitive, human-level ...을 개선하고, Importantly, as is typical of TAMP methods, the original approach checks for a finite set of ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
