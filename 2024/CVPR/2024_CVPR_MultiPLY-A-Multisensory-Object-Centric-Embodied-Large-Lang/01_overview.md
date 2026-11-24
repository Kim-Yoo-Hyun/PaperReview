# MultiPLY: A Multisensory Object-Centric Embodied Large Language Model in 3D World

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Yining Hong, Zishuo Zheng, Peihao Chen, Yian Wang, Junyan Li, Chuang Gan
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: LLM, 3D Vision, sensor fusion
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf)

## Why This Paper Is Here

MultiPLY는 실내 장면에서 물체에 행동을 가한 뒤 얻는 시각·소리·촉각·온도 정보를 언어 모델의 물체 중심 표현에 반영한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf#page=3)

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

- 스캔 장면과 물체 자산에 상호작용 및 감각 정보를 결합해 Multisensory Universe 자료를 구성하고 행동과 관측 상태를 토큰으로 표현한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf#page=5)
- 여러 감각을 이용하는 물체 검색, 도구 사용과 질의 등에서 상호작용과 감각 입력의 기여를 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf#page=8)

## Evaluation Scope

Multisensory Universe는 실내 스캔에 배치한 물체와 시뮬레이션 상호작용을 사용한다. 촉각 표식의 변위는 DiffTactile로 생성하고 각 물체의 온도 값은 온도 라벨을 조건으로 언어 모델에 질의해 부여했다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.pdf#page=4)

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** One limitation of our model is that currently MultiPLY does not involve detailed navigation and control policy, but utilizes pre-defined policies for carrying out the ...
- **p. 6 / 5.1. Object Retrieval - extractive body cue:** As these models cannot interact with the environment to get the tactile, impact sound, and temperature data, we refine three setups for the baselines: 1) ...
- **p. 7 / 5.1. Object Retrieval - extractive body cue:** Second, 3Dbased models surpass 2D models, mainly because singleview images sometimes fail to provide enough information to reason about the objects due to view inconsistency ...
- **p. 7 / 5.3. Multisensory Captioning - extractive body cue:** LLaVA and 3D-LLM take the holistic representation as inputs, and thus fail to compete with models that could interact with the models to switch between ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 5 (4.4. Training & Inference), p. 6 (4.4. Training & Inference)이다.
