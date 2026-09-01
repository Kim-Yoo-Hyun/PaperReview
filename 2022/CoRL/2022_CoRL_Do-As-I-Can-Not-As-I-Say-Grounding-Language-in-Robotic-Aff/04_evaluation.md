# Evaluation - Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (34 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2204.01691; PDF retrieval source: https://arxiv.org/pdf/2204.01691. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (5.1 Results), p. 10 (5.1 Results), p. 8 (5.1 Results), p. 8 (5.1 Results)): Table 2: Success rates of instructions by family. PaLM-SayCan achieves a planning success rate of 84% and execution success rate of 74% in the training environment and 81% planning and ...

## Evaluation Body Digest

- **p. 7 / 5.1 Results - extractive PDF cue:** The robot interacts with a large portion of the kitchen environment and successfully performs sequences of manipulation and navigation skills.
- **p. 7 / 5.1 Results - extractive PDF cue:** These tasks require PaLMSayCan to plan many steps without error and for the robot to navigate and interact with a significant portion of the kitchen.
- **p. 8 / 5.1 Results - extractive PDF cue:** This requires long-horizon reasoning over a required order, an abstract understanding of the instruction, and knowledge of both the environment and robot's capabilities.
- **p. 11 / 5.1 Results - extractive PDF cue:** The environment is shown in Figure 8 and is a tabletop with a UR5 robot and randomly generated sets of colored blocks and bowls.
- **p. 11 / 5.1 Results - extractive PDF cue:** Step 1. pick up the blue block and place it in the blue bowl Step 2. pick up the green block and place it in ...
- **p. 8 / 5.1 Results - extractive PDF cue:** We have shown that PaLM-SayCan responds "I would: 1. find a sponge, 2. pick up the sponge, 3. bring it to you, 4. done" and ...
- **p. 9 / 5.1 Results - extractive PDF cue:** Though FLAN was fine-tuned on instruction answering, the broader and improved dataset for PaLM may make up for this difference in training.
- **p. 9 / 5.1 Results - extractive PDF cue:** This result indicates a potential future where the fields of language processing and robotics can collaboratively improve each other and scale together.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5.1 Results (p. 7); C.3 RL and BC Policy Evaluations (p. 21).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2: Success rates of instructions by family. PaLM-SayCan achieves a planning success rate of 84% and execution success rate of 74% in the ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3: Success rates of instructions by family. SayCan achieves a planning success rate of 84% and execution success rate of 74% with PaLM ... | p. 9 (Figure/Table caption) |
| 5.1 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the mock kitchen, PaLMSayCan achieved a planning success rate of 84% and an execution rate of 74%. | p. 7 (5.1 Results) |
| 5.1 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 8, and there is almost no performance drop in planning success rate when changing the queries from English to Chinese, French and Spanish. | p. 10 (5.1 Results) |
| 5.1 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results in Table 2 illustrate the necessity of the language grounding where BC NL achieves 0% in all tasks and BC USE achieves ... | p. 8 (5.1 Results) |

## Dataset / Benchmark Role

