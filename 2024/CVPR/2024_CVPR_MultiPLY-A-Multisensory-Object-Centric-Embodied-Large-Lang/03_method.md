# Method - MultiPLY: A Multisensory Object-Centric Embodied Large Language Model in 3D World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (4.4. Training & Inference), p. 5 (4.4. Training & Inference), p. 6 (4.4. Training & Inference), p. 6 (4.4. Training & Inference), p. 4 (4.2. Action Tokens), p. 4 (4.2. Action Tokens)): Our training loss consists of two parts.

## Method Body Digest

- **p. 5 / 4.4. Training & Inference - extractive body cue:** Our training loss consists of two parts.
- **p. 5 / 4.4. Training & Inference - extractive body cue:** Model Architecture We use LLaVA [37] as our backbone multi-modal large language model.
- **p. 6 / 4.4. Training & Inference - extractive body cue:** Inference At the inference time, our MultiPLY first takes the task prompt and abstracted scene representation as inputs and generates subsequent tokens.
- **p. 6 / 4.4. Training & Inference - extractive body cue:** We use FSDP on 128 V100 GPUS for efficient training.
- **p. 4 / 4.2. Action Tokens - extractive body cue:** The object is chosen by the attention between the language features (i.e., the last hidden state of the LLM of the SELECT token), and the ...
- **p. 4 / 4.2. Action Tokens - extractive body cue:** It selects the object with the maximum attention score.
- **p. 6 / 4.4. Training & Inference - extractive body cue:** The feature goes through a Sigmoid layer, and is optimized with a binary cross entropy (BCE) loss.
- **p. 5 / 4.4. Training & Inference - extractive body cue:** The first one is the LLM loss which is the same as the original LLaVA 26410

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To sum up, the contributions of this paper are: • We propose Multisensory Universe, a large-scale multisensory dataset comprising 500k data collected by an agent ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose MultiPLY, a multisensory embodied LLM that could encode multisensory object-centric representations, including visual, audio, tactile, and thermal information, by deploying ...
- **p. 5 / 4.4. Training & Inference - extractive body cue:** Our training loss consists of two parts.

## Source Evidence Cues

