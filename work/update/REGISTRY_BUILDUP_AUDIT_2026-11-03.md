# Registry 최신화와 비실험 buildup 절차 감사

- Work ID: REG-R8 / BUILDUP-AUDIT2
- Date: 2026-11-03 KST
- 범위: 현행 registry 정합성·선택한 직접 선행의 공식 게재 확인·6개 연구 후보 절차 대조. 1,098편 전체의 게재 상태를 전수 재조사하지 않았다.
- 실험·환경 재시도·host dependency 설치·weights/assets/PDF 다운로드·외부 연락·git commit/push: 없음.

## Registry 반영

**1,090 → 1,098편**, 표준 노트 **5,450 → 5,490개**. CORE 47 / NEXT 321 / REFERENCE 488 / ARCHIVE 242; 집중 tracker 368 / history 47. 신규 8편 중 7편은 2025–2026 직접 선행, 1편은 2018 Q-filter 기원이다. 현재 VLA+RL 후보의 강한 baseline/충돌을 반영했다.

| Stable ID | 논문·표준 노트 | 검증한 게재 | Tier·등록 이유 |
|---|---|---|---|
| pr-1091 | [PLD](../../2026/ICLR/2026_ICLR_Self-Improving-Vision-Language-Action-Models-with-Data-Gen/01_overview.md) | [ICLR 2026](https://iclr.cc/virtual/2026/poster/10008318) | NEXT · VLA의 residual 개선→데이터 생성→base 갱신을 잇는 직접 선행이다. 현재 후보에서 이 루프 자체를 새 기여로 주장하지 않도록 NEXT에 추가한다. |
| pr-1092 | [Object-Centric Residual RL](../../2026/CoRL/2026_CoRL_Object-Centric-Residual-RL-for-Zero-Shot-Sim-to-Real-VLA-E/01_overview.md) | [CoRL 2026](https://www.corl.org/program/accepted-papers) | NEXT · Object-centric residual의 전이를 이미 다룬 직접 충돌 선행이다. 다양한 로봇·base 갱신 전이와 sim-to-real 전이를 구분할 NEXT다. |
| pr-1093 | [EXPO](../../2026/ICLR/2026_ICLR_EXPO-Stable-Reinforcement-Learning-with-Expressive-Policie/01_overview.md) | [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d56a652ad743308b24b6c4d0e6411dd7-Abstract-Conference.html) | NEXT · Residual/editor와 value 선택을 결합한 강한 직접 baseline이다. Q 선택·base 모방·editor RL이라는 조합 자체의 신규성 주장을 막는 NEXT다. |
| pr-1094 | [EXPO-FT](../../2026/CoRL/2026_CoRL_EXPO-FT-Sample-Efficient-Reinforcement-Learning-Finetuning/01_overview.md) | [CoRL 2026](https://www.corl.org/program/accepted-papers) | NEXT · 현재 VLA+RL 후보의 가장 가까운 공동 적응 baseline이다. 독립 base 갱신과 editor 공동 학습을 구별할 NEXT다. |
| pr-1095 | [Policy Decorator](../../2025/ICLR/2025_ICLR_Policy-Decorator-Model-Agnostic-Online-Refinement-for-Larg/01_overview.md) | [ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html) | NEXT · Frozen large policy+bounded residual의 핵심 비교 선행이다. 현재 후보의 scalar gain·탐색 schedule이라는 단순 대안을 놓치지 않도록 NEXT에 추가한다. |
| pr-1096 | [Uncertainty-Aware Residual RL](../../2026/RA-L/2026_RA-L_Accelerating-Residual-Reinforcement-Learning-With-Uncertai/01_overview.md) | [RA-L 2026](https://api.crossref.org/works/10.1109/LRA.2025.3636808) | NEXT · 현재 후보의 critic mismatch 대안을 검토할 직접 선행이다. 합성 행동 critic을 새 알고리즘으로 재주장하지 않도록 NEXT에 등록한다. |
| pr-1097 | [Q-filter](../../2018/ICRA/2018_ICRA_Overcoming-Exploration-in-Reinforcement-Learning-with-Demo/01_overview.md) | [ICRA 2018](https://api.crossref.org/works/10.1109/ICRA.2018.8463162) | REFERENCE · 선택적 Q 기반 imitation의 직접 기원으로 REFERENCE에 추가한다. 2024–2026 최신 동향 수에는 포함하지 않으며 기존 SAC/DDPG 기반 읽기 흐름을 보완한다. |
| pr-1098 | [DICE-RL](../../2026/ICML/2026_ICML_From-Prior-to-Pro-Efficient-Skill-Mastery-via-Distribution/01_overview.md) | [ICML 2026](https://proceedings.mlr.press/v306/sun26al.html) | NEXT · Frozen prior+residual+선택적 모방의 최신 직접 선행이다. 현재 후보의 규칙 조합만으로 독립 방법 기여를 주장하지 않도록 NEXT에 추가한다. |

Exact/normalized title와 public identifier 충돌을 registration dry-run에서 검사했다. [입력·출처](../sources/registry_admissions_2026-11-03.json)의 지정 본문 절 검토를 5개 노트에 반영했으며 FULL_TEXT_CHECKED는 전체 정독이 아니다. Reading status는 신규 NEXT 7편 모두 UNREAD이며 기존 입력을 보존한다. CoRL은 공식 accepted list의 exact title/forum으로 채택을 확인했고 OpenReview의 접근 제약을 우회하지 않았다. RA-L/ICRA는 publisher-deposited Crossref 서지와 저자 source를 함께 확인했다. 공개 code를 실행하거나 conference final text의 동일성을 확인한 것은 아니다.

기존 **pr-1080 Diagnosing Compositional Generalization in Sequential Robot Tasks**는 [CoRL 공식 목록](https://www.corl.org/program/accepted-papers)과 forum `gQFYIM5dJy` 연결을 확인해 arXiv → CoRL로 갱신했다. Stable ID와 사용자 읽기 입력·분석 본문을 보존하면서 해당 폴더만 venue hierarchy에 맞춰 옮기고 참조를 갱신했다. Spotlight는 승격하지 않았다. 과거 11/01 조사 당시의 미확인 기록은 역사로 남겼다.

새 admission 후 [42편 survey 원장](../sources/vla_rl_gap_review_2026-11-03.json)의 현재 연결은 등록 24·미등록 18편이다. 원 S1/R1/R2의 당시 집계는 보존하고 `registry_sync`에 현재 identity를 분리했다. 나머지를 일괄 등록하지 않았으며 workshop/preprint를 main-conference로 올리지 않았다.

## 비실험 절차 조사와 후보 감사

공개 연구 지침에서 문제·선행·기여·비용/기간·중간 점검, 선택적 정독, 조기 글쓰기와 외부 비판, 단순화와 실패 이해를 추렸다. 출처별 의미와 한계는 [갱신 가이드](../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)에 통합했다. 최종 논문 심사 기준을 탐색의 진입 장벽으로 쓰지 않으며, 이 과정이 논문 채택을 보장한다는 주장은 하지 않는다.

[현재 6개 후보별 감사표](../research_topics/README.md#nonexperimental-process-audit)가 단일 비교 본문이다. **모두 내부 문헌·논리·최소 비교 설계를 진행해 대체로 부합한다. 실제 독립 피드백은 모두 미수신이며 GPU 외 미구현/미확보 조건이 있다.** 반복 문서 작성보다 판단을 바꾸는 다음 관측이 필요하다. 연구 효과·신규성·실험 준비를 모두 완료한 것으로 표시하지 않는다.

이번 보완은 각 후보의 첫 구현 점검 산출물과 사람의 작업 시간을 재평가할 지점을 공통 표에 명시한 것이다. 첫 주 점검은 운영 제안이며 완료 기간이나 학습 실행 승인이 아니다. REVISION의 상위 모델이 아직 미동결이라는 낡은 표현을 11/01 계약에 맞춰 **설계 고정 / 구현 미검증**으로 수정했다.

## 정리와 보존

- TODO의 반복 S1/R1/R2/N1·이전 완료 설명을 압축하고 상세 내용은 기존 주제/이력에 연결했다.
- 현재 6개 주제와 기존 5개 상대 평가·기존 정책 준비 3개를 구분했다. 기존 5개 중 REVISION 권고와 현재 새 VLA+RL 작업 VRL을 같은 순위로 혼동하지 않도록 정리했다.
- 현재 snapshot·공식 게재·source 연결을 README/AGENTS/research/synthesis에 동기화했다. 주제별 새 보고서 6개를 만들지 않았다.
- 확인한 `work/scripts/__pycache__/registry_profiles.cpython-312.pyc`, `registry_schema.cpython-312.pyc`만 제거했다. 이번 생성 검증의 bytecode는 저장소 밖 임시 경로를 사용했다.
- 동일 bytes인 두 navigation 작업의 `docker_version.json`은 서로 다른 실행의 provenance여서 보존했다. 불필요한 dependency/install artifact는 새로 만들지 않았다.
- 과거 실험 원시 결과·실행 계약·PDF·기존 사용자 변경과 staged index를 보존한다. 과거 HOLD/NO-GO·재개 gate 변경 없음.

## 검증

- Registry audit: 1,098편·5,490개 노트·368 active/47 history·7개 queue, 오류 0·경고 0.
- 등록 dry-run → apply, tier generator compile/rebuild, priority-only reconcile dry-run → apply, catalog/view 재생성 완료. 마지막 priority dry-run은 추가 변경 없음.
- 기존 active/history의 **408개 paper에 대해 status·evidence·날짜·사용자 분석 11개 필드가 모두 보존**됐다. 신규 NEXT 7개만 UNREAD로 추가됐다.
- 기존 노트는 pr-1080 overview의 게재 metadata 외 본문을 보존했다. pr-1080의 나머지 4개 노트는 이동 전후 bytes가 같다. 5,490개 표준 노트의 C0/C1 제어문자 잔여는 0이다.
- `git diff --check`, staged diff 검사와 신규 파일 whitespace/JSON 검사를 수행했다. 기존 staged index는 동일하며 commit/push하지 않았다.
- 기계 검증·보존 결과와 조사 출처: [maintenance record](../sources/registry_maintenance_2026-11-03.json). 실험·native 성능·외부 피드백 검증을 뜻하지 않는다.
