# Method - World Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1803.10122; PDF retrieval source: https://arxiv.org/pdf/1803.10122. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 9 (4.5. Cheating the World Model), p. 3 (2.1. VAE (V) Model), p. 9 (4.5. Cheating the World Model), p. 3 (2.2. MDN-RNN (M) Model), p. 4 (2.3. Controller (C) Model), p. 2 (2. Agent Model)): Recent work (Nagabandi et al., 2017) combines the model-based approach with traditional model-free RL training by first initializing the policy network with the learned policy, but must subsequently rely on ...

## Method Body Digest

- **p. 9 / 4.5. Cheating the World Model - extractive body cue:** Recent work (Nagabandi et al., 2017) combines the model-based approach with traditional model-free RL training by first initializing the policy network with the learned policy, ...
- **p. 3 / 2.1. VAE (V) Model - extractive body cue:** Here, we use a simple Variational Autoencoder (Kingma & Welling, 2013; Rezende et al., 2014) as our V model to compress each image frame into ...
- **p. 9 / 4.5. Cheating the World Model - extractive body cue:** The weakness of this approach of learning a policy inside a learned dynamics model is that our agent can easily find an adversarial policy that ...
- **p. 3 / 2.2. MDN-RNN (M) Model - extractive body cue:** We use a similar model to predict the next latent vector zt.
- **p. 4 / 2.3. Controller (C) Model - extractive body cue:** World Models Below is the pseudocode for how our agent model is used in the OpenAI Gym (Brockman et al., 2016) environment: def rollout(controller): ''' ...
- **p. 2 / 2. Agent Model - extractive body cue:** Our agent consists of three components that work closely together: Vision (V), Memory (M), and Controller (C)
- **p. 5 / V Model Only - extractive body cue:** Training an agent to drive is not a difficult task if we have a good representation of the observation.
- **p. 3 / 2.3. Controller (C) Model - extractive body cue:** The Controller (C) model is responsible for determining the course of actions to take in order to maximize the expected cumulative reward of the agent ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We use similar terminology and notation as On Learning to Think: Algorithmic Information Theory for Novel Combinations of RL Controllers and RNN World Models (Schmidhuber, ...
- **p. 2 / 1. Introduction - extractive body cue:** In this article, we present a simplified framework that we can use to experimentally demonstrate some of the key concepts from these papers, and also ...
- **p. 6 / V MODEL WITH HIDDEN LAYER - extractive body cue:** To our knowledge, our method is the first reported solution to solve this task.

## Source Evidence Cues

- **p. 9 / 4.5. Cheating the World Model - extractive body cue:** Recent work (Nagabandi et al., 2017) combines the model-based approach with traditional model-free RL training by first initializing the policy network with the learned policy, ...
- **p. 3 / 2.1. VAE (V) Model - extractive body cue:** Here, we use a simple Variational Autoencoder (Kingma & Welling, 2013; Rezende et al., 2014) as our V model to compress each image frame into ...
- **p. 9 / 4.5. Cheating the World Model - extractive body cue:** The weakness of this approach of learning a policy inside a learned dynamics model is that our agent can easily find an adversarial policy that ...
- **p. 3 / 2.2. MDN-RNN (M) Model - extractive body cue:** We use a similar model to predict the next latent vector zt.
- **p. 4 / 2.3. Controller (C) Model - extractive body cue:** World Models Below is the pseudocode for how our agent model is used in the OpenAI Gym (Brockman et al., 2016) environment: def rollout(controller): ''' ...
- **p. 2 / 2. Agent Model - extractive body cue:** Our agent consists of three components that work closely together: Vision (V), Memory (M), and Controller (C)
- **p. 5 / V Model Only - extractive body cue:** Training an agent to drive is not a difficult task if we have a good representation of the observation.
- **Detected method headings:** 2. Agent Model (p. 2); 2.1. VAE (V) Model (p. 2); 2.2. MDN-RNN (M) Model (p. 3); 2.3. Controller (C) Model (p. 3); 3.1. World Model for Feature Extraction (p. 4); V Model Only (p. 5); V MODEL (p. 6); V MODEL WITH HIDDEN LAYER (p. 6); 3. Train MDN-RNN (M) to model (p. 7); 6. Use learned policy from (5) on actual environment (p. 7); 4.4. Transfer Policy to Actual Environment (p. 8); 4.5. Cheating the World Model (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Recent work (Nagabandi et al., 2017) combines the model-based approach with traditional model-free RL training by first initializing the policy network with ... | p. 9 (4.5. Cheating the World Model), p. 3 (2.1. VAE (V) Model) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | Here, we use a simple Variational Autoencoder (Kingma & Welling, 2013; Rezende et al., 2014) as our V model to compress each ... | p. 3 (2.1. VAE (V) Model), p. 9 (4.5. Cheating the World Model) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | The weakness of this approach of learning a policy inside a learned dynamics model is that our agent can easily find an ... | p. 9 (4.5. Cheating the World Model), p. 3 (2.2. MDN-RNN (M) Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2.3. Controller (C) Model - extractive body cue:** The Controller (C) model is responsible for determining the course of actions to take in order to maximize the expected cumulative reward of the agent ...
- **p. 9 / 4.5. Cheating the World Model - extractive body cue:** Therefore our agent can efficiently explore ways to directly manipulate the hidden states of the game engine in its quest to maximize its expected cumulative ...
- **p. 10 / 5. Iterative Training Procedure - extractive body cue:** Train M to model P(xt+1, rt+1, at+1, dt+1/xt, at, ht) and train C to optimize expected rewards inside of M.
- **p. 10 / 5. Iterative Training Procedure - extractive body cue:** Therefore we can adapt and reuse M's training loss function to encourage curiosity.
- **p. 4 / 2.3. Controller (C) Model - extractive body cue:** World Models Below is the pseudocode for how our agent model is used in the OpenAI Gym (Brockman et al., 2016) environment: def rollout(controller): ''' ...
- **p. 4 / 2.3. Controller (C) Model - extractive body cue:** Advances in deep learning provided us with the tools to train large, sophisticated models efficiently, provided we can define a well-behaved, differentiable loss function.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 4 (2.3. Controller (C) Model), p. 10 (5. Iterative Training Procedure), p. 10 (5. Iterative Training Procedure), p. 3 (2.3. Controller (C) Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Previous, works, Hnermann, Bling, Lau, have, good, hand-engineered, information, about, observation, LIDAR, angles, positions | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | Previous, works, Hnermann, Bling, Lau, have, good, hand-engineered, information, about | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | similar, terminology, notation, Learning, Think, Algorithmic, Information, Theory, Novel, Combinations | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | Controller, model, responsible, determining, course, actions, take, order, maximize, expected | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / V Model Only - extractive body cue:** Previous works (Hnermann, 2017; Bling, 2015; Lau, 2016) have shown that with a good set of hand-engineered information about the observation, such as LIDAR information, ...
- **p. 3 / 2.3. Controller (C) Model - extractive body cue:** M will then take the current zt and action at as an input to update its own hidden state to produce ht+1 to be used ...
- **p. 3 / 2.3. Controller (C) Model - extractive body cue:** C is a simple single layer linear model that maps zt and ht directly to action at at each time step: at = Wc [zt ...
- **p. 2 / 2.1. VAE (V) Model - extractive body cue:** The environment provides our agent with a high dimensional input observation at each time step.
- **p. 4 / 2.3. Controller (C) Model - extractive body cue:** World Models Below is the pseudocode for how our agent model is used in the OpenAI Gym (Brockman et al., 2016) environment: def rollout(controller): ''' ...
- **p. 6 / 3.4. Car Racing Dreams - extractive body cue:** We can ask it to produce the probability distribution of zt+1 given the current states, sample a zt+1 and use this sample as the real ...
- **p. 8 / 4.3. Training Inside of the Dream - extractive body cue:** For instance, if the agent selects the left action, the M model learns to move the agent to the left and adjust its internal representation ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | We can use the VAE to reconstruct each frame using zt at each time step to visualize the quality of the information ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | There are no explicit rewards in this environment, so to mimic natural selection, the cumulative reward can be defined to be the ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 4.5. Cheating the World Model - extractive body cue:** Recent work (Nagabandi et al., 2017) combines the model-based approach with traditional model-free RL training by first initializing the policy network with the learned policy, ...
- **p. 9 / 4.5. Cheating the World Model - extractive body cue:** The weakness of this approach of learning a policy inside a learned dynamics model is that our agent can easily find an adversarial policy that ...
- **p. 4 / 2.3. Controller (C) Model - extractive body cue:** World Models Below is the pseudocode for how our agent model is used in the OpenAI Gym (Brockman et al., 2016) environment: def rollout(controller): ''' ...
- **p. 5 / V Model Only - extractive body cue:** Training an agent to drive is not a difficult task if we have a good representation of the observation.
- **p. 4 / 3.1. World Model for Feature Extraction - extractive body cue:** Training each model only required less than an hour of computation time on a single GPU.
- **p. 4 / 3.1. World Model for Feature Extraction - extractive body cue:** We can also train individual VAE and MDN-RNN models without having to exhaustively tune hyperparameters.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Recent, Nagabandi, combines, model-based, traditional, model-free, training, first, initializing, policy, network, learned, must, subsequently, rely, methods, fine-tune, actual, environment, Here.
- **Relevant PDF headings:** 2. Agent Model (p. 2); 2.1. VAE (V) Model (p. 2); 2.2. MDN-RNN (M) Model (p. 3); 2.3. Controller (C) Model (p. 3); 3.1. World Model for Feature Extraction (p. 4); V Model Only (p. 5); V MODEL (p. 6); V MODEL WITH HIDDEN LAYER (p. 6); 3. Train MDN-RNN (M) to model (p. 7); 6. Use learned policy from (5) on actual environment (p. 7); 4.4. Transfer Policy to Actual Environment (p. 8); 4.5. Cheating the World Model (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | To train our V model, we first collect a dataset of 10,000 random rollouts of the environment. | p. 4 (3.1. World Model for Feature Extraction), p. 4 (3.1. World Model for Feature Extraction) |
| Filtering / recovery | We can also train individual VAE and MDN-RNN models without having to exhaustively tune hyperparameters. | p. 4 (3.1. World Model for Feature Extraction), p. 1 (Figure/Table caption) |
| Monitoring / re-entry | Figure 11. Limiting our controller to see only zt, but not ht results in wobbly and unstable driving behaviours. Although the agent ... | p. 5 (Figure/Table caption), p. 4 (3.1. World Model for Feature Extraction) |

## Failure and Ablation Link

- **p. 4 / 3.1. World Model for Feature Extraction - extractive body cue:** We can also train individual VAE and MDN-RNN models without having to exhaustively tune hyperparameters.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. A World Model, from Scott McCloud's Understanding Comics. (McCloud, 1993; E, 2012) current motor actions (Keller et al., 2012; Leinweber et al., 2017). ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 4. Our agent consists of three components that work closely together: Vision (V), Memory (M), and Controller (C)
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 18. Agent discovers an adversarial policy to automatically extinguish fireballs after they are fired during some rollouts. This weakness could be the reason that ...
- **p. 12 / 7. Discussion - extractive body cue:** After all, unsupervised learning cannot, by definition, know what will be useful for the task at hand.
- **p. 12 / 7. Discussion - extractive body cue:** The choice of using a VAE for the V model and training it as a standalone model also has its limitations, since it may encode ...
- **p. 13 / 7. Discussion - extractive body cue:** Experiments with those more general approaches are left for future work.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 9 (4.5. Cheating the World Model), p. 3 (2.1. VAE (V) Model), p. 9 (4.5. Cheating the World Model), p. 3 (2.2. MDN-RNN (M) Model), p. 4 (2.3. Controller (C) Model), p. 2 (2. Agent Model), objective p. 3 (2.3. Controller (C) Model), p. 9 (4.5. Cheating the World Model), p. 10 (5. Iterative Training Procedure), p. 10 (5. Iterative Training Procedure), p. 4 (2.3. Controller (C) Model), p. 4 (2.3. Controller (C) Model), temporal p. 5 (3.1. World Model for Feature Extraction), p. 7 (4.1. Learning Inside of a Dream), p. 7 (4.1. Learning Inside of a Dream), p. 13 (7. Discussion), p. 5 (3.1. World Model for Feature Extraction), p. 2 (2.1. VAE (V) Model).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Previous works (Hnermann, 2017; Bling, 2015; Lau, 2016) have shown that with a good set of hand-engineered information about the observation, such as LIDAR information, angles, positions and velocities, one ... (p. 5, V Model Only).
- **Objective/update evidence:** Train M to model P(xt+1, rt+1, at+1, dt+1/xt, at, ht) and train C to optimize expected rewards inside of M. (p. 10, 5. Iterative Training Procedure).
- **Temporal/runtime evidence:** Its task is simply to compress and predict the sequence of image frames observed. (p. 5, 3.1. World Model for Feature Extraction).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