- **p. 5 / 4.4. Training & Inference - extractive body cue:** Our training loss consists of two parts.
- **p. 5 / 4.4. Training & Inference - extractive body cue:** Model Architecture We use LLaVA [37] as our backbone multi-modal large language model.
- **p. 6 / 4.4. Training & Inference - extractive body cue:** Inference At the inference time, our MultiPLY first takes the task prompt and abstracted scene representation as inputs and generates subsequent tokens.
- **p. 6 / 4.4. Training & Inference - extractive body cue:** We use FSDP on 128 V100 GPUS for efficient training.
- **p. 4 / 4.2. Action Tokens - extractive body cue:** The object is chosen by the attention between the language features (i.e., the last hidden state of the LLM of the SELECT token), and the ...
- **p. 4 / 4.2. Action Tokens - extractive body cue:** It selects the object with the maximum attention score.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Our training loss consists of two parts. | p. 5 (4.4. Training & Inference), p. 5 (4.4. Training & Inference) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Model Architecture We use LLaVA [37] as our backbone multi-modal large language model. | p. 5 (4.4. Training & Inference), p. 6 (4.4. Training & Inference) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Inference At the inference time, our MultiPLY first takes the task prompt and abstracted scene representation as inputs and generates subsequent tokens. | p. 6 (4.4. Training & Inference), p. 6 (4.4. Training & Inference) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4.4. Training & Inference - extractive body cue:** The feature goes through a Sigmoid layer, and is optimized with a binary cross entropy (BCE) loss.
- **p. 5 / 4.4. Training & Inference - extractive body cue:** Our training loss consists of two parts.
- **p. 5 / 4.4. Training & Inference - extractive body cue:** The first one is the LLM loss which is the same as the original LLaVA 26410
- **p. 6 / 4.4. Training & Inference - extractive body cue:** We add one more loss that forces the model to select the right object to attend to.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.4. Training & Inference), p. 5 (4.4. Training & Inference), p. 6 (4.4. Training & Inference), p. 6 (4.4. Training & Inference).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | contributions, Multisensory, Universe, large-scale, dataset, comprising, data, collected, agent, engaging, embodied, environment, covering, diverse | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | contributions, Multisensory, Universe, large-scale, dataset, comprising, data, collected, agent, engaging | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, Multisensory, Universe, large-scale, dataset, comprising, data, collected, agent, engaging | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | feature, goes, through, Sigmoid, layer, optimized, binary, cross, entropy, BCE | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** To sum up, the contributions of this paper are: • We propose Multisensory Universe, a large-scale multisensory dataset comprising 500k data collected by an agent ...
- **p. 2 / 1. Introduction - extractive body cue:** In the inference time, MultiPLY could generate a series of action tokens through the LLM, instructing the agent to take the action and receive the ...
- **p. 6 / 4.4. Training & Inference - extractive body cue:** The observation outcome of the agent is sent back to the LLM as inputs via state tokens.
- **p. 5 / 4.2. Action Tokens - extractive body cue:** The interaction results are appended back to the LLM via state tokens. • <NAVIGATE> token asks an agent to navigate to the selected object.
- **p. 6 / 4.4. Training & Inference - extractive body cue:** The LLM further generates next tokens based on the current state inputs.
- **p. 5 / 4.2. Action Tokens - extractive body cue:** Note that the navigation action could be executed by any pre-defined pathfinder module and is not the research focus of this paper. • <OBSERVE> token ...
- **p. 4 / 4.2. Action Tokens - extractive body cue:** The object is chosen by the attention between the language features (i.e., the last hidden state of the LLM of the SELECT token), and the ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | To perform instruction tuning with pretrained LLM on such generated data, we first encode the 3D scene as abstracted object-centric representations, and ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The reason could be that retrieval models fuse the multisensory embeddings into a whole, and do not disentangle the representation, or interact ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.4. Training & Inference - extractive body cue:** Our training loss consists of two parts.
- **p. 6 / 4.4. Training & Inference - extractive body cue:** Inference At the inference time, our MultiPLY first takes the task prompt and abstracted scene representation as inputs and generates subsequent tokens.
- **p. 6 / 4.4. Training & Inference - extractive body cue:** We use FSDP on 128 V100 GPUS for efficient training.
- **p. 6 / 4.4. Training & Inference - extractive body cue:** Inference At the inference time, our MultiPLY first takes the task prompt and abstracted scene representation as inputs and generates subsequent tokens.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** training, loss, consists, parts, Model, Architecture, LLaVA, backbone, multi-modal, large, language, Inference, time, MultiPLY, first, takes, task, prompt, abstracted, scene.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | As presented in Figure 2, we begin by explaining how we input interactive objects into the scene to construct object-centric 3D scenes ... | p. 3 (3. The Multisensory-Universe Dataset), p. 3 (3.1. Inputting Interactive Objects into 3D Scenes) |
| Semantic / temporal fusion | In general, our MultiPLY outperforms the baseline models a lot. | p. 7 (5.1. Object Retrieval), p. 6 (5.1. Object Retrieval) |
| Robot query / planning handoff | The select action could be achieved by calculating the similarity between the object embedding and the language embedding, and the object with ... | p. 6 (5.1. Object Retrieval), p. 8 (5.4. Task Decomposition) |

## Failure and Ablation Link

- **p. 6 / 5.1. Object Retrieval - extractive body cue:** We also experiment with MultiPLY-2D, a 2D variant of our model, where we replace 3D features with 2D single-view features.
- **p. 6 / 5. Experiments - extractive body cue:** Due to space limits, we attach more ablative studies in the Supplementary Material, where we experiment with each possible combination of sensory inputs from different ...
- **p. 8 / 5.4. Task Decomposition - extractive body cue:** From the table, we observe that models without interaction have very poor results, probably because vision-language models have hallucination to a great extent.
- **p. 8 / 5.4. Task Decomposition - extractive body cue:** Note that there is a domain gap between the task decomposition data 3D-LLM was trained on and our setting, which yields almost zero success rates ...
- **p. 7 / 5.2. Tool Use - extractive body cue:** For example, we could use a steel spoon to replace the can opener, but we can't use a plastic spoon.
- **p. 8 / 6. Conclusion - extractive body cue:** One limitation of our model is that currently MultiPLY does not involve detailed navigation and control policy, but utilizes pre-defined policies for carrying out the ...
- **p. 6 / 5.1. Object Retrieval - extractive body cue:** As these models cannot interact with the environment to get the tactile, impact sound, and temperature data, we refine three setups for the baselines: 1) ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (4.4. Training & Inference), p. 5 (4.4. Training & Inference), p. 6 (4.4. Training & Inference), p. 6 (4.4. Training & Inference), p. 4 (4.2. Action Tokens), p. 4 (4.2. Action Tokens), objective p. 6 (4.4. Training & Inference), p. 5 (4.4. Training & Inference), p. 5 (4.4. Training & Inference), p. 6 (4.4. Training & Inference), temporal p. 1 (Abstract), p. 7 (5.1. Object Retrieval), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Related Works), p. 4 (4. MultiPLY).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