- **p. 7 / 5.1 Results - extractive PDF cue:** The robot interacts with a large portion of the kitchen environment and successfully performs sequences of manipulation and navigation skills.
- **p. 7 / 5.1 Results - extractive PDF cue:** These tasks require PaLMSayCan to plan many steps without error and for the robot to navigate and interact with a significant portion of the kitchen.
- **p. 8 / 5.1 Results - extractive PDF cue:** This requires long-horizon reasoning over a required order, an abstract understanding of the instruction, and knowledge of both the environment and robot's capabilities.
- **p. 11 / 5.1 Results - extractive PDF cue:** The environment is shown in Figure 8 and is a tabletop with a UR5 robot and randomly generated sets of colored blocks and bowls.
- **p. 11 / 5.1 Results - extractive PDF cue:** Step 1. pick up the blue block and place it in the blue bowl Step 2. pick up the green block and place it in ...
- **p. 8 / 5.1 Results - extractive PDF cue:** We have shown that PaLM-SayCan responds "I would: 1. find a sponge, 2. pick up the sponge, 3. bring it to you, 4. done" and ...
- **p. 9 / 5.1 Results - extractive PDF cue:** Though FLAN was fine-tuned on instruction answering, the broader and improved dataset for PaLM may make up for this difference in training.
- **p. 9 / 5.1 Results - extractive PDF cue:** This result indicates a potential future where the fields of language processing and robotics can collaboratively improve each other and scale together.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: LLMs have not interacted with their environment and observed the outcome of their responses, and thus are not grounded in the world. SayCan ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: A value function module (a) is queried to form a value function space of action primitives based on the current observation. Visualizing "pick" ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Given a high-level instruction, SayCan combines probabilities from a LLM (the probability that a skill is useful for the instruction) with the prob
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: The experiments were performed in an office kitchen and a mock kitchen mirroring this setup, with 5 locations and 15 objects. The robot ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: List of instruction family definitions: We evaluate the algorithm on 101 instructions. We group the instructions into different families, with each family focusing ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Timelapse of rollouts to two long-horizon queries. The robot interacts with a large portion of the kitchen environment and successfully performs sequences of ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 16. We believe such real-time and clear interpretability opens avenues to more interactive operation. 7
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: Visualization of PaLM-SayCan's decision making, where the top combined score chooses the correct skill. When comparing the performance of different instruction families in ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The robot interacts with a large portion of the kitchen environment and successfully performs sequences of manipulation and navigation skills. | embodiment, simulator version and control stack | p. 7 (5.1 Results), p. 7 (5.1 Results) |
| Task/environment | These tasks require PaLMSayCan to plan many steps without error and for the robot to navigate and interact with a significant portion of the ... | reset, timeout, object/scene variation | p. 7 (5.1 Results), p. 8 (5.1 Results) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (2 Preliminaries), p. 3 (2 Preliminaries) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (2 Preliminaries), p. 6 (2 Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2: Success rates of instructions by family. PaLM-SayCan achieves a planning success rate of 84% and execution success rate of 74% in the ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 16: Failure cases. The planning success rate was 84%. Of the errors, 65% were a result of an LLM error and 35% were ... | definition/direction/unit from same section | p. 33 (Figure/Table caption) |
| While it is expected that the generative performance of the language model will improve with better language models, it is unclear how the LLM ... | definition/direction/unit from same section | p. 9 (5.1 Results) |
| 8, and there is almost no performance drop in planning success rate when changing the queries from English to Chinese, French and Spanish. | definition/direction/unit from same section | p. 10 (5.1 Results) |
| In the mock kitchen, PaLMSayCan achieved a planning success rate of 84% and an execution rate of 74%. | definition/direction/unit from same section | p. 7 (5.1 Results) |
| The No VF and Generative approaches performed similarly, achieving 67% and 74% planning success rate respectively, and worse than PaLM-SayCan's 84%. | definition/direction/unit from same section | p. 8 (5.1 Results) |
| Figure 10: Network architecture in BC policy sampled proportionally to their priority, defined as 1 + 10 · /p -0.5/, where p is the ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Table 7: Plan and execution success rate of drawer tasks E.4 Chain of Thought Reasoning Here we show the chain of thought prompt that ... | definition/direction/unit from same section | p. 29 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We also find that PaLM outperforms FLAN. | comparison identity and matched condition | p. 9 (5.1 Results) |
| The results show that the system using PaLM with affordance grounding (PaLM-SayCan) chooses the correct sequence of skills 84% of the time and executes ... | comparison identity and matched condition | p. 9 (5.1 Results) |
| Table 6: Ablations over the size of the LLM. Compared only with the generative outputs (no value function) with USE embeddings [15]. Listing 2: ... | comparison identity and matched condition | p. 29 (Figure/Table caption) |
| These tasks require PaLMSayCan to plan many steps without error and for the robot to navigate and interact with a significant portion of the ... | comparison identity and matched condition | p. 7 (5.1 Results) |
| To study the importance of the LLM, we conduct two ablation experiments using the language-conditioned policy (see Sections 4-4). | comparison identity and matched condition | p. 8 (5.1 Results) |
| Human: Can you bring a fruit-flavored drink without caffeine? | comparison identity and matched condition | p. 10 (5.1 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| These tasks require PaLMSayCan to plan many steps without error and for the robot to navigate and interact with a significant portion of the ... | component/input/data sensitivity | p. 7 (5.1 Results) |
| To study the importance of the LLM, we conduct two ablation experiments using the language-conditioned policy (see Sections 4-4). | component/input/data sensitivity | p. 8 (5.1 Results) |
| We compare PaLM-SayCan to (1) No VF, which removes the value function grounding (i.e., choosing the maximum language score skill) and to (2) Generative, ... | component/input/data sensitivity | p. 8 (5.1 Results) |
| Finally we show the system can work with multilingual queries, without explicitly being designed to. | component/input/data sensitivity | p. 9 (5.1 Results) |
| Human: Can you bring a fruit-flavored drink without caffeine? | component/input/data sensitivity | p. 10 (5.1 Results) |
| Table 6: Ablations over the size of the LLM. Compared only with the generative outputs (no value function) with USE embeddings [15]. Listing 2: ... | component/input/data sensitivity | p. 29 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We evaluate our method on a number of real-world robotic tasks, where we show the need for real-world grounding and that this approach is ... | Table 2: Success rates of instructions by family. PaLM-SayCan achieves a planning success rate of 84% and execution success rate of 74% in the ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (5.1 Results), p. 10 (5.1 Results), p. 8 (5.1 Results), p. 8 (5.1 Results) |
| Primary metric/result | Table 3: Success rates of instructions by family. SayCan achieves a planning success rate of 84% and execution success rate of 74% with PaLM ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 5.1 Results - extractive PDF cue:** When comparing the performance of different instruction families in Table 2 (see Table 1 for an explanation of families), we see that the natural language ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** Algorithm 1 SayCan Given: A high level instruction i, state s0, and a set of skills Π and their language descriptions ℓΠ 1: n = ...
- **p. 6 / 2 Preliminaries - extractive PDF cue:** Inspired by common skills one might pose to a robot in a kitchen environment, we propose 551 skills that span seven skill families and 17 ...
- **p. 6 / 2 Preliminaries - extractive PDF cue:** 5 Experimental Evaluation Figure 4: The experiments were performed in an office kitchen and a mock kitchen mirroring this setup, with 5 locations and 15 ...
- **p. 6 / 2 Preliminaries - extractive PDF cue:** We use 15 objects commonly found in an office kitchen and 5 known locations with semantic meaning (two counters, a table, a trash can, and ...
- **p. 6 / 2 Preliminaries - extractive PDF cue:** The robot used is a mobile manipulator from Everyday Robots 2 with a 7 degree-of-freedom arm and a two-fingered gripper.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work that extends the repertoire of skills and improves their robustness would mitigate this limitation. | p. 12 (7 Related Work) |
| body limitation/failure cue | 8 Conclusions, Limitations and Future Work We presented SayCan, a method that enables leveraging and grounding the rich knowledge in large language models to ... | p. 12 (7 Related Work) |
| body limitation/failure cue | Appendix E.6 shows additional rollouts with complex decisions, embodiment grounding, and long-horizon tasks in Figures 14-17 as well as failures in Figure 16. | p. 7 (5.1 Results) |
| body limitation/failure cue | Overall, 65% of the errors were LLM failures and 35% were affordance failures. | p. 8 (5.1 Results) |
| body limitation/failure cue | The embodiment tasks were planned correctly 64% of the time, generally with failures as a result of affordance function misclassification. | p. 8 (5.1 Results) |
| body limitation/failure cue | Over 21 queries we found a planning rate of 100% and an execution rate of 33% (due to failures of the chained manipulation policy), ... | p. 10 (5.1 Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Steps are output in the form "pick up the object and place it in location", leveraging the ability of LLMs to output code structures. | p. 11 (5.1 Results) |
| Large language models can encode a wealth of semantic knowledge about the world. | p. 1 (Abstract) |
| The project's website, the video, and open sourced code in a tabletop domain can be found at say-can.github.io. | p. 1 (Abstract) |
| and we might wonder whether knowledge of everyday tasks that is encoded in such models can be used by robots to perform complex tasks ... | p. 2 (1 Introduction) |
| Furthermore, this combination results in a fully explainable sequence of steps that the robot will execute to accomplish an instruction - an interpretable plan ... | p. 2 (1 Introduction) |
| While typical generation applications (e.g., conversational agents) sample from this distribution or decode the maximum likelihood completion, we can also use the model to ... | p. 3 (2 Preliminaries) |
| However, this is not enough to fully constrain the output to admissible primitive skills for an embodied agent, and indeed at times it can ... | p. 3 (2 Preliminaries) |
| The optimal skill according to the language model is computed via ℓπ = arg maxℓπ∈ℓΠ p(ℓπ/i). | p. 4 (2 Preliminaries) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / 7 Related Work - extractive PDF cue:** Future work that extends the repertoire of skills and improves their robustness would mitigate this limitation.
- **p. 12 / 7 Related Work - extractive PDF cue:** 8 Conclusions, Limitations and Future Work We presented SayCan, a method that enables leveraging and grounding the rich knowledge in large language models to complete ...
- **p. 7 / 5.1 Results - extractive PDF cue:** Appendix E.6 shows additional rollouts with complex decisions, embodiment grounding, and long-horizon tasks in Figures 14-17 as well as failures in Figure 16.
- **p. 8 / 5.1 Results - extractive PDF cue:** Overall, 65% of the errors were LLM failures and 35% were affordance failures.
- **p. 8 / 5.1 Results - extractive PDF cue:** The embodiment tasks were planned correctly 64% of the time, generally with failures as a result of affordance function misclassification.
- **p. 10 / 5.1 Results - extractive PDF cue:** Over 21 queries we found a planning rate of 100% and an execution rate of 33% (due to failures of the chained manipulation policy), with ...

- **PDF anchors reviewed:** datasets p. 7 (5.1 Results), p. 7 (5.1 Results), p. 8 (5.1 Results), p. 11 (5.1 Results), p. 11 (5.1 Results), p. 8 (5.1 Results), metrics p. 9 (Figure/Table caption), p. 33 (Figure/Table caption), p. 9 (5.1 Results), p. 10 (5.1 Results), p. 7 (5.1 Results), p. 8 (5.1 Results), baselines p. 9 (5.1 Results), p. 9 (5.1 Results), p. 29 (Figure/Table caption), p. 7 (5.1 Results), p. 8 (5.1 Results), p. 10 (5.1 Results), results p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (5.1 Results), p. 10 (5.1 Results), p. 8 (5.1 Results), p. 8 (5.1 Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
