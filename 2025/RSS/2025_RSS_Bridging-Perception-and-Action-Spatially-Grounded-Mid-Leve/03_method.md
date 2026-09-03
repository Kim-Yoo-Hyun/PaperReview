# Method - Bridging Perception and Action: Spatially-Grounded Mid-Level Representations for Robot Generalization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p155.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p155.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (V. ARCHITECTURE), p. 5 (B. Training), p. 4 (V. ARCHITECTURE), p. 6 (B. Training), p. 6 (4) Which policy architecture offers the best tradeoff be), p. 9 (C. Different Architectures offer Different Tradeoffs berween)): We implement our method on a diffusion policy similar to the one proposed in [40]. ‘The policy takes as input 4 images from different viewpoints (2 third-person images and 2 ...

## Method Body Digest

- **p. 4 / V. ARCHITECTURE - extractive body cue:** We implement our method on a diffusion policy similar to the one proposed in [40]. ‘The policy takes as input 4 images from different viewpoints ...
- **p. 5 / B. Training - extractive body cue:** Once the expert modules are trained independently, their parameters are frozen. ‘Then, the policy network trained endto-end with a noise prediction loss.
- **p. 4 / V. ARCHITECTURE - extractive body cue:** At each state, we denoise the decoder predicts ¢ = 10 action chunks simultaneously with a transformer.
- **p. 6 / B. Training - extractive body cue:** By iteratively refining the training data and adjusting the weighting of consistent samples, our method creates a feedback loop that promotes tighter self-consistency between policy ...
- **p. 6 / 4) Which policy architecture offers the best tradeoff be - extractive body cue:** 5) Can mid-level representations be effectively used as supervision signals during training to enhance policy precision and generalization across tasks?
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** Overall, these findings underscore the effectiveness of Mid-Level MoE in leveraging task-specific representations through attention mechanisms, By selectively attending 10 pertinent information and maintaining robustness, ...
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** Wee ablate different policy architectures in Tables 1 and Il Table Il records the average success rates for our architecture across all simulation and real-world ...
- **p. 6 / B. Training - extractive body cue:** where A(s,a) represents the advantage function, which modulates the policy gradient loss Cyc based on the estimated benefit of selecting action « in states.

## Design Rationale

- **p. 2 / 1. Ivrropuction - extractive body cue:** We show that while different mid-level representations excel at different tasks, our method can leverage these task-specitfic benefits to achieve consistently higher performance on a ...
- **p. 6 / B. Training - extractive body cue:** Similarly, our approach integrates mid-level expert outputs as implicit guidance in scenarios where no explicit reward signal is available, Instead of an advantage function, we ...
- **p. 1 / Abstract - extractive body cue:** We propose a novel mixture-of-experts policy architecture that can combine multiple specialized expert models, each trained on a distinct ‘mid-level representation, to improve the generalization ...

## Source Evidence Cues

