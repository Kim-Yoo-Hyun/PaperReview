# MultiPLY: A Multisensory Object-Centric Embodied Large Language Model in 3D World

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: LLM, 3D Vision, sensor fusion
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Looking ahead, challenges inevitably exist for building embodied multisensory large language models.를 문제로 두고, To sum up, the contributions of this paper are: • We propose Multisensory Universe, a large-scale multisensory dataset comprising 500k data collected by an agent engaging with the 3D embodied environment, covering ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Human beings possess the capability to multiply a m´elange of multisensory cues while actively exploring and interacting with the 3D world.
- **p. 1 / Abstract - extractive body cue:** Current multi-modal large language models, however, passively absorb sensory data as inputs, lacking the capacity to actively interact with the objects in the 3D environment ...
- **p. 1 / Abstract - extractive body cue:** To usher in the study of this area, we propose MultiPLY, a multisensory embodied large language model that could incorporate multisensory interactive data, including visual, ...
- **p. 1 / Abstract - extractive body cue:** To this end, we first collect Multisensory Universe, a large-scale multisensory interaction dataset comprising 500k data by deploying an LLM-powered embodied agent to engage with ...
- **p. 1 / Abstract - extractive body cue:** To perform instruction tuning with pretrained LLM on such generated data, we first encode the 3D scene as abstracted object-centric representations, and then introduce action ...
- **p. 2 / 1. Introduction - extractive body cue:** Looking ahead, challenges inevitably exist for building embodied multisensory large language models.
- **p. 2 / 1. Introduction - extractive body cue:** The first challenge resides in the paucity of multisensory interaction data for training such an LLM.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To sum up, the contributions of this paper are: • We propose Multisensory Universe, a large-scale multisensory dataset comprising 500k data collected by an agent ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose MultiPLY, a multisensory embodied LLM that could encode multisensory object-centric representations, including visual, audio, tactile, and thermal information, by deploying ...
- **p. 5 / 4.4. Training & Inference - extractive body cue:** Our training loss consists of two parts.
- **p. 5 / 4.2. Action Tokens - extractive body cue:** Note that the navigation action could be executed by any pre-defined pathfinder module and is not the research focus of this paper. • <OBSERVE> token ...
- **p. 5 / 4.4. Training & Inference - extractive body cue:** Model Architecture We use LLaVA [37] as our backbone multi-modal large language model.
- **p. 6 / 4.4. Training & Inference - extractive body cue:** Inference At the inference time, our MultiPLY first takes the task prompt and abstracted scene representation as inputs and generates subsequent tokens.
- **p. 6 / 4.4. Training & Inference - extractive body cue:** We use FSDP on 128 V100 GPUS for efficient training.
- **p. 4 / 4.2. Action Tokens - extractive body cue:** The object is chosen by the attention between the language features (i.e., the last hidden state of the LLM of the SELECT token), and the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To sum up, the contributions of this paper are: • We propose Multisensory Universe, a large-scale multisensory dataset comprising 500k data collected by an agent engaging with the 3D embodied environment, covering ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | contributions, Multisensory, Universe, large-scale, dataset, comprising, data, collected, agent, engaging, embodied, environment | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.4. Training & Inference) |
| Output/action | In the inference time, MultiPLY could generate a series of action tokens through the LLM, instructing the agent to take the action and receive the outcome of the action as the next-state ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 6 (4.4. Training & Inference), p. 5 (4.2. Action Tokens) |
| Objective/outcome | The feature goes through a Sigmoid layer, and is optimized with a binary cross entropy (BCE) loss. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (4.4. Training & Inference), p. 5 (4.4. Training & Inference), p. 5 (4.4. Training & Inference) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To sum up, the contributions of this paper are: • We propose Multisensory Universe, a large-scale multisensory dataset comprising 500k data collected by an agent ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose MultiPLY, a multisensory embodied LLM that could encode multisensory object-centric representations, including visual, audio, tactile, and thermal information, by deploying ...
- **p. 5 / 4.4. Training & Inference - extractive body cue:** Our training loss consists of two parts.
- **p. 5 / 4.2. Action Tokens - extractive body cue:** Note that the navigation action could be executed by any pre-defined pathfinder module and is not the research focus of this paper. • <OBSERVE> token ...
- **p. 6 / 5.1. Object Retrieval - extractive body cue:** The select action could be achieved by calculating the similarity between the object embedding and the language embedding, and the object with the highest score ...
- **p. 8 / 5.4. Task Decomposition - extractive body cue:** Note that there is a domain gap between the task decomposition data 3D-LLM was trained on and our setting, which yields almost zero success rates ...
- **p. 8 / 5.4. Task Decomposition - extractive body cue:** For each baseline we have two variants: 1) wo Interaction: generate all actions all at once, and execute the actions sequentially in the environment; 2) ...
- **p. 7 / 5.1. Object Retrieval - extractive body cue:** Third, LLMs outperform similarity-based retrieval models.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (5.1. Object Retrieval), p. 8 (5.4. Task Decomposition) |
| Embodiment/environment | As presented in Figure 2, we begin by explaining how we input interactive objects into the scene to construct object-centric 3D scenes for our dataset in Section 3.1. | hardware/simulator version and reset protocol | p. 3 (3. The Multisensory-Universe Dataset), p. 3 (3.1. Inputting Interactive Objects into 3D Scenes) |
| Dataset/benchmark | We ensure that no scenes and objects in the Multisensory Universe appear in the evaluation setup. | role, split, size and leakage | p. 3 (3. The Multisensory-Universe Dataset), p. 3 (3.1. Inputting Interactive Objects into 3D Scenes), p. 6 (5. Experiments), p. 6 (5.1. Object Retrieval) |
| Metric | Note that there is a domain gap between the task decomposition data 3D-LLM was trained on and our setting, which yields almost zero success rates of 3D-LLM without finetuning. | definition, denominator, direction and uncertainty | p. 8 (5.4. Task Decomposition), p. 8 (5.4. Task Decomposition), p. 6 (5.1. Object Retrieval) |
| Baseline/ablation | In general, our MultiPLY outperforms the baseline models a lot. | fair input/data/compute/action matching | p. 7 (5.1. Object Retrieval), p. 6 (5.1. Object Retrieval), p. 6 (5.1. Object Retrieval) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** One limitation of our model is that currently MultiPLY does not involve detailed navigation and control policy, but utilizes pre-defined policies for carrying out the ...
- **p. 6 / 5.1. Object Retrieval - extractive body cue:** As these models cannot interact with the environment to get the tactile, impact sound, and temperature data, we refine three setups for the baselines: 1) ...
- **p. 7 / 5.1. Object Retrieval - extractive body cue:** Second, 3Dbased models surpass 2D models, mainly because singleview images sometimes fail to provide enough information to reason about the objects due to view inconsistency ...
- **p. 7 / 5.3. Multisensory Captioning - extractive body cue:** LLaVA and 3D-LLM take the holistic representation as inputs, and thus fail to compete with models that could interact with the models to switch between ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Looking ahead, challenges inevitably exist for building embodied multisensory large language models.를 문제로 두고, To sum up, the contributions of this paper are: • We propose Multisensory Universe, a large-scale multisensory dataset comprising 500k data collected by an agent engaging with the 3D embodied environment, covering ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.4. Training & Inference), p. 5 (4.4. Training & Inference), p. 6 (4.4. Training & Inference), p. 6 (4.4. Training & Inference) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
