# Method - AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://xbpeng.github.io/projects/AMP/; PDF retrieval source: https://doi.org/10.1145/3450626.3459670. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (4 BACKGROUND), p. 6 (4 BACKGROUND), p. 4 (4 BACKGROUND), p. 4 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 5 (4 BACKGROUND)): 6.2 Network Architecture Each policy 𝜋is modeled by a neural network that maps a given state s𝑡and goal g to a Gaussian distribution over actions 𝜋(a𝑡/s𝑡, g) = N (𝜇(s𝑡, ...

## Method Body Digest

- **p. 7 / 4 BACKGROUND - extractive body cue:** 6.2 Network Architecture Each policy 𝜋is modeled by a neural network that maps a given state s𝑡and goal g to a Gaussian distribution over actions ...
- **p. 6 / 4 BACKGROUND - extractive body cue:** 6.1 States and Actions The state s𝑡consists of a set of features that describes the configuration of the character's body.
- **p. 4 / 4 BACKGROUND - extractive body cue:** At each time step 𝑡, the agent observes the state s𝑡∈S of the system, then samples an action a𝑡∈A from a policy a𝑡∼𝜋(a𝑡/s𝑡, g).
- **p. 4 / 4 BACKGROUND - extractive body cue:** GAIL addresses some of the limitations of behavioral cloning by learning an objective function that measures the similarity between the policy and the demonstrations, and ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** However, this loss tends to lead to optimization challenges due to vanishing gradients as the sigmoid function saturates, which can hamper training of the policy ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** (3) This adversarial training procedure can be interpreted as training a policy to produce states and actions that appear to the discriminator as being indistinguishable ...
- **p. 6 / 4 BACKGROUND - extractive body cue:** This set of observation features for the discriminator is selected to provide a compact representation of the motion across a single state transition.
- **p. 5 / 4 BACKGROUND - extractive body cue:** 5.2 Least-Squares Discriminator The standard GAN objective detailed in Equation 5 typically uses a sigmoid cross-entropy loss function.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The central contribution of this work is an adversarial learning approach for physics-based character animation that combines goalconditioned reinforcement with an adversarial motion prior, which ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Our framework enables physically simulated character to solve challenging tasks while adopting stylistic behaviors specified by unstructured motion data.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We present one of the first adversarial learning systems that is able to produce high-quality full-body motions for physically simulated characters.

## Source Evidence Cues

