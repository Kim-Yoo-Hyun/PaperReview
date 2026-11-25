# Method - ViSPLA: Visual Iterative Self-Prompting for Language-Guided 3D Affordance Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://neurips.cc/virtual/2025/poster/119081; PDF retrieval source: https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): By injecting LLM reasoning into dense point features, our approach bridges high-level semantic understanding with low-level geometric representation. • We introduce an Implicit Neural Affordance Field technique that learns a ...

## Method Body Digest

- **p. 3 / 1 Introduction - extractive body cue:** By injecting LLM reasoning into dense point features, our approach bridges high-level semantic understanding with low-level geometric representation. • We introduce an Implicit Neural Affordance ...
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are: • We introduce Visual Iterative Self-Prompting for 3D Affordance Learning (ViSPLA), which leverages geometric features from predicted masks as visual ...
- **p. 1 / Abstract - extractive body cue:** This feedback is encoded into visual prompts that drive a multi-stage refinement decoder, enabling the model to self-correct and adapt to complex spatial structures.
- **p. 1 / 1 Introduction - extractive body cue:** Although conventional methodologies have predominantly focused on visual modalities, attempting to infer functionality from geometric structures or 2D visual features, such approaches inherently lack the ...
- **원문 대조:** 초기 affordance mask는 M_0=f_θ(P,L)이며, 이후 M_t=f_θ(P,G(M_{t−1}),L)로 갱신한다. G는 이전 mask에서 곡률·normal derivative 등의 기하 prompt를 추출한다. 이는 방법 정의이며 평가 수치는 아니다. ([PDF p. 2](https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf#page=2), §1 Introduction, iterative formulation).
- **p. 2 / 1 Introduction - extractive body cue:** This approach addresses several critical challenges in the field: (1) Existing single-pass inference methods lack the ability to iteratively refine predictions, often leading to suboptimal ...
- **p. 2 / 1 Introduction - extractive body cue:** Recent progress in Large Language Models (LLMs) has shown impressive capabilities in sequential reasoning and knowledge grounding [7], but these models are often decoupled from ...
- **p. 1 / Abstract - extractive body cue:** We redefine affordance detection as a language-conditioned segmentation task: given a 3D point cloud and language instruction, our model predicts a sequence of refined affordance ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are: • We introduce Visual Iterative Self-Prompting for 3D Affordance Learning (ViSPLA), which leverages geometric features from predicted masks as visual ...
- **p. 3 / 1 Introduction - extractive body cue:** Unlike existing single-pass methods, our approach establishes a self-improving cycle that enhances precision across multiple object geometries. • We propose a novel Differential Geometric Self-Prompting ...
- **p. 2 / 1 Introduction - extractive body cue:** Unlike prior approaches that perform singlepass inference, our method implements a closed-loop system where each predicted affordance mask is used to generate geometric self-prompts that ...

## Source Evidence Cues

- **p. 3 / 1 Introduction - extractive body cue:** By injecting LLM reasoning into dense point features, our approach bridges high-level semantic understanding with low-level geometric representation. • We introduce an Implicit Neural Affordance ...
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are: • We introduce Visual Iterative Self-Prompting for 3D Affordance Learning (ViSPLA), which leverages geometric features from predicted masks as visual ...
- **p. 1 / Abstract - extractive body cue:** This feedback is encoded into visual prompts that drive a multi-stage refinement decoder, enabling the model to self-correct and adapt to complex spatial structures.
- **p. 1 / 1 Introduction - extractive body cue:** Although conventional methodologies have predominantly focused on visual modalities, attempting to infer functionality from geometric structures or 2D visual features, such approaches inherently lack the ...
- **원문 대조:** 초기 affordance mask는 M_0=f_θ(P,L)이며, 이후 M_t=f_θ(P,G(M_{t−1}),L)로 갱신한다. G는 이전 mask에서 곡률·normal derivative 등의 기하 prompt를 추출한다. 이는 방법 정의이며 평가 수치는 아니다. ([PDF p. 2](https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf#page=2), §1 Introduction, iterative formulation).
- **p. 2 / 1 Introduction - extractive body cue:** This approach addresses several critical challenges in the field: (1) Existing single-pass inference methods lack the ability to iteratively refine predictions, often leading to suboptimal ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | By injecting LLM reasoning into dense point features, our approach bridges high-level semantic understanding with low-level geometric representation. • We introduce an ... | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In summary, our contributions are: • We introduce Visual Iterative Self-Prompting for 3D Affordance Learning (ViSPLA), which leverages geometric features from predicted ... | p. 3 (1 Introduction), p. 1 (Abstract) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | This feedback is encoded into visual prompts that drive a multi-stage refinement decoder, enabling the model to self-correct and adapt to complex ... | p. 1 (Abstract), p. 1 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** Recent progress in Large Language Models (LLMs) has shown impressive capabilities in sequential reasoning and knowledge grounding [7], but these models are often decoupled from ...
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are: • We introduce Visual Iterative Self-Prompting for 3D Affordance Learning (ViSPLA), which leverages geometric features from predicted masks as visual ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | redefine, affordance, detection, language-conditioned, segmentation, task, given, point, cloud, language, instruction, model, predicts, sequence | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | redefine, affordance, detection, language-conditioned, segmentation, task, given, point, cloud, language | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, introduce, Visual, Iterative, Self-Prompting, Affordance, Learning, ViSPLA, leverages | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Recent, progress, Large, Language, Models, LLMs, impressive, capabilities, sequential, reasoning | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** We redefine affordance detection as a language-conditioned segmentation task: given a 3D point cloud and language instruction, our model predicts a sequence of refined affordance ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose an iterative self-prompting-based 3D affordance detection paradigm that bridges the gap between language understanding and affordance segmentation through geometric feedback-driven ...
- **p. 2 / 1 Introduction - extractive body cue:** This formulation opens avenues for handling more diverse and complex scenarios-potentially allowing models to interpret novel affordance types via linguistic cues, handle multi-step tasks through ...
- **p. 1 / 1 Introduction - extractive body cue:** Affordance, initially conceptualized by Gibson [1], defines the potential action possibilities that objects present to an agent.
- **p. 3 / 1 Introduction - extractive body cue:** accuracy, especially in complex or ambiguous settings; (3) the disconnect between high-level language semantics and low-level geometric features, hindering precise and context-aware affordance prediction across ...
- **p. 3 / 1 Introduction - extractive body cue:** This approach enables more accurate affordance localization by incorporating intrinsic geometric cues rather than relying solely on language. • We develop a Multi-Stage Refinement Decoder ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Finally, unlike their static segmentation output, our Affordance Dictionary Adaptive Fusion fuses temporal and functional context across steps, enabling robust multi-stage affordance ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The process converges after T steps, enabling precise, language-guided 3D affordance segmentation MT through closed-loop geometric feedback. to generate a response sequence ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** This approach addresses several critical challenges in the field: (1) Existing single-pass inference methods lack the ability to iteratively refine predictions, often leading to suboptimal ...

## Method-Specific Formal Details

- **Body-defined terms:** injecting, LLM, reasoning, dense, point, features, bridges, high-level, semantic, understanding, low-level, geometric, representation, introduce, Implicit, Neural, Affordance, Field, technique, learns.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets. | p. 1 (Abstract), p. 1 (1 Introduction) |
| Action / skill decoding | Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets. | p. 1 (Abstract), p. 1 (Abstract) |
| Receding execution / feedback | Figure 4: Qualitative comparison of our affor- dance segmentation results with GEAL [5]. Our proposed framework achieves consistent and sub- stantial performance ... | p. 8 (Figure/Table caption), p. 1 (Abstract) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4. (3) The most substantial gains come from incorporating Iterative Differential Geometry-Based Self-Prompting (IDGSP), which provides a significant boost on LASO seen (+2.5 aIoU) ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Ablation study of different components. The best results are in bold. Type PIAD LASO IDGSP INAFS SCSP aIoU
- **p. 1 / Abstract - extractive body cue:** To further enhance precision and coherence, we introduce Implicit Neural Affordance Fields, which define continuous probabilistic regions over the 3D surface without additional supervision.
- **p. 3 / 1 Introduction - extractive body cue:** By injecting LLM reasoning into dense point features, our approach bridges high-level semantic understanding with low-level geometric representation. • We introduce an Implicit Neural Affordance ...
- **p. 3 / 1 Introduction - extractive body cue:** accuracy, especially in complex or ambiguous settings; (3) the disconnect between high-level language semantics and low-level geometric features, hindering precise and context-aware affordance prediction across ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative visualization of ablation
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Performance analysis (aIoU on "seen" setting) with varying T and K values. Following 3D-AffordanceLLM [6], we utilize Phi-3.5-mini-instruct [27] as our base LLM ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), objective p. 2 (1 Introduction), p. 3 (1 Introduction), temporal p. 4 (2 Related Work), p. 5 (2 Related Work), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (2 Related Work).
