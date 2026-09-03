# Method - NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1143_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01143.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 7 (3 Method)): 2: Model architecture of NavGPT-2, it consists of a multimodality Large Language Model and a topological graph-based navigation policy network.

## Method Body Digest

- **p. 6 / 3 Method - extractive body cue:** 2: Model architecture of NavGPT-2, it consists of a multimodality Large Language Model and a topological graph-based navigation policy network.
- **p. 5 / 3 Method - extractive body cue:** 3.1 VLMs Latent as Visual-Linguistic Representation In this section, we discuss the model design within the Large Vision-Language Model, how to enable frozen LLMs to ...
- **p. 5 / 3 Method - extractive body cue:** For action prediction, the model employs both hidden representations of image tokens and instruction text tokens that have been processed by the LLM encoder as ...
- **p. 4 / 3 Method - extractive body cue:** The architecture of NavGPT-2, as depicted in Figure 2, comprises two primary components: a Large Vision-Language Model (VLM) and a navigation policy network.
- **p. 6 / 3 Method - extractive body cue:** For encoderdecoder based LLMs, we retrieve the hidden representation of the image tokens and instruction tokens from the last Transformer encoder layer.
- **p. 7 / 3 Method - extractive body cue:** Specifically, the node embeddings are first cross-attended with the instructions encoded by the LLM, then go through a graph-aware self-attention (GASA), which considers both distances ...
- **p. 9 / 3 Method - extractive body cue:** When fine-tuning the downstream navigation policy network, we follow previous work to combine Behaviour cloning and DAgger loss [61]: \ m a t h cal ...
- **p. 5 / 3 Method - extractive body cue:** Furthermore, we generate 10K navigational reasoning data from the R2R training set [6] and perform instruction-tuning to the Q-former and the projection layer on the ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are as follows: (1) We propose a pipeline to incorporate VLN specialists with VLMs free from LLM training.
- **p. 3 / 1 Introduction - extractive body cue:** In light of this, we propose NavGPT-2, a system that finds a balance between the two aforementioned extremes, incorporating effective navigational modules to facilitate navigational ...
- **p. 5 / 3 Method - extractive body cue:** Moreover, we introduce special tokens <IMG>, </IMG>, <INST> and </INST> to insert images tokens and instructions into the prompt.

## Source Evidence Cues

