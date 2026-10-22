# D1-L1 — 직접 baseline의 방법·공개 구현 경계

- 검토일: 2026-10-22 KST. [TODO](../../../TODO.md)의 D1-L1 산출물.
- 범위: G-PSMR의 지정 절, GAP 공식판·고정 commit, ReViP 버전 경계를 추가 대조했다. 정책·simulator 실행, 학습, package 설치는 없다.
- 기록: [source/commit/hash와 정적 파싱 결과](./baseline_method_sources_2026-10-22.json). 전체 baseline 역할은 [dossier](./BASELINE_DOSSIER.md)를 따른다.
- 완료 의미: **접근 가능한 직접 근거와 미확인 항목을 구분한 문헌 감사 완료**. 모든 방법의 재현 준비나 D1의 효과 검증 완료가 아니다.

## 1. G-PSMR: gate 시점과 결합 순서 확인

**Paper-supported:** Publisher §3.5 Eq.(11)의 state gate는 첫 policy query에서 초기 회전과 clean reference의 SO(3) 거리를 비교한다. Threshold는 0.07 rad이고 gate는 episode 동안 고정된다. Gate가 열리면 orientation에 `Rc R0⁻¹ Rt`를 적용하며 position/gripper는 유지한다. §3.6의 joint variant는 state를 먼저 보정한 뒤 visual gate를 계산한다. [Publisher 원문](https://www.mdpi.com/1099-4300/28/9/975).

근거 범위는 **publisher 검색 색인에 제공된 지정 절**이다. 직접 HTML 접근은 rate limit으로 제한됐다. 공식 구현·calibration manifest를 식별하지 못했으므로 source와 수식의 일치, frame/rotation conversion, 실제 실행은 검증하지 않았다. 이전 dossier에서 미확인으로 남겼던 **수식 수준의 gate 시점은 이번에 확인**했다.

**D1 해석:**

- Episode 도중 생긴 오류에 매번 gate를 다시 계산하는 구현은 원래 M2와 다르다. 원논문 M2와 prefix-only 재평가 변형을 별도로 비교해야 한다.
- Visual gate의 입력이 state correction에 의존하므로 M1과 M2의 효과를 독립·가산이라고 가정할 수 없다. B0/M1/M2/M3의 factorial 비교가 필요하다.
- 초기 reference가 맞는 constant orientation bias는 단순한 이 연산만으로 제거될 수 있다. 그러한 조건에서 원인 분류기 추가를 정당화할 수 없다. 정확한 가정과 도출은 [claim 계약](./CLAIM_EVIDENCE_CONTRACT.md)에 둔다.

## 2. GAP: 공식 수식과 공개 training entrypoint의 차이

공식 [ICLR 2026 본문 §4.3 Eq.(5), Algorithm 1](https://proceedings.iclr.cc/paper_files/paper/2026/file/2b3bb2c95195130977a51b3bb251c40a-Paper-Conference.pdf)을 확인했다. 아래 차이는 arXiv 버전에서만 찾은 것이 아니다.

| 확인 대상 | 직접 확인한 내용 | 재현에 주는 영향 |
|---|---|---|
| 공식판 Eq.(5), Algorithm 1 | Gradient 계수 `λ(1−ρ)`, mini-batch의 average indicator | 수식·pseudocode 기준 variant |
| 공개 `gap/gap.py` L83, L86, L91 | Batch maximum phase로 `1−λ max(phase)`를 만들고 backward 후 누적 gradient에 곱함 | 평균/최댓값과 λ의 위치가 모두 다름. 같은 λ로 동일 알고리즘이라고 볼 수 없음 |
| 같은 파일 L85 | `lambda = self.cfg.lambda`에서 Python `ast.parse`가 SyntaxError를 반환 | 해당 commit의 training entrypoint는 수정 없이 Python 문법 파싱을 통과하지 못함 |
| 같은 파일 L88 | Zero-based epoch 0부터 50까지 inclusive 조건 | 문자열상의 “first 50 epochs”와 boundary 차이를 기록해야 함 |
| 선택 config·optimizer | `gap.yaml`의 λ=0.3, optimizer는 AdamW | Gradient scaling을 곧바로 같은 비율의 parameter-update scaling이라고 해석하지 않음 |
| 전체 27개 blob tree | Octo 전용 recipe/checkpoint를 식별하지 못함 | 논문에 Octo 평가가 있어도 해당 재현 자산이 확인된 것은 아님 |

Source는 [공식 repository의 고정 commit](https://github.com/GeWu-Lab/GAP/tree/2f605436c68eedf328c05520d52877604af730d3), [training 파일](https://github.com/GeWu-Lab/GAP/blob/2f605436c68eedf328c05520d52877604af730d3/gap/gap.py#L83), [선택 config](https://github.com/GeWu-Lab/GAP/blob/2f605436c68eedf328c05520d52877604af730d3/gap/cfgs/gap.yaml), [optimizer config](https://github.com/GeWu-Lab/GAP/blob/2f605436c68eedf328c05520d52877604af730d3/gap/cfgs/optimizer/adam.yaml)다. 9개 source/config를 메모리에서 읽었고 Python 4개를 **실행·import 없이** stdlib AST로 파싱했다. Training 파일 1개 실패, 나머지 3개 통과다. 원문 code나 package를 로컬에 설치하지 않았다.

**해석과 처리:** 공개 snapshot의 문제이지 논문 실험 결과가 틀렸다는 증거는 아니다. 이번에는 upstream을 수정하지 않았다. 추후에는 syntax 수정 diff와 선택한 규칙을 기록하고, `paper-equation variant`와 `released-rule variant`를 구분한다. Holdout 성능을 본 뒤 유리한 규칙을 “원래 GAP”로 선택하지 않는다. Native model로 옮기면 여전히 GAP-style port다. AdamW의 adaptive state·weight decay까지 포함한 실제 최적화 효과는 미검증이다.

## 3. ReViP: 버전과 추가 정보 비용 유지

**확인 사실:** [arXiv v3](https://arxiv.org/html/2601.16667v3)의 §4·implementation appendix는 visual task-stage observer, TSFiLM과 policy fine-tuning을 설명한다. [현재 저자 project](https://isee-laboratory.github.io/ReViP/)는 추가 attention rebalance·Flash를 소개하며 Code coming soon을 표시한다. 최신 project 연결 manuscript와 supplementary는 이번 web 도구의 크기 제한으로 본문을 확인하지 못했다.

**D1 계약:** v3 기반 port와 최신 project의 방법을 같은 재현으로 취급하지 않는다. 외부 observer가 보는 task goal·workspace view, observer 지연·cue의 나이, fine-tuning 비용을 모두 비교 조건에 넣는다. Frozen wrapper와 training-based variant는 예산이 다르다. 최신 버전의 정확한 구현과 accepted venue는 계속 미확인이다.

## 4. 완료한 판단과 남긴 의존성

| 항목 | 지금 가능한 결정 | 남은 의존성 |
|---|---|---|
| G-PSMR | 원논문 gate와 online 변형을 분리; 결합 순서 통제 | 공식 구현·rotation convention·calibration manifest |
| GAP | 공개 코드 링크만으로 runnable 판정하지 않음; 수식/공개 규칙 구별 | 수정/clarification, Octo recipe, 실제 qualification |
| ReViP | 최신 project를 누락한 약한 novelty 비교 방지 | 최신 구현/본문의 동일 버전 확인 |
| D1 | 단순 보정이 충분한 반례와 task-dependent 필요성 심사로 진행 | 실제 task source·관측 가능성 검토, 이후 native 정책 실험 |

외부 자산 의존성은 TODO의 D1-R1에 남긴다. 이 항목들은 다음 비실험 분석을 막지 않는다. 사용자 정독 tracker, registry membership, paper note의 evidence level은 변경하지 않았다.