- **p. 4 / V. ARCHITECTURE - extractive body cue:** We implement our method on a diffusion policy similar to the one proposed in [40]. ‘The policy takes as input 4 images from different viewpoints ...
- **p. 5 / B. Training - extractive body cue:** Once the expert modules are trained independently, their parameters are frozen. ‘Then, the policy network trained endto-end with a noise prediction loss.
- **p. 4 / V. ARCHITECTURE - extractive body cue:** At each state, we denoise the decoder predicts ¢ = 10 action chunks simultaneously with a transformer.
- **p. 6 / B. Training - extractive body cue:** By iteratively refining the training data and adjusting the weighting of consistent samples, our method creates a feedback loop that promotes tighter self-consistency between policy ...
- **p. 6 / 4) Which policy architecture offers the best tradeoff be - extractive body cue:** 5) Can mid-level representations be effectively used as supervision signals during training to enhance policy precision and generalization across tasks?
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** Overall, these findings underscore the effectiveness of Mid-Level MoE in leveraging task-specific representations through attention mechanisms, By selectively attending 10 pertinent information and maintaining robustness, ...
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** Wee ablate different policy architectures in Tables 1 and Il Table Il records the average success rates for our architecture across all simulation and real-world ...
- **Detected method headings:** V. ARCHITECTURE (p. 4); 4) Which policy architecture offers the best tradeoff be (p. 6); C. Different Architectures offer Different Tradeoffs berween (p. 9)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | We implement our method on a diffusion policy similar to the one proposed in [40]. ‘The policy takes as input 4 images ... | p. 4 (V. ARCHITECTURE), p. 5 (B. Training) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | Once the expert modules are trained independently, their parameters are frozen. ‘Then, the policy network trained endto-end with a noise prediction loss. | p. 5 (B. Training), p. 4 (V. ARCHITECTURE) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | At each state, we denoise the decoder predicts ¢ = 10 action chunks simultaneously with a transformer. | p. 4 (V. ARCHITECTURE), p. 6 (B. Training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / B. Training - extractive body cue:** where A(s,a) represents the advantage function, which modulates the policy gradient loss Cyc based on the estimated benefit of selecting action « in states.
- **p. 6 / B. Training - extractive body cue:** In RL, the loss function typically incorporates an advantage term, given by:
- **p. 5 / B. Training - extractive body cue:** Once the expert modules are trained independently, their parameters are frozen. ‘Then, the policy network trained endto-end with a noise prediction loss.
- **p. 5 / B. Training - extractive body cue:** The language prompts are carefully tuned for each task to minimize noise as much as possible, For pose-aware representations on top of bounding boxes, we ...
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** This rechction suggests that weighted imitation learning enables policies to focus more precisely on pertinent features, potentially minimizing the influence of noisy or irrelevant information.
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 6 (B. Training), p. 5 (B. Training), p. 6 (B. Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | iteratively, refining, training, data, adjusting, weighting, consistent, samples, creates, feedback, loop, promotes, tighter, self-consistency | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | iteratively, refining, training, data, adjusting, weighting, consistent, samples, creates, feedback | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | while, different, mid-level, representations, excel, tasks, leverage, task-specitfic, benefits, achieve | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | where, represents, advantage, function, modulates, policy, gradient, loss, Cyc, estimated | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / B. Training - extractive body cue:** By iteratively refining the training data and adjusting the weighting of consistent samples, our method creates a feedback loop that promotes tighter self-consistency between policy ...
- **p. 4 / V. ARCHITECTURE - extractive body cue:** We implement our method on a diffusion policy similar to the one proposed in [40]. ‘The policy takes as input 4 images from different viewpoints ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** By analyzing this relationship, we can view the mid-level representations as a bridge between the sensory inputs of the policy and the lower-level joint actions, ...
- **p. 4 / 1. Ivrropuction - extractive body cue:** Suppose £(s) provides the locations of objects of interest in the scene, A policy which utilizes these representations must consistently use these locations to output ...
- **p. 6 / B. Training - extractive body cue:** where A(s,a) represents the advantage function, which modulates the policy gradient loss Cyc based on the estimated benefit of selecting action « in states.
- **p. 2 / 1. Ivrropuction - extractive body cue:** We first systematically study these representations across four critical dimensions: object centrieity, or understanding of the locations and geometry ‘of objects on the scene; motion-centricity ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** between high-level inputs (e-g., language commands or simple ‘object markers) and the low-level action space of a robot.
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | points, with one annotation every 10 timesteps. | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | One potential drawback to the hierachical learning framework is its rigidity in structure. | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / B. Training - extractive body cue:** Once the expert modules are trained independently, their parameters are frozen. ‘Then, the policy network trained endto-end with a noise prediction loss.
- **p. 6 / B. Training - extractive body cue:** By iteratively refining the training data and adjusting the weighting of consistent samples, our method creates a feedback loop that promotes tighter self-consistency between policy ...
- **p. 6 / 4) Which policy architecture offers the best tradeoff be - extractive body cue:** 5) Can mid-level representations be effectively used as supervision signals during training to enhance policy precision and generalization across tasks?
- **p. 5 / B. Training - extractive body cue:** During inference time, each of the expert models are executed asynchronously.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** implement, diffusion, policy, similar, takes, input, images, different, viewpoints, third-person, wrist, directly, outputs, absolute, joint, positions6, arm-as, well, continuous, gripper.
- **Relevant PDF headings:** V. ARCHITECTURE (p. 4); 4) Which policy architecture offers the best tradeoff be (p. 6); C. Different Architectures offer Different Tradeoffs berween (p. 9).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | For RT-H, ‘we relabel robot demonstrations with the language "move the arm leftright/up/down." For each environment in simulation and the real-world, we ... | p. 7 (C. Experiment Setup) |
| Coverage / augmentation | In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ablation based on MOKA (25] and ... | p. 7 (C. Experiment Setup), p. 7 (C. Experiment Setup) |
| Downstream learning interface | Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations of different mid-level representations. ... | p. 1 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / C. Experiment Setup - extractive body cue:** In the Keypoint ablation, we identify important points of interest in the image by querying a VLM.
- **p. 7 / C. Experiment Setup - extractive body cue:** In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ablation based on MOKA (25] and a language baseline ...
- **p. 6 / 4) Which policy architecture offers the best tradeoff be - extractive body cue:** tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs?
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** Meanwhile, Table I! records the sensitivity scores for each of our mid-level experts as well as the robustness index. ‘The robustness index is computed by ...
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** This suggests that the benefits of more targeted feature utilization outweigh the slight decrease in robustness.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (V. ARCHITECTURE), p. 5 (B. Training), p. 4 (V. ARCHITECTURE), p. 6 (B. Training), p. 6 (4) Which policy architecture offers the best tradeoff be), p. 9 (C. Different Architectures offer Different Tradeoffs berween), objective p. 6 (B. Training), p. 6 (B. Training), p. 5 (B. Training), p. 5 (B. Training), p. 9 (C. Different Architectures offer Different Tradeoffs berween), temporal p. 5 (B. Training), p. 2 (1. Ivrropuction), p. 4 (V. ARCHITECTURE), p. 5 (B. Training), p. 7 (B. Real-World Environment).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** At each state, we denoise the decoder predicts ¢ = 10 action chunks simultaneously with a transformer. (p. 4, V. ARCHITECTURE).
- **Objective/update evidence:** where A(s,a) represents the advantage function, which modulates the policy gradient loss Cyc based on the estimated benefit of selecting action « in states. (p. 6, B. Training).
- **Temporal/runtime evidence:** One potential drawback to the hierachical learning framework is its rigidity in structure. (p. 2, 1. Ivrropuction).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
