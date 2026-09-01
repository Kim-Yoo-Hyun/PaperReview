# Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Lookahead_Exploration_with_Neural_Radiance_Representation_for_Continuous_Vision-Language_Navigation_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_Lookahead_Exploration_with_Neural_Radiance_Representation_for_Continuous_Vision-Language_Navigation_CVPR_2024_paper.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: NEXT
- Tags: Vision-Language Navigation, NeRF, Planning
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Lookahead_Exploration_with_Neural_Radiance_Representation_for_Continuous_Vision-Language_Navigation_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_Lookahead_Exploration_with_Neural_Radiance_Representation_for_Continuous_Vision-Language_Navigation_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 navigation 문제를 이해하기 위해 읽는다. 본문은 First, our model directly predicts robust multi-level semantic features for future candidate locations, avoiding the difficulty of pixel-level image reconstruction in unseen environments as used in existing methods like RNR-Map [24, 35] ...를 문제로 두고, In this work, our main contributions include: • We propose a hierarchical neural radiance representation model to produce multi-level semantic representations for future environments with better quality and efficiency. • Utilizing predi ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-and-language navigation (VLN) enables the agent to navigate to a remote location following the natural language instruction in 3D environments.
- **p. 1 / Abstract - extractive body cue:** At each navigation step, the agent selects from possible candidate locations and then makes the move.
- **p. 1 / Abstract - extractive body cue:** For better navigation planning, the lookahead exploration strategy aims to effectively evaluate the agent's next action by accurately anticipating the future environment of candidate locations.
- **p. 1 / Abstract - extractive body cue:** To this end, some existing works predict RGB images for future environments, while this strategy suffers from image distortion and high computational cost.
- **p. 1 / Abstract - extractive body cue:** To address these issues, we propose the pre-trained hierarchical neural radiance representation model (HNR) to produce multi-level semantic features for future environments, which are more ...
- **p. 2 / 1. Introduction - extractive body cue:** First, our model directly predicts robust multi-level semantic features for future candidate locations, avoiding the difficulty of pixel-level image reconstruction in unseen environments as used ...
- **p. 1 / 1. Introduction - extractive body cue:** This phenomenon raises a challenge to accurately represent future environments with visual occlusions, leading to incorrect action decisions.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this work, our main contributions include: • We propose a hierarchical neural radiance representation model to produce multi-level semantic representations for future environments with ...
- **p. 2 / 1. Introduction - extractive body cue:** The advantages of our method over previous methods for future environment prediction are three-fold.
- **p. 3 / 3.2. Hierarchical Neural Radiance Representation - extractive body cue:** Through the downsized depth images {dt,i ∈RH×W }12 i=1, each grid feature gt,j ∈RD is mapped to its 3D world position Pt,j = [px, py, ...
- **p. 5 / 3.2. Hierarchical Neural Radiance Representation - extractive body cue:** The view encoder consists of four-layer transformers.
- **p. 5 / 3.3. Architecture of the Lookahead VLN model - extractive body cue:** Each transformer layer consists of a cross-attention layer and a graph-aware self-attention layer (GASA).
- **p. 5 / 3.2. Hierarchical Neural Radiance Representation - extractive body cue:** During training, we randomly sample some region features and then minimize the loss between predicted features and actual CLIP embeddings, by maximizing cosine similarity as ...
- **p. 4 / 3.2. Hierarchical Neural Radiance Representation - extractive body cue:** Then a MLPfeature network is used to aggregate the k-nearest features of Pn within radius R to produce a latent vector rn ∈RD and the ...
- **p. 4 / 3.2. Hierarchical Neural Radiance Representation - extractive body cue:** To enhance interaction among different region features, we use both region-level semantic alignment Lregion and view-level semantic alignment Lview after view level encoding in Section ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | together with a learnable view token V is inputted into the view encoder and output the encoded ˆR and ˆV. | camera/depth stream, pose, map와 language goal | p. 5 (3.2. Hierarchical Neural Radiance Representation), p. 6 (3.3. Architecture of the Lookahead VLN model) |
| State/latent | together, learnable, view, token, inputted, encoder, output, encoded, Lookahead, Exploration, Action, Prediction | robot pose, free-space/semantic map와 local goal | p. 5 (3.2. Hierarchical Neural Radiance Representation), p. 6 (3.3. Architecture of the Lookahead VLN model), p. 3 (3.2. Hierarchical Neural Radiance Representation) |
| Output/action | 3.3.3 Lookahead Exploration and Action Prediction The model predicts a navigation goal score for each node in the topological map as follows: S = FFN(ˆV) (14) where FFN denotes a feed-forward network. | collision-free trajectory 또는 velocity command | p. 6 (3.3. Architecture of the Lookahead VLN model), p. 3 (3.2. Hierarchical Neural Radiance Representation), p. 2 (1. Introduction) |
| Objective/outcome | During training, we randomly sample some region features and then minimize the loss between predicted features and actual CLIP embeddings, by maximizing cosine similarity as follows: Lregion = X h,w (1 - ... | goal reach, safety, localization error와 replanning latency | p. 5 (3.2. Hierarchical Neural Radiance Representation), p. 5 (3.2. Hierarchical Neural Radiance Representation), p. 6 (3.3. Architecture of the Lookahead VLN model) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In this work, our main contributions include: • We propose a hierarchical neural radiance representation model to produce multi-level semantic representations for future environments with ...
- **p. 2 / 1. Introduction - extractive body cue:** The advantages of our method over previous methods for future environment prediction are three-fold.
- **p. 3 / 3.2. Hierarchical Neural Radiance Representation - extractive body cue:** Through the downsized depth images {dt,i ∈RH×W }12 i=1, each grid feature gt,j ∈RD is mapped to its 3D world position Pt,j = [px, py, ...
- **p. 5 / 3.2. Hierarchical Neural Radiance Representation - extractive body cue:** The view encoder consists of four-layer transformers.
- **p. 5 / 3.3. Architecture of the Lookahead VLN model - extractive body cue:** Each transformer layer consists of a cross-attention layer and a graph-aware self-attention layer (GASA).
- **p. 6 / 4.2. Comparison to State-of-the-Art Methods - extractive body cue:** Compared with DREAMWALKER [39] in Table 1, which adopts a similar idea of lookahead exploration, our HNR model achieves performance improvement of about 10% on ...
- **p. 6 / 4.2. Comparison to State-of-the-Art Methods - extractive body cue:** Meanwhile, as illustrated in Table 2, the proposed method also achieves the improvement of 2% in the majority of metrics on the RxR-CE dataset.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Row 2 doesn't use the lookahead node scores to evaluate the future paths and gain marginal performance improvement, confirming the necessity of the lookahead node ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 6 (4.2. Comparison to State-of-the-Art Methods) |
| Embodiment/environment | As illustrated in Table 1, for the val unseen split of the R2R-CE dataset, our model outperforms our baseline method ETPNav [9] by 4% on SR and 2% on SPL. | hardware/simulator version and reset protocol | p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 7 (4.3. Ablation Study) |
| Dataset/benchmark | The effect of different numbers of nearest features in the HNR model on the val unseen split of the R2R-CE dataset. | role, split, size and leakage | p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study) |
| Metric | There are several standard metrics [5] in VLN for evaluating the agent's performance, including Trajectory Length (TL), Navigation Error (NE), Success Rate (SR), SR given the Oracle stop policy (OSR), Normalized inverse ... | definition, denominator, direction and uncertainty | p. 6 (4.1. Datasets and Evaluation Metrics), p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 7 (4.3. Ablation Study) |
| Baseline/ablation | As illustrated in Table 1, for the val unseen split of the R2R-CE dataset, our model outperforms our baseline method ETPNav [9] by 4% on SR and 2% on SPL. | fair input/data/compute/action matching | p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.3. Ablation Study - extractive body cue:** Without the position and orientation of the k-nearest features relative to the sampled point (row 7) in Table 3, MLPfeature network cannot accurately estimate the ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** The lookahead node closest to the destination (i.e., Hard target) is not sure of the highest semantic match score with the instruction due to visual ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of different methods to represent the naviga- ble candidate locations. (a) uses the single-view observation (yel- low sector area). (b) uses the ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Hierarchical encoding and multi-level semantic alignment help HNR integrate surrounding contexts and predict features of empty regions caused by visual occlusions.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** As shown in Table 3, without the training objective Lregion of region-level semantic alignment (row 6) in Section 3.2.3, the performance of the HNR model ...

## Why Read It

Planning and control의 navigation 문제를 이해하기 위해 읽는다. 본문은 First, our model directly predicts robust multi-level semantic features for future candidate locations, avoiding the difficulty of pixel-level image reconstruction in unseen environments as used in existing methods like RNR-Map [24, 35] ...를 문제로 두고, In this work, our main contributions include: • We propose a hierarchical neural radiance representation model to produce multi-level semantic representations for future environments with better quality and efficiency. • Utilizing predi ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.2. Hierarchical Neural Radiance Representation), p. 4 (3.2. Hierarchical Neural Radiance Representation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
