# 필수과제 개발 및 실행 증빙

## 1. 개발 환경 확인

다음 명령어로 Python과 Git 개발 환경을 확인했다.

```powershell
py --version
git --version
git config --global user.name
git config --global user.email
git config --global init.defaultBranch
```

확인 결과:

- Python 3.10 이상 설치 확인
- Git 설치 및 버전 확인
- Git 사용자 이름과 이메일 설정 확인
- 기본 브랜치 main 설정 확인
- VS Code Python 확장 설치 확인

관련 이미지:

- `prompt-manager_과제제출증빙/52_개발환경_Python_Git설정.png`
- `prompt-manager_과제제출증빙/53_VSCode_Python확장_설치확인.png`

## 2. 공개 저장소 Clone 실습

GitHub의 공개 샘플 저장소를 clone하고 폴더 구조와 로그를 확인했다.

```powershell
git clone https://github.com/octocat/Hello-World.git clone-practice
cd clone-practice
dir
git remote -v
git log --oneline -5
```

확인 결과:

- 공개 저장소가 clone-practice 폴더로 복제됨
- README 등 폴더 구조 확인
- 원격 저장소 주소 확인
- 공개 저장소 커밋 로그 확인

관련 이미지:

- `prompt-manager_과제제출증빙/35_공개저장소_Clone및로그확인.png`

## 3. 프로그램 실행 확인

실행 명령어:

```powershell
py prompt_manager.py
```

확인한 기능:

1. 프롬프트 추가
2. 전체 목록 보기
3. 카테고리별 조회
4. 제목·내용 키워드 검색
5. 프롬프트 상세 보기
6. 즐겨찾기 추가 및 해제
7. 즐겨찾기 목록
8. 빈 입력값 처리
9. 잘못된 번호 처리
10. 0 입력 시 프로그램 종료
11. 재실행 시 기본 프롬프트 3개로 초기화

관련 이미지:

- `prompt-manager_과제제출증빙/37_최종프로그램_메뉴화면.png`
- `prompt-manager_과제제출증빙/38_최종테스트_프롬프트추가.png`
- `prompt-manager_과제제출증빙/39_최종테스트_전체목록.png`
- `prompt-manager_과제제출증빙/40_최종테스트_카테고리조회.png`
- `prompt-manager_과제제출증빙/41_최종테스트_키워드검색.png`
- `prompt-manager_과제제출증빙/42_최종테스트_상세보기.png`
- `prompt-manager_과제제출증빙/43_최종테스트_즐겨찾기추가.png`
- `prompt-manager_과제제출증빙/44_최종테스트_즐겨찾기목록.png`
- `prompt-manager_과제제출증빙/45_최종테스트_잘못된입력.png`
- `prompt-manager_과제제출증빙/46_최종테스트_프로그램종료.png`
- `prompt-manager_과제제출증빙/47_프로그램재실행_기본3개초기화.png`

## 4. 기능 단위 커밋

하나의 기능을 완성할 때마다 별도 커밋을 생성했다.

주요 커밋:

- 프로젝트 기본 구조 생성
- 기본 프롬프트 데이터 3개 등록
- 메인 메뉴와 프로그램 종료 기능 구현
- 프롬프트 추가와 입력값 검증 기능 구현
- 프롬프트 전체 목록 보기 기능 구현
- 카테고리별 프롬프트 조회 기능 구현
- 제목과 내용 키워드 검색 기능 구현
- 프롬프트 상세 보기와 번호 검증 기능 구현
- 즐겨찾기 추가와 해제 기능 구현
- 즐겨찾기 목록 조회 기능 구현
- README 프로그램 설명과 실행 방법 완성

## 5. 브랜치 생성과 병합

`feature/prompt-list` 브랜치에서 전체 목록 기능을 개발한 후 main 브랜치에 병합했다.

사용한 주요 명령어:

```powershell
git checkout -b feature/prompt-list
git add prompt_manager.py
git commit -m "프롬프트 전체 목록 보기 기능 구현"
git checkout main
git merge --no-ff feature/prompt-list
git push origin main
```

검증 명령어:

```powershell
git log --oneline --graph --decorate --all
```

관련 이미지:

- `prompt-manager_과제제출증빙/19_브랜치생성_커밋_병합그래프.png`
- `prompt-manager_과제제출증빙/51_git_log_oneline_graph_최종.png`
- `prompt-manager_과제제출증빙/56_GitHub_브랜치목록.png`

## 6. 병합 충돌 해결

로컬과 GitHub에 서로 다른 README가 있어 pull 과정에서 충돌이 발생했다.

해결 순서:

1. `git status`로 충돌 파일 확인
2. VS Code에서 양쪽 README 내용 확인
3. 필요한 내용을 모두 유지하고 충돌 표시 제거
4. `git add README.md`
5. 병합 커밋 생성
6. `git log --oneline --graph`로 검증
7. `git push origin main`

관련 이미지:

- `prompt-manager_과제제출증빙/09_Push거절_GitHub변경사항확인.png`
- `prompt-manager_과제제출증빙/11_README충돌해결_병합완료.png`

## 7. 데이터 유지 범위

프롬프트는 Python 리스트와 딕셔너리에 저장된다. 프로그램을 한 번 실행하는 동안에는 추가한 프롬프트와 즐겨찾기 변경 상태가 유지된다.

사용자가 0을 선택하여 프로그램을 종료하면 실행 중 추가한 데이터가 초기화된다. 재실행하면 코드에 등록된 기본 프롬프트 3개로 시작한다. 이는 필수과제의 종료 시 초기화 조건에 맞춘 동작이다.