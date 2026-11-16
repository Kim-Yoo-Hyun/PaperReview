# 행동 토큰화의 복원 오차와 실행 구간 — 새 후보 buildup 결과

**현행 투자 판단 — 2026-11-07:** [8개 후보 비교](../../README.md#candidate-priority)에서 평가 자료를 보존하고 독립 방법 투자는 보류한다. 낮은 순위의 핵심은 GPU 부재가 아니라 기존 결과가 알려진 변환·양자화로 설명되고 추가 행동상의 가치가 미확인이라는 점이다. 호환 codec에서 설정 선택과 실제 제어가 바뀌는 새 증거가 재검토 조건이다.

현행 비실험 상태 검토: **2026-11-05** · [7단계 상태·기여 가설·판단 분기](#buildup-status). 기존 문헌/계약/결과를 대조한 보강이며 새 효과 관측은 없다.

**11/05 통합 판단:** 새로 등록한 ProAct는 H/실행 길이 및 tokenizer-free flow policy 비교까지 포함한다. 따라서 일반 reconstruction/control 불일치나 horizon 차이 발견을 새 기여로 쓰지 않는다. 남는 것은 H·rate·normalizer를 맞춘 설정 선택에서 prefix metric의 추가 가치다. 기존 CPU 결과는 알려진 전역 변환/양자화 설명을 넘지 못했으므로 독립 방법 투자는 보류하고 평가 자료를 보존한다. Learned codec 호환성도 필요해 GPU만의 문제가 아니다.

근거·전체 상대 비교: [기존 6개+새 2개 공백 검토](../../../update/INTEGRATED_GAP_REVIEW_2026-11-05.md). 신규 paper별 확인 절과 status는 [등록 원장](../../../sources/registry_admissions_2026-11-05.json)에 통합한다. 기존 실행 계약·원시 결과·과거 source 날짜는 보존한다.

- 검토·실행일: 2026-11-03 KST; 내부 ID `GAP-CODEC1`.
- 추가 비실험 보완: 같은 날 [N1 검토](#nonexperimental-followup)에서 적용 범위·수학적 대안 설명·현재 공개 interface·공정 비교를 보완했다. 기존 실험 결과를 재측정하거나 변경하지 않았다. 최신 후속 판단은 §8을 따른다.
- **결론:** 수행 가능한 내부 문헌·논리 검토와 Docker CPU 진단을 완료했다. 실행을 가정한 앞부분의 복원 오차를 따로 점검할 실무적 이유는 확인했다. 그러나 현재 결과는 알려진 전역 변환·양자화의 성질로 설명 가능하며 **독립적인 새 방법 연구로 본격 투자할 근거는 부족하다.** 좁은 평가 후보로 보존한다.
- 기존 정책 실험 준비 3개와 REVISION 우선순위는 유지한다. 이번 작업은 네 번째 정책 실행 packet이 아니다. 실제 외부 피드백·VLA 정책 실행·성공률 검증은 미완료다.
- 근거: [source ledger](sources.json), [동결 비교 계약](../재현%20방법/CONTRACT.json), [실행 결과](../재현%20방법/results/verified/results.json), [보충 대조 결과](../재현%20방법/results/suffix_verified/results.json), [재현 안내](../재현%20방법/README.md).

## 1. 공백부터 후보를 고른 과정

2024–2026을 검색 범위로 기존 registry와 외부 공식 proceedings·저자 본문·공개 코드를 함께 대조했다. 검색 종료일은 11월 3일이다. 직접 근거는 2025–2026 행동 토큰화 논문에 집중했다. 모든 venue를 전수 조사한 체계적 고찰이나 해당 분야의 신규성 확정은 아니다.

| 검토 방향 | 가치와 기존 답 | 이번 판단 |
|---|---|---|
| 카메라·좌표계 변경과 VLA 행동 일관성 | 다른 로봇에 옮길 때 중요하지만 D1/E1의 정렬·행동 support 문제와 겹침 | 기존 후보의 재명명으로 시작하지 않음 |
| 지연·비동기 chunk 실행 | 실행 feedback에 직접 연결되나 E2·기존 latency 검토와 최신 horizon 방법이 이미 있음 | 신규 timing controller 제안으로 확장하지 않음 |
| 성공 판정·평가의 신뢰도 | 유용하지만 TERM·기존 실패 판정 검토와 중복 | 이번 후보에서 분리 |
| **토큰화 평가와 실제 사용할 행동 구간의 관계** | 전체 복원 점수로 tokenizer를 고를 때 실제 사용할 앞부분을 얼마나 설명하는지 확인할 가치 | 알려진 큰 주장부터 제거하고, 동일 앞부분의 복원 안정성으로 좁힘 |

**5개 항목 후보 카드**

1. 문제: VLA가 긴 행동 chunk를 예측하고 앞부분만 사용할 때, tokenizer의 전체 chunk 점수와 앞부분 점수가 다른 선택을 유도하는가?
2. 중요성: 답에 따라 tokenizer·horizon 선택 시 보고할 평가 항목이 달라진다. 로봇 실패 비용의 크기는 아직 측정하지 않았다.
3. 알려진 답: reconstruction만으로 정책 성공을 설명할 수 없고, 예측·실행 horizon을 분리한 평가도 이미 있다.
4. 남긴 질문: **원 행동의 앞부분을 고정하고 인코딩할 미래 길이/내용만 바꾸면, 동일 앞부분의 복원값은 얼마나 달라지는가?** 이것이 단순 수치적 성질을 넘어 유용한 선택 기준인지가 후속 질문이다.
5. 최소 검사: 공식 FAST를 공개 시연의 행동 배열에 적용하고, 전체/앞부분 오차·동일 앞부분 간 차이·단순 불변성 대조를 비교한다. 정책이나 성공률을 대신 측정했다고 해석하지 않는다.

## 2. 가장 가까운 선행과 실제 확인 범위

| 근거·공식 상태 | 이미 답한 부분·interface | 이번 후보에 주는 제약 / 확인 범위 |
|---|---|---|
| [FAST, RSS 2025](https://www.roboticsproceedings.org/rss21/p012.html); [본문](https://arxiv.org/html/2501.09747v1) §V–VI, Appendix B | 정규화한 연속 행동을 DCT·양자화·BPE로 압축하며 복원과 압축 관계를 평가 | 전역 DCT 자체나 복원 trade-off는 신규성이 아님. 공식 processor 전체를 검토하고 실행; BPE는 양자화된 계수의 부호화를 담당 |
| [OAT, RSS 2026](https://www.roboticsproceedings.org/rss22/p075.html); [본문](https://arxiv.org/html/2602.04215v1) §V-A1, V-C3, Fig. 5 | 행동 horizon과 latent 길이, 실행 길이를 바꿔 평가. 토큰 prefix로 전체 행동 chunk를 복원 | 예측/실행 horizon 분리 자체를 gap으로 주장할 수 없음. [공개 코드](https://github.com/Chaoqi-LIU/oat)의 FAST wrapper·OAT forward/loss 확인; 모델 실행 없음. 토큰 prefix와 시간상 행동 prefix는 다름 |
| [FASTer, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9dc5accb1e4f4a9798eae145f2e4869b-Abstract-Conference.html) | 학습 tokenizer와 block-wise VLA decoding의 복원·효율·정책 성능 연결 | 최종 공식 abstract/status 확인. [arXiv v2](https://arxiv.org/html/2512.04952v2) §3–4는 이전 버전이므로 세부 구조를 최종판과 동일시하지 않음. 최종 전체 본문·checkpoint 실행 미확인 |
| [Beyond Reconstruction / ProAct, 2026-10 preprint](https://arxiv.org/abs/2610.09170); [본문](https://arxiv.org/pdf/2610.09170v1) §3–6.3, Fig. 1–2, Table 1–2 | 복원 외에 토큰 예측 가능성·잘못 예측한 토큰의 해독 견고성을 다룸. Horizon 및 정책 rollout 비교도 수행 | 가장 강한 직접 선행. “복원 오차만으로 성공을 설명 못 한다”는 신규 주장을 폐기. 62쪽 전체 정독은 아님. [project](https://ripl.github.io/action-tokenization-web/proact/)의 code는 `soon`; 구현 재현 없음 |
| [When Do Discrete Actions Make Good Continuous Controllers?, 2026-10 preprint](https://arxiv.org/html/2610.20429v1) §3–5, Appendix E.4/G.1 일부 | 이산화 정밀도와 표현 분해·정책 제어 특성을 구분 | 낮은 수치 오차를 좋은 controller와 동일시하지 않는 반대 설명. 코드 실행 없음 |
| [Real-Time Execution with Autoregressive Policies / REALFAST, 2026-06 preprint](https://arxiv.org/html/2606.13355v1) §3.3 및 관련 부록 | 실제 queued 실행에 맞춘 chunk·토큰화 길이 조정 | 실행 horizon에 맞춘 변경이라는 넓은 방법 역시 이미 존재. 실시간 이득을 이번 offline 결과에서 추정하지 않음 |
| [ActionCodec2 저자 project](https://zibindong.github.io/actioncodec2-page/) / [code](https://github.com/ZibinDong/actioncodec2) | Streaming·per-step 오차 제어라는 대안 family를 공개 | 학회 채택·논문 식별자·본문은 미확인. README/tree/interface 설명만 검토. 저자 소개의 성능 수치를 채택 논문 증거로 사용하지 않음 |

Registry의 FAST `pr-0749`가 출발점이다. 새 외부 source는 이번 후보의 ledger에 남겼으며, 신규 paper folder 등록·tier·사용자 reading status 변경은 하지 않았다. 위 표는 최초 검토의 범위다. 이후 OAT 확장판의 지정 부분과 유지보수 코드를 §8에서 추가 확인했으며 전체 정독·모든 learned tokenizer의 조건 재현은 아니다.

## 3. 기제·경쟁 설명과 주장–증거 연결

정규화 행동 배열 `x`의 크기를 `H × d`, 앞부분 길이를 `e ≤ H`라 하자. FAST의 계수 clipping이 없는 경우 핵심 수치 변환은 다음과 같다.

```text
q_H = round(10 × DCT_H(x)),   x_hat_H = IDCT_H(q_H / 10)
full_MSE   = mean((x_hat_H − x)^2)
prefix_MSE = mean((x_hat_H[:e] − x[:e])^2)
prefix_delta_RMS = sqrt(mean((x_hat_short[:e] − x_hat_long[:e])^2))
```

양자화를 없애면 DCT/IDCT는 입력을 복원한다. 양자화가 있으면 전역 기저와 미래 행동이 계수의 반올림을 바꾸어 앞부분 복원값도 변할 수 있다. **이는 알려진 변환의 성질에서 예상한 설명이며 새 정리가 아니다.** 미래의 실제 관측을 정책에 제공한 것도 아니다. 여기서는 저장된 시연 행동을 codec에 넣었다.

| 잠정 주장 | 구별할 설명·대조 | 결과와 허용하는 해석 |
|---|---|---|
| 같은 앞부분도 horizon에 따라 복원이 달라짐 | 공식 decode 오류·계수 clipping·정규화 변경 가능성 | 동일 normalizer·공식 구현과 독립 DCT parity·clipping 검사 통과. 아래 표의 제한된 현상 확인 |
| 전체 오차가 앞부분 오차의 선택을 가릴 수 있음 | 서로 다른 길이의 평균 분모·오차 분포 차이만으로도 발생 가능 | 일부 episode에서 선호 불일치. 데이터셋 평균 순위 역전은 없음; 새로운 metric이 정책 선택을 개선한다는 주장 불가 |
| 미래 내용이 앞부분 복원에 영향을 줌 | 첫 비교는 horizon 기저 길이도 바꿈 | 고정 길이·합성 hold suffix 보충 대조로 미래 내용 의존성 확인. 자연적인 행동 분기의 빈도/위험은 미확인 |
| 이것이 VLA 정책 실패 원인임 | 정책의 토큰 예측 오류·control tolerance·관측 feedback이 더 중요할 수 있음 | 정책·접촉·성공 미측정. 지지하지 않음 |
| 새 tokenizer가 필요함 | Pointwise/streaming 또는 기존 horizon tuning으로 충분할 수 있음 | Pointwise는 불변성 통과하지만 bitrate 미정합. 새 방법 필요성·기존 방법 우열은 미확인 |

## 4. 실제 실행한 최소 진단

기본 설계는 실행 전에 [CONTRACT](../재현%20방법/CONTRACT.json)에 고정했다. 최초 결과를 본 뒤 horizon 길이와 미래 내용의 혼동을 분리하도록 [보충 계약](../재현%20방법/CONTRACT_SUFFIX.json)을 작성하고 별도로 실행했다. 보충 검사를 처음부터 사전 등록된 primary endpoint로 표시하지 않는다.

- **자원:** M4 ARM64·host 16 GiB. 로컬 Docker Desktop 28.3.3, Linux/aarch64, 10 CPU·약 7.65 GiB. NVIDIA 할당은 exit 125로 실패했다. CPU 진단은 실제 실행했다.
- **제한:** 각 run 2 CPU·3 GiB·600초·다운로드 100 MiB 이하. 실제 각각 9.29초/8.53초, 3,634,507/3,629,570 bytes. 이는 설치·build 시간이나 정책 지연이 아니다.
- **데이터:** [ALOHA sim transfer cube human](https://huggingface.co/datasets/lerobot/aloha_sim_transfer_cube_human)와 [PushT](https://huggingface.co/datasets/lerobot/pusht)의 고정 revision 행동 parquet만 사용. 이미지·영상은 받지 않았다. 두 데이터셋 모두 시뮬레이션 시연이며 real-robot·cross-embodiment 전이 실험이 아니다.
- **분리:** 데이터셋별 episode 0–4로 q01/q99 normalizer를 추정하고 5–14를 진단. 앞 번호의 편의 표본이며 무작위 모집단 표본·정책 학습 독립 holdout·성공 인증 시연으로 주장하지 않는다.
- **구간:** 1초/2초 horizon을 비교하고 앞 0.2초를 실행 예정 구간으로 가정했다. ALOHA는 50/100/10 steps·14차원, PushT는 10/20/2 steps·2차원. 실제 executor는 실행하지 않았다. Episode 경계나 padding 없이 최대 8개 비중첩 구간을 선택했다.
- **정규화·대조:** 값은 clipping하지 않았다. 진단 episode 전체에서 범위 밖 비율은 각각 4.01%/4.32%. Identity·0.1 간격 pointwise 반올림 대조를 두었다. Pointwise는 같은 bitrate 비교가 아니다. 원 단위 MAE는 차원별로 보존하고 다른 단위를 합산하지 않았다.
- **구현:** 공식 FAST+ processor/tokenizer 고정 revision·scale 10. Decode에 horizon/dimension을 명시하고 독립 DCT 계산과 대조했다. 모든 구간에서 parity 최대 오차 0, coefficient floor clipping 0, decode failure 0. 공식 decoder의 silent zero fallback을 성공으로 처리하지 않도록 검사했다.

### 4.1 Horizon 길이 비교

아래 평균은 **episode별 평균을 먼저 구한 후 episode에 같은 가중치**를 준 값이다. 한 episode의 여러 window는 독립 시행이 아니다. 각 데이터셋을 별도로 해석하며 101개 로봇 rollout으로 부르지 않는다.

| 항목 | ALOHA sim | PushT |
|---|---:|---:|
| 진단 episode / 행동 window | 10 / 40 | 10 / 61 |
| 전체 MSE, 1초 → 2초 | 0.0001593 → 0.0001655 | 0.0004384 → 0.0004266 |
| 앞 0.2초 MSE, 1초 → 2초 | 0.0001783 → 0.0002193 | 0.0006218 → 0.0005588 |
| 동일 앞부분의 복원값 차이 RMS | 0.01691 | 0.02564 |
| 전체/앞부분 오차의 horizon 선호가 다른 episode | 2/10 | 4/10 |
| 같은 불일치가 있는 window, 기술 통계 | 18/40 | 26/61 |
| 평균 BPE token 수, 1초 → 2초 | 51.63 → 98.93 | 4.78 → 7.23 |

**데이터셋 전체 평균에서는 순위가 뒤집히지 않았다.** ALOHA는 두 metric 모두 1초를, PushT는 모두 2초를 선호했다. 작은 episode별 차이를 실용적으로 중요한 선택 오류로 해석할 수 없다. 두 full MSE는 서로 다른 길이의 원 행동에 대한 평균이므로 동일 support에서의 공정한 tokenizer 우열 비교도 아니다. RMS 0.01 초과는 계약의 기술적 flag이며 로봇 안전·성공 임계값이 아니다.

### 4.2 길이를 고정한 보충 대조

각 2초 window의 앞 0.2초는 그대로 두고 나머지는 앞부분 마지막 행동을 반복하는 **합성 hold suffix**로 바꿨다. 원 데이터에서 실제로 발생한 다른 continuation이나 물리적으로 실행 가능한 시연 쌍을 만들었다는 뜻은 아니다. Source asset·원 행동 window hash는 최초 결과와 일치했다.

| 동일 앞부분 복원값의 차이 | ALOHA sim | PushT |
|---|---:|---:|
| FAST, episode 균등 평균 RMS | 0.01802 | 0.02808 |
| 양자화 없는 DCT/IDCT, window 최대 RMS | 2.60e-16 | 2.80e-16 |
| Pointwise 반올림, 최대 RMS | 0 | 0 |

보충 대조는 양자화된 전역 표현의 미래 내용 의존성이라는 해석을 지지한다. BPE 토큰 순서의 인과성이나 VLA가 미래를 관측한다는 주장이 아니다. Native 정책의 자연 분포·고정 training horizon에서 같은 위험이 중요한지는 남아 있다.

<a id="buildup-status"></a>

## 5. 비실험 buildup 현행 상태 — 2026-11-04

**판정: 좁은 평가 자료 보존 · 내부 검토/과거 CPU 진단 완료 · 독립 방법 투자 근거 부족.** [7단계 비실험 절차](../../../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)를 기존 문헌·논리·계약에 적용해 정리했다. 아래 상태는 새 실험 결과나 11/04 신규 문헌 전수조사가 아니다.

**한 문단 기여 가설:** 행동 tokenizer 설정을 고를 때 전체 복원 점수와 실제 실행 구간 점수가 다른 결정을 유도하는지 묻는다. 기여 후보는 **같은 입력·horizon·rate에서 실행 구간 평가가 실질적인 설정 선택을 바꾸는 조건**이다. DCT/양자화의 알려진 성질을 새 tokenizer 원리로 재명명하지 않는다.

| 비실험 단계 | 상태 | 현재 근거·완료 경계 |
|---|---|---|
| 1 문제·독자 | 정리됨 | §1: 행동 표현/제어 연구자의 codec 설정 선택. 수치 오차의 차이와 실제 제어 손실은 별개 |
| 2 가까운 선행 | 지정 범위 확인·후속 artifact 미확정 | §2/§8: FAST/OAT/FASTer/ProAct·streaming 대안. Learned codec의 지원 checkpoint·normalizer·IO는 아직 선택/검증되지 않음 |
| 3 질문·대안 | 논리 검토·좁은 실제 진단 있음 | §3/§8: 시간 prefix와 token prefix, 길이와 미래 내용, 양자화와 정책 예측을 분리. 알려진 전역 변환 설명이 남음 |
| 4 기여 서술 | 평가 질문만 유지 | 앞부분 점검의 실무 용도는 있으나 새 지식의 범위가 좁음. 데이터셋 평균 선택 역전·native 피해는 관측하지 못함 |
| 5 최소 비교 | 과거 CPU 완료·후속은 설계 | §4의 20 episode/101 window와 보충 계약은 실제 결과. §8의 고정 H/rate learned codec 비교·정책 효과는 미실행 |
| 6 실행 부담 | 후속 source/입출력 조건 미확정 | [재현 방법](../재현%20방법/README.md)은 기존 CPU 결과 경로. 새로운 codec 비교의 image/adapter 준비 완료와 다름; CPU 적합성도 checkpoint 뒤 판단 |
| 7 외부 비판 | 질문 준비·미수신 | §6의 ProAct/OAT 차별성·pointwise 대안·평가 체크 항목 가치 질문. 실제 독립 응답 없음 |

**결과에 따른 판단 — 아직 관측하지 않은 분기 포함**

| 다음 증거 | 바뀌는 판단 | 이 증거만으로 하지 않을 주장 |
|---|---|---|
| 호환 설정에서도 알려진 양자화 차이만 확인됨 | 재사용할 평가 점검 자료로 보존하고 독립 방법 투자는 보류 | 작은 RMS 차이를 로봇 위험/새 현상으로 확대 |
| 같은 H/rate에서 held-out 설정 선택 또는 사전에 정한 제어 허용 판단을 바꿈 | 그 결정 차이의 빈도·조건을 후속 조사 | 사후에 유리한 지표/허용치를 골라 기여로 주장 |
| 해당 선택 차이가 native 제어에서 반복 확인됨 | 예측 오류·codec 오류·실행 길이를 분리한 평가 연구 가능성을 검토 | Offline 복원 결과만으로 정책 성공 향상을 추정 |

현재 CPU 결과의 비용과 새 learned codec/정책 비교 비용은 별개다. 코드 공개만으로 checkpoint 호환성을 가정하지 않으며, 입력 의미·원 normalizer·실제 code length를 먼저 맞춘다. 필요 artifact를 얻지 못했다고 임의 tokenizer 재학습으로 확대하지 않는다.

**외부 검토 준비:** 가장 강한 외부 질문은 “평균 선택 역전이 없고 알려진 양자화 설명이 남는 현재 결과가, ProAct/OAT 이후 독립 연구보다 평가 체크 항목으로서 더 적절한가?”다. 긍정 사례와 무차이 결과를 함께 보여 준다. 실제 응답·반영이 생기면 내용과 source 위치를 기록한다. 미수신은 작은 탐색을 금지하는 진입 조건이 아니다.

**다음 확인과 문서 종료점:** 선택 가능한 후속은 호환 codec 한 개를 정할 수 있을 때의 고정 H/rate 비교다. 첫 작업 주에는 지원 horizon/단위·normalizer·checkpoint와 사용 가능한 데이터의 대응부터 검토한다. 전체 field의 NO-GO가 아니며, 평균 순위 역전만을 유일한 가치 기준으로 강제하지도 않는다. 새로운 직접 선행·자료·반례·피드백 없이 같은 문서 검토를 반복할 내부 과제로 만들지 않는다. 실행 범위·상한은 기존 계약과 [재현 안내](../재현%20방법/README.md)가 관리한다.

## 6. 연구 가치와 다음 행동

**얻은 것:** 동일 원 행동의 앞부분이 codec의 미래 길이/내용에 따라 달라지는 정도를 재현 가능한 공식 구현·두 데이터셋에서 기록했다. 전체 오차와 실행 예정 구간 오차를 구분하는 작은 평가 도구로 재사용할 수 있다. 좁은 offline 성질에만 실험 근거가 있으며 정책 관련 질문의 evidence maturity를 자동 승격하지 않는다.

**아직 약한 것:** 예측 가능한 양자화 성질이고, aggregate 선택 역전·정책 피해·단순 대안 이후의 이득이 없다. ProAct/OAT와 다른 중요한 새 지식을 보여 주지 못했다. 따라서 큰 학습·새 codec 구현으로 넘어가지 않는다. 이 판단은 행동 토큰화 분야 전체의 NO-GO가 아니다.

후속이 필요할 때 가장 정보가 되는 작은 비교는 **공개 learned tokenizer 한 개를 지원 training horizon·원 normalizer 그대로** 평가하고, 같은 원 window에서 bitrate를 맞춘 단순 pointwise 대안과 비교하는 것이다. 원 decoder의 입력·shape·정규화와 실제 code length를 먼저 고정한다. CPU 적합성은 해당 checkpoint를 고른 뒤 다시 판단한다. 낮은 수치 오차만 반복되면 진단 note로 종료한다. 특정 제어 허용 오차나 자연적인 실행 선택을 바꾸는 차이가 보일 때만 native 정책의 paired 비교를 설계한다. 현재 이 후속의 checkpoint/adapter는 구현·검증되지 않았고 실행 준비 완료로 세지 않는다.

Native 효과를 연구 주장으로 올리려면 같은 관측·정책·초기 상태·action interface·실행 길이·계산 예산에서 정책 예측 오류와 codec round-trip 오류를 분리해야 한다. 해당 조건의 성공/실패와 차원별 제어 오차를 함께 봐야 한다. GPU 확보만으로 이러한 차별성이 생기지는 않는다. 당장의 기존 GPU 재개 순서는 REVISION을 유지한다.

독립 검토자에게 보낼 질문은 다음 세 개다. 발송은 이번 작업에 포함하지 않았다.

1. ProAct/OAT가 이미 설명한 결과에서, 동일 action prefix의 안정성을 따로 보고 얻는 판단이 남는가?
2. 정상 training horizon과 native normalizer에서 pointwise·streaming 대안 이후에도 유의미한 제어 차이가 남을 가능성이 있는가?
3. Episode별 순위 차이와 aggregate 역전 부재를 고려하면, 이 작업을 독립 연구보다 평가 체크 항목으로 남기는 편이 적절한가?

기존 C3는 여러 token이 같은 실행 행동으로 합쳐지는 RL 목적함수 문제다. 이번에는 연속 행동 chunk를 압축·복원하는 성질을 검사했다. C3·E2의 과거 NO-GO/HOLD와 기존 세 후보의 자원/과학적 재개 조건은 변경하지 않았다.

## 7. 재현·보존 점검

실제 실행의 contract·source revision/hash·normalizer·개별 window·package 버전을 결과 JSON에 보존했다. 최종 Docker recipe는 실제 설치된 20개 dependency 버전을 고정했다. 원 결과 image와 최종 recipe image는 다르며, 최종 image에서 package freeze 일치·import·DCT smoke·계약/코드 hash·episode 집계 일치를 network 없이 확인했다. 데이터 실험을 최종 image로 다시 실행했다고 표시하지 않는다.

환경·검증·정리 내역은 [runtime 기록](../재현%20방법/results/runtime.json)을 따른다. 패키지·다운로드 자산은 container 안에만 두었고 raw action·weight·PDF를 host에 설치하지 않았다. Host에는 실행 코드·문서·작은 결과/설정 JSON만 남긴다. 이번 전용 image는 제거했고 남은 container는 0개다. 기존 사용자 image 1개는 보존했으며 전역 build cache 정리는 하지 않았다. 원격 게시·새 컴퓨터의 실행 검증은 미실시다.

필수 generator compile·재생성, repository audit, staged/unstaged whitespace 검사를 통과했다. Audit 오류·경고 0; registry 1,090편·표준 노트 5,450개·CORE/NEXT/REFERENCE/ARCHIVE 47/314/487/242를 유지했다. 작업 전 봉인한 canonical registry·읽기 CSV·기존 후보/실험 파일 **306개가 byte 단위로 동일**하고 staged index도 보존됐다.

<a id="nonexperimental-followup"></a>

## 8. 추가 비실험 buildup — 해석·대안·비교 설계 보완

2026-11-03 후속 검토. 새 데이터 계산·정책 실행·학습은 수행하지 않았다. 아래 수학은 기존 변환의 성질을 이 질문에 적용한 연구자 분석이고, 문헌·코드는 지정한 부분을 정적으로 읽었다. 기존 primary/supplemental 결과와 계약은 변경하지 않았다.

### 8.1 새로 확인한 선행이 바꾸는 적용 범위

[OAT 확장판](https://arxiv.org/html/2607.21670v1) §2, §4.2, §5.2, §6.2와 Appendix B/E를 추가 검토했다. RSS 원 논문의 확장 preprint이며 새 채택 venue는 확인하지 않았다. 두 경로를 구분한다. AR에서는 예측 token을 해독해 제어한다. Token co-training에서는 token loss를 학습 감독에 쓰고 추론은 별도 연속 action expert가 담당한다. 따라서 이번 codec 왕복 오차에서 **모든 VLA의 실제 실행 오차**로 가는 경로는 성립하지 않는다. 후속 적용 범위는 먼저 token을 실제 해독하는 AR 정책으로 제한한다. Token-budget prefix를 복원하는 OAT의 평가 역시 시간상 action prefix와 구별한다.

유지보수 중인 [Praxis 코드](https://github.com/Chaoqi-LIU/praxis-vla/tree/d99d1bb405c56f88998b978f5ec9e913afb31f1b)의 `evaluate_reconstruction.py`, OAT/core tokenizer, normalizer 관련 경로를 대조했다. 평가기는 checkpoint의 PolicyIO·normalizer를 요구하며 action 전체에 대한 raw MSE/MAE와 지원 token-prefix budget을 계산한다. 별도 train config에서 episode split·frame drop도 읽는다. **새 일반 reconstruction evaluator를 만드는 것은 기여로 삼지 않는다.** 현재 필요한 추가 항목은 고정된 시간상 실행 구간의 측정이며, 그것이 정책 선택을 바꾸는지는 미측정이다. 공개 README·project와 해당 author의 HF 목록 조회에서는 바로 쓸 OAT checkpoint를 특정하지 못했다. 이것은 전 세계 미공개라는 판정이 아니다.

[FASTer arXiv v2](https://arxiv.org/html/2512.04952v2) §4.2, Eq. 4, Fig. 5–6의 VRR은 이미 허용 오차 내 복원 비율과 horizon trade-off를 다룬다. 단순히 평균 대신 허용 오차를 쓰는 것 역시 신규성이 아니다. 해당 버전의 L1 표기와 거리 설명을 그대로 하나의 물리 metric으로 취급하지 않는다. 최종 ICLR PDF는 웹 도구 용량 제한/접근 확인 화면으로 전체 대조하지 못했으므로 v2의 세부를 최종판 검증으로 승격하지 않았다.

[ActionCodec2 공식 model card](https://huggingface.co/ZibinDong/ActionCodec2/tree/51ddccf2b414830351b1ca9d68690a5564758ed1)를 추가 확인했다. 공개 자산은 있으나 EEF의 metre/radian·rotation convention·gripper 의미·resampling·boundary state를 요구한다. ALOHA의 joint 배열이나 PushT의 2D 좌표를 그대로 7D EEF 입력으로 바꾸는 대조는 부적합하다. Joint profile도 차원·단위·gripper·현재 상태를 먼저 맞춰야 한다. Streaming이라는 이름만으로 원 sample-rate prefix의 불변성이 보장된다고 쓰지 않는다. 구현 전체나 성능은 실행 검증하지 않았다.

### 8.2 전체 평균과 앞부분 평균의 차이는 새 현상인가?

고정된 동일 `H × d` 구간의 오차를 `E`, 실행 예정 길이를 `e`라 하면 단순 분할 항등식이 성립한다.

```text
R_full = ||E||²_F / (H d)
R_exec = ||E[:e]||²_F / (e d)
R_tail = ||E[e:]||²_F / ((H-e) d)
R_full = (e/H) R_exec + (1-e/H) R_tail       (e < H)
```

두 tokenizer가 서로 다른 위치에 오차를 배분하면 `R_full`과 `R_exec`의 순위가 달라질 수 있다. 이 자체는 평균의 성질이다. 기존 1초/2초 비교는 원 support와 DCT 기저 길이까지 다르므로 **동일 bitrate·동일 horizon에서의 tokenizer 선택 오류를 증명하지 않는다.** 고정 길이 합성 suffix 검사는 미래 내용 의존성을 확인했지만 자연적인 로봇 실패율을 식별하지 않는다.

[SciPy DCT의 orthonormal 정의](https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.dct.html)에 따라, coefficient clipping이 없고 반올림 간격이 `1/s`이면 계수별 오차 절댓값은 `1/(2s)` 이하다. Parseval 관계와 앞부분 에너지가 전체보다 크지 않다는 사실을 적용하면:

```text
R_full ≤ 1/(4s²)
R_exec ≤ H/(4e s²)
```

이는 느슨한 수학적 상한이며 안전 보장이 아니다. `s=10`의 전체 상한 0.0025를 로봇의 물리 허용 오차로 해석할 수 없다. 추가로 계수 오차가 독립·평균 0·균등 분포라고 가정하면 각 시간 위치의 기대 오차 분산은 `1/(12s²)`로 같아진다. 실제 행동 데이터가 이 가정을 만족한다는 증거는 없지만, **DCT라는 이유만으로 앞부분이 체계적으로 더 나쁘다는 결론도 나오지 않는다.** 전체/앞부분 차이가 중요한지에는 오차 위치·물리 단위·실행 분포의 추가 근거가 필요하다.

### 8.3 비교 가능성 심사 — 확보한 것과 없는 것

| 비교 대상 | 이번에 확보한 비실험 근거 | 아직 필요한 조건 | 현재 판단 |
|---|---|---|---|
| FAST+ | 공식 revision·실제 기존 encode/decode·차원별 원 단위 오차 | 다른 scale/설정 선택은 별도 calibration 필요 | 기존 진단의 재현 가능 |
| OAT/Praxis | 고정 code revision·입출력·checkpoint sidecar·평가 split 경로 | 실제 tokenizer checkpoint, training horizon/units·normalizer·학습 노출 정보·라이선스 | 구현 경로 확인; 비교 실행 준비 완료 아님 |
| FASTer | ICLR status, 이전 본문 VRR/horizon 분석 | 최종 상세 정의와 사용할 공개 자산·config·revision | 문헌 대조용; 이번 실행 baseline으로 확정하지 않음 |
| ActionCodec2 | 공개 HF revision·명시적 행동 의미·boundary 요구 | 현재 데이터와 의미 호환 증명·resampling 경계·원 단위 tolerance | 다른 표현을 임의 reshape하여 비교하지 않음 |
| Pointwise quantization | 미래 구간에 독립적인 단순 대안·기존 불변성 대조 | 동일 공통 입력·clipping 정책·진짜 부호 길이와 rate calibration | 인과성 대조로 유효; 아직 성능/효율 우열 대조 아님 |

같은 token 수는 vocabulary가 다르면 같은 nominal bitrate가 아니고, 같은 nominal bitrate도 같은 latency가 아니다. Header/EOS·profile 분기·실제 token sequence 길이를 포함해 `n × log2(V)`와 실제 저장 bytes를 별도로 보고한다. 모델 backbone·KV cache·batch·generation schedule까지 맞추지 않은 wall time을 codec 자체의 효율로 귀속하지 않는다. Training 데이터 규모가 다른 codec의 결과는 해당 공개 artifact 비교이며 architecture의 순수 효과가 아니다.

### 8.4 가장 작은 후속 비교를 어떻게 바꿀 것인가

후속은 **방법 개발 없이 고정 `H`의 비교 설계**로 좁힌다. 아직 실행 승인이 필요한 새 권한을 만든 것이 아니라, 다음 관측이 무엇을 구분해야 하는지 정한 것이다. 구체 checkpoint가 없어 실행 계약 JSON을 하나 더 만들지 않았다.

1. 지원되는 행동 표현·sampling rate·고정 training horizon과 normalizer를 가진 공개 codec 한 개를 먼저 특정한다. 기존 FAST의 편의 표본을 그 학습 분포에 맞는 것으로 간주하지 않는다. Shape만 맞춘 padding·resampling·단위 변환은 금지하고 필요한 변환은 별도로 검증한다.
2. 같은 원 행동·같은 `H`·같은 실행 예정 `e`에서 full/prefix 원 단위 오차와 normalized 오차를 함께 측정한다. 두 horizon의 서로 다른 평균을 주 비교로 삼지 않는다. Gripper의 이산 의사결정은 연속 joint 평균과 분리한다. Controller 허용 오차가 없으면 임의 성공 임계값을 만들지 않는다.
3. Rate 설정·pointwise bin 폭·metric/tie 규칙은 calibration episode에서 고정하고, 선택 후 평가 episode에서는 변경하지 않는다. 전체 metric으로 고른 설정과 prefix metric으로 고른 설정의 **별도 평가 episode에서의 prefix 오차 차이**를 보고한다. 같은 평가 window에서 가장 좋아 보이는 설정을 고른 값을 선택 이득으로 쓰지 않는다.
4. 작은 표본에서는 episode별 paired 원자료와 실제 차이 크기를 먼저 보고한다. Window를 독립 반복으로 bootstrap하지 않고, 표본 수/검정력은 아직 확정하지 않는다. 자연 prefix pair가 없다면 합성 suffix 결과는 별도 stress 진단으로만 남긴다.
5. 차이가 없거나 rate/normalizer 보정 후 사라지면 현재 note로 종료한다. 차이가 있어도 원 단위의 제어 의미가 없으면 정책 학습으로 확대하지 않는다. 실제 해독 경로·허용 오차·공통 정책 조건에 연결되는 근거가 생길 때만 native 평가를 설계한다.

이 수정으로 구별할 경쟁 설명은 (a) 다른 평균 support, (b) bitrate/normalizer 차이, (c) 학습 분포 밖 입력, (d) 정책에서 codec을 실제 사용하지 않음이다. 기존 결과는 이 네 가지를 모두 배제하지 못했다. 반면 장면·목표를 본 뒤 threshold를 맞추는 방법이나 새 loss를 바로 추가하는 방식은 현재 자료로 정당화되지 않는다.

### 8.5 보완 후 판단

**내부 비실험 검토 보완 완료, 좁은 평가 후보 유지.** 선택 가능한 작은 비교의 조건을 더 명확히 했으며 탐색 진입 기준을 올리지는 않았다. 다만 공개 code가 있다는 사실과 곧바로 비교할 수 있는 checkpoint·데이터가 있다는 사실을 구분했다. GPU 부족이 현재 남은 유일한 문제는 아니다. 실제 codec artifact의 의미 호환성과 이 측정이 바꾸는 연구 판단을 먼저 확보해야 한다.

독립 새 방법의 본격 GO는 여전히 근거 부족이다. 기존 CPU 결과의 사실성은 유지하지만 VLA 일반 성능으로 확대할 수 있는 범위는 더 좁아졌다. 외부 검토 질문에는 “실제 해독형 AR 정책에 한정하고 같은 H/rate에서 설정 선택을 바꿔도 선행 대비 새 지식이 남는가?”를 추가한다. 실제 외부 발송·응답은 없었다.
