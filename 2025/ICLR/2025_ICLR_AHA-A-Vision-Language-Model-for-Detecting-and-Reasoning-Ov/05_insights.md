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

- **Paper-specific interface:** 4.1 Failure Reasoning Formulation Unlike previous works [48, 28, 22] that primarily focus on detecting task success as binary classification problem, we approach failure reasoning by first predicting a binary ... (p. 6, 4 Method).
- **Paper-specific mechanism:** We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation. (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is Table 2: Quantitative Evaluation on Failure Detection and Reasoning. AHA-13B was evaluated and benchmarked against three open and three proprietary VLMs and one visual prompting baseline across three evaluation datasets. ... (p. 8, Figure/Table caption); the relevant task/metric cue is Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As an instruction-tuned VLM, it can enhance task performance in robotic applications that ... (p. 3, Figure/Table caption). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, and returns any sampled plan that ... (p. 10, 4 Method).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, and returns any sampled plan that does not ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 4.1 Failure Reasoning Formulation Unlike previous works [48, 28, 22] that primarily focus on detecting task success as binary classification problem, we approach failure reasoning by first predicting a binary ... (p. 6, 4 Method); preserve the objective/update rule: To systematically assess the reasoning capabilities of different VLMs under budget constraints, we sampled one reward function initially and allowed for iterations over two sessions of GPT API calls. (p. 10, 4 Method).
2. Use the paper-reported task/data/environment cue: Lastly, we adapted a failure benchmark from the RoboFail dataset [48], which features real-world robot failures in seven UR5 robot tasks. (p. 8, 4 Method).
3. Compare against the reported or matched baseline: Table 2: Quantitative Evaluation on Failure Detection and Reasoning. AHA-13B was evaluated and benchmarked against three open and three proprietary VLMs and one visual prompting baseline across three evaluation datasets. ... (p. 8, Figure/Table caption).
4. Report the body metric with its denominator and aggregation: Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As an instruction-tuned VLM, it can enhance task performance in robotic applications that ... (p. 3, Figure/Table caption).
5. Re-run the reported ablation or stress/failure condition: The first dataset, AHA dataset (Test), includes 11k image-question pairs from 10 RLBench tasks, generated similarly to the fine-tuning data via FailGen (Section 3.2) but without overlapping with the tasks ... (p. 8, 4 Method); if none is reported, design one around: Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, and returns any sampled plan that ... (p. 10, 4 Method).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 3 (Figure/Table caption), and measure the boundary at p. 10 (4 Method), p. 1 (Abstract).

## Falsifiable research question

Under the paper's stated interface (4.1 Failure Reasoning Formulation Unlike previous works [48, 28, 22] that primarily focus on detecting task success as binary classification problem, we ...), does the paper-specific mechanism (We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation.) retain the reported evaluation outcome (Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As ...) when tested against the paper's strongest explicit boundary (Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation. (p. 2, 1 Introduction).
- **Paper-supported outcome:** Table 2: Quantitative Evaluation on Failure Detection and Reasoning. AHA-13B was evaluated and benchmarked against three open and three proprietary VLMs and one visual prompting baseline across three evaluation datasets. ... (p. 8, Figure/Table caption).
- **Strongest explicit boundary:** Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, and returns any sampled plan that ... (p. 10, 4 Method).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
