# GAP-DE2 — 변형체 식별의 공개 비교 자산 충분성 심사

- 검토일: 2026-10-24 KST. **작업 DONE / 현재 공개 자산 기반 설계 종료 / 문헌 진단 HOLD**. 일반 방법 NO-GO·native VLA HOLD는 유지한다.
- [DE1 문헌 비교](./DEFORMABLE_IDENTIFICATION_REVIEW_2026-10-24.md)의 다음 단계다. Canonical 질문은 [GAP-DEFORM](../../synthesis/03_manipulation_contact.md#gap-deform-2026), 출처·고정 revision·지정 구간·hash·검증은 [source ledger](../sources/deformable_asset_sufficiency_review_2026-10-24.json)에 둔다.
- AdaptiGraph·JIGGLE·PGND·DPSI의 4개 자료군을 심사했다. GitHub 3개 revision의 source/config/doc, PGND Hugging Face 2개 release의 목록·README·dataset manifest만 확인했다. Source는 실행/import하지 않았고 PDF·dataset archive·checkpoint payload는 받지 않았다. 실제 데이터 무결성이나 native 실행 검증이 아니다.

## 1. 결론

**개별 구성 요소는 공개되어 있지만, 이번 질문을 그대로 검증할 비교 구성이 확인되지는 않았다.** AdaptiGraph에는 물성 변화·조작·관측 저장 경로가 있고, PGND에는 공개 관측 데이터와 동역학 checkpoint가 있으며, DPSI에는 물성·마찰 fitting과 목표 형상 계획이 있다. 그러나 material와 숨은 attachment를 독립 변화시킨 같은 task, 정책에 허용된 행동 전 정보, 모든 탐색 시도·물리 시간·힘/변위 비용, 단순 feedback과의 비교를 연결하지 못했다.

따라서 DE1에서 정한 종료 규칙을 적용한다. 현재 공개 자료를 이어 붙여 효과를 평가하는 설계는 끝내고 **추가 수집/환경 수정이 필요한 문헌 진단**으로 보존한다. 이는 연구 가설이 실험으로 반박됐다는 뜻도, 물리적으로 그런 비교를 만들 수 없다는 뜻도 아니다. 이 턴은 자료·구현 계약의 정적 심사이며 연구 효과는 미측정이다.

다음 연구 목표를 “timestamp 수정”이나 “attachment 옵션 추가”로 바꾸지 않는다. 이런 수정은 공정한 실험을 위한 준비이지 독립적인 연구 기여가 아니다. GPU를 확보해도 현재 자료의 관측·대조군·비용 의미가 자동으로 채워지지 않는다.

## 2. 하나의 증거표: 무엇이 있고 무엇이 부족한가

`확인`은 아래 지정 source에서 확인한 내용, `부분`은 구성 요소만 존재, `미확보`는 이번 범위에서 연결하지 못한 증거다. 공개 데이터 전체에 해당 정보가 없다고 단정하는 표가 아니다.

| 자료군 | Material × attachment 독립 설정 | 관측–행동–시간–결과 연결 | 목표/제약을 바꾼 task pair | Feedback/fixed probe 공정 비교 | 재사용 가능한 부분 / 새로 필요한 부분 |
|---|---|---|---|---|---|
| [AdaptiGraph code](https://github.com/Boey-li/AdaptiGraph/tree/a7c75357793422e9108c36f58c6928f3f8a123ad) | **부분.** Cloth 강성·마찰이 같은 `sf`에 결합. Grasp의 임시 pin은 있지만 지속적인 숨은 환경 anchor의 독립 설정은 지정 경로에서 미확보 | Episode별 물성·action·particle/eef 저장. H5 `timestamp`는 프레임 수. 재시도와 비균일 샘플 간 실제 시간/비용 보존 미충족 | Target PCD/box cost와 재관측 loop는 있음. 같은 상태·다른 목표에서 필요한 정보가 갈리는 사례는 미확보 | Fixed probe·MPC의 부품은 가능. 현재 데이터만으로 모든 시도와 물리 시간을 맞춘 반사실 비교는 안 됨 | Scene/estimator/planner 재사용 후보. 물성/마찰 분리·환경 anchor·시간/attempt log·동일 초기 상태 재개 계약 추가 필요 |
| [JIGGLE 본문](https://arxiv.org/html/2405.09743v1)·[저자 페이지](https://nikhilushinde.github.io/) | Boundary strength field는 formulation에 있음. 이를 material와 독립 변화하는 공개 실행 설정은 미확보 | 본문에 state/action·boundary belief와 sim active sensing은 있음. 저자 공식 code/raw episode packet은 이번 검색에서 식별하지 못함 | 정보량·boundary safety의 목적과 후속 task utility 비교는 다름 | Predefined motion primitive 등 선행 baseline은 있음. 동일 자산에서 material/attachment/task를 묶을 수 있는지는 미확인 | Boundary 모델의 개념 기준. 구현/config·초기 상태·실행 비용·goal evaluator를 새로 연결해야 함. “코드 미공개”로 확정하지 않음 |
| [PGND code](https://github.com/kywind/pgnd/tree/06ef5dbbe9612b56aaee317c938dcf953074c05f)·[dataset release](https://huggingface.co/datasets/kaifz/pgnd-dataset/tree/58932f8ac660a2cba3d880675181369a4dc66cbc) | 실제 object별 관측/짧은 history의 dynamics. 검토 schema에는 material/anchor ground truth·factorial condition 지정이 없음 | Source/merged window와 camera/robot 기록 경로 확인. Offline interpolation과 카메라 timestamp/image 선택 불일치 가능성을 분리해야 함 | 목표 PCD·Chamfer cost는 있음. Goal별 feasible action 차이·관측상 동등한 물리 쌍은 미확보 | 재관측 MPC 부품은 있음. Recorded trajectory window가 미실행 probe의 outcome이나 비용은 아님 | 동역학·perception baseline 후보. 시간 정합 검증·조건 label·실제 command/attempt/force log·matched task 수집 필요 |
| [DPSI code/data tree](https://github.com/IanYangChina/SI4RP-data/tree/d4f01a503aa6700c1fe6222f81c10ecf1ca4c013) | Material/friction 파라미터는 명시적. 지정 env의 boundary는 cube workspace/table이며 숨은 attachment가 아님 | 시작 mesh·끝 PCD와 motion/data ID가 연결. Simulation `dt_global`·trajectory도 있음. 연속 관측 이력·실제 acquisition 비용과는 별개 | Target height map 교체와 후보 poking-shifting 비교 가능. 숨은 anchor와 goal을 교차한 실제 task pair는 미확보 | 고정 motion·zero action·planning 부품은 가능. 같은 hidden-anchor task에서 history feedback와 비교하려면 확장 필요 | 기존 SysID/shape-planning 기준. Elastic sheet의 attachment와 연결하려면 물체/환경/관측 모델도 새 설계 필요 |

**다른 논문의 증거를 합쳐 하나의 완성 자산으로 세지 않았다.** 예를 들어 AdaptiGraph의 material randomization과 JIGGLE의 boundary 결과는 같은 mesh·controller·관측·시간 기준을 공유하는 paired trial이 아니다. PGND의 공개 모델도 이 둘을 자동으로 이어 주지 않는다.

## 3. AdaptiGraph: 독립 요인과 시간·시도 단위

### 3.1 Material·friction 결합과 boundary라는 이름의 의미

[`scenes.py:139–175`](https://github.com/Boey-li/AdaptiGraph/blob/a7c75357793422e9108c36f58c6928f3f8a123ad/src/sim/sim_env/scenes.py#L139)는 `sf`에서 stiffness factor와 dynamic friction을 함께 만든다. 이 cloth 생성 설정에서 물성 knob를 움직인 결과를 stiffness 단독 효과로 설명할 수 없다. 이는 DE1에서 확인한 **논문 부록의 별도 rope stiffness/friction 실험이 없다는 주장과 다르다**.

`FlexScene`의 scene 29는 C++ `SoftgymCloth`로 연결되며, [scene constructor](https://github.com/Boey-li/AdaptiGraph/blob/a7c75357793422e9108c36f58c6928f3f8a123ad/PyFleX/bindings/scenes/by_softgym_cloth.h#L18)는 강성·마찰·mass를 받는다. [`flex_env.py:472–496`](https://github.com/Boey-li/AdaptiGraph/blob/a7c75357793422e9108c36f58c6928f3f8a123ad/src/sim/sim_env/flex_env.py#L472)의 `boundary_points`는 cloth의 가장자리 grasp 후보다. 같은 파일의 grasp loop는 particle inverse mass를 0으로 바꾸고 선택한 pick point의 mass를 복원한다. 이것을 환경의 숨은 anchor 위치/강도 label로 사용할 수 없다.

### 3.2 저장된 frame·유효 interaction이 모든 물리 시도는 아님

[`data.py:24–34`](https://github.com/Boey-li/AdaptiGraph/blob/a7c75357793422e9108c36f58c6928f3f8a123ad/src/sim/data_gen/data.py#L24)의 `info.timestamp=T`는 배열의 frame 수다. Cloth config는 접촉 근처와 그 밖에서 저장 간격을 다르게 정하고, [step loop](https://github.com/Boey-li/AdaptiGraph/blob/a7c75357793422e9108c36f58c6928f3f8a123ad/src/sim/sim_env/flex_env.py#L365)에는 별도 grasp/settling step도 있다. 저장 index를 고정 주기의 timestamp로 대체할 수 없다.

[`data_gen.py:64–105`](https://github.com/Boey-li/AdaptiGraph/blob/a7c75357793422e9108c36f58c6928f3f8a123ad/src/sim/data_gen/data_gen.py#L64)는 행동 실행 뒤 영상 변화가 작으면 buffer를 비우고 다시 시도한다. 그 branch에서 simulator state를 이전 값으로 되돌리는 호출은 보이지 않는다. **이 writer에서 파일 사이의 연속성이 모든 실행 시도·시간을 보존한다는 보장은 없다.** 실제 배포 archive의 발생 빈도/영향은 payload를 검사하지 않아 미측정이다.

Real interface에는 camera timestamp가 있고 목표 오차를 갱신하는 loop도 있다. 그러나 [`plan.py:274–295`](https://github.com/Boey-li/AdaptiGraph/blob/a7c75357793422e9108c36f58c6928f3f8a123ad/src/planning/plan.py#L274)의 interaction NPZ writer는 action·초기/예측/실측 state를 저장하며 이 timestamp나 force/총 비용을 함께 쓰지 않는다. **상위 interface에 필드가 있는 것과 비교 artifact까지 보존되는 것은 다르다.**

## 4. PGND: 공개 release가 제공하는 것과 정합 경계

### 4.1 원본 episode와 trajectory window를 구별

공식 code의 다운로드 helper가 가리키는 `release-20260831`을 HF API로 확인했다. Dataset revision은 `58932f8ac660a2cba3d880675181369a4dc66cbc`, checkpoint revision은 `893e8b9b2f443f8c98066f7eadca0dbf7d92851d`다. [Dataset manifest](https://huggingface.co/datasets/kaifz/pgnd-dataset/blob/58932f8ac660a2cba3d880675181369a4dc66cbc/DATASET_MANIFEST.json)는 cloth의 **650 trajectory windows·19 raw episodes·40 eval windows**를 구별한다. 650개를 독립적인 물리 조건/로봇 시행 수로 세지 않는다.

`traj.npz`의 schema는 `xyz`, `v`; 그 밖에 end-effector trajectory/rotation/gripper, camera indices, metadata 파일이 명시된다. [Dataset card](https://huggingface.co/datasets/kaifz/pgnd-dataset/blob/58932f8ac660a2cba3d880675181369a4dc66cbc/README.md)는 source/merged window의 중복을 hardlink로 포장한다고 설명한다. 이것은 재사용 경로의 장점이지만 material/attachment의 factorial label, 각 probe 후보의 실제 outcome, native task 성공·힘 비용을 뜻하지 않는다. Counts·hash는 저자 manifest의 보고이며 archive checksum을 직접 검증한 결과가 아니다.

### 4.2 Offline 정합을 online 정책 입력으로 바꾸지 않음

Camera recorder는 frame index와 camera timestamp를 기록한다. Robot pose writer는 queue를 읽는 host 시각과 pose/gripper를 저장한다. [`postprocess.py:126–175`](https://github.com/kywind/pgnd/blob/06ef5dbbe9612b56aaee317c938dcf953074c05f/experiments/real_world/postprocess.py#L126)는 인접 robot sample 사이에서 보간한다. 이 미래 쪽 sample을 사용한 사후 정렬은 offline dynamics 학습용일 수 있지만, 의사결정 당시 이용 가능한 history와 동일하게 취급하면 안 된다.

더 구체적인 정적 불일치가 있다. [같은 파일 :83–124](https://github.com/kywind/pgnd/blob/06ef5dbbe9612b56aaee317c938dcf953074c05f/experiments/real_world/postprocess.py#L83)는 다른 camera의 가까운 timestamp를 `t-1` 또는 `t`에서 고른 뒤 기록하지만, RGB/depth를 복사할 때는 모든 camera에 `t`를 사용한다. **`t-1`이 선택되는 경우 기록된 시각과 복사된 image index가 어긋날 수 있다.** 현재 release가 이 branch의 영향을 받은 비율·정책 성능 영향은 확인하지 않았으며, paper-run commit도 미확인이다. 재현 실행·전체 데이터 오류 판정을 한 것이 아니다.

[`dataset.py:23–72`](https://github.com/kywind/pgnd/blob/06ef5dbbe9612b56aaee317c938dcf953074c05f/pgnd/data/dataset.py#L23)는 설정된 `dt_frame`으로 end-effector 위치 차분을 velocity로 만든다. 이를 실제 command issue/acknowledgement 기록으로 바꾸어 해석하지 않는다. [Planning objective](https://github.com/kywind/pgnd/blob/06ef5dbbe9612b56aaee317c938dcf953074c05f/experiments/real_world/modules_planning/planning_module.py#L171)는 목표 PCD와의 Chamfer 및 workspace/EEF 제약이며, 검토한 목적 함수 자체가 접촉 force 한도 평가기는 아니다.

## 5. DPSI와 JIGGLE: 다른 종류의 boundary

DPSI의 [`SysIDEnv`](https://github.com/IanYangChina/SI4RP-data/blob/d4f01a503aa6700c1fe6222f81c10ecf1ca4c013/simulator/doma/envs/sys_id_env.py#L51)는 table·mesh·cube workspace를 정의한다. `make_env`는 같은 data index의 초기 mesh와 최종 PCD를 연결하거나 planning target height map을 선택한다. [Greedy planner](https://github.com/IanYangChina/SI4RP-data/blob/d4f01a503aa6700c1fe6222f81c10ecf1ca4c013/scripts/experiments/greedy_planning.py#L160)는 두 poking-shifting trajectory의 위치 offset과 zero action을 최종 height-map loss로 비교한다. 이는 유용한 고정 행동·목표 기준이지만, 숨은 sheet anchor·force cap·continuous observation history의 비교를 이미 제공하는 것은 아니다.

Data tree에는 motion별 초기/최종 geometry와 trajectory/timestamp 이름의 파일, 두 planning target이 있다. **파일명과 loader 연결만 확인했으며 실제 array 값·시각 동기화·단위는 검증하지 않았다.** `dt_global=0.01`인 simulation 설정과 실제 로봇의 acquisition/대기/스캔 시간은 별개다. 실제 로봇 결과를 그리는 한 script도 이미지 montage를 만들므로, 이 script 하나로 전체 trial/cost ledger의 존재나 부재를 판단하지 않았다.

JIGGLE의 [§III·IV](https://arxiv.org/html/2405.09743v1)는 환경에 붙은 tissue의 attachment strength를 별도 변수로 둔다. 이는 위 코드의 geometric edge나 workspace wall과 다르다. [공식 RSS entry](https://roboticsproceedings.org/rss20/p007.html)·저자 페이지·exact-title/code 검색을 재확인했지만, 이번 범위에서 저자가 연결한 실행 code와 paired raw data를 식별하지 못했다. 같은 제목의 workshop PDF를 별도 신규 연구나 실행 자산으로 세지 않았다. 기존 boundary 추정 방법의 존재와 공개 자산 연결 가능성은 별도 판단이다.

## 6. 무엇을 재사용하고 무엇을 새로 만들어야 하는가

| 구분 | 현재 확보한 근거 | 현재 확보하지 못한 것 / 필요한 작업 |
|---|---|---|
| 물리 조건 | AdaptiGraph의 cloth 물성 입력, JIGGLE boundary formulation | Material/friction/anchor를 독립 설정하고 숨은 값이 policy에 새지 않는 단일 환경. 이는 구현·물리 검증이 필요한 새 자산 |
| 초기 상태와 episode identity | Episode/interaction/window 저장 규칙·source 매핑 metadata | 동일 관측 prefix에서 분기할 state/controller/RNG snapshot 및 instance-level holdout. Window별 무작위 split만으로 대체 불가 |
| 정책에 허용한 관측 | RGB-D/point cloud·robot pose의 writer/loader | 실제 capture/receive/decision time·force calibration·online history. Offline 미래 sample 보간과 분리 |
| Task pair | Target PCD/box/height map을 바꾸는 interface | 같은 history에서 목표/제약에 따라 유효 행동이 갈리는 물리 사례. 공통의 느린 feedback 행동도 대안으로 허용 |
| 비용과 평가 | Geometry error·일부 timing 출력·simulation step 설정 | 실패/무효 probe·reset·대기 포함 attempt ledger, force/변위/물리 시간, native success/constraint evaluator |
| Baseline | Fixed action·재관측 MPC·기존 SysID/ILC의 문헌·코드 부품 | 동일 sensor/controller/goal/budget 아래 no-extra-probe history feedback, fixed/max-displacement probe, 기존 task-oriented 방법의 비교 구성 |
| VLA | Object segmentation text·목표 geometry의 interface | Instruction이 실제 목표/제약을 바꾸는 task와 checkpoint/controller/evaluator 연결, oracle 조건의 기본 수행 능력 |

문헌·코드만으로 이미 효과가 있어야 한다고 요구한 것은 아니다. 작은 pilot을 하려면 **무엇이 독립 변수이고 어떤 기록으로 비용·결과를 셀 수 있는지**가 먼저 정해져야 한다. 현재는 새 simulation/fixture·수집·정합 작업이 포함되는 별도 프로젝트 규모이며, 그 투자를 정당화할 차별적 조건 예측도 아직 확인되지 않았다.

## 7. 종료·재개·다음 TODO

- **현재 종료:** 기존 release를 바로 재조합하는 GAP-DE 설계. `executable=false`, 자료 gate `NOT_MET`. DE3·학습·payload 다운로드를 자동으로 만들지 않는다. DE1의 조건부 질문은 문헌 진단 HOLD로 보존한다.
- **재심사 입력:** 독립 material/anchor 조건과 실제 관측/행동/시간/비용/평가를 잇는 새 source 또는 수집 계획, 공통 feedback 행동과 구별되는 예측, 같은 환경에서 가능한 baseline. 긍정 효과를 미리 입증할 필요는 없다. GPU나 같은 metadata 재조회만으로 재개하지 않는다.
- **다음 GAP-S1:** 지금까지 심사한 공백을 중간 종합하고 VLA 중심의 다음 연구 선택을 정리한다. 기존 NO-GO 원리의 재명명을 제외하고, 남은 질문의 차별적 예측·공개 실행 자산·필요한 새 수집을 비교해 **이어갈 한 후보 또는 현재 채택 가능한 후보 없음**을 결정한다. 현재 synthesis의 질문 소유권을 유지하고 별도 gap/priority registry를 만들지 않는다.

## 8. 유지보수

Registry·tier·읽기 입력·DE1 근거와 기존 실험 artifact를 보존했다. TODO·manipulation/VLA synthesis·buildup guide·navigation을 이번 종료 판단과 맞춘다. 생성기·repository audit·diff 및 기존 dirty 보존 검증은 source ledger의 `validation`에 기록한다. 임시 source/metadata는 URL·revision·hash 보존 뒤 삭제한다. Host 설치·Docker 변경·새 실험·Git commit/push는 없다.
