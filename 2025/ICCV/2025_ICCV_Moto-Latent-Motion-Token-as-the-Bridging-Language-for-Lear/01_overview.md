# Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 The main challenge is finding an appropriate representation for autoregressive pre-training on video data that effectively captures prior knowledge for robot manipulation.를 문제로 두고, In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving as a bridging "language" for autoregressive pre-training ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent developments in Large Language Models (LLMs) pre-trained on extensive corpora have shown significant success in various natural language processing (NLP) tasks with minimal fine-tuning.
- **p. 1 / Abstract - extractive body cue:** This success offers new promise for robotics, which has long been constrained by the high cost of action-labeled data.
- **p. 1 / Abstract - extractive body cue:** We ask: given the abundant video data containing interaction-related knowledge available as a rich "corpus", can a similar generative pretraining approach be effectively applied to ...
- **p. 1 / Abstract - extractive body cue:** The key challenge is to identify an effective representation for autoregressive pre-training that benefits robot manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** Inspired by the way humans learn new skills through observing dynamic environments, we propose that effective robotic learning should emphasize motion-related knowledge, which is closely ...
- **p. 2 / 1. Introduction - extractive body cue:** The main challenge is finding an appropriate representation for autoregressive pre-training on video data that effectively captures prior knowledge for robot manipulation.
- **p. 2 / 1. Introduction - extractive body cue:** These learned priors are subsequently transferred to enhance robot manipulation performance through a co-fine-tuning strategy.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving ...
- **p. 3 / 3.1. Overview - extractive body cue:** 2, Moto consists of three stages: 1) unsupervised training of the Latent Motion Tokenizer, 2) pre-training of the generative model MotoGPT, and 3) co-fine-tuning for ...
- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive body cue:** To address this, during fine-tuning, we introduce special action query tokens into Moto-GPT's input, enabling the generation of real robot actions through a flexible action ...
- **p. 2 / 1. Introduction - extractive body cue:** The performance can be further boosted with human video pre-training, highlighting the potential of our approach in transferring motion knowledge learned from Internet-scale videos to ...
- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive body cue:** The total action loss Laction is defined as: \math c al {L } _{act i on} = \mathcal {L} (\Delta x) + \mathcal {L} (\Delta ...
- **p. 4 / 3.2. Latent Motion Tokenizer - extractive body cue:** For de-tokenization, we use a ViT Decoder for image reconstruction, which takes the linearly embedded patches of o_{t-1} and recovers the pixel values for o_ ...
- **p. 3 / 3.2. Latent Motion Tokenizer - extractive body cue:** The output query features are then processed by a VQ codebook with a vocabulary size of 128 to produce discrete latent motion tokens.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | An MLP-based action head projects the output hidden state of each action query token into the real robot action space. | image/video, language instruction, proprioception과 history | p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 2 (1. Introduction) |
| State/latent | MLP-based, action, head, projects, output, hidden, state, query, token, real, robot, space | language-grounded task state와 action-policy context | p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 2 (1. Introduction), p. 4 (3.3. Motion Token Autoregressive Pre-training) |
| Output/action | In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving as a bridging "language" for autoregressive pre-training ... | continuous action, pose 또는 action chunk | p. 2 (1. Introduction), p. 4 (3.3. Motion Token Autoregressive Pre-training), p. 3 (3.1. Overview) |
| Objective/outcome | The total action loss Laction is defined as: \math c al {L } _{act i on} = \mathcal {L} (\Delta x) + \mathcal {L} (\Delta \theta ) + \mathcal {L} (\Delta grip) ... | instruction following, task success, generalization과 latency | p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 4 (3.3. Motion Token Autoregressive Pre-training) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving ...
- **p. 3 / 3.1. Overview - extractive body cue:** 2, Moto consists of three stages: 1) unsupervised training of the Latent Motion Tokenizer, 2) pre-training of the generative model MotoGPT, and 3) co-fine-tuning for ...
- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive body cue:** To address this, during fine-tuning, we introduce special action query tokens into Moto-GPT's input, enabling the generation of real robot actions through a flexible action ...
- **p. 2 / 1. Introduction - extractive body cue:** The performance can be further boosted with human video pre-training, highlighting the potential of our approach in transferring motion knowledge learned from Internet-scale videos to ...
- **p. 7 / 5.3. Moto-GPT as an Effective Robot Policy - extractive body cue:** 8, Moto-GPT consistently outperforms Moto w/o Motion Token on these tasks, improving the average success rate from 23.33% to Moto w/o Motion Token Moto (OXE) ...
- **p. 8 / 5.3. Moto-GPT as an Effective Robot Policy - extractive body cue:** For instance, Moto-GPT achieves a 52.5% success rate with just 1% of labeled data, compared to 0% for the variant.
- **p. 6 / 5.3. Moto-GPT as an Effective Robot Policy - extractive body cue:** It significantly outperforms Moto w/o Motion Token, which is trained from scratch without latent motion tokens, underscoring the effectiveness of transferring motion priors learned from ...
- **p. 7 / 5.3. Moto-GPT as an Effective Robot Policy - extractive body cue:** With additional human video (SSV2) pre-training, Moto (OXE+SSV2) significantly outperforms both Moto w/o Motion Token and Moto (OXE) on the Move Near task in SIMPLER.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |
| Embodiment/environment | We conduct real-world evaluations with a FANUC LR Mate 200iD robot on three tasks: "pick-place banana", "close laptop", and "disassembly" (Fig. | hardware/simulator version and reset protocol | p. 5 (4. Benchmarks and Datasets), p. 5 (4. Benchmarks and Datasets) |
| Dataset/benchmark | It also maintains competitiveness against OpenVLA (finetuned), which is further fine-tuned specially on the RT-1 Robot-Action trajectories, despite its pre-training data already containing action labels from this dataset. | role, split, size and leakage | p. 5 (4. Benchmarks and Datasets), p. 5 (4. Benchmarks and Datasets), p. 6 (5.3. Moto-GPT as an Effective Robot Policy), p. 7 (5.3. Moto-GPT as an Effective Robot Policy) |
| Metric | The "Overall" column reports the success rate averaged across the sub-tasks of all task types. | definition, denominator, direction and uncertainty | p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |
| Baseline/ablation | Figure 8. Evaluation results in the real-world environment. also generalizes well in the unseen CALVIN environment, outperforming baseline models that use various pre-training strategies (see supplementary material for detailed descrip- ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 6 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 5.2. Moto-GPT as a Useful Motion Prior Learner - extractive body cue:** 7, clearly differentiate successful trajectories from failures and random attempts.
- **p. 6 / 5.2. Moto-GPT as a Useful Motion Prior Learner - extractive body cue:** The top-k token prediction accuracy and the visualization of predicted video trajectories 20 40 60 80 Sequence Step 5.0 4.5 4.0 3.5 Log Likelihood ( ...
- **p. 8 / 5.3. Moto-GPT as an Effective Robot Policy - extractive body cue:** Future work will improve model architectures and incorporate more diverse human videos to tackle complex manipulation tasks.
- **p. 7 / 5.3. Moto-GPT as an Effective Robot Policy - extractive body cue:** This further demonstrates the robustness of MotoGPT in real-world deployment.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 9. With additional human video (SSV2) pre-training, Moto (OXE+SSV2) significantly outperforms both Moto w/o Motion Token and Moto (OXE) on the Move Near task ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 The main challenge is finding an appropriate representation for autoregressive pre-training on video data that effectively captures prior knowledge for robot manipulation.를 문제로 두고, In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving as a bridging "language" for autoregressive pre-training ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 4 (3.2. Latent Motion Tokenizer), p. 3 (3.2. Latent Motion Tokenizer) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
