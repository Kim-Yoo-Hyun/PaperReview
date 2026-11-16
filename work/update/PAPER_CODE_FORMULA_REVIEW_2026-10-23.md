# DOC-QA3 — 지정 5편의 원문·공개 구현 대조

- 검토일: 2026-10-23 KST
- 상태: **DONE — 지정 대조·노트/metadata 반영·무결성 검증·임시 파일 정리 완료**
- 입력: [DOC-QA2의 지정 5개 질문](./PDF_NOTE_REVIEW_FOLLOWUP_2026-10-23.md#원문-자체에-남은-해석-확인-항목)
- 상세 근거: [commit·source SHA256·호출 경로·노트 수정 hash·metadata 변경 ledger](../sources/paper_code_formula_review_2026-10-23.json)

## 결론

5편 모두 공식 공개 구현을 찾았고 지정 식의 실제 호출 경로를 정적으로 대조했다. **공개 구현에서 쓰는 식은 확인했으나, 해당 commit이 논문 실험의 정확한 버전인지는 미확인**이다. 논문 원문을 코드에 맞춰 덮어쓰지 않고 두 계약을 구분했다. 저자가 확인한 정오표나 논문 성능의 오류라고 판정하지 않는다.

| 논문·질문 | 원문과 공개 구현의 차이 | 재사용 시 결정 |
|---|---|---|
| SAGE-3D: PS | 원문의 clipped heading-change 평균과 달리, 코드는 nonzero XY 변위들의 차이 norm 평균 a를 `1/(1+10a)`로 변환 | 동일 이름의 PS를 동일 metric으로 합치지 않음. 측정 시점·좌표 단위·필터링을 고정 |
| cdViews / 3D QA: BCE | 인쇄 Eq. (8)의 log 안팎 배치와 달리, 코드는 cosine을 `(cos+1)/2`로 바꾼 뒤 prediction–target 순서로 BCE 호출 | 역전된 인쇄 식이나 raw cosine을 loss에 바로 넣지 않음 |
| RoboFlow4D: sampler | 단일 γ power law+floor와 달리, 코드는 양끝 piecewise warp+round 및 uniform fallback | 두 γ·rounding·반복 index·fallback까지 별도 구현 계약으로 보존 |
| QuadricFormer: z 지수 | 원문 z 항은 `2/ε₂`; 코드의 XY/outer 항에 맞춘 기호 대응에서 z 항은 `2/ε₁` | 인쇄식과 CUDA primitive를 구분. Gradient 정확성은 별도 미검증 |
| LIO-SAM: residual | 인쇄식에는 제곱이 명시되지 않지만, 코드는 가중 Jacobian/residual로 normal equations를 구성 | 각 선형화 단계의 가중 최소제곱으로 해석. 고정된 전역 objective라고 확대하지 않음 |

이번 발견은 문서·재현 계약의 정합성 문제다. 신규 VLA 연구 공백이나 기존 후보의 GO 근거로 승격하지 않는다. 논문에 보고된 수치도 재계산하거나 무효화하지 않았다.

## 근거와 버전

원문은 DOC-QA2에서 시각 대조한 PDF의 URL·hash·페이지를 이어받고, 4편의 지정 식은 arXiv HTML에서도 확인했다. 이번 작업에서는 PDF를 새로 받지 않았다. 공식 저자 project 또는 논문에서 code 링크를 확인하고 GitHub commit을 고정했다. 외부 코드는 텍스트로만 읽었으며 import·설치·빌드·추론·학습·성능 측정을 하지 않았다.

| 논문 | 공식 연결 근거 | 고정 commit / commit date (UTC) |
|---|---|---|
| SAGE-3D | [저자 project](https://sage-3d.github.io/) → 공식 repository | [69e60c2123ac](https://github.com/Galery23/SAGE-3D_Official/commit/69e60c2123aca55ff2ad96d66a80a9bac5a7912d) / 2026-07-27 |
| cdViews | [논문 abstract의 code 링크](https://arxiv.org/html/2505.22143v1) | [e1df64c5490c](https://github.com/fereenwong/cdViews/commit/e1df64c5490c75d117f0ece5c334a6d818cf5d83) / 2026-03-04 |
| RoboFlow4D | [저자 project](https://simonlinsx.github.io/RoboFlow4D_Page/) · [저자 연구실](https://pirlab.github.io/research/roboflow4d/index.html); Simonlinsx code URL은 EDEM-AI로 redirect | [31c950750f00](https://github.com/EDEM-AI/RoboFlow4D/commit/31c950750f0074067cd7c8ff5df86b8d6fa6f223) / 2026-06-11 |
| QuadricFormer | [저자 project](https://zuosc19.github.io/QuadricFormer/) → 공식 repository | [f4b5b03d9d2f](https://github.com/zuosc19/QuadricFormer/commit/f4b5b03d9d2f73b18b874b5ed9ce1f465bb8f490) / 2025-07-13 |
| LIO-SAM | [저자 repository](https://github.com/TixiaoShan/LIO-SAM), ROS1 master | [0be1fbe6275f](https://github.com/TixiaoShan/LIO-SAM/commit/0be1fbe6275fb8366d5b800af4fc8c76a885c869) / 2023-04-17 |

Repository README와 issue/PR index의 제목·본문을 함께 확인했다. 확인 건수는 위 순서로 18 / 7 / 3 / 14 / 100건이다. **LIO-SAM은 첫 100건만** 확인했고, 전체 댓글·과거 release·모든 branch를 조사한 것은 아니다. 지정 식에 대한 저자 확인 정오표는 이 범위에서 식별하지 못했다. 다른 사용자의 bug/reproduction 보고를 저자의 인정이나 검증된 성능 결과로 사용하지 않았다.

## 호출 경로별 판단

### SAGE-3D

`run_benchmark.py`의 task branch가 measure manager를 생성하고 `default_measures` 또는 `nogoal_measures`에 등록된 `PathSmoothness`를 갱신한다. Command 전후 update 및 episode JSON dump 경로까지 연결했다. [Metric 구현](https://github.com/Galery23/SAGE-3D_Official/blob/69e60c2123aca55ff2ad96d66a80a9bac5a7912d/Code/benchmark/environment_evaluation/measures.py#L338-L381)은 heading을 읽지 않고 dt로 나누지도 않는다. 정지/제자리 회전처럼 유효 XY 변위가 2개 미만이면 1을 반환한다. 이는 코드에서 도출한 경계이며 실제 rollout으로 측정한 결과가 아니다.

**남은 경계:** [원문 §3.3](https://arxiv.org/html/2510.21307v2)과 공개 PS가 다르다. 논문 table의 PS가 어느 evaluator revision으로 생성되었는지는 확인하지 못했다. 시간 정규화되지 않은 차분을 물리 가속도로 표시하거나 두 지표의 수치를 같은 열에 넣지 않는다.

### cdViews / 3D QA

`eval_model`의 학습 loop → `train_epoch` → [BCELoss wrapper](https://github.com/fereenwong/cdViews/blob/e1df64c5490c75d117f0ece5c334a6d818cf5d83/cdviews/ViewSelector.py#L326-L336)로 이어진다. Dataset의 positive/negative view는 1/0 target이다. [PyTorch 공식 API](https://docs.pytorch.org/docs/2.14/generated/torch.nn.BCELoss.html)는 prediction–target 인수 순서와 기본 mean reduction을 확인하는 보조 근거다. 코드에서 사용하는 API의 수치 경계 처리를 별도 임의 수식으로 대체하지 않는다.

**남은 경계:** [원문 Eq. (8)](https://arxiv.org/html/2505.22143v1)의 순서를 구현에서 사용하지 않는다는 것은 확인했다. 문서에서 열람한 PyTorch 버전이 논문 실행 환경과 같다는 뜻은 아니며 checkpoint·training log의 일치도 확인하지 않았다.

### RoboFlow4D

Flow training의 `main` → `FutureKDataset` → `__getitem__` → [resample_on_traj](https://github.com/EDEM-AI/RoboFlow4D/blob/31c950750f0074067cd7c8ff5df86b8d6fa6f223/3DFlowModel/train_flow_model.py#L815-L851)를 확인했다. γs=1.2 / γe=1.6을 쓰고, unique 수가 `int(0.7K)` 미만이면 uniform sampling으로 바꾼다. 이 fallback도 index 중복 제거를 보장하지 않는다. Policy target helper에도 같은 형태가 있지만 모든 cache 생성 경로를 전수 감사하지 않았다.

**남은 경계:** [원문 §3.5·Appendix C](https://arxiv.org/html/2605.17522v1)의 단일 power law와 공개 구현은 별도다. 한 exponent 오타를 고친 것으로 축약하지 않으며, 어느 sampler로 보고된 checkpoint를 만들었는지 단정하지 않는다.

### QuadricFormer

Config → `SuperQuadricOccHeadProb` → Python autograd wrapper → pybind `LocalAggregateCUDA` → aggregator → [CUDA forward](https://github.com/zuosc19/QuadricFormer/blob/f4b5b03d9d2f73b18b874b5ed9ce1f465bb8f490/model/head/localagg_prob_sq/src/forward.cu#L80-L97)의 u/v 전달 순서를 확인했다. XY 항·outer power를 맞춰 u↔ε₂, v↔ε₁로 읽는 것은 **연구자의 기호 대응**이다. 좌표를 제곱한 뒤 지수를 취하는 구현도 보존한다. Backward의 scalar f는 같지만 analytic gradient의 정확성을 시험한 것은 아니다.

**남은 경계:** [원문 Eq. (4)](https://arxiv.org/html/2506.10977v1)의 z 지수와 차이가 확인됐다. 빌드된 extension·checkpoint·논문 결과의 대응은 미검증이다. 이 코드 경로를 확인했다고 occupancy 수치를 재현한 것으로 기록하지 않는다.

### LIO-SAM

Build target의 `mapOptmization.cpp` → callback → `scan2MapOptimization` → corner/surface residual → `combineOptimizationCoeffs` → [LMOptimization](https://github.com/TixiaoShan/LIO-SAM/blob/0be1fbe6275fb8366d5b800af4fc8c76a885c869/src/mapOptmization.cpp#L1182-L1255)을 연결했다. Residual과 Jacobian 모두 s가 곱해진다. `AᵀA δ=Aᵀb`를 QR로 풀고 degeneracy projection을 적용한다.

**남은 경계:** 선형화 단계의 가중 최소제곱이라는 해석은 정적 수학적 대조다. 함수명만으로 damping을 포함한 LM 구현이라 하지 않는다. 반복마다 대응·s가 바뀌므로 고정 전역 loss로 치환하지 않는다. 2023 ROS1 master를 [2020 논문](https://arxiv.org/abs/2007.00258)의 실행 버전이라고 가정하지 않는다.

## 저장소 반영과 종료 조건

- 5편의 method note에 원문·code·연구자 해석을 구분해 기록하고 overview에서 연결했다. SAGE-3D와 QuadricFormer의 evaluation note에도 관련 경계를 연결했다: 총 **12개 노트**.
- 기존 `not_identified`였던 공식 code **4건**, 저자 project **3건**을 canonical manifest와 `PAPER.md`에 반영했다. Code availability만 갱신하며 publication·tier·content evidence·사용자 읽기 이력은 유지한다.
- 새 논문 등록은 없다. 기존 1,037편·47 CORE / 275 NEXT / 473 REFERENCE / 242 ARCHIVE를 유지한다.
- DOC-QA2 ledger의 after-hash는 당시 snapshot이다. 이번 수정은 별도 before/after-hash로 이어지며 과거 ledger를 덮어쓰지 않는다.

지정 5개 질문에 대한 비실험 대조를 종료한다. 같은 공개 코드 검색을 반복하거나 DOC-QA4를 자동 생성하지 않는다. **현재 다음 READY 항목은 없다.** PORT-R1은 다른 물리 컴퓨터가 필요하고, 연구 후보는 [TODO](../../TODO.md)의 새 비교 증거 조건을 따른다. GPU만 확보했다고 기존 HOLD/NO-GO를 변경하지 않는다. 저자 정오표나 paper-run revision이 새로 확인되면 해당 노트의 버전 경계만 재심사한다.

## 검증·임시 파일 정리

| 검사 | 결과 |
|---|---|
| `python3 -m py_compile work/scripts/build_reading_tiers.py` | PASS |
| `python3 work/scripts/build_reading_tiers.py` | PASS; 47 / 275 / 473 / 242 유지 |
| `reconcile_registry.py --priorities-only` dry-run → apply | paper/header 변경 0, reading status·source evidence 변경 없음 |
| `build_registry_views.py` dry-run → apply | 1,037 index rows, 526 resource entries, 49 relations |
| 변경 전·후 `audit_repository.py` | 최종 오류 0 / 경고 0; 5,185개 note·322 active / 47 history 유지 |
| Tier·active/history CSV SHA256 | 작업 전후 동일 |
| Manifest 범위 | 지정 4개 record의 code/project 관련 필드만 변경; 나머지 1,033개 record 보존 |
| 기존 dirty worktree 보존 | 시작 시 343개 파일 중 의도한 변경 외 변경·삭제 없음 |
| Source·note 검증 | 31개 source SHA256·line anchor 범위 및 수정한 12개 note after-hash 확인 |
| 전체 표준 노트 C0/C1 재검사 | 5,185개 / 잔여 0 |
| `git diff --check` | PASS |

중간 audit는 임시로 가져온 외부 README의 누락 asset·문서 형식 때문에 15건을 보고했다. 해당 항목 모두 task 전용 cache 경로임을 확인했고, cache 삭제 후 전체 audit가 통과했다. Registry 논문 노트의 링크 오류로 보고하지 않는다.

공식 소스 텍스트 31개와 metadata 응답·대조용 helper·patch·snapshot 등 이번 task의 임시 디렉토리를 삭제했다. PDF·dataset·model payload를 내려받지 않았고 package 설치나 실험 실행은 없다. Permanent ledger에는 URL·commit·hash·지정 구간과 해석만 보존한다. Git commit/push는 이번 작업에서 수행하지 않았다.
