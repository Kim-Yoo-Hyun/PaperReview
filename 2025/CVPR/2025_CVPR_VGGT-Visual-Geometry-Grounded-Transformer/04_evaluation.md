# Evaluation — VGGT: Visual Geometry Grounded Transformer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: source PDF 또는 공식 full-text source의 problem/method formulation profile과 기존 evaluation cue를 결합해 구조화했다; exact evaluation table/page와 trial details는 원문 확인 필요. tracker의 reading status/evidence는 변경하지 않았다.

## Evaluation in One Sentence

camera estimation, multi-view depth, dense point reconstruction and point tracking are named as evaluation tasks; dataset-role mapping remains unresolved.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / 3D VISION SYSTEM` (provisional; source body에서 확인 필요)
- **Target system/task:** 3D scene/object와 robot coordinate frame
- **Input/observation boundary:** RGB-D, image set, point cloud, depth와 camera pose
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility
- **Scope rule:** theory/formulation papers use assumptions, theorem/analytic examples or controller behavior; empirical papers use matched task/data/baseline/trial records; benchmark papers use task/protocol/score definitions.

## Experimental Matrix

| Experiment / claim | Type & setting | Dataset / split | Robot / system | Baseline | Metric / result cue | Trials / seeds | Source |
|---|---|---|---|---|---|---|---|
| geometric accuracy, semantic consistency와 planning/manipulation utility | setting not found in current note | ScanNet / Replica / KITTI / Objaverse / DTU / ETH3D / Habitat; split/role unresolved | 3D scene/object와 robot coordinate frame | MASt3R and prior multi-view systems appear in the protocol cue; exact baseline table/configuration not recorded. | camera/depth/reconstruction/tracking metrics; The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking. MASt3R have shown promising results in this direction, but these networks can only process two images at once and rely on post-processing to reconstruct more images, fusing pairwise …. | trials: not reported; seeds: not reported | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |

## Dataset / Benchmark Role

| Resource | Role | Split / size | Source |
|---|---|---|---|
| ScanNet / Replica / KITTI / Objaverse / DTU / ETH3D / Habitat | legacy resource cues; train/eval/pretraining role not resolved | not reported | override/profile cue; exact source location 확인 필요 |

- Dataset names found only by legacy keyword extraction are not accepted as verified evaluation datasets until their role is located in the experiment section.

## Embodiment / Environment

| Dimension | Recorded cue | Interpretation / missing detail | Source |
|---|---|---|---|
| Evaluation type | EMPIRICAL / 3D VISION SYSTEM | provisional classification from current source cue; verify body | source cue / title/domain |
| Robot / simulator / hardware | robot/simulator platform not reported | reported status not fully resolved | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |
| Observation / sensor | RGB-D, image set, point cloud, depth와 camera pose | scope cue from problem profile; exact sensor/calibration verify | 02 problem scope |
| Control / inference rate | not reported | numeric value only if explicitly present | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |
| Task / episode unit | The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking. | task count, reset, timeout and denominator not reported unless stated | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |
| Generalization split/variation | generalization condition not found | split and unseen dimensions require body verification | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |

## Metrics and Success Definition

| Metric / success signal | Direction / unit | Status | Source |
|---|---|---|---|
| camera/depth/reconstruction/tracking metrics | direction/unit not reported | task-level target; current keyword list is not accepted as verified metric set | profile/protocol cue; exact metric definition/table 확인 필요 |

- **Success/failure/timeout definition:** not reported in the current note unless stated above; exact denominator, collision/contact rule and termination condition require body verification.

## Baselines and Fairness

| Baseline / comparison cue | What it should isolate | Same data/observation/compute? | Source |
|---|---|---|---|
| MASt3R and prior multi-view systems appear in the protocol cue; exact baseline table/configuration not recorded. | comparison identity/claim | not reported | override/protocol cue; exact baseline table 확인 필요 |

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
| multi-image processing, feature/geometry fusion and post-processing sensitivity; reported ablation not found. | Semantic / temporal fusion | isolate the paper-specific mechanism | cue; exact ablation table 확인 필요 |
| not reported — 3D geometry/semantic fusion variant | Geometry extraction | sensitivity to the main interface assumption | minimum audit to run; not a paper-reported ablation |

## Main Results / Claim–Evidence Map

| Claim / target | Evidence or result cue | Evaluation type | Strength | Source |
|---|---|---|---|---|
| geometric accuracy, semantic consistency와 planning/manipulation utility | The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking. MASt3R have shown promising results in this direction, but these networks can only process two images at once and rely on post-processing to reconstruct more images, fusing pairwise …. | EMPIRICAL / 3D VISION SYSTEM | legacy protocol cue; exact main table/figure and conditions require verification | 04_evaluation.md `Evaluation Protocol and Results`; exact table/figure/page 확인 필요 |

## Generalization and Failure Cases

| Assumption / regime | Failure or stress test | Status | Source |
|---|---|---|---|
| training 3D data가 deployment camera/scene distribution을 충분히 cover | domain shift·dynamic object는 inconsistent map | profile/formulation-derived stress test; not necessarily paper-reported | 02 problem profile; exact failure evidence verify |
| single forward pass의 correspondence가 geometry ambiguity를 해소 | textureless/repetitive scene은 scale/pose ambiguity | profile/formulation-derived stress test; not necessarily paper-reported | 02 problem profile; exact failure evidence verify |

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
| Evaluation mode | EMPIRICAL / 3D VISION SYSTEM | system/theory/empirical distinction must govern what statistics are applicable | evaluation type audit |

## Limitations and Verification Questions

- **Evidence boundary:** evaluation cue를 reported result로 승격하지 않았으며, exact table/figure/page는 원문 확인이 필요하다.
- **Missing comparison fields:** trial/seed statistics.
- **Interpretation rule:** `not applicable`은 평가 유형상 해당하지 않음을, `not found`는 현재 note에서 이름을 찾지 못했음을, `not reported`는 paper/source에서 보고 여부가 확인되지 않았음을 뜻한다.
- **Do not overclaim:** success/accuracy cue만으로 generalization, robustness, causality 또는 real-robot reproducibility를 주장하지 않는다.
- **Research-facing limitation:** 입력 images가 충분한 overlap과 공통 scene geometry를 갖고 camera/projective ambiguity를 학습된 convention으로 해소해야 한다.

- **Source anchor:** 본문의 feed-forward multi-image input, camera·point map·depth·track joint output과 optimization-free 3D task formulation.; exact dataset table, split, baseline configuration, ablation table and result figure must be located.
- **Evaluation type check:** this note classifies the evidence as `EMPIRICAL / 3D VISION SYSTEM`; confirm that theory/system/learning/benchmark fields are not being mixed.
- **Claim–condition check:** every result must name task, embodiment/simulator, input/action interface, metric, baseline, trials/seeds and source location.
- **Reproduction check:** record reset/timeout/success denominator, preprocessing, checkpoint, compute, inference/control rate and failure handling before comparing numbers.
- **Statistical check:** distinguish one demonstration/episode/example from repeated trials and report uncertainty when the source provides it.
