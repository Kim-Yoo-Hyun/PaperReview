# Evaluation — EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: source PDF 또는 공식 full-text source의 problem/method formulation profile과 기존 evaluation cue를 결합해 구조화했다; exact evaluation table/page와 trial details는 원문 확인 필요. tracker의 reading status/evidence는 변경하지 않았다.

## Evaluation in One Sentence

현재 source cue에서 확인되는 evaluation은 geometric accuracy, semantic consistency와 planning/manipulation utility를 검증하는 범위이며, exact protocol과 result는 아래 audit에서 분리한다.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / LEARNING OR SIMULATION` (provisional; source body에서 확인 필요)
- **Target system/task:** 3D scene/object와 robot coordinate frame
- **Input/observation boundary:** RGB-D, image set, point cloud, depth와 camera pose
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility
- **Scope rule:** theory/formulation papers use assumptions, theorem/analytic examples or controller behavior; empirical papers use matched task/data/baseline/trial records; benchmark papers use task/protocol/score definitions.

## Experimental Matrix

| Experiment / claim | Type & setting | Dataset / split | Robot / system | Baseline | Metric / result cue | Trials / seeds | Source |
|---|---|---|---|---|---|---|---|
| geometric accuracy, semantic consistency와 planning/manipulation utility | setting not found in current note | ScanNet; split/role unresolved | 3D scene/object와 robot coordinate frame | not found in current note | mIoU; To achieve these objectives, we propose an Online Sparse Coefficients Field with a CLIP Global Codebook where it binds the 2D CLIP embeddings to each 3D Gaussian while …. | trials: not reported; seeds: not reported | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |

## Dataset / Benchmark Role

| Resource | Role | Split / size | Source |
|---|---|---|---|
| ScanNet | legacy dataset/benchmark cue; train/eval/pretraining/auxiliary role unresolved | not reported | 04_evaluation.md `Dataset / Benchmark`; exact table/figure/page 확인 필요 |
| ScanNet200 | legacy dataset/benchmark cue; train/eval/pretraining/auxiliary role unresolved | not reported | 04_evaluation.md `Dataset / Benchmark`; exact table/figure/page 확인 필요 |
| Replica | legacy dataset/benchmark cue; train/eval/pretraining/auxiliary role unresolved | not reported | 04_evaluation.md `Dataset / Benchmark`; exact table/figure/page 확인 필요 |

- Dataset names found only by legacy keyword extraction are not accepted as verified evaluation datasets until their role is located in the experiment section.

## Embodiment / Environment

| Dimension | Recorded cue | Interpretation / missing detail | Source |
|---|---|---|---|
| Evaluation type | EMPIRICAL / LEARNING OR SIMULATION | provisional classification from current source cue; verify body | source cue / title/domain |
| Robot / simulator / hardware | robot/simulator platform not reported | reported status not fully resolved | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |
| Observation / sensor | RGB-D, image set, point cloud, depth와 camera pose | scope cue from problem profile; exact sensor/calibration verify | 02 problem scope |
| Control / inference rate | not reported | numeric value only if explicitly present | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |
| Task / episode unit | task/episode definition not found | task count, reset, timeout and denominator not reported unless stated | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |
| Generalization split/variation | generalization condition not found | split and unseen dimensions require body verification | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |

## Metrics and Success Definition

| Metric / success signal | Direction / unit | Status | Source |
|---|---|---|---|
| mIoU | direction/unit not reported | legacy keyword cue; metric role and direction not verified | 04_evaluation.md `Metrics`; exact table/figure/page 확인 필요 |
| mAP | direction/unit not reported | legacy keyword cue; metric role and direction not verified | 04_evaluation.md `Metrics`; exact table/figure/page 확인 필요 |
| geometric accuracy, semantic consistency and downstream planning/manipulation utility | direction/unit not reported | downstream metric target; not claimed as paper-reported metric | 02 problem scope; exact paper metric 확인 필요 |

- **Success/failure/timeout definition:** not reported in the current note unless stated above; exact denominator, collision/contact rule and termination condition require body verification.

## Baselines and Fairness

| Baseline / comparison cue | What it should isolate | Same data/observation/compute? | Source |
|---|---|---|---|
| not found in current note | comparison identity or claimed comparison | not reported | 04_evaluation.md `Baselines`; exact table/figure/page 확인 필요 |

**Baseline fairness audit**

| Fairness dimension | Current record | Required check |
|---|---|---|
| Observation/action interface | not reported | hold sensor modality, action space and preprocessing fixed |
| Data/pretraining | not reported | match demonstrations, pretraining and additional labels |
| Compute/runtime | not reported | match parameter budget, inference steps, latency and control rate |
| Evaluation protocol | not reported | match task split, reset/timeout, seeds and success denominator |

## Ablations and Sensitivity

| Ablation / sensitivity factor | Method component | Expected interpretation | Reported status / source |
|---|---|---|---|
| not reported — remove the core module while holding data/input/compute fixed | Semantic / temporal fusion | causal attribution of the core module | minimum audit to run; not a paper-reported ablation |
| not reported — 3D geometry/semantic fusion variant | Geometry extraction | sensitivity to the main interface assumption | minimum audit to run; not a paper-reported ablation |

## Main Results / Claim–Evidence Map

| Claim / target | Evidence or result cue | Evaluation type | Strength | Source |
|---|---|---|---|---|
| geometric accuracy, semantic consistency와 planning/manipulation utility | To achieve these objectives, we propose an Online Sparse Coefficients Field with a CLIP Global Codebook where it binds the 2D CLIP embeddings to each 3D Gaussian while …. | EMPIRICAL / LEARNING OR SIMULATION | legacy protocol cue; exact main table/figure and conditions require verification | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |

## Generalization and Failure Cases

| Assumption / regime | Failure or stress test | Status | Source |
|---|---|---|---|
| streaming view와 pose가 scene coverage를 빠르게 제공 | long-tail unseen area와 pose drift는 holes/semantic misalignment | profile/formulation-derived stress test; not necessarily paper-reported | 02 problem profile; exact failure evidence verify |
| CLIP codebook이 robot query vocabulary를 cover | fine-grained affordance·part relation은 부족 | profile/formulation-derived stress test; not necessarily paper-reported | 02 problem profile; exact failure evidence verify |

- **Untested regime audit:** embodiment, sensor noise/calibration, contact mode, long horizon, unseen object/task/scene and recovery behavior are not assumed covered unless the source explicitly reports them.

## Statistics, Efficiency, and Reproducibility

| Reproducibility field | Recorded value/cue | Status | Source |
|---|---|---|---|
| Trials / episodes | not reported | not reported means no count was found; it is not zero | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |
| Random seeds / repeats | not reported | not reported | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |
| Mean ± std / CI | not reported | not reported | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |
| Latency / throughput | not reported | numeric value only if explicitly present | 04_evaluation.md `Reproducibility Notes`; exact table/figure/page 확인 필요 |
| Compute / hardware dependency | not reported | not reported unless current note contains a cue | 04_evaluation.md `Reproducibility Notes`; exact table/figure/page 확인 필요 |
| Train/eval split and leakage control | not reported | role and split require body verification | 04_evaluation.md `Dataset / Benchmark`; exact table/figure/page 확인 필요 |
| Code / checkpoint / environment | see 01_overview.md; not duplicated here | availability/configuration not reprinted as metadata | 01_overview.md |
| Evaluation mode | EMPIRICAL / LEARNING OR SIMULATION | system/theory/empirical distinction must govern what statistics are applicable | evaluation type audit |

## Limitations and Verification Questions

- **Evidence boundary:** evaluation cue를 reported result로 승격하지 않았으며, exact table/figure/page는 원문 확인이 필요하다.
- **Missing comparison fields:** baseline identity/fairness, trial/seed statistics.
- **Interpretation rule:** `not applicable`은 평가 유형상 해당하지 않음을, `not found`는 현재 note에서 이름을 찾지 못했음을, `not reported`는 paper/source에서 보고 여부가 확인되지 않았음을 뜻한다.
- **Do not overclaim:** success/accuracy cue만으로 generalization, robustness, causality 또는 real-robot reproducibility를 주장하지 않는다.
- **Research-facing limitation:** camera pose/stream alignment, incremental memory budget과 sparse semantic coefficients를 유지하면서 scene 전체를 누적해야 한다.

- **Source anchor:** 본문의 online whole-scene 3DGS, Online Sparse Coefficients Field+CLIP Global Codebook과 embodied perception objective.; exact dataset table, split, baseline configuration, ablation table and result figure must be located.
- **Evaluation type check:** this note classifies the evidence as `EMPIRICAL / LEARNING OR SIMULATION`; confirm that theory/system/learning/benchmark fields are not being mixed.
- **Claim–condition check:** every result must name task, embodiment/simulator, input/action interface, metric, baseline, trials/seeds and source location.
- **Reproduction check:** record reset/timeout/success denominator, preprocessing, checkpoint, compute, inference/control rate and failure handling before comparing numbers.
- **Statistical check:** distinguish one demonstration/episode/example from repeated trials and report uncertainty when the source provides it.
