# Registry 최신화·누락 선행 등록·중복 내용 정리

- Work ID: **REG-R14** / 2026-11-12 KST
- 범위: 전체 로컬 registry의 identity·노트·분류·링크·생성 문서 정합성, 최근 VLA 공백 조사에 인용했으나 등록하지 않았던 8편의 외부 출처 재확인. **전체 1,179편의 게재 상태·본문을 인터넷으로 전수 재검토한 것은 아니다.**
- [등록 입력](../sources/registry_admissions_2026-11-12.json) · [정리·보존·검증 원장](../sources/registry_maintenance_2026-11-12.json) · [직전 유지보수](./REGISTRY_MAINTENANCE_2026-11-09.md) · [현재 TODO](../../TODO.md)

## 추가한 논문

| 논문·registry ID | 확인한 상태 | 분류·등록 이유 |
|---|---|---|
| [RL’s Razor, pr-1172](../../2026/ICLR/2026_ICLR_RL-s-Razor-Why-Online-Reinforcement-Learning-Forgets-Less/01_overview.md) | [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/618c95f4557c15b253fb0e6f548ea0c0-Abstract-Conference.html) | NEXT · RL/SFT의 기존 능력 보존과 정책 KL을 비교하는 직접 선행 |
| [DeLock, pr-1173](../../2026/arXiv/2026_arXiv_Breaking-Lock-In-Preserving-Steerability-under-Low-Data-VL/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2604.23121) | NEXT · 저데이터 VLA 후학습의 지시별 행동 보존과 직접 충돌 |
| [TEMPO, pr-1174](../../2026/arXiv/2026_arXiv_TEMPO-Semantic-Action-Decoupled-RL-Post-Training-for-Visio/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2608.07314) | NEXT · 의미와 동작을 구분하는 VLA RL 후학습 기준선 |
| [When Vision Overrides Language, pr-1175](../../2026/arXiv/2026_arXiv_When-Vision-Overrides-Language-Evaluating-and-Mitigating-C/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2602.17659) | NEXT · 관측과 지시의 반사실적 평가·paired task source |
| [CAT, pr-1176](../../2026/ECCV/2026_ECCV_Trajectory-Level-Continuous-Action-Representation-for-Robo/01_overview.md) | [ECCV 2026](https://link.springer.com/chapter/10.1007/978-3-032-37369-4_24) | NEXT · 연속 궤적 표현과 제어 간격 질문의 직접 선행 |
| [Same Path, Less Time, pr-1177](../../2026/arXiv/2026_arXiv_Same-Path-Less-Time-Training-Free-Fast-Execution-of-Vision/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2611.01390) | REFERENCE · 학습 없는 실행 시간 조정이라는 단순 대안 |
| [ActMem-VLA, pr-1178](../../2026/arXiv/2026_arXiv_ActMem-VLA-Action-History-Memory-with-Dual-Expert-Denoisin/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2609.37307) | REFERENCE · 행동 이력 기억과 실제 행동 결과 기억을 구분하는 비교 대상 |
| [Is Your Robot’s Memory Just a Clock?, pr-1179](../../2026/arXiv/2026_arXiv_Is-Your-Robot-s-Memory-Just-a-Clock-Temporal-Shortcuts-in/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2611.14488) | NEXT · 기억의 시간 shortcut과 null-event 대조를 요구하는 직접 선행 |

신규 8편에 각각 **5개 표준 노트**, source/provenance·추가 이유·반증 가능한 질문을 작성했다. **NEXT6·REFERENCE2**, 노트 근거는 **ABSTRACT_CHECKED**, 신규 집중 읽기 6건은 **UNREAD**다. 이전 LANGRET-N1/N2의 지정 본문·source 대조는 기존 원장에서 유지하며, 그 이력을 새 초록 노트나 사용자 정독 상태로 확대하지 않았다.

## 출처와 판단 경계

- RL’s Razor의 공식 최종 제목은 *Why Online Reinforcement Learning Forgets Less*다. 저자 페이지의 *On-Policy* 표기는 같은 arXiv identity의 alias로 두었다. CAT은 Springer의 ECCV chapter·DOI로 확인했다. 이 2편만 이번 등록에서 공식 conference 게재로 분류했다.
- When Vision Overrides Language의 최신 v3·저자 페이지는 CoRL 2026 Spotlight를 표기하지만, 이번 확인에서 공식 proceedings/forum 근거를 확보하지 못했다. 따라서 arXiv를 유지한다. 나머지 5편도 확인한 preprint 상태로 등록했다.
- TEMPO의 논문 내 anonymous project URL은 식별했으나 이번 접근으로 페이지 내용을 확인하지 못했다. 작동하는 구현을 확보한 것으로 표시하지 않는다. 동일 약어의 *Learning Temporal Context for Dynamic Robot Manipulation*과는 다른 연구다.
- DeLock의 code는 Coming Soon으로 **not released**, 식별하지 못한 code는 **not identified**로 구별했다. VLA-CF·Memory Clock 공개 repository는 연결했지만 코드 존재가 재현 성공을 뜻하지 않는다.
- 전체 제목 정규화·공개 식별자 검사에서 기존 논문과 충돌은 없었다. 최근 조사 원장의 8개 registry ID를 실제 등록에 연결하고, 원래의 “당시 등록 없음” 상태는 `registry_action_at_scout`로 보존했다.

## 병합·정리와 보존

- TODO·root/research/work README·주제 index·synthesis 안내의 반복 인계는 **현재 행동 → 주제별 내용/재현 방법 → 당시 update 기록**으로 정리했다. LANGRET을 현재 행동으로 연결하고, U1의 11/07 투자 판단과 CONTACT의 11/09 선택은 과거 이력으로 구별했다. 기존 후보의 판단·실행 상한은 유지했다.
- 지시별 행동 보존·제어 간격·기억 관련 synthesis에서 새 paper folder로 연결했다. RL’s Razor의 결론과 연구자 가설을 분리해 RL 트랙의 Open Question을 보완했다. 자동 reading queue와 수동 연구 판단을 구별한다.
- 전체 파일 hash에서 동일 내용은 2쌍이다. 서로 다른 Docker build context의 `.dockerignore` 2개와 두 과거 navigation 실행의 `docker_version.json` 2개는 각각 필요한 자료이므로 보존했다. 제목 유사도 보조 검색도 병합할 논문 후보를 찾지 못했다. 이 검색은 의미상 중복의 완전한 부재를 증명하지 않는다.
- 삭제할 임시 로그·캐시·불필요한 패키지는 발견하지 못해 **기존 파일 삭제는 0개**다. 중복 문장을 줄였으며 논문 노트·과거 결과·source·재개 코드를 제거하지 않았다. 오래됐다는 이유만으로 종료 후보나 실행 증거를 삭제하지 않았다.
- 이번 작업에서 실험·Docker 실행·host dependency 변경·PDF/weights 다운로드·git commit/push는 수행하지 않았다. 사용자 dirty/staged 작업을 보존한다.

## 현행 규모와 검증

전체 **1,179편·표준 노트 5,895개**, **CORE47 / NEXT386 / REFERENCE504 / ARCHIVE242**, active433 / history47이다. Source evidence는 FULL_TEXT_CHECKED967 / ABSTRACT_CHECKED212다. 기존 읽기 완료 5편의 상태는 유지한다.

등록 dry-run/apply, tier 생성기 compile/rebuild, priority-only reconcile, catalog/resource/index/stats 재생성을 완료했다. 최종 reconcile dry-run의 추가 변경은 0건이다. 읽기 이력 검사 **6개 통과**, working/staged `git diff --check` 통과, 전체 audit는 **오류0 / 경고0**이다. Markdown **6,120개·내부 링크 13,116개**, 전체 registry row와 표준 노트·queue를 확인했다.

작업 시작 시점과 비교해 기존 paper metadata **1,171편**, 표준 노트 **5,855개**, tier assignment **1,171건**, 사용자 읽기 입력 **474건**을 보존했다. 신규 집중 읽기 **6건**만 UNREAD로 추가했다. 주제별 재현 자료·과거 실험 파일 **236개**, 기존 staged patch가 byte-identical이며 LANGRET-N1/N2/P0 원장의 연구 증거도 그대로다. 기존 파일 삭제는 없다.

다음 연구 행동은 [LANGRET-P0](../../TODO.md)의 호환 local NVIDIA 최소 실행 검증이다. 이번 registry 갱신은 연구 효과·독립 방법 기여·출판 가능성의 실증을 추가하지 않았다.