- **p. 6 / 3 Method - extractive body cue:** 2: Model architecture of NavGPT-2, it consists of a multimodality Large Language Model and a topological graph-based navigation policy network.
- **p. 5 / 3 Method - extractive body cue:** 3.1 VLMs Latent as Visual-Linguistic Representation In this section, we discuss the model design within the Large Vision-Language Model, how to enable frozen LLMs to ...
- **p. 5 / 3 Method - extractive body cue:** For action prediction, the model employs both hidden representations of image tokens and instruction text tokens that have been processed by the LLM encoder as ...
- **p. 4 / 3 Method - extractive body cue:** The architecture of NavGPT-2, as depicted in Figure 2, comprises two primary components: a Large Vision-Language Model (VLM) and a navigation policy network.
- **p. 6 / 3 Method - extractive body cue:** For encoderdecoder based LLMs, we retrieve the hidden representation of the image tokens and instruction tokens from the last Transformer encoder layer.
- **p. 7 / 3 Method - extractive body cue:** Specifically, the node embeddings are first cross-attended with the instructions encoded by the LLM, then go through a graph-aware self-attention (GASA), which considers both distances ...
- **p. 9 / 3 Method - extractive body cue:** When fine-tuning the downstream navigation policy network, we follow previous work to combine Behaviour cloning and DAgger loss [61]: \ m a t h cal ...
- **Detected method headings:** 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | 2: Model architecture of NavGPT-2, it consists of a multimodality Large Language Model and a topological graph-based navigation policy network. | p. 6 (3 Method), p. 5 (3 Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | 3.1 VLMs Latent as Visual-Linguistic Representation In this section, we discuss the model design within the Large Vision-Language Model, how to enable ... | p. 5 (3 Method), p. 5 (3 Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | For action prediction, the model employs both hidden representations of image tokens and instruction text tokens that have been processed by the ... | p. 5 (3 Method), p. 4 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Method - extractive body cue:** Furthermore, we generate 10K navigational reasoning data from the R2R training set [6] and perform instruction-tuning to the Q-former and the projection layer on the ...
- **p. 9 / 3 Method - extractive body cue:** The overall loss function is given by L = λLBC + LDAG, where λ is a balancing factor.
- **p. 9 / 3 Method - extractive body cue:** When fine-tuning the downstream navigation policy network, we follow previous work to combine Behaviour cloning and DAgger loss [61]: \ m a t h cal ...
- **p. 5 / 3 Method - extractive body cue:** For action prediction, the model employs both hidden representations of image tokens and instruction text tokens that have been processed by the LLM encoder as ...
- **p. 8 / 3 Method - extractive body cue:** 3.3 Multi-stage Learning for Action and Reasoning We perform a two-stage training to learn action prediction and navigation reasoning generation for LLM.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3 Method), p. 9 (3 Method), p. 9 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | action, prediction, model, employs, hidden, representations, image, tokens, instruction, text, have, been, processed, LLM | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | action, prediction, model, employs, hidden, representations, image, tokens, instruction, text | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | contributions, follows, pipeline, incorporate, VLN, specialists, VLMs, free, LLM, training | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Furthermore, generate, navigational, reasoning, data, R2R, training, perform, instruction-tuning, Q-former | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 Method - extractive body cue:** For action prediction, the model employs both hidden representations of image tokens and instruction text tokens that have been processed by the LLM encoder as ...
- **p. 4 / 3 Method - extractive body cue:** Within the VLM, visual observations and instructions are processed by
- **p. 5 / 3 Method - extractive body cue:** The agent predicts the subsequent action by selecting the relative angle at from Ot, the policy π parametrized by Θ that the agent is required ...
- **p. 8 / 3 Method - extractive body cue:** We employ a two-layer feed-forward network to process the output node representations of the GASA to generate an action score.
- **p. 8 / 3 Method - extractive body cue:** We asked GPT-4V to determine the next step toward completing the instruction based on the current observation of the surroundings and relevant landmarks.
- **p. 9 / 3 Method - extractive body cue:** When fine-tuning the downstream navigation policy network, we follow previous work to combine Behaviour cloning and DAgger loss [61]: \ m a t h cal ...
- **p. 3 / 1 Introduction - extractive body cue:** As shown in Figure 1, NavGPT-2 could generate interpretative actions with language, and demonstrate the significant potential of building a communicative VLN agent that allows ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | The step embedding of the unexplored nodes is 0 and a ‘stop' node is added to the graph memory to denote a ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Each view is represented by the summation of its visual features ¯ H′v, its directional embedding Ed representing the location of each ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | The step embedding of the unexplored nodes is 0 and a ‘stop' node is added to the graph memory to denote a ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 3 Method - extractive body cue:** When fine-tuning the downstream navigation policy network, we follow previous work to combine Behaviour cloning and DAgger loss [61]: \ m a t h cal ...
- **p. 9 / 4 Experiments - extractive body cue:** In stage one, we initialize the model from pretrained InstructBLIP checkpoints and train the Q-former for 200K steps with a batch size of 8.
- **p. 9 / 4 Experiments - extractive body cue:** In stage two, we freeze the pretrained VLM from stage one and finetune the downstream policy network with a batch size of 2 and a ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Model, architecture, NavGPT-2, consists, multimodality, Large, Language, topological, graph-based, navigation, policy, network, VLMs, Latent, Visual-Linguistic, Representation, section, discuss, design, within.
- **Relevant PDF headings:** 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | 4.5 Cross Dataset Generalization Ability We evaluate the generalization ability of NavGPT-2 in two aspects: generalize to free-form language instructions and to ... | p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Global / local decision | Compared to the baseline methods, NavGPT-2 bypass it by 4% SR and 2% SPL on the test split even if we do ... | p. 11 (4 Experiments), p. 9 (4 Experiments) |
| Motion execution / recovery | Additionally, we can see from Model#3 of Table 5 that the pretraining of Q-former on reasonings brings slight improvement to the success ... | p. 13 (4 Experiments), p. 9 (4 Experiments) |

## Failure and Ablation Link

- **p. 13 / 4 Experiments - extractive body cue:** 4.6 Ablation Study We ablate the core design choices applied in this paper, including the effect of incorporating a navigation-specific policy model, pretraining the Q-former ...
- **p. 12 / 4 Experiments - extractive body cue:** 4.4 The Effect of Data Amount In Table 3 we initialize DUET from LXMERT and compare the model performance when finetuning 10%, 50%, and full ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 5: Effect of navigation policy network and pretrained Q-former for reasoning. Methods # Val Seen Val Unseen TL NE↓OSR↑SR↑SPL↑TL NE↓OSR↑SR↑SPL↑ NavGPT-2FlanT5-XL 1 13.02 3.34 ...
- **p. 12 / 4 Experiments - extractive body cue:** NavGPT-2 outperforms all DUET variants in SR on the validation unseen split, and it reaches the same performance as DUET with full R2R data when ...
- **p. 13 / 4 Experiments - extractive body cue:** To achieve this, we remove all the visual-language cross-attention layers in the Q-former and policy network and use only a single graph-aware self-attention layer followed ...
- **p. 9 / 4 Experiments - extractive body cue:** In stage two, we freeze the pretrained VLM from stage one and finetune the downstream policy network with a batch size of 2 and a ...
- **p. 10 / 4 Experiments - extractive body cue:** Specifically, we categorized them into distinct categories: - VLN Specialists with Vision-Language-Action Pretraining [3,14, 15,26-28,31,57,75]: These methods are initialized from general vision-language models [40,63] and ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 7 (3 Method), objective p. 5 (3 Method), p. 9 (3 Method), p. 9 (3 Method), p. 5 (3 Method), p. 8 (3 Method), temporal p. 7 (3 Method), p. 7 (3 Method), p. 5 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 9 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
