# 나만의 프롬프트 관리 프로그램

Python 기초 문법과 Git·GitHub 버전 관리를 학습하기 위해 제작한 콘솔 기반 프롬프트 관리 프로그램입니다.

터미널에서 메뉴 번호를 입력하여 프롬프트를 추가하고, 목록·카테고리·검색·상세 보기·즐겨찾기 기능을 사용할 수 있습니다.

## 주요 기능

1. 새로운 프롬프트 추가
2. 전체 프롬프트 목록 보기
3. 카테고리별 프롬프트 조회
4. 제목 또는 내용 키워드 검색
5. 프롬프트 상세 내용 보기
6. 즐겨찾기 추가 및 해제
7. 즐겨찾기 목록 보기
8. 잘못된 번호와 빈 입력값 안내
9. 프로그램 종료 후 메뉴 종료

## 기본 프롬프트

프로그램 시작 시 이전 미션에서 활용한 프롬프트 3개가 기본 데이터로 등록됩니다.

- 사회복지기관 생성형 AI 교육자료 작성
- 따뜻한 수채화 동화 삽화 생성
- 교육 문의 자동회신 작성

각 프롬프트는 다음 정보를 포함합니다.

- 제목
- 내용
- 카테고리
- 즐겨찾기 여부

## 프롬프트 카테고리

기본 카테고리는 다음과 같습니다.

- 텍스트 생성
- 이미지 생성
- 영상 생성
- 페르소나
- 자동화
- 기타

프롬프트를 추가할 때 새로운 카테고리를 직접 입력할 수도 있습니다.

## 개발 환경

- Python 3.10 이상
- Visual Studio Code
- Git
- GitHub
- 외부 라이브러리 사용 없음

## 실행 방법

### 1. 저장소 내려받기

```bash
git clone https://github.com/silverhealthleader-source/prompt-manager.git
```

### 2. 프로젝트 폴더로 이동

```bash
cd prompt-manager
```

### 3. 프로그램 실행

Windows 환경:

```bash
py prompt_manager.py
```

또는:

```bash
python prompt_manager.py
```

## 메뉴 구성

```text
=== 나만의 프롬프트 관리 ===
1. 프롬프트 추가
2. 프롬프트 목록
3. 카테고리별 조회
4. 프롬프트 검색
5. 프롬프트 상세 보기
6. 즐겨찾기 관리
7. 즐겨찾기 목록
0. 종료
```

## 데이터 저장 방식

프롬프트 데이터는 Python의 리스트와 딕셔너리를 사용하여 관리합니다.

프로그램 실행 중에 추가한 프롬프트와 변경한 즐겨찾기 상태는 유지됩니다. 프로그램을 종료하면 실행 중 추가한 데이터는 초기화되고 기본 프롬프트 3개로 돌아갑니다.

## 코드 구조

기능별로 함수를 분리하여 작성했습니다.

- `input_required()` : 빈 입력값 방지
- `select_category()` : 카테고리 선택
- `add_prompt()` : 프롬프트 추가
- `show_list()` : 전체 목록 출력
- `show_by_category()` : 카테고리별 조회
- `search_prompt()` : 키워드 검색
- `show_detail()` : 상세 보기
- `manage_favorite()` : 즐겨찾기 추가·해제
- `show_favorites()` : 즐겨찾기 목록
- `show_menu()` : 메인 메뉴 출력
- `main()` : 프로그램 실행과 메뉴 선택 처리

## Git·GitHub 학습 내용

이 프로젝트에서는 다음 Git 명령어를 실습했습니다.

- `git init`
- `git add`
- `git commit`
- `git push`
- `git pull`
- `git checkout`
- `git clone`
- `git merge`

`feature/prompt-list` 브랜치에서 프롬프트 목록 기능을 개발하고, 기능 완성 후 `main` 브랜치에 병합했습니다.

## 저장소 주소

https://github.com/silverhealthleader-source/prompt-manager