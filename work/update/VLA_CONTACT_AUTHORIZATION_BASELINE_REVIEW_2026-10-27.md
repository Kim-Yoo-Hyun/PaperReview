# GAP-AUTH4 — 로컬 지각과 단순 baseline의 충분성 심사

- 완료: 2026-10-27 KST. **비실험 심사 DONE / 현재 두 과제의 방법 채택 NO-GO / 진단 HOLD / 실행 packet PARTIAL·native gate NOT_MET.**
- 핵심 판단: 구현 후보는 좁혔지만, **초기 지시 grounding + 목표 identity 고정 + 매 시점 geometry 갱신** 이후에 남는 방법적 이득을 확보하지 못했다. 연구 가설이 실험으로 반증됐다는 뜻은 아니다.
- 이전: [AUTH3 계약](./VLA_CONTACT_AUTHORIZATION_CONTRACT_REVIEW_2026-10-27.md), [AUTH2 두 과제](./VLA_CONTACT_AUTHORIZATION_SOURCE_REVIEW_2026-10-27.md), [canonical 질문](../../synthesis/05_world_models_safety.md#gap-authorization-2026).
- 산출물: [source·선택 자산·baseline·재개 gate JSON](../sources/vla_contact_authorization_baseline_review_2026-10-27.json). 환경 실행용 manifest가 아니며 `executable=false`다.
- 공식 저자 YOLOE revision의 source/config/license 20파일과 AEGIS revision의 2파일 지정 구간, HF release metadata 1건, Apple weights URL의 HEAD metadata를 확인했다. 논문은 지정 본문/공식 metadata 범위만 확인했다.
- 실험·모델/API 호출·Docker/GPU probe·설치·학습·PDF/weights/init payload 다운로드 없음. 공개 source text와 release metadata만 읽었으며 registry 등록·tier·읽기 status 변경 없음.

## 1. 결론이 바뀐 이유

AUTH1–3의 좁은 질문은 정책의 잘못된 대상 추정이 안전 필터의 잘못된 보호 제외로 전파되는가였다. 이 진단 자체는 남아 있다. 그러나 현재 task는 **첫 목표 접촉까지 목표 identity가 고정된 두 과제**다. 위치를 계속 추적해야 한다는 사실이 목표를 계속 다시 선택해야 한다는 뜻은 아니다.

기존 B3는 *정책이 처음 예측한 대상*을 고정하고, B4는 *지시의 관계를 별도로 해석*하는 대안이었다. 둘만 비교하면 **초기 판단의 출처**와 **판단 갱신 빈도**를 동시에 바꿀 수 있다. 이번에는 지시를 처음 해석한 대상을 고정하는 강한 단순 baseline을 추가했다. 모든 arm에서 물체 geometry는 계속 갱신한다.

이 대안으로 설명되지 않는 자연 사례·차별적 예측이 아직 없다. 따라서 새 learned guard나 복잡한 동적 authorization 방법을 만들 근거가 부족하다. 지각 파이프라인을 더 보강하는 것만으로 연구 가치가 생기지는 않는다.

## 2. 하나로 좁힌 공통 지각 후보

선택은 **공식 YOLOE-11m text-prompted segmentation + 같은 source tree의 ByteTrack**이다. 작은 물체·관계 anchor를 찾을 수 있는 공개 mask interface가 있고, 별도 cloud VLM 없이 모든 arm이 같은 검출 결과를 공유하도록 설계할 수 있기 때문이다. 최고 성능이라는 선택도, SafeLIBERO에서 작동을 확인했다는 선택도 아니다.

| 항목 | 확인한 기준과 한계 |
|---|---|
| 논문 | [YOLOE: Real-Time Seeing Anything, ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_YOLOE_Real-Time_Seeing_Anything_ICCV_2025_paper.html). CVF 검색 결과의 공식 bib metadata 확인; 직접 HTML fetch는 403. 본문은 [arXiv v1 §3.1–3.2](https://arxiv.org/html/2503.07465v1#S3.SS1) 사용, camera-ready 전체 대조 아님 |
| Code | `THU-MIG/yoloe@40cd606cabdbe2b566d6f14a6b162c89206e9a1b` |
| Checkpoint | 저자 README가 연결한 HF `jameslahm/yoloe`, revision `b584da188a198a2e6aa0e013d3fef6d55b212603`, `yoloe-11m-seg.pt` |
| Checkpoint identity | 60,276,714 bytes; LFS SHA256 `785199b7cc75a5f4041dec15782a4b8a4105e5a34d7ffb287a0a10781724c5bd`. **서버 metadata이며 byte 다운로드/검증은 안 함** |
| Text encoder | 배포 log config는 `mobileclip:blt`. Source가 `mobileclip_blt.pt`를 local load한 뒤 text embedding을 생성 |
| Text weights | [Apple 공개 URL](https://docs-assets.developer.apple.com/ml-research/datasets/mobileclip/mobileclip_blt.pt), HEAD 200; 599,214,572 bytes, ETag `d61231bd164d23e7e500076e0e8f0d3e`, Last-Modified 2024-02-27. ETag를 SHA256으로 취급하지 않음; 내용 hash 미확인 |
| License provenance | YOLOE source LICENSE 및 HF card는 AGPL-3.0. Vendored MobileCLIP code는 MIT, weights/data는 별도 Apple `LICENSE_weights_data`. 모두 하나의 MIT license로 묶지 않음 |
| Tracker | 이 fork의 ByteTrack. 기반 [ECCV 2022 공식 accepted list](https://eccv2022.ecva.net/program/accepted-papers/)에서 논문 확인; 원 저자 구현 전체와의 동등성을 주장하지 않음 |
| 실행 상태 | Model load·목표 class 검출·ID 유지·depth registration·latency·native reset 모두 미확인 |

근거: [저자 README의 모델/설치 연결](https://github.com/THU-MIG/yoloe/blob/40cd606cabdbe2b566d6f14a6b162c89206e9a1b/README.md#L47), [배포 config](https://github.com/THU-MIG/yoloe/blob/40cd606cabdbe2b566d6f14a6b162c89206e9a1b/logs/yoloe-11m-seg/args.yaml#L116), [text encoder](https://github.com/THU-MIG/yoloe/blob/40cd606cabdbe2b566d6f14a6b162c89206e9a1b/ultralytics/nn/text_model.py#L38), [HF revision](https://huggingface.co/jameslahm/yoloe/tree/b584da188a198a2e6aa0e013d3fef6d55b212603), [Apple weights license](https://github.com/THU-MIG/yoloe/blob/40cd606cabdbe2b566d6f14a6b162c89206e9a1b/third_party/ml-mobileclip/LICENSE_weights_data). 이는 배포물의 표기를 기록한 것이며 법적 호환성 판단은 아니다.

**중요:** KNOWS는 YOLOE를 해당 환경에 finetune하고 가림 처리·HSV 기반 재연결을 설명한다. 공개 일반 checkpoint + ByteTrack은 그 구성의 재현이 아니다. 같은 YOLOE 이름만으로 KNOWS의 지각 성능/비용을 가져오지 않는다. [KNOWS §3.2·4.1](https://arxiv.org/html/2606.09749v1#S3.SS2).

## 3. 연결할 수 있는 interface와 실제 약한 고리

### Mask와 시간적 identity

[공식 예제](https://github.com/THU-MIG/yoloe/blob/40cd606cabdbe2b566d6f14a6b162c89206e9a1b/predict_text_prompt.py#L49)는 `get_text_pe → set_classes → predict`를 사용한다. 결과는 box/class/confidence와 instance mask다. `get_text_pe`는 text encoder를 실제로 생성하므로 checkpoint 하나만 있으면 모든 초기화가 끝난다고 가정하지 않는다. 고정 vocabulary의 embedding은 초기화 때 생성·hash 후 재사용하는 설계다. 아직 생성하지 않았다.

YOLOE의 class prompt는 관계 해석기가 아니다. 두 검은 그릇을 모두 `bowl`로 검출할 수 있어도 `between plate and ramekin` 또는 `on stove`가 어느 instance를 뜻하는지는 별도로 계산해야 한다. 이 환경의 ramekin·flat stove·작은 그릇에 대한 zero-shot 성능도 미확인이다.

[Tracking callback L18–87](https://github.com/THU-MIG/yoloe/blob/40cd606cabdbe2b566d6f14a6b162c89206e9a1b/ultralytics/trackers/track.py#L18)과 [ByteTrack L270–438](https://github.com/THU-MIG/yoloe/blob/40cd606cabdbe2b566d6f14a6b162c89206e9a1b/ultralytics/trackers/byte_tracker.py#L270)에서 다음을 확인했다.

- `persist=True`는 tracker 보존 옵션이지 실제 object identity 보장이 아니다. Matcher는 box IoU와 score를 사용하며 해당 거리 계산에는 class 또는 appearance embedding을 넣지 않는다. 같은 모양 그릇의 교차·가림 이후 재연결은 별도 위험이다.
- Callback은 기본 frame_rate=30으로 tracker를 만들고, detection이 0개이면 `update`를 건너뛴다. 따라서 frame counter와 잃어버린 track의 수명을 simulator 시간으로 바로 해석할 수 없다.
- Tracking이 성공하면 detection index로 Results를 subset해 mask도 같은 순서로 연결한다. Detection이나 track이 없을 때 기존 결과가 tracking ID 없이 남을 수 있으므로 `boxes.id=None`을 정상 identity로 보완해서는 안 된다.
- Default tracker는 배포 config에서 BoT-SORT다. 이번 ByteTrack 선택은 **명시적 변경**이며 이름만 지정하고 기본값을 그대로 쓴 결과로 기록하지 않는다.

비교용 adapter에는 case/branch/camera namespace, reset, 매 control timestamp의 빈 frame 처리, 실제 갱신 시간, track/mask join 검증이 필요하다. Class 간 잘못된 연결은 class별 tracker로 제한하되, `ramekin`과 `bowl`의 중복/분류 모호성은 숨기지 않고 invalid로 남긴다. 이 수정들은 **미구현**이다.

### RGB·depth·camera frame

선택 계약은 agent camera의 RGB-D 한 쌍이다. YOLOE 입력은 640 letterbox, geometry는 원래 해상도의 metric depth와 native-size mask를 사용한다. `retina_masks=True`를 명시하면 해당 source의 native mask 경로를 선택할 수 있다. 기본 false일 때 `masks.data`를 원래 depth에 그대로 곱하지 않는다. [Segmentation postprocess L28–55](https://github.com/THU-MIG/yoloe/blob/40cd606cabdbe2b566d6f14a6b162c89206e9a1b/ultralytics/models/yolo/segment/predict.py#L28).

NumPy 입력 경로의 predictor는 BGR→RGB를 수행한다. Simulator의 RGB를 이 경로에 넘기려면 경계에서 BGR로 한 번 바꾸거나, 검증된 다른 입력 경로를 명시해야 한다. [Preprocess L116–160](https://github.com/THU-MIG/yoloe/blob/40cd606cabdbe2b566d6f14a6b162c89206e9a1b/ultralytics/engine/predictor.py#L116).

AEGIS는 runner의 RGB/D 회전, helper의 재회전·box 좌표 변환·vertical pixel 변환을 거친 뒤 카메라 K/T로 역투영한다. 첫 bbox만 사용하는 경로를 여러 mask에 그대로 확대하지 않는다. 새 계약은 각 mask pixel을 **공식 camera convention에 맞는 동일한 좌표계로 역변환한 뒤** metric depth와 K/T로 역투영하는 것이다. 224 정책 이미지용 변환은 별도로 기록한다. 특정 행렬을 적용해 이미 정렬됐다고 검증한 결과는 없다. [AEGIS helper L155–255](https://github.com/THU-RCSCT/vlsa-aegis/blob/ce5683c069983baef4e66025aef9da30d9d67ca2/main/utils.py#L155).

여기서 simulator depth와 알려진 calibration은 모든 guard에 제공되는 **명시적 합성 센서 가정**이다. Object pose·segmentation truth·target body ID와 구별한다. RGB-only 정책에 비해 guard가 받는 정보가 늘어난다는 사실도 숨기지 않는다. 모든 authorization arm에 같은 RGB-D·track·geometry 접근을 주되, 같은 접근 권한이 동일한 계산 방식이나 통계적 오류 독립성을 뜻하지는 않는다.

## 4. 최소 지각 설정 — 실행 가능한 환경으로 오인하지 않기

| 항목 | 문서상 v0 선택 |
|---|---|
| Vocabulary | 두 과제 공통 `bowl, plate, ramekin, stove`; 전체 지시·target ID는 detector에 주지 않음 |
| 범위 | 이 네 class가 모든 장애물을 덮는다는 주장 없음. 오접촉 primary는 두 그릇에 한정; 다른 장애물 safety를 주장하려면 별도 전체 inventory 필요 |
| 검출 | imgsz=640, batch=1, conf=0.10, NMS IoU=0.70, max_det=300, retina_masks=true, augment=false |
| ByteTrack | high=0.25, low=0.10, new=0.25, match=0.80, fuse_score=true. 제공 YAML에서 가져온 시작값이며 검증된 최적값 아님 |
| Clock | 20 Hz control frame마다 지각 갱신, 정책은 5 tick마다 query. 독립 update timestamp와 empty-frame 기록 필요 |
| Track age | nominal frame_rate=20, buffer=30이면 source 식상 max_time_lost=20 update. 실제 1초 보장은 uniform frame·빈 frame 갱신 때만 가능; stale track은 허용 대상으로 사용하지 않음 |
| Identity key | case/branch/camera/class/track_id. 다른 rollout의 tracker state 재사용 금지 |
| 기하 | 동기화된 visible mask-depth의 points/centroid/extent. 가려진 전체 형상·실제 support contact를 복원했다고 부르지 않음 |
| 결측 | Missing/duplicate anchor, zero-area mask, invalid depth, track ID 불명, 색/종류 모호함이면 abstain/invalid. Ground-truth mask/pose로 몰래 대체하지 않음 |
| 비용 | 초기 text encoding, 매 frame segmentation/tracking/depth, rule 평가, QP·serialization, peak memory·annotation을 분리. 성능/VRAM 측정 없음 |

Black 속성을 무시한 채 general instruction grounding으로 부르지 않는다. 두 후보가 모두 black이라는 실측 확인이 있는 이 task slice에서만 공간 관계로 구분할 수 있다. 그렇지 않으면 별도 color 판정과 calibration이 필요하다. Vocabulary·관계 grammar가 두 task에 맞춰 고정된 비용도 baseline에 기록한다. 자유 형식 언어 일반화는 주장하지 않는다.

향후 선택 자산을 실행한다면 설치와 모델 load는 local Docker 내부에서만 수행한다. 저자 설치 예시는 Python 3.10을 사용하지만, AUTH3의 JAX server·SafeLIBERO client와 합친 lock/image/VRAM은 검증되지 않았다. 이번 단계에서는 Dockerfile·runtime patch·model cache를 만들지 않았다.

## 5. 단순 관계 baseline을 구체화

**Task identity는 AUTH2를 그대로 따른다.** T1은 plate와 ramekin 사이의 그릇, T2는 stove 위의 그릇이다. Native goal은 특정 초기 instance를 plate 위에 놓는 것이며, 평가용 `bowl_1` 이름을 아래 규칙에 전달하지 않는다.

### T1: between

원 지시를 제한된 grammar로 parse해 target category=bowl, anchors=plate/ramekin으로 만든다. 관측에서 얻은 anchor 중심 p·r과 후보 그릇 중심 b를 동일 table/world plane에 투영한다. 다음은 **연구자가 정한 geometry rule**이지 YOLOE 논문의 방법이 아니다.

- λ = (b−p)·(r−p) / ||r−p||²
- d = ||b−p−λ(r−p)|| / ||r−p||
- λ가 두 anchor 사이이고 d가 사전 tolerance 안인 후보를 찾되, anchor spacing이 작거나 둘 이상 통과하면 abstain한다.
- Visible depth 중심은 물체의 실제 중심과 다를 수 있다. Normal/depth/centroid uncertainty와 tolerance는 별도 dev calibration 대상이며 현재 숫자를 임의 확정하지 않는다.

### T2: on

Stove의 보이는 support surface/footprint와 bowl의 visible cloud를 비교한다. 수평 포함/겹침과 수직 간격이 사전 tolerance를 만족하는 유일한 bowl을 선택한다. Stove의 top surface가 가려져 추정할 수 없거나 두 bowl이 구별되지 않으면 abstain한다.

Image의 “위쪽”이나 2D box overlap만을 물리적 `On`으로 쓰지 않는다. 이 규칙은 depth 기반 **지지 관계의 시각적 proxy**이며 MuJoCo contact predicate와 다르다. 원 native goal의 evaluator를 baseline 내부에서 호출하면 정보 누출이다.

### 처음 가리킨 대상과 현재 관계를 만족하는 대상

지시에서 “stove 위의 그릇”은 이 task slice에서 **처음 지시가 지칭한 물체**다. 그릇이 움직였다는 이유로 현재 stove 위의 다른 그릇을 새 target으로 바꾸면 다른 목표를 수행한다. 따라서 주된 단순 대안은 **초기 관계로 정한 visual identity를 고정하고 그 위치를 계속 추적**한다. 이후 관계 재계산은 identity/추적의 검증 단서가 될 수 있지만 target을 무조건 다시 바인딩하는 규칙은 공정한 baseline이 아니다.

## 6. 빠져 있던 2×2 비교와 조건부 충분성

모든 cell은 같은 지각·모든 물체의 최신 geometry·controller·QP·budget을 쓴다. `init`은 **허용 identity**만 고정한다. Geometry를 초기 위치에 고정하는 약한 비교가 아니다.

| 초기/갱신 판단 출처 | 처음 identity 고정 | Query마다 다시 판단 |
|---|---|---|
| 내부 attention proxy | I-init: 기존 B3 | I-refresh: 기존 B1, B2는 confidence-only 대안 |
| 원 지시 + 같은 perceived relation | **R-init: 새로 명시한 필수 단순 baseline** | R-refresh: 기존 B4 해석을 제한; 원 지시의 instance identity를 보존해야 함 |

B0 무필터, B5 전부 보호/정지, B6 oracle permission은 별도 reference로 유지한다. 두 관계 규칙은 별도 learned grounding model이 아니며, narrow grammar 비용을 숨기지 않는다.

### 조건부 충분성 논증 — 실험 결과가 아님

첫 접촉 구간의 정답 instance를 o*, 허용 집합을 A={o*}라 하자. 초기 관계 규칙이 track k*를 정확히 고르고, 매 시점 track-to-object mapping m_t(k*)=o*가 유지된다면,

**E_t={m_t(k*)}=A**

이므로 R-init의 잘못된 보호 제외는 이 조건 아래 이미 0이다. 동적인 learned authorization이 이 오류를 더 줄일 수 없다. 이는 가정 아래의 논리적 결과이며 **초기 grounding 정확도, tracking 정확도 또는 contact-free 동작을 증명하지 않는다.** Geometry/controller 오차로는 여전히 접촉할 수 있다.

| 실패/성공 조건 | 기존 단순 대안의 설명력 | 남는 질문 |
|---|---|---|
| 초기 선택은 맞지만 내부 score가 다른 bowl로 바뀜; tracking 정상 | I-init 또는 R-init으로 막을 수 있음 | 단순 고정 이후 새 방법 이득 미확보 |
| 내부 초기 선택은 틀리고 관계 규칙은 처음부터 맞음 | R-init의 초기 grounding 차이 | “동적 독립성” 이득으로 해석 불가 |
| 초기 관계는 모호/오류, 이후 새 관측이 관계를 해소 | 고정만으로 부족할 수 있음 | 실제 정보가 증가한 자연 packet 필요. 단순 재평가·abstention 이후의 이득도 비교 |
| Track swap/가림으로 identity가 틀림 | 초기 고정도 실패 가능 | Authorization과 tracker 재식별 문제를 분리; 모든 arm에 같은 association을 적용 |
| Mask/depth가 잘못됨 | 공통 실패 가능 | 독립 코드가 오류 독립성의 증거가 아님 |
| Refresh가 현재 관계를 만족하는 다른 bowl로 목표 변경 | 잘못 정의된 baseline | 새로운 task/phase 문제로 몰래 전환하지 않고 비교 기각 |

**안전율 하나만으로 충분하지 않다.** 자연적인 오접촉 빈도, 실제 nominal action/첫 접촉 대상, 유효 head baseline, 정상 작업 완료·abstention·invalid·시간을 함께 봐야 한다. Attention argmax 자체를 정책의 진짜 의도나 실행할 물체의 정답으로 정의하지 않는다.

## 7. Buildup 판정과 재개 조건

선택 자산의 존재와 class/mask/track 인터페이스는 확보했다. 하지만 실제 두 그릇과 anchor의 검출, camera-depth 정합, 초기 referent 선택, ID 유지, native filter/evaluator는 검증되지 않았다. 또한 현재 고정 target/첫 접촉 범위에서 R-init 뒤에 남는 새 방법의 이득도 확보하지 못했다.

따라서 이번 TODO의 사전 중단 규칙에 따라 **현재 설계의 비실험 확장을 종료하고 진단 HOLD로 둔다. 방법 채택은 NO-GO**다. “이 현상은 없다” 또는 “YOLOE가 이 task에서 실패했다”는 실험적 결론이 아니다. GPU가 없어서만 멈춘 것도 아니다.

**GAP-AUTH-R1 — WAITING_EVIDENCE.** 다음 자료가 새로 생겼을 때에만 재심사한다.

1. 원 지시·동일 instance의 RGB-D/frame/time·읽기 가능한 action/contact 경로가 연결된 자연 사례. 공개 문헌/저자 artifact도 가능하며, 지금 새 rollout을 수집하라는 지시가 아니다.
2. Detector/track 오류와 별개로, 검증된 내부 readout의 높은 confidence가 잘못된 제외와 실제 nominal 행동에 연결된 witness. 주입 label·평균 proxy만의 오류는 별도 표기.
3. R-init/I-init·confidence threshold·단순 relation re-evaluation/abstention 뒤에도 남는 차별적 예측. 초기 목표 오류, 새 관측 정보, track swap, phase 변화 중 무엇이 원인인지 명시.
4. 모든 arm의 같은 지각·geometry·timing/비용과 독립 evaluator. Oracle mask/body ID에만 의존한 개선은 deployment 근거로 승격하지 않음.

같은 source를 재집계하거나 학습/환경 이식으로 이 공백을 덮지 않는다. 기존 DATA-TRANSFER/N3와 16개 후보 판단도 유지한다. 다음 실행 가능한 비실험 TODO는 **GAP-S2: 기존 보류 주제와 겹치지 않는 다른 VLA 공백을 최대 3개로 재선별**하는 것이다. 구현 난이도보다 직접 선행·단순 대안·남는 예측을 먼저 비교하고, 새 주제의 GO를 미리 약속하지 않는다.

## 8. 문서·registry 검증

- `py_compile`, tier generator, `git diff --check` 통과. Repository audit **오류 0·경고 0**, 수정 문서 local link 624개에서 깨진 경로 0개.
- Registry 1,072편·CORE 47/NEXT 297/REFERENCE 486/ARCHIVE 242·active tracker 344/history 47·표준 note 5,360개 유지. Canonical registry/manifest/meta/tier/tracker 6파일 hash 동일.
- 작업 전 dirty 641파일 중 이번 수동 수정 7파일 외 **634파일**의 byte를 보존했고 기존 missing 10경로도 유지했다. Source 22파일 SHA256·읽기 구간을 확인한 뒤 임시 source/metadata 26파일을 삭제했다.
- 문서·registry 유지보수 결과이며, detector 성능·tracking·native safety 또는 정책 효과 검증으로 기록하지 않는다.
