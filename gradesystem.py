def loadFile(filename): #학생 성적 파일 불러오기
    with open(filename, 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        data = {}
        subjects = lines[0].strip().split(':')[1:]
        for line in lines[1:]:
            name, *scores = line.strip().split(':')
            data[name] = {subjects[i]: float(score) for i, score in enumerate(scores)}
        return data, subjects

def saveFile(filename, data, subjects): #학생 성적 파일 저장하기
    print(subjects)
    with open(filename, 'w', encoding = 'utf-8') as file:
        file.write(f":{' '.join(subjects)}\n")
        for name, scores in data.items():
            scoreTostr = ':'.join([str(score) for score in scores.values()])
            file.write(f"{name}:{scoreTostr}\n")

def printScore(data, name): #학생 성적 조회하기
    if name not in data:
        print("등록되지 않은 학생입니다.")
        return
    print(f"다음은 {name} 학생 성적 정보입니다.")
    for subject, score in data[name].items():
        print(f"{subject}: {score}")
    scores = data[name].values()
    average = sum(scores) / len(scores)
    print(f"평균 성적: {average:.1f}")

def inputScore(data, name, subject, score): #학생 성적 입력하기
    if name not in data:
        data[name] = {}

    if subject not in data[name]:
        data[name][subject] = float(score)
        print("성적이 입력되었습니다.")
    else:
        print("이미 입력된 성적입니다.")

def updateScore(data, name, subject, score): #학생 성적 수정하기
    if name not in data:
        print("등록되지 않은 학생입니다.")
        return
    if subject in data[name]:
        data[name][subject] = float(score)
        print("성적이 수정되었습니다.")
    else:
        print("성적이 수정되지 않았습니다.")

def printMenu(): #메뉴 출력 기능
    print("=== 성적 관리 시스템입니다 ===")
    print("1.학생 성적 조회")
    print("2.학생 성적 입력")
    print("3.학생 성적 수정")
    print("4.프로그램 종료")
    print("=== 수행할 번호를 입력하세요 ===")
    order = int(input())
    return order

if __name__ == "__main__":
    try:
        data, subjects = loadFile("student.txt")
    except FileNotFoundError:
        print("성적 파일이 존재하지 않습니다.")
        subjects, data = [], {}

    while True:
        order = printMenu()
        if order == 1: #학생 성적 조회
            name = input("조회할 학생 이름을 입력하세요: ")
            printScore(data, name)

        elif order == 2: #학생 성적 입력
            name = input("학생 이름을 입력하세요: ")
            subject = input("과목을 입력하세요: ")
            score = input("성적을 입력하세요: ")
            if subject not in subjects:
                subjects.append(subject)
            inputScore(data, name, subject, score)
            saveFile("student.txt", data, subjects)

        elif order == 3: #학생 성적 수정
            name = input("학생 이름을 입력하세요: ")
            subject = input("과목을 입력하세요: ")
            score = input("수정할 성적을 입력하세요: ")
            updateScore(data, name, subject, score)
            saveFile("student.txt", data, subjects)

        elif order == 4: #프로그램 종료
            print("프로그램을 종료합니다.")
            break

        else:
            print("유효하지 않은 값입니다. 다시 입력해주세요.")