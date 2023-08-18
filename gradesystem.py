def loadFile(filename): #파일 불러오기
    data = {}
    try:
        with open(filename, 'r', encoding = 'utf-8') as file:
            lines = file.readlines()
            for line in lines:
                name, subject, score = line.strip().split(':')
                if name not in data:
                    data[name] = {}
                data[name][subject] = float(score)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

    return data
def saveFile(data, filename): #파일 저장하기
    with open(filename, 'w', encoding = 'utf-8') as file:
        for name, subjects in data.items():
            for subject, score in subjects.items():
                file.write(f"{name}:{subject}:{score}\n")

def printScore(data, name): #학생 성적 조회하기
    if name in data:
        avg = []
        print(f"{name}의 성적 정보:")
        for subject, score in data[name].items():
            print(f"{subject}: {score}")
            avg.append(score)
        print(f"평균: {sum(avg)/len(avg)}")
    else:
        print("등록되지 않은 학생입니다.")

def inputScore(data, name, subject, score): #학생 성적 입력받기
    if name not in data:
        data[name] = {}
    data[name][subject] = float(score)
    print("성적이 입력되었습니다.")

def updateScore(data, name, subject, score): #학생 성적 수정하기
    if name in data and subject in data[name]:
        data[name][subject] = float(score)
        print("성적이 수정되었습니다.")
    else:
        print("성적을 수정할 수 없습니다.")

def printMenu(): #메뉴 출력하기
    print("=== 성적 관리 시스템입니다 ===")
    print("1.학생 성적 조회")
    print("2.학생 성적 입력")
    print("3.학생 성적 수정")
    print("4.프로그램 종료")
    print("====수행할 번호를 입력하세요 ===")
    order = int(input())
    return order

if __name__ == "__main__":
    filename = "students.txt"
    data = loadFile(filename)

    while True:
        order = printMenu()
        if order == 1: #학생 성적 조회
            name = input("학생 이름을 입력하세요: ")
            printScore(data, name)
        elif order == 2: #학생 성적 입력
            name = input("학생 이름을 입력하세요: ")
            subject = input("과목을 입력하세요: ")
            score = input("성적을 입력하세요: ")
            inputScore(data, name, subject, score)
            saveFile(data, filename)
        elif order == 3: #학생 성적 수정
            name = input("학생 이름을 입력하세요: ")
            subject = input("과목을 입력하세요: ")
            score = input("수정할 성적을 입력하세요: ")
            updateScore(data, name, subject, score)
            saveFile(data, filename)
        elif order == 4: #프로그램 종료
            print("프로그램을 종료합니다.")
            break
        else:
            print("유효하지 않은 값입니다. 다시 입력해주세요.")
