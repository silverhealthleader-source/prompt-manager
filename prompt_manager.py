# 나만의 프롬프트 관리 프로그램

prompts = [
    {
        "title": "사회복지기관 생성형 AI 교육자료 작성",
        "content": (
            "당신은 생성형 AI 전문 강사입니다. "
            "사회복지기관 종사자가 쉽게 이해할 수 있도록 "
            "생성형 AI 업무 활용 교육자료를 작성해주세요. "
            "어려운 용어는 쉬운 말로 설명하고 실제 업무 사례를 포함해주세요."
        ),
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "따뜻한 수채화 동화 삽화 생성",
        "content": (
            "따뜻한 파스텔 색상의 수채화 동화 삽화를 만들어주세요. "
            "부드러운 자연광, 색연필 질감, 수채화 종이 질감을 표현하고 "
            "인물의 표정은 친근하고 따뜻하게 구성해주세요."
        ),
        "category": "이미지 생성",
        "favorite": True
    },
    {
        "title": "교육 문의 자동회신 작성",
        "content": (
            "당신은 교육기관의 친절한 담당자입니다. "
            "교육 신청자의 이름, 신청 과정, 교육 일정을 반영하여 "
            "접수 완료 안내 이메일을 정중하고 이해하기 쉽게 작성해주세요."
        ),
        "category": "자동화",
        "favorite": False
    }
]

CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]

def input_required(message):
    """빈칸이 아닌 값이 입력될 때까지 반복합니다."""
    while True:
        value = input(message).strip()

        if value:
            return value

        print("입력값을 비워둘 수 없습니다. 다시 입력해주세요.")


def select_category():
    """카테고리를 목록에서 선택하거나 직접 입력받습니다."""
    print("\n카테고리 선택:")

    for number, category in enumerate(CATEGORIES, start=1):
        print(f"{number}) {category}")

    print("7) 직접 입력")

    while True:
        choice = input("선택: ").strip()

        if choice in ["1", "2", "3", "4", "5", "6"]:
            return CATEGORIES[int(choice) - 1]

        if choice == "7":
            return input_required("새 카테고리 이름: ")

        print("1부터 7까지의 번호를 입력해주세요.")

def add_prompt():
    """새로운 프롬프트를 prompts 리스트에 추가합니다."""
    print("\n=== 프롬프트 추가 ===")

    title = input_required("제목: ")
    content = input_required("내용: ")
    category = select_category()

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print(f"\n'{title}' 프롬프트가 추가되었습니다!")
    print(f"현재 총 {len(prompts)}개의 프롬프트가 있습니다.")

def manage_favorite():
    """선택한 프롬프트의 즐겨찾기를 추가하거나 해제합니다."""
    print("\n=== 즐겨찾기 관리 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    prompt_number = input("즐겨찾기를 변경할 프롬프트 번호: ").strip()

    if not prompt_number.isdigit():
        print("번호는 숫자로 입력해주세요.")
        return

    index = int(prompt_number) - 1

    if index < 0 or index >= len(prompts):
        print(f"1부터 {len(prompts)}까지의 번호를 입력해주세요.")
        return

    selected_prompt = prompts[index]

    selected_prompt["favorite"] = not selected_prompt["favorite"]

    if selected_prompt["favorite"]:
        print(
            f"\n'{selected_prompt['title']}' 프롬프트를 "
            "즐겨찾기에 추가했습니다!"
        )
    else:
        print(
            f"\n'{selected_prompt['title']}' 프롬프트의 "
            "즐겨찾기를 해제했습니다!"
        )

def show_detail():
    """선택한 프롬프트의 전체 정보를 출력합니다."""
    print("\n=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    prompt_number = input("상세히 볼 프롬프트 번호: ").strip()

    if not prompt_number.isdigit():
        print("번호는 숫자로 입력해주세요.")
        return

    index = int(prompt_number) - 1

    if index < 0 or index >= len(prompts):
        print(f"1부터 {len(prompts)}까지의 번호를 입력해주세요.")
        return

    selected_prompt = prompts[index]
    favorite_mark = "⭐" if selected_prompt["favorite"] else "등록 안 됨"

    print("\n────────────────────────────")
    print(f"제목: {selected_prompt['title']}")
    print(f"카테고리: {selected_prompt['category']}")
    print(f"즐겨찾기: {favorite_mark}")
    print("────────────────────────────")
    print("내용:")
    print(selected_prompt["content"])
    print("────────────────────────────")

def search_prompt():
    """제목 또는 내용에 포함된 키워드로 프롬프트를 검색합니다."""
    print("\n=== 프롬프트 검색 ===")

    keyword = input_required("검색어: ")
    keyword_lower = keyword.lower()

    search_results = []

    for prompt in prompts:
        title_lower = prompt["title"].lower()
        content_lower = prompt["content"].lower()

        if keyword_lower in title_lower or keyword_lower in content_lower:
            search_results.append(prompt)

    if not search_results:
        print(f"\n'{keyword}' 검색 결과가 없습니다.")
        return

    print("\n검색 결과:")

    for number, prompt in enumerate(search_results, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f'{number}. [{prompt["category"]}] '
            f'{prompt["title"]}{favorite_mark}'
        )

    print(f"\n{len(search_results)}개의 프롬프트를 찾았습니다.")


def show_by_category():
    """선택한 카테고리의 프롬프트만 출력합니다."""
    print("\n=== 카테고리별 조회 ===")

    selected_category = select_category()

    matched_prompts = []

    for prompt in prompts:
        if prompt["category"] == selected_category:
            matched_prompts.append(prompt)

    if not matched_prompts:
        print(f"\n[{selected_category}] 카테고리에 등록된 프롬프트가 없습니다.")
        return

    print(f"\n[{selected_category}] 카테고리 프롬프트:")

    for number, prompt in enumerate(matched_prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""
        print(f"{number}. {prompt['title']}{favorite_mark}")

    print(f"\n총 {len(matched_prompts)}개의 프롬프트")


def show_list():
    """저장된 모든 프롬프트를 번호와 함께 출력합니다."""
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for number, prompt in enumerate(prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f'{number}. [{prompt["category"]}] '
            f'{prompt["title"]}{favorite_mark}'
        )

    print(f"\n총 {len(prompts)}개의 프롬프트")

def show_menu():
    """프로그램의 메인 메뉴를 화면에 출력합니다."""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

def main():
    """메뉴 선택을 반복하여 처리하는 메인 함수입니다."""
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            manage_favorite()
        elif choice == "0":
            print("프롬프트 관리 프로그램을 종료합니다.")
            break
        elif choice in ["7"]:
            print("해당 기능은 다음 단계에서 구현됩니다.")
        else:
            print("잘못된 번호입니다. 0부터 7까지의 번호를 입력해주세요.")

if __name__ == "__main__":
    main()