- **p. 7 / 4 BACKGROUND - extractive body cue:** 6.2 Network Architecture Each policy 𝜋is modeled by a neural network that maps a given state s𝑡and goal g to a Gaussian distribution over actions ...
- **p. 6 / 4 BACKGROUND - extractive body cue:** 6.1 States and Actions The state s𝑡consists of a set of features that describes the configuration of the character's body.
- **p. 4 / 4 BACKGROUND - extractive body cue:** At each time step 𝑡, the agent observes the state s𝑡∈S of the system, then samples an action a𝑡∈A from a policy a𝑡∼𝜋(a𝑡/s𝑡, g).
- **p. 4 / 4 BACKGROUND - extractive body cue:** GAIL addresses some of the limitations of behavioral cloning by learning an objective function that measures the similarity between the policy and the demonstrations, and ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** However, this loss tends to lead to optimization challenges due to vanishing gradients as the sigmoid function saturates, which can hamper training of the policy ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** (3) This adversarial training procedure can be interpreted as training a policy to produce states and actions that appear to the discriminator as being indistinguishable ...
- **p. 6 / 4 BACKGROUND - extractive body cue:** This set of observation features for the discriminator is selected to provide a compact representation of the motion across a single state transition.
- **Detected method headings:** C LATENT SPACE MODEL (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | 6.2 Network Architecture Each policy 𝜋is modeled by a neural network that maps a given state s𝑡and goal g to a Gaussian ... | p. 7 (4 BACKGROUND), p. 6 (4 BACKGROUND) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | 6.1 States and Actions The state s𝑡consists of a set of features that describes the configuration of the character's body. | p. 6 (4 BACKGROUND), p. 4 (4 BACKGROUND) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | At each time step 𝑡, the agent observes the state s𝑡∈S of the system, then samples an action a𝑡∈A from a policy ... | p. 4 (4 BACKGROUND), p. 4 (4 BACKGROUND) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4 BACKGROUND - extractive body cue:** 5.2 Least-Squares Discriminator The standard GAN objective detailed in Equation 5 typically uses a sigmoid cross-entropy loss function.
- **p. 5 / 4 BACKGROUND - extractive body cue:** The policy is then trained using the RL objective detailed in Equation 1, with rewards specified by, 𝑟𝑡= -log (1 -𝐷(s𝑡, a𝑡)) .
- **p. 4 / 4 BACKGROUND - extractive body cue:** These style-rewards are combined with task-rewards 𝑟𝐺 𝑡and used to train a policy that enables a simulated character to satisfy task-specific goals g, while also ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** High-level task objectives that the character should perform can be specified by relatively simple reward functions, while the low-level style of the character's behaviors can ...
- **p. 7 / 4 BACKGROUND - extractive body cue:** The two rewards are combined according to Equation 4 to yield the reward for the particular timstep.
- **p. 7 / 4 BACKGROUND - extractive body cue:** At each time step 𝑡, the agent receives a task-reward 𝑟𝐺 𝑡= 𝑟𝐺(s𝑡, a𝑡, s𝑡+1, g) from the environment, it then queries the motion prior ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 5 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 6 (4 BACKGROUND), p. 7 (4 BACKGROUND), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Network, Architecture, policy, modeled, neural, maps, given, state, goal, Gaussian, distribution, over, actions, input-dependent | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Network, Architecture, policy, modeled, neural, maps, given, state, goal, Gaussian | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | central, contribution, adversarial, learning, physics-based, character, animation, combines, goalconditioned, reinforcement | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | Least-Squares, Discriminator, standard, GAN, objective, detailed, Equation, typically, uses, sigmoid | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / 4 BACKGROUND - extractive body cue:** 6.2 Network Architecture Each policy 𝜋is modeled by a neural network that maps a given state s𝑡and goal g to a Gaussian distribution over actions ...
- **p. 4 / 4 BACKGROUND - extractive body cue:** Behavioral cloning can be used to directly fit a policy to map from states observed in M to their corresponding actions using supervised learning [Bojarski ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** As such, before a state transition is provided as input to the discriminator, we first apply an observation map Φ(s𝑡) that ACM Trans.
- **p. 4 / 4 BACKGROUND - extractive body cue:** At each time step 𝑡, the agent observes the state s𝑡∈S of the system, then samples an action a𝑡∈A from a policy a𝑡∼𝜋(a𝑡/s𝑡, g).
- **p. 5 / 4 BACKGROUND - extractive body cue:** (2) 𝑑M (s, a) and 𝑑𝜋(s, a) denote the state-action distribution of the dataset and policy respectively.
- **p. 6 / 4 BACKGROUND - extractive body cue:** 6.1 States and Actions The state s𝑡consists of a set of features that describes the configuration of the character's body.
- **p. 6 / 4 BACKGROUND - extractive body cue:** Note, the gradient penalty is calculated with respect to the observation features 𝜙= (Φ(s), Φ(s′)), not the full set of state features (s, s′).
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | But extending these techniques to effectively leverage large unstructured motion datasets remains challenging, since a suitable motion clip needs to be selected ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | The target pose at each time step can then be conveniently determined by selecting the target pose according to the phase. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4 BACKGROUND - extractive body cue:** However, this loss tends to lead to optimization challenges due to vanishing gradients as the sigmoid function saturates, which can hamper training of the policy ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** (3) This adversarial training procedure can be interpreted as training a policy to produce states and actions that appear to the discriminator as being indistinguishable ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Network, Architecture, policy, modeled, neural, maps, given, state, goal, Gaussian, distribution, over, actions, input-dependent, mean, fixed, diagonal, covariance, matrix, States.
- **Relevant PDF headings:** C LATENT SPACE MODEL (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | Each environment is denoted by "Character: Task (Dataset)". | p. 8 (8 RESULTS), p. 9 (8 RESULTS) |
| Balance-aware whole-body execution | AMP produces results of comparable quality when compared to prior tracking-based methods, without requiring a manually designed reward function or synchronization between ... | p. 12 (8 RESULTS), p. 10 (8 RESULTS) |
| Recovery / adaptation | Training the motion prior with a diverse dataset results in more flexible and optimal policies that are able to achieve a wider ... | p. 9 (8 RESULTS), p. 10 (8 RESULTS) |

## Failure and Ablation Link

- **p. 7 / 8 RESULTS - extractive body cue:** The characters automatically learn to compose and generalize different skills from the motion data in order to fulfill high-level task objectives, without requiring mechanisms for ...
- **p. 9 / 8 RESULTS - extractive body cue:** These intricate behaviors arise naturally from the motion prior, without requiring a motion planner to explicitly select which motion the character should execute in a ...
- **p. 10 / 8 RESULTS - extractive body cue:** Learning curves comparing the task performance of AMP to latent space models (Latent Space) and policies trained from scratch without motion data (No Data).
- **p. 10 / 8 RESULTS - extractive body cue:** Again, this composition of different skills emerges automatically from the motion prior, without requiring a motion planner or other mechanisms for motion selection.
- **p. 11 / 8 RESULTS - extractive body cue:** In this setting, the character's objective is to imitate a single motion clip at a time, without additional task objectives.
- **p. 11 / 8 RESULTS - extractive body cue:** Nonetheless, our method is able to produce results of comparable quality without the need to manually design or tune reward functions for different motions.
- **p. 12 / 8 RESULTS - extractive body cue:** AMP is able to closely imitate a diverse repertoire of complex motions, without manual reward engineering.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (4 BACKGROUND), p. 6 (4 BACKGROUND), p. 4 (4 BACKGROUND), p. 4 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 5 (4 BACKGROUND), objective p. 5 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 4 (4 BACKGROUND), p. 1 (Body text (section boundary not confidently recovered)), p. 7 (4 BACKGROUND), p. 7 (4 BACKGROUND), temporal p. 2 (1 INTRODUCTION), p. 3 (2 RELATED WORK), p. 4 (4 BACKGROUND), p. 7 (4 BACKGROUND), p. 11 (8 RESULTS), p. 9 (8 RESULTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** 6.2 Network Architecture Each policy 𝜋is modeled by a neural network that maps a given state s𝑡and goal g to a Gaussian distribution over actions 𝜋(a𝑡/s𝑡, g) = N (𝜇(s𝑡, ... (p. 7, 4 BACKGROUND).
- **Objective/update evidence:** The policy is then trained using the RL objective detailed in Equation 1, with rewards specified by, 𝑟𝑡= -log (1 -𝐷(s𝑡, a𝑡)) . (p. 5, 4 BACKGROUND).
- **Temporal/runtime evidence:** But extending these techniques to effectively leverage large unstructured motion datasets remains challenging, since a suitable motion clip needs to be selected for the character to track at each time ... (p. 2, 1 INTRODUCTION).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
