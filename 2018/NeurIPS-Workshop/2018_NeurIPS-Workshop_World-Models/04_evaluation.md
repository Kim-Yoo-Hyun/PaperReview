# Evaluation - World Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1803.10122; PDF retrieval source: https://arxiv.org/pdf/1803.10122. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 4 (3.1. World Model for Feature Extraction), p. 4 (3. Car Racing Experiment), p. 6 (Figure/Table caption), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption)): Figure 11. Limiting our controller to see only zt, but not ht results in wobbly and unstable driving behaviours. Although the agent is still able to navigate the race track ...

## Evaluation Body Digest

- **p. 4 / 3.1. World Model for Feature Extraction - extractive body cue:** To train our V model, we first collect a dataset of 10,000 random rollouts of the environment.
- **p. 4 / 3.1. World Model for Feature Extraction - extractive body cue:** We use this dataset to train V to learn a latent space of each frame observed.
- **p. 7 / 4.2. Procedure - extractive body cue:** In this simulation, we do not need the V model to encode any real pixel frames during the hallucination process, so our agent will therefore ...
- **p. 7 / 4.1. Learning Inside of a Dream - extractive body cue:** Each rollout of the environment runs for a maximum of 2100 time steps (∼60 seconds), and the task is considered solved if the average survival ...
- **p. 5 / 3.1. World Model for Feature Extraction - extractive body cue:** Its task is simply to compress and predict the sequence of image frames observed.
- **p. 5 / 3.1. World Model for Feature Extraction - extractive body cue:** Only the Controller (C) Model has access to the reward information from the environment.
- **p. 6 / 4.1. Learning Inside of a Dream - extractive body cue:** We have just seen that a policy learned inside of the real environment appears to somewhat function inside of the dream environment.
- **p. 6 / 4.1. Learning Inside of a Dream - extractive body cue:** This begs the question - can we train our agent to learn inside of its own dream, and transfer this policy back to the actual ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 3. Car Racing Experiment (p. 4); 3.3. Experiment Results (p. 5); 4. VizDoom Experiment (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 11. Limiting our controller to see only zt, but not ht results in wobbly and unstable driving behaviours. Although the agent is still ... | p. 5 (Figure/Table caption) |
| 3.1. World Model for Feature Extraction | EMPIRICAL / SIMULATION | 3In principle, we can train both models together in an end-toend manner, although we found that training each separately is more practical, and also ... | p. 4 (3.1. World Model for Feature Extraction) |
| 3. Car Racing Experiment | EMPIRICAL / SIMULATION | To our knowledge, our agent is the first known solution to achieve the score required to solve this task.2 2We find this task interesting ... | p. 4 (3. Car Racing Experiment) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 1. CarRacing-v0 scores achieved using various methods. Our agent is able to achieve a score of 906 ± 21 over 100 random trials, ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 24. Training of CarRacing-v0 Since the requirement of this environment is to have an agent achieve an average score above 900 over 100 ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / 3.1. World Model for Feature Extraction - extractive body cue:** To train our V model, we first collect a dataset of 10,000 random rollouts of the environment.
- **p. 4 / 3.1. World Model for Feature Extraction - extractive body cue:** We use this dataset to train V to learn a latent space of each frame observed.
- **p. 7 / 4.2. Procedure - extractive body cue:** In this simulation, we do not need the V model to encode any real pixel frames during the hallucination process, so our agent will therefore ...
- **p. 7 / 4.1. Learning Inside of a Dream - extractive body cue:** Each rollout of the environment runs for a maximum of 2100 time steps (∼60 seconds), and the task is considered solved if the average survival ...
- **p. 5 / 3.1. World Model for Feature Extraction - extractive body cue:** Its task is simply to compress and predict the sequence of image frames observed.
- **p. 5 / 3.1. World Model for Feature Extraction - extractive body cue:** Only the Controller (C) Model has access to the reward information from the environment.
- **p. 6 / 4.1. Learning Inside of a Dream - extractive body cue:** We have just seen that a policy learned inside of the real environment appears to somewhat function inside of the dream environment.
- **p. 6 / 4.1. Learning Inside of a Dream - extractive body cue:** This begs the question - can we train our agent to learn inside of its own dream, and transfer this policy back to the actual ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. A World Model, from Scott McCloud's Understanding Comics. (McCloud, 1993; E, 2012) current motor actions (Keller et al., 2012; Leinweber et al., 2017). ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 2. What we see is based on our brain's prediction of the future (Kitaoka, 2002; Watanabe et al., 2018).
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 3. In this work, we build probabilistic generative models of OpenAI Gym environments. The RNN-based world models are trained using collected observations recorded from ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 4. Our agent consists of three components that work closely together: Vision (V), Memory (M), and Controller (C)
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 5. Flow diagram of a Variational Autoencoder (VAE). Here, we use a simple Variational Autoencoder (Kingma & Welling, 2013; Rezende et al., 2014) as ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 6. RNN with a Mixture Density Network output layer. The MDN outputs the parameters of a mixture of Gaussian distribution used to sample a ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 7. SketchRNN (Ha & Eck, 2017) is an example of a MDN- RNN used to predict the next pen strokes of a sketch drawing. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 8. Flow diagram of our Agent model. The raw observation is first processed by V at each time step t to produce zt. The ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To train our V model, we first collect a dataset of 10,000 random rollouts of the environment. | embodiment, simulator version and control stack | p. 4 (3.1. World Model for Feature Extraction), p. 4 (3.1. World Model for Feature Extraction) |
| Task/environment | We use this dataset to train V to learn a latent space of each frame observed. | reset, timeout, object/scene variation | p. 4 (3.1. World Model for Feature Extraction), p. 7 (4.2. Procedure) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 5 (V Model Only), p. 3 (2.3. Controller (C) Model) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 3 (2.3. Controller (C) Model), p. 2 (2.1. VAE (V) Model) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Using this pre-processed data, along with the recorded random actions at taken, our MDN-RNN can now be trained to model P(zt+1 / at, zt, ... | definition/direction/unit from same section | p. 4 (3.1. World Model for Feature Extraction) |
| Figure 25. Histogram of cumulative rewards. Score is 906 ± 21. We also experimented with an agent that has access to only the z ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| In this environment, the tracks are randomly generated for each trial, and our agent is rewarded for visiting as many tiles as possible in ... | definition/direction/unit from same section | p. 4 (3.1. World Model for Feature Extraction) |
| Use CMA-ES to solve for a Wc and bc that maximizes the expected cumulative reward. | definition/direction/unit from same section | p. 5 (3.2. Procedure) |
| Only the Controller (C) Model has access to the reward information from the environment. | definition/direction/unit from same section | p. 5 (3.1. World Model for Feature Extraction) |
| There are no explicit rewards in this environment, so to mimic natural selection, the cumulative reward can be defined to be the number of ... | definition/direction/unit from same section | p. 7 (4.1. Learning Inside of a Dream) |
| Figure 16. Deploying our policy learned inside of the dream RNN environment back into the actual VizDoom environment. We took the agent trained inside ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 2. Take Cover scores at various temperature settings. We see that while increasing the temperature of the M model makes it more difficult ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We can also train individual VAE and MDN-RNN models without having to exhaustively tune hyperparameters. | comparison identity and matched condition | p. 4 (3.1. World Model for Feature Extraction) |
| Figure 1. A World Model, from Scott McCloud's Understanding Comics. (McCloud, 1993; E, 2012) current motor actions (Keller et al., 2012; Leinweber et al., ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We can also train individual VAE and MDN-RNN models without having to exhaustively tune hyperparameters. | component/input/data sensitivity | p. 4 (3.1. World Model for Feature Extraction) |
| Figure 1. A World Model, from Scott McCloud's Understanding Comics. (McCloud, 1993; E, 2012) current motor actions (Keller et al., 2012; Leinweber et al., ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Figure 4. Our agent consists of three components that work closely together: Vision (V), Memory (M), and Controller (C) | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Figure 18. Agent discovers an adversarial policy to automatically extinguish fireballs after they are fired during some rollouts. This weakness could be the reason ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We use similar terminology and notation as On Learning to Think: Algorithmic Information Theory for Novel Combinations of RL Controllers and RNN World Models ... | Figure 11. Limiting our controller to see only zt, but not ht results in wobbly and unstable driving behaviours. Although the agent is still ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 4 (3.1. World Model for Feature Extraction), p. 4 (3. Car Racing Experiment), p. 6 (Figure/Table caption), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption) |
| Primary metric/result | 3In principle, we can train both models together in an end-toend manner, although we found that training each separately is more practical, and also ... | numeric claim only at cited anchor | p. 4 (3.1. World Model for Feature Extraction) |

- Numeric sentences retained from the body:
- **p. 5 / 3.1. World Model for Feature Extraction - extractive body cue:** Since there are a mere 867 parameters inside the linear controller model, evolutionary algorithms such as CMA-ES are well suited for this optimization task.
- **p. 5 / 3.2. Procedure - extractive body cue:** Collect 10,000 rollouts from a random policy.
- **p. 7 / 4.2. Procedure - extractive body cue:** Collect 10,000 rollouts from a random policy.
- **p. 5 / V Model Only - extractive body cue:** This handicapped agent achieved an average score of 632 ± 251 over 100 random trials, in line with the performance of other agents on OpenAI ...
- **p. 5 / V Model Only - extractive body cue:** Adding a hidden layer to C's policy network helps to improve the results to 788 ± 141, but not quite enough to solve this environment.
- **p. 6 / V Model Only - extractive body cue:** SCORE DQN (PRIEUR, 2017) 343 ± 18 A3C (CONTINUOUS) (JANG ET AL., 2017) 591 ± 45 A3C (DISCRETE) (KHAN & ELIBOL, 2016) 652 ± 10 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | After all, unsupervised learning cannot, by definition, know what will be useful for the task at hand. | p. 12 (7. Discussion) |
| body limitation/failure cue | The choice of using a VAE for the V model and training it as a standalone model also has its limitations, since it may ... | p. 12 (7. Discussion) |
| body limitation/failure cue | Experiments with those more general approaches are left for future work. | p. 13 (7. Discussion) |
| body limitation/failure cue | Figure 11. Limiting our controller to see only zt, but not ht results in wobbly and unstable driving behaviours. Although the agent is still ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Figure 17. An interactive VAE of Doom in the online article. We see that even though the V model is not able to capture ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | After all, our agent does not directly observe the reality, but only sees what the world model lets it see. | p. 6 (4.1. Learning Inside of a Dream) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training each model only required less than an hour of computation time on a single GPU. | p. 4 (3.1. World Model for Feature Extraction) |
| We can also train individual VAE and MDN-RNN models without having to exhaustively tune hyperparameters. | p. 4 (3.1. World Model for Feature Extraction) |
| Train VAE (V) to encode frames into z ∈R32. | p. 5 (3.2. Procedure) |
| To summarize the Car Racing experiment, below are the steps taken: 1. | p. 5 (3.2. Procedure) |
| Our agent achieved a score of ∼900 time steps in the virtual environment. | p. 7 (4.3. Training Inside of the Dream) |
| There are no explicit rewards in this environment, so to mimic natural selection, the cumulative reward can be defined to be the number of ... | p. 7 (4.1. Learning Inside of a Dream) |
| The score over 100 random consecutive trials is ∼1100 time steps, far beyond the required score of 750 time steps, and also much higher ... | p. 8 (4.4. Transfer Policy to Actual Environment) |
| It also has a memory component that makes predictions about future codes based on historical information. | p. 2 (2. Agent Model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / 7. Discussion - extractive body cue:** After all, unsupervised learning cannot, by definition, know what will be useful for the task at hand.
- **p. 12 / 7. Discussion - extractive body cue:** The choice of using a VAE for the V model and training it as a standalone model also has its limitations, since it may encode ...
- **p. 13 / 7. Discussion - extractive body cue:** Experiments with those more general approaches are left for future work.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 11. Limiting our controller to see only zt, but not ht results in wobbly and unstable driving behaviours. Although the agent is still able ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 17. An interactive VAE of Doom in the online article. We see that even though the V model is not able to capture all ...
- **p. 6 / 4.1. Learning Inside of a Dream - extractive body cue:** After all, our agent does not directly observe the reality, but only sees what the world model lets it see.

- **Evidence anchors reviewed:** datasets p. 4 (3.1. World Model for Feature Extraction), p. 4 (3.1. World Model for Feature Extraction), p. 7 (4.2. Procedure), p. 7 (4.1. Learning Inside of a Dream), p. 5 (3.1. World Model for Feature Extraction), p. 5 (3.1. World Model for Feature Extraction), metrics p. 4 (3.1. World Model for Feature Extraction), p. 15 (Figure/Table caption), p. 4 (3.1. World Model for Feature Extraction), p. 5 (3.2. Procedure), p. 5 (3.1. World Model for Feature Extraction), p. 7 (4.1. Learning Inside of a Dream), baselines p. 4 (3.1. World Model for Feature Extraction), p. 1 (Figure/Table caption), results p. 5 (Figure/Table caption), p. 4 (3.1. World Model for Feature Extraction), p. 4 (3. Car Racing Experiment), p. 6 (Figure/Table caption), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 11. Limiting our controller to see only zt, but not ht results in wobbly and unstable driving behaviours. Although the agent is still able to navigate the race track ... (p. 5, Figure/Table caption).
- **Metric evidence:** Using this pre-processed data, along with the recorded random actions at taken, our MDN-RNN can now be trained to model P(zt+1 / at, zt, ht) as a mixture of Gaussians.3 ... (p. 4, 3.1. World Model for Feature Extraction).
- **Baseline/ablation evidence:** We can also train individual VAE and MDN-RNN models without having to exhaustively tune hyperparameters. (p. 4, 3.1. World Model for Feature Extraction).
- **Failure/negative evidence:** For instance, it reproduced unimportant detailed brick tile patterns on the side walls in the Doom environment, but failed to reproduce task-relevant tiles on the road in the Car Racing ... (p. 12, 7. Discussion).
