# 시연 저장소 확장에 따른 VLA의 기존 과제 성능 보존 — 비실험 buildup

**현행 투자 판단 — 2026-11-07:** [8개 후보 비교](../../README.md#candidate-priority)의 낮은 우선 진단이다. 목표별 분리를 넘어 다른 과제의 유용한 정보를 보존하는 조건은 남지만, 선행과의 차이가 좁고 원 시연의 성공·평가 독립성과 native 연결도 미확보다. 현재 GPU만으로 본격 연구 전환이 되는 후보는 아니다.

현행 비실험 상태 검토: **2026-11-05** · [7단계 상태·기여 가설·판단 분기](#buildup-status). 기존 문헌/계약/결과를 대조한 보강이며 새 효과 관측은 없다.

**11/05 통합 판단:** 새로 등록한 When Does Retrieval Help와 ICML RA-VLA를 직접 선행에 포함한다. Cross-task 시연의 도움/간섭이나 semantic retrieval 자체는 새 질문이 아니다. 고정 target bank와 token 예산에서 donor 증가의 도움을 goal partition보다 더 보존하는지가 남는다. RA-VLA는 이번 공식 abstract 확인 수준이므로 상세 bank 실험 부재를 확정하지 않는다. 성공 provenance·평가 독립성과 native adapter는 별도 미완료다. 우선순위는 제한된 진단으로 낮게 유지한다.

근거·전체 상대 비교: [기존 6개+새 2개 공백 검토](../../../update/INTEGRATED_GAP_REVIEW_2026-11-05.md). 신규 paper별 확인 절과 status는 [등록 원장](../../../sources/registry_admissions_2026-11-05.json)에 통합한다. 기존 실행 계약·원시 결과·과거 source 날짜는 보존한다.

- 검토일: **2026-11-02 KST** / 작업: **GAP-RETRIEVAL-N1 비실험 buildup 검토 DONE / native 미검증**
- 판단: **탐색 후보로 유지(EXPLORE)**. 문헌 공백은 조건부이며 신규 방법·효과·출판 가능성을 입증한 상태가 아니다.
- 질문 소유: [VLA synthesis](../../../../synthesis/04_vla_generalist.md#gap-retrieval-library-2026). 활성 순서: [TODO](../../../../TODO.md).
- 근거: [검색·본문·공개 코드/metadata ledger](sources.json).
- 현행 비교 설계: [현행 단일 비교 계약(revision 3)](../재현%20방법/COMPARISON_CONTRACT.json). 문헌·정적 source에 기초한 설계이며 실행 manifest는 아니다.
- 적용 절차: [단계 0–8과 탐색/확증 구분](../../../../research/IDEA_BUILDUP_GUIDE.md#stage-appropriate-gates).
- 문서 정리: 2026-11-02 REG-R7에서 반복 초안을 현행 N1·단일 계약으로 통합했다. R1/R2/A1/N1 anchor와 과거 source/실행 증거는 보존했다.
- 최신 범위: [N1 최종 검토](#retrieval-n1)에서 직접 충돌·무작위 기준선·형식/길이 대안·제어/분할 설계를 보완했다. N1은 비실험 작업만 했으며 Docker·GPU 재확인·archive/weight 다운로드·추론은 0이다. A1의 CPU 자산 감사는 이전에 실제 실행한 별도 증거다. 아래 R1/R2/A1은 단계별 기록이며 현행 판단·설계는 N1과 revision 3 계약을 따른다.

## 후보 카드

**문제:** 고정된 VLA에 새 과제의 시연을 추가하면 재학습 없이 행동 범위를 넓힐 수 있다. 그러나 검색 대상이 바뀌므로 기존 과제의 행동도 바뀔 수 있다. 저장소를 통합할지, 목표별로 나눌지, 먼저 해당 목표의 시연을 더 모을지 결정할 근거가 필요하다.

**연구 질문:** 목표 과제의 시연과 VLA 파라미터를 그대로 둔 채 다른 목표의 유효한 시연만 추가했을 때, 기존 과제의 성공률·잘못된 목표 수행은 어떻게 달라지는가? 단순 목표별 검색으로 충분한가, 아니면 부족한 시연을 다른 과제의 공통 동작으로 보완하는 이득을 잃는 조건이 있는가?

**기여 유형:** 우선 조건을 밝히는 실증·평가 연구. “시연 검색을 VLA에 붙인다”, “잘못된 시연이 해롭다”, “phase-aware retrieval”을 새로운 방법으로 제안하지 않는다.

**가치 판단:** 작은 탐색의 가치는 있다. 시연 추가가 무조건 이롭다는 가정 아래 저장소를 확장할지 결정하는 데 직접 연결된다. 다만 목표별 검색으로 충분하다면 새 router를 학습할 이유가 없다. 다른 과제 시연의 유용성과 충돌 자체는 이미 보고되어 있어 **신규성 여유는 좁다**. 의미 있는 조건별 결과가 남기 전에는 본격 연구 GO로 올리지 않는다.

## 단계 1–3. 알려진 답과 비교 가능한 조건

아래 확인 깊이는 이 작업의 source review 범위다. 사용자 reading tracker의 READ/SYNTHESIZED 전환을 뜻하지 않는다.

| 선행·확인 범위 | 이미 알려진 답·interface | 이번 질문과의 관계 |
|---|---|---|
| [Graph Search and Retrieval, RSS 2024](https://roboticsproceedings.org/rss20/p054.html), 공식 abstract; registry pr-0638 | 저장 경험에서 행동을 선택해 BC 학습에 사용 | 학습 데이터 개선과 추론 context 교체를 구별하는 기반 |
| [RICL, CoRL 2025](https://proceedings.mlr.press/v305/sridhar25a.html), [본문 §4–5](https://arxiv.org/html/2508.02062v1#S4), 공개 code | VLA를 ICL 가능하게 post-train한 뒤, 목표 시연을 context로 제공. 원 방법에는 검색 행동과 예측 token의 interpolation도 포함 | Frozen deployment는 처음부터 training-free라는 뜻이 아님. Context 선택 효과와 직접 행동 혼합 효과를 구별해야 함 |
| [DARP, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html), 공식 abstract; pr-1040 | 이웃 상태·행동과 상대 차이로 행동을 예측하는 semi-parametric IL | Retrieval 자체와 local correction은 새 원리가 아님. 언어 VLA 비교로 바로 치환하지 않음 |
| [MemER, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9da515b1ad19d032a7398f00f5ff9b0c-Abstract-Conference.html), 공식 abstract | 실행 history의 keyframe을 선택하고 하위 VLA에 지시 | 외부 task demonstration bank와 episode memory를 분리하는 인접 선행 |
| [When Does Retrieval Help?, 2026 preprint](https://arxiv.org/html/2610.05492v1), §2–3·Appendix D–E | LIBERO용 RICL에서 image/state/VLA feature/random 검색 비교. 검색 지표와 정책 이득의 불일치, 관련 과제 재사용·목표 충돌 사례. 원 RICL의 interpolation은 제외 | 가장 가까운 진단 선행. 이 현상의 존재를 재발견하는 것은 부족. 고정 target bank에 다른 과제만 추가하는 개입과 목표별 검색의 비용/이득을 따로 물어야 함 |
| [Retrieve, Don't Retrain / ReCAP, 2026 preprint](https://arxiv.org/html/2606.15631v1), §4.2·5.3·Appendix D–E | 목표/초기 장면 prefilter와 subframe 검색. Frozen policy에서 저장소를 키우며 held-out task 시연도 순차 추가 | Pool 크기와 목표 시연 coverage가 함께 변함. 이 결과만으로 **target support를 고정한 다른-goal 추가의 효과**를 판정할 수 없다는 것은 우리 해석 |
| [StellaVLA, 2026 preprint](https://arxiv.org/html/2608.11671v1), §3.2–3.3·4.1·4.4/Table 5·Appendix A | Structured demo 1개를 episode 동안 고정. Same-checkpoint correct/no/wrong-task context 비교를 이미 수행. Simulation은 exact task match | Wrong-demo test 자체는 신규성이 없음. 자연적인 bank expansion에 따른 선택 변화와 강한 task-routing baseline이 남는 질문 |
| [Retrieve to Act / R2A, 2026 preprint](https://arxiv.org/html/2610.37215v1), §3.3–3.5·§5–6 | Task/progress 정보를 사용하는 motion graph 검색과 action harmonization으로 visual OOD 대응 | Phase·goal-aware retrieval/gating을 새로운 방법으로 내세우지 않음. Scene geometry와 목표 support를 고정한 library expansion은 별도 조건 |
| [RA-VLA, 2026 preprint](https://arxiv.org/html/2608.25585v1), §5.1·5.3–5.6·Appendix F | 목표 task 시연 buffer, 행동에 맞춘 검색과 context adherence; buffer N와 context K 변화도 비교 | 단순 “buffer 크기 효과” 연구도 이미 있음. 같은 목표 시연 증가와 다른 목표 시연 증가를 분리해야 함 |

2024 [ICRT](https://arxiv.org/abs/2408.15980)와 2026 [Behavior Prompting Policy](https://arxiv.org/html/2606.30457v1)는 demo가 task specification인 계보다. “언어 목표가 항상 우선”이라는 계약을 자동 적용하면 안 된다. 두 논문은 각각 abstract/project와 지정 본문 부분까지 확인했다. 신규성 직접 근거는 위 표의 고정 VLA 비교다.

공식 게재를 확인한 RSS 2024·CoRL 2025·ICLR 2026과 arXiv preprint를 구별했다. ResearchGate에서 발견한 `Retrieval Beats Rehearsal When Demonstrations Conflict`는 독립적인 공식/저자 primary source를 확보하지 못해 연구 결과의 근거로 채택하지 않았다. 큰 구현 전 중복 검색의 미확인 항목으로만 남긴다. 웹 검색 누락이나 registry 미등록은 연구 공백의 증거가 아니다.

## 현행 설계와 과거 검토의 연결

현재 설계의 단일 소유자는 [COMPARISON_CONTRACT.json revision 3](../재현%20방법/COMPARISON_CONTRACT.json)이다. 검색 점수·encoder pin·H/G/S/U·제어·분할·길이 guard·cache 격리·반증 규칙은 이 계약과 아래 N1만 갱신한다. 같은 설계의 초기 초안을 별도 활성 계획처럼 반복하지 않는다. [Source ledger](sources.json)는 당시 read scope·hash·선택 변경과 검증 이력을 보존한다.

<a id="retrieval-r1"></a>
### R1 — 공개 interface 검토 완료 당시의 핵심

- Stock StellaVLA는 공개 instruction으로 task pool을 찾고 내부 index로 시연을 읽는다. Benchmark task ID와 demo index는 다르며 실제 join은 A1에서 확인했다. Exact 목표 partition을 유지한 다른 목표 추가가 선택을 바꾸지 않는다는 정적 사실은 방법 신규성이 아니다.
- 긴 prefix의 image·plan·motion/state text와 current primary/wrist RGB·state_text·lang이 실제 action head에 들어간다. Numeric state packet의 존재를 별도 소비 경로로 추정하지 않는다.
- Runtime `task.language`는 BDDL의 `:language`와 다를 수 있다. Cabinet task의 drawer 표현 차이를 query 수정이나 evaluator-ID fallback으로 감추지 않는다.
- 당시 LIBERO-Goal의 bowl→plate/cabinet-top, wine→rack/cabinet 과제 쌍을 검토했다. 초기 LIBERO-90 pair를 공개 four-suite checkpoint의 능력 증거로 쓰지 않았다. 같은 scene 선언과 같은 숫자 seed는 같은 reset instance를 뜻하지 않는다.
- R1의 archive·native 미확인은 당시 기록이다. Archive 구조는 아래 A1에서 확인했고 실제 정책 능력은 여전히 미확인이다. Reader schema·정확한 source permalink와 hash는 ledger의 R1에 있다.

<a id="retrieval-r2"></a>
### R2 — 초기 비교 설계와 이후 수정

H exact goal / G global visual / S top-two lexical의 3-arm 설계는 N1의 U 추가로 대체되었다. 당시 48개 논리 칸은 현재 64개이며 독립 시작 단위는 8개다. 같은 실행 입력·상태·난수의 동등성이 검증될 때만 최대 24개 고유 rollout을 공유할 수 있다. 이는 실행 승인이 아니다.

DINOv2 고정 feature는 시연의 subgoal endframe을 요약하므로 matched initial-state nearest neighbor와 다르다. 목표 2개만 있으면 S=G가 되므로 세 번째 donor를 두었다. Wrong-demo 강제 주입, no-demo OOD 진단, evaluator routing은 자연적인 bank 확장 비교와 구분한다. Goal inclusion과 배타적 wrong-goal도 구분하며 terminal target/alternate 00/01/10/11을 남긴다. 현행 정의·판정은 계약과 N1을 따른다.

## 11/02 registry 보완에서 추가한 직접 선행

[Dejavu / CVPR 2026](../../../../2026/CVPR/2026_CVPR_Dejavu-Towards-Experience-Feedback-Learning-for-Embodied-I/01_overview.md)는 고정 VLA에 검색 경험과 **RL로 학습한 residual**을 결합한다. 따라서 frozen backbone·bank 성장 자체를 신규 기여로 주장하지 않는다. 현재 후보는 residual 학습 없이 target support를 고정한 reference 선택의 총효과를 묻는 제한된 진단으로 유지한다. 이번 보완은 [공식 abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.html)·저자 project 범위이며 전체 본문/code 대조나 연구 효과를 확인한 것은 아니다.

<a id="retrieval-a1"></a>
## GAP-RETRIEVAL-A1 — 실제 자산 확인과 Docker 재개 준비

- 결과: **CPU 자산 감사 완료, native 정책 실행 조건 미충족**. 실물 결과는 [ASSET_AUDIT.json](../재현%20방법/ASSET_AUDIT.json), 다른 컴퓨터에서의 명령은 [재개 안내](../재현%20방법/README.md)에 둔다.
- 실제 환경: macOS ARM64, host RAM 16 GiB, local Docker Desktop 28.3.3의 Linux aarch64·10 CPU·8,218,034,176 bytes RAM. Local socket/daemon을 확인했다. 기존 image로 `--gpus all`을 요청했으며 **exit 125, GPU capability에 맞는 device driver를 선택할 수 없음**을 확인했다. CUDA/EGL·모델 load는 미검증이다.
- GPU 실패 이후에는 해당 검사를 반복하지 않고, 직접 관련된 작은 archive 감사만 CPU Docker에서 진행했다. Python 3.11.14 고정 multi-arch image, CPU 2·memory 512 MiB·standard library로 수행했다. 시연은 Docker volume에서만 읽고 host에 설치하지 않았다.

### 1. 실물 manifest와 시연 identity

[고정 HF archive](https://huggingface.co/StellarEdge/StellaVLA/blob/46d0cf698cacacc02edcf5301a7f30547e9b8cdb/libero/demo/demo_pack.tar)를 Docker 안에서 받아 **12,840,960 bytes와 SHA-256을 직접 검증**했다. 원격 hash를 인용만 한 R1/R2보다 확인 범위가 늘었다. Manifest SHA-256은 `bc1b8e6bf374607785a79133b4884390999e06b10d92217ba4eb414f2ef8e35d`다.

- 4 suite, **40개 pool·40개 payload**, 각 pool의 시연은 **정확히 1개**다. Meta도 이 고정 구성을 명시한다.
- Referenced frame **261개** 모두 경로가 존재하며 256×256 PNG header를 가진다. Frame/state 개수·선언된 suite/task/episode·지시 mapping의 검사에서 오류는 없었다.
- Canonical payload JSON 및 frame bytes의 동일 hash 중복은 없었다. 이는 **학습/평가 trajectory 중복 배제의 증거가 아니다**.

| 용도 | Runtime 지시 | Benchmark ID (order 0) | Demo task index | 실제 payload ID | Frame |
|---|---|---:|---:|---|---:|
| d1 / A1 목표 | `put the bowl on the plate` | 8 | 0 | `libero_goal#0` | 8 |
| d2 / A2 목표 | `put the bowl on top of the cabinet` | 4 | 8 | `libero_goal#19` | 5 |
| d3 / donor | `put the wine bottle on the rack` | 9 | 1 | `libero_goal#1` | 6 |

세 runtime 문자열은 manifest와 payload 지시에 직접 일치했다. Alias나 task-ID fallback이 필요하지 않았다. **Benchmark ID와 demo task index는 실제로 다르며**, `ep_idx` 역시 benchmark 초기 상태 번호로 해석하지 않는다.

### 2. 실제 frame·annotation 확인의 한계

세 시연의 첫/마지막 **6개 이미지**를 수동 시각 확인했다. 단일 외부 카메라 형태이며 그릇→접시/캐비닛의 끝 frame은 해당 배치와 시각적으로 일치한다. 병→rack 끝 frame은 병이 rack 부근에 있으나 gripper·물체 접촉/가림이 있어 release와 native 성공을 확정하지 않았다. 전체 261개는 header/hash 검증이며 모두 pixel decode·의미 검토한 것으로 표시하지 않는다.

Structured plan에는 d1의 grasp/lift 반복 등 길이 차이가 있다. 이를 임의로 정리하거나 성공/실패 label로 바꾸지 않는다. Frame 8·5·6개를 그대로 유지하고 공통 demo-frame ceiling은 **8**로 지정했다. 동일 demo 1개는 동일 정보량이 아니며 goal conflict 효과를 보려면 길이·annotation 차이도 함께 보고해야 한다.

Archive에는 별도 성공 판정, 원 trajectory/dataset revision, 평가 split 중복을 확인할 근거가 없다. “정상 성공 시연만 추가했다”는 강한 결과 주장은 아직 허용되지 않는다. 공개 reference context를 비교하는 작은 탐색은 유지하되, 원 trajectory/evaluator와 연결하기 전에는 성공/provenance를 미확인으로 둔다.

### 3. 비교 설계에 반영한 결과

Actual instruction으로 S의 lexical prefilter만 계산했다. A1/A2 모두 **두 그릇 시연을 남기고 병 시연을 제외**한다. 따라서 H/S/G 후보는 각각 1/2/3개로 구별된다. DINOv2 embedding과 실제 query가 없으므로 visual rank·최종 선택·정책 효과는 계산하지 않았다. 후보 집합의 차이를 행동 차이로 확대하지 않는다.

공개 pack 전체가 task당 1개이므로 목표 시연의 sparse/dense 조건을 이 자산만으로 비교할 수 없다. 이는 R2 작은 탐색은 가능하게 하지만 후속 coverage 요인에는 별도의 추가 시연이 필요하다는 제약이다. 데이터 수집이나 큰 sweep을 자동 시작하지 않는다.

### 4. Portable 준비와 남은 native 조건

[자산 감사 launcher](../재현%20방법/resume_assets.sh)는 repository-relative 경로·고정 image digest·local endpoint 검사·소유 label 기반 cleanup을 갖췄다. 실제 audit/preview/check는 동작했고, remote endpoint는 exit 3으로 거절했다. 실행한 archive는 전용 volume과 함께 삭제했고 이번에 pull한 Python image 참조도 제거했다. 종료 후 container 0개, 기존 `paper-gap-p3` image 1개만 남았으며 다른 작업 자산은 보존했다.

Native 환경의 근거는 [고정 upstream Dockerfile](https://github.com/StellEdge-AI/StellaVLA/blob/e5634b31d4d0b555419fdaa192340f6f2698c894/docker/Dockerfile)과 [배포 config](https://huggingface.co/StellarEdge/StellaVLA/blob/46d0cf698cacacc02edcf5301a7f30547e9b8cdb/libero/config.yaml)다. Python 3.10 정책/시뮬레이터 환경을 분리하고 torch·transformers·MuJoCo 등의 설정은 [계약 `native_resume_requirements`](../재현%20방법/COMPARISON_CONTRACT.json)에 기록했다. Config의 base VLM은 Qwen3-VL-4B-Instruct이며 향후 재현용 revision도 선정했다. 원 저자의 cached revision과 동일하다는 뜻은 아니다.

공개 전체 Dockerfile은 불필요한 simulator/asset과 일부 미고정 dependency를 포함하므로 아직 native 실행 recipe로 검증하지 않았다. 다음은 **GAP-RETRIEVAL-P0-PREP**: 호환 NVIDIA local Docker에서 LIBERO-only image·runtime lock·selector/cache adapter와 작은 IO 검증을 준비하는 작업이다. Weight/normalizer hash, 실제 prefix token 수·truncation, 초기 상태·평가 split, CUDA/EGL·base competence는 남아 있다. Config의 `max_seq_len=2200`을 실제 prefix 허용량으로 간주하지 않는다.

**판단:** 공개 입력 경로의 불확실성은 줄었고 탐색 가치는 유지한다. 방법 효과·신규성·성공률은 미측정이다. 실험 준비 후보 3개와 REVISION 우선순위는 그대로이며, 이번에 추가한 것은 CPU 자산 감사 경로다. 문서 완료나 GPU 확보만으로 네 번째 정책 P0 준비 완료라고 표시하지 않는다.

<a id="retrieval-n1"></a>
## GAP-RETRIEVAL-N1 — 비실험 buildup 최종 검토

**결론: 현재 수행 가능한 내부 비실험 검증을 완료했다. 작은 진단을 시도할 가치는 유지하지만, 새 검색 방법이나 본격 논문 연구의 GO를 뒷받침하지는 못한다.** 새로 확인한 선행 때문에 방법 신규성의 범위는 더 좁아졌다. 연구 질문은 **“목표 시연을 고정한 공개 시연 저장소 확장이 기존 과제 결과를 어떻게 바꾸며, 단순 선택으로 충분한가”**로 제한한다. “성공이 인증된 다른 과제 시연의 효과”는 원 trajectory와 evaluator 연결 후에만 주장할 수 있다.

### 1. 직접 선행과 반대 설명 재검토

| 근거·확인 깊이 | 이번 판단에 반영한 내용 |
|---|---|
| [TOWN-VLA, arXiv 2026](https://arxiv.org/html/2608.23224v1), Method·Q2–Q4·Discussion | 검색 후보의 text compatibility 검사·canonical instruction·거절 시 원 prompt 복원은 이미 제안되었다. 의미 있는/없는 append의 길이 통제도 수행하므로 “목표 필터로 보호한다”나 “외부 문맥이 제어 입력이다”는 새 기여가 아니다. 다만 이 논문은 instruction 변경, 현재 후보는 학습된 구조의 시연 prefix 선택이다. 논문의 실패율을 StellaVLA에 전이하지 않는다. 공개 구현은 이번 primary-source 검색에서 확인하지 못했고 conference status도 미확인이다. |
| [Stable Language Guidance for Vision–Language–Action Models, ACL 2026](https://aclanthology.org/2026.acl-long.190/), 공식 게재 정보·abstract | 지시 표현에 대한 민감성과 language/vision 영향 분리가 인접 연구다. 입력 지시를 그대로 유지하고 demo 선택 효과와 지시 paraphrase 효과를 섞지 않는다. 정량 결과·세부 구현을 정독한 근거로 사용하지 않았다. |
| [When Does Retrieval Help?, §3.1–3.2](https://arxiv.org/html/2610.05492v1) | 무작위 검색도 유의미한 기준선이다. 기존 H/G/S에 **전체 bank의 균등 무작위 선택 U**를 추가했다. 이 논문의 여러 context/상태·행동 단위와 현재 whole-demo 1개 단위를 동일시하지 않는다. |
| [StellaVLA Appendix A](https://arxiv.org/html/2608.11671v1#A1)·[고정 README](https://github.com/StellEdge-AI/StellaVLA/blob/e5634b31d4d0b555419fdaa192340f6f2698c894/README.md) | 저자는 학습 시 leave-one-out retrieval을 설명하고 공개 repo는 평가 코드·checkpoint를 제공한다. 이 진술이 공개 payload 3개의 성공·원 trajectory identity·평가 중복 배제를 직접 증명하지는 않는다. |

ReCAP의 bank 확장·다른 과제 도움과 StellaVLA의 wrong-demo 실험을 새 현상으로 주장하지 않는 이전 판단을 유지한다. 출처 미확인 `Retrieval Beats Rehearsal When Demonstrations Conflict`도 exact-title 검색을 다시 했으나 검증 가능한 primary source를 얻지 못했다. 이 제목은 증거나 탐색 차단 조건으로 사용하지 않는다. 이번 검토는 목표 질문의 직접 충돌 확인이며 모든 분야를 빠짐없이 조사했다는 뜻이 아니다.

### 2. 누락된 비교와 실행 없이 정할 수 있는 항목

현행 값의 단일 소유자는 [COMPARISON_CONTRACT.json, revision 3](../재현%20방법/COMPARISON_CONTRACT.json)이다.

- **U 기준선:** 전체 bank에서 완전한 시연 1개를 균등 추출하고 episode 동안 고정한다. 시작 단위별 난수 생성 규칙을 사전 지정하며 결과를 보고 다시 뽑지 않는다. B0는 singleton이다. 4개 규칙이면 **64개 논리 칸·8개 paired 시작 단위**이고, 실제 동일 입력/상태 실행을 공유할 수 있을 때 **최대 24개 고유 rollout**이다. U 한 번의 추출을 무작위 정책의 정확한 기대값으로 보고하지 않으며, 관측하지 않은 시연 결과를 평균에 채우지 않는다. 첫 IO 검증은 이 비교와 별개다.
- **제어·분할 설계:** 공개 [평가 client](https://github.com/StellEdge-AI/StellaVLA/blob/e5634b31d4d0b555419fdaa192340f6f2698c894/examples/LIBERO/eval_files/eval_libero.py#L94), [chunk 처리](https://github.com/StellEdge-AI/StellaVLA/blob/e5634b31d4d0b555419fdaa192340f6f2698c894/examples/LIBERO/eval_files/model2libero_interface.py#L110), [LIBERO wrapper](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/envs/env_wrapper.py#L27)를 근거로 settling 10회 후 300 policy step·20 Hz·chunk 8·최대 38 action 요청, seed 7을 정했다. 각 task의 init slot 0은 기술 검증, 1–4는 서술적 비교에 사용한다. 같은 slot 번호가 서로 다른 task에서 동일 물리 상태라는 뜻은 아니다. Init 파일 hash·중복·복원·성공 판정은 실제로 확인해야 하며, 이 분할은 학습 데이터와 독립인 holdout을 인증하지 않는다.
- **입력 길이:** [실제 inference 경로](https://github.com/StellEdge-AI/StellaVLA/blob/e5634b31d4d0b555419fdaa192340f6f2698c894/stellavla/model/framework/stellavla.py#L337)는 직접 processor를 호출한다. 다른 wrapper의 `max_seq_len` 주석만으로 이 경로의 truncation을 보장하지 않는다. 설계상 완전한 prefix·최대 8 demo frame과 **전체 입력 2,200 token guard**를 지정했다. 이는 config 값에 근거한 보수적 설계이며 실제 token 수·수용량의 측정 결과가 아니다. 초과 시 어느 방식도 잘라 쓰지 않고 실행 자격을 수정한다.
- **구현 혼입 축소:** 첫 비교는 모든 방식에서 optional prefix KV reuse를 끄고 full forward를 사용한다. 선택 cache/queue/상태 격리는 여전히 필요하다. Upstream의 일회 action 오차 허용 검사는 bit-identical 실행 증거가 아니다. Cache 성능 검증을 연구 질문의 필수 선행 과제로 늘리지 않는다.
- **기제 주장 제한:** 실제 시연은 8/5/6 frame이고 annotation도 다르다. 동일 serializer와 상한만으로 의미·길이·내용의 영향을 분리할 수 없다. 현재는 bank 개입의 전체 효과를 묻는다. 순수한 목표 충돌 기제를 주장하려면 유효한 길이/형식 대조와 독립 goal 근거가 추가로 필요하다. 이를 만들기 위해 임의 dummy text나 잘라낸 시연을 현재 실험에 자동 추가하지 않는다.

위 숫자는 **설계 완료**이고 native 실행 확인은 아니다. 이미지/adapter·processor·weight/normalizer와 reset 상태의 실제 연결은 남는다. GPU가 없어서 못 정한 문서 값과 실행해야만 확인할 값을 구분했다.

### 3. 검증을 통과하지 못한 강한 주장과 남는 가치

| 가능한 설명 | 구별할 관측·판단 |
|---|---|
| Exact 목표 선택만으로 충분함 | H는 bank 확장 전후 동일 입력이어야 한다. G/S에서 추가 이득이 관측되지 않으면 관측 범위의 단순 운영 규칙으로 끝내고 learned router를 만들지 않는다. |
| 유사도 검색이 필요하지 않음 | G/S를 U와도 비교한다. 작은 표본의 비우위를 모집단 동등성으로 주장하지 않으며 encoder 비용을 정당화할 근거가 있는지 본다. |
| 다른 과제의 정보가 이득·퇴행을 동시에 만듦 | 자연적인 G/S 선택에서 target support 고정 후 양쪽 전환을 기록한다. 이후 다른 task/시연에서 반복될 때 support 요인 연구로 발전시킬 수 있다. |
| 형식·길이·잘못된 annotation 또는 구현 문제 | 총효과와 의미 기제를 구분한다. Cache/mapping/reset 오류는 연구 현상으로 세지 않는다. 단지 강제 wrong-demo가 실패하는 결과는 기존 연구의 재현 범위다. |

**공개 출처로 닫을 수 없는 항목:** pinned repo의 README·공개 파일 경로·모델 배포 목록과 기존 실제 manifest에서 원 trajectory↔payload↔평가 episode의 연결이나 성공 인증을 찾지 못했다. 성공 시연에서 만들었다는 저자 설명과 per-payload 검증은 다르다. 파일명 검색은 공개되지 않은 코드의 부재를 입증하지도 않는다. 따라서 공개 reference를 쓰는 제한된 기술/서술적 진단은 가능하지만, 독립 평가·성공 donor에 관한 강한 해석은 새 데이터/저자 근거가 있어야 한다. 동일 archive 집계를 반복해서 해결되는 문제가 아니다.

<a id="buildup-status"></a>

### 4. 비실험 buildup 현행 상태 — 2026-11-04

**판정: 제한된 입력 간섭 진단 유지 · 내부 설계 정리 · 원 시연 근거/정책 연결 미확보.** [7단계 비실험 절차](../../../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)를 기존 문헌·논리·계약에 적용해 정리했다. 아래 상태는 새 실험 결과나 11/04 신규 문헌 전수조사가 아니다.

**한 문단 기여 가설:** 목표 시연은 그대로 둔 채 다른 목표의 reference를 추가할 때 저장소를 합치는 편이 유용한지 결정하려 한다. 기여 후보는 **목표별 분리의 안정성과 다른 목표 정보의 재사용 이득이 갈리는 조건**이다. 잘못된 demo가 해롭다는 재현이나 목표별 분리의 자명한 불변성만으로는 기여가 부족하다.

| 비실험 단계 | 상태 | 현재 근거·완료 경계 |
|---|---|---|
| 1 문제·독자 | 정리됨 | [후보 카드](#후보-카드): VLA 시연 저장소 운영. Target support 고정과 전체 bank 성장의 효과를 구분 |
| 2 가까운 선행 | 지정 범위 확인·자료 경계 남음 | RICL/ReCAP/StellaVLA/When Does Retrieval Help?/TOWN 등 N1 비교. 원 성공 trajectory↔payload↔평가 episode join은 확인 안 됨 |
| 3 질문·대안 | 정리됨 | H 목표 분리·G visual·S lexical·U uniform, 길이/형식·cache·목표 충돌 대조. H 입력 불변은 구현 sanity check |
| 4 기여 서술 | 좁은 주장만 가능 | 현재는 공개 reference 확장의 서술적 입력/행동 비교. 성공 donor를 늘린 효과·학습 데이터 독립성·새 router 기여는 보류 |
| 5 최소 비교 | 설계됨·native 미실행 | [revision 3 계약](../재현%20방법/COMPARISON_CONTRACT.json): 8 paired starts·64 논리 칸/조건부 24 고유 rollout. 그 전체가 첫 IO 실행 범위는 아님 |
| 6 실행 부담 | 자산 구조 일부 확인·핵심 자료 미확보 | 과거 A1의 40개/261 frame 감사는 실제 증거. 성공 provenance·평가 중복·image/selector/full-forward adapter·token ceiling은 미검증 |
| 7 외부 비판 | 질문 준비·미수신 | 원 데이터/정책 기여·가장 가까운 선행에 대한 실제 응답 없음. 아래 질문으로 원 자료의 부족도 함께 드러냄 |

**결과에 따른 판단 — 아직 관측하지 않은 분기 포함**

| 다음 증거 | 바뀌는 판단 | 이 증거만으로 하지 않을 주장 |
|---|---|---|
| 목표별 H 입력이 확장 전후 같음 | 예정한 불변성 대조가 성립하는지 확인 | 이 성질만을 새 연구 성과로 주장 |
| G/S의 차이가 형식·길이·오류 수정으로 설명됨 | Pipeline 총효과 또는 구현 진단으로 범위를 줄임 | 의미적 간섭 기제나 새로운 검색 원리 |
| 자연적인 선택에서 H/U 이후 이득과 퇴행이 반복됨 | 출처가 확인된 독립 task/시연으로 조건을 후속 조사 | 현재 단일 payload·소표본으로 광범위 scaling 주장 |

가장 먼저 필요한 자료는 donor 성공/원 trajectory와 평가 episode의 연결 근거다. 새로운 근거가 없으면 공개 reference 입력 진단으로 범위를 유지할 수 있지만 성공 시연 증가의 효과를 주장하지 않는다. 추가 encoder·이미지/token·full-forward 시간·데이터 정리에 드는 사람 공수도 비용이다.

**외부 검토 준비:** 외부 검토 질문은 “고정 target support의 자연적인 bank 확장을 이미 다룬 연구가 있는가?”, “H/U 이후 결과가 실제 저장소 운영을 바꾸는가?”, “공개 payload의 provenance 경계에서 어느 주장까지 유효한가?”다. 질문은 준비했으며 전송·수신 기록은 없다. 실제 응답·반영이 생기면 내용과 source 위치를 기록한다. 미수신은 작은 탐색을 금지하는 진입 조건이 아니다.

**다음 확인과 문서 종료점:** 첫 구현을 선택하면 원 자료 연결의 확보 여부와 정책 입력의 실제 구성부터 점검한다. 자료를 확보하지 못하면 진단 범위를 명시적으로 유지하며 archive 개수 재집계로 해결됐다고 하지 않는다. 기존 VLA+RL 탐색과 별도의 조건부 후보이며 GPU만으로 실행 준비 완료가 되지 않는다. 새로운 직접 선행·자료·반례·피드백 없이 같은 문서 검토를 반복할 내부 과제로 만들지 않는다. 실행 범위·상한은 기존 계약과 [재현 안내](../재현%20방법/README.md)가 관리한다.

## N1 완료 당시의 저장소 검증

- **N1 내부 비실험 buildup: DONE.** 실험 효과·per-payload 성공/중복·독립 외부 피드백은 미검증으로 남겼다. 위 단계 표가 현재 완료 범위다.
- **A1 실행 증거 보존:** 실제 CPU 자산 감사와 임시 자원 정리는 이전 ledger에 유지한다. N1에서 다시 실행하지 않았다.
- Registry·tier·읽기 상태·기존 실험 packet 변경 없음. 신규 논문 등록 없이 조사 근거만 source ledger에 보완했다.
- N1 문서/계약 정합성·생성기 문법/재생성·작업 트리와 staged diff 검사 통과. Audit 오류/경고 0, 1,080편·352 active·47 history 유지. 사전 보호 파일 308개 중 의도한 계약·재개 안내 2개만 변경했고 나머지 306개·staged index는 동일하다. A1 실물 감사 결과와 모든 실행 코드는 보존했다. 상세 및 과거 A1 검증은 source ledger에 둔다.
