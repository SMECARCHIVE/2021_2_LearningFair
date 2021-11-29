import time

def ans():
    print("------------------------------------------------------------------------")
    print("1.냉장고")
    print("2.화이트 보드")
    print("3.컴퓨터")
    print("4.특수계산기")
    print("5.백신제조기계")
    
    n=int(input("어디 먼저 조사할까?(1~5까지 선택해주세요.) : "))

    if n==1:
        print("------------------------------------------------------------------------")
        print ("냉장고다. 잠겨져있다. 열기 위해서는 비밀번호가 필요할 것 같다.")

        r=int(input("비밀번호를 입력하시오. : "))
        if r==965:
             print ("냉장고를 열어보니 T-20, CO-BA라고 적힌 두가지 약물들이 들어있다. 아마 백신 재료인듯 하다.")
             print ("재료를 획득했다.")
             time.sleep(2)
             print()
             print("첫 화면으로 돌아갑니다.")
             global o
             o=o+1

        else:
            print ("비밀번호가 맞지 않는 것 같다. 다시 생각해보자.")
            time.sleep(2)
            print()
            print ("첫 화면으로 돌아갑니다.")
                       
    elif n==2:
        print("------------------------------------------------------------------------")
        print("-화이트보드-")
        print("숫자와 공식이 어지럽게 적혀져 있는 화이트보드다.")
        print("동료가 붙여놓은 듯한 메모들이 어지럽게 붙어있다.")
        time.sleep(2)
        print("--------------------------------------------------")
        print("235, 하나의 숫자가 자리까지 맞다.")
        print("246, 하나의 숫자가 맞지만 자리는 맞지 않는다.")
        print("592, 두 개의 숫자가 맞지만, 자리는 맞지 않는다.")
        print("073, 맞는 것이 하나도 없다.")
        time.sleep(2)
        print("--------------------------------------------------")
        print("'뭔가 힌트가 될 것 같은데?'")
        time.sleep(3)
        print()
        print("첫 화면으로 돌아갑니다.")
        
    elif n==3:
        print("------------------------------------------------------------------------")
        print("-컴퓨터-")
        print("어떤 창이 떠 있다.")
        print("이 기호들은 뭘 의미하는 걸까?")
        time.sleep(2)
        print("--------------------------------------------------")
        print("VIVIS 백신 제조법")
        print("T-20 약물을 아래의 용량만큼 넣는다.")
        print("(2□3)△34")
        print("CO-BA 약물을 아래의 용량만큼 넣는다.")
        print("(2□1)☆7")
        time.sleep(2)
        print("--------------------------------------------------")
        print("이 기호들을 어디서 본 것 같은데..?")
        time.sleep(3)
        print()
        print("첫 화면으로 돌아갑니다.")

    elif n==4:
        print("------------------------------------------------------------------------")
        print("-특수계산기-")
        print("일반 계산기와 다르게 사칙연산 기호를 쓰지 않는 것 같다.")

        answer=input("계산기를 사용할까?(y/n) :")

        if answer == "n":
            ans()

        elif answer == "y": 
            A=int(input("첫 번째 숫자를 입력해주세요 : "))
            C=input("부호를 입력해 주세요(□/△/☆) : ")
            B=int(input("두 번째 숫자를 입력해주세요 : "))

            if C=="□":
                result=(A*A-B)
                global square

                square=square+1
    
                if square>3:
                    print("더 이상 작동이 되지 않습니다.")
                    time.sleep(2)
                    print()
                    print("첫 화면으로 돌아갑니다.")
                    ans()

                else:
                    print("답:", result)
                    print("네모 부호의 사용 횟수가 1회 차감되었습니다.")
                    print("현재 남은 사용 가능 횟수 :", 3-square, "번입니다.")
                    time.sleep(2)
                    print()
                    print("첫 화면으로 돌아갑니다.")
                    ans()


            elif C=="△":
                result=((A*B)+B)
                global triangle

                triangle=triangle+1

                if triangle>3:
                    print("더 이상 작동이 되지 않습니다.")
                    ans()

                else:
                    print("답:", result)
                    print("세모 부호의 사용 횟수가 1회 차감되었습니다.")
                    print("현재 남은 사용 가능 횟수 :", 3-triangle, "번입니다.")
                    time.sleep(2)
                    print()
                    print("첫 화면으로 돌아갑니다.")
                    ans()
            

            elif C=="☆":
                result=((A+B)*2)
                global star

                star=star+1

                if star>3:
                    print("더 이상 작동이 되지 않습니다.")
                    ans()

                else:
                    print("답:", result)
                    print("별  부호의 사용 횟수가 1회 차감되었습니다.")
                    print("현재 남은 사용 가능 횟수 :", 3-star, "번입니다.")
                    time.sleep(2)
                    print()
                    print("첫 화면으로 돌아갑니다.")
                    ans()
            

            else:
                print("사용하지 않는 부호입니다.")
                print("첫 화면으로 돌아갑니다.")


        else:
            print("yes 아니면 no로 대답해주세요")
            print("첫 화면으로 돌아갑니다.")


    elif n==5:
        print("------------------------------------------------------------------------")
        print("-백신 제조 기계-")
        print("여기에 적절한 양의 약물을 조합하여 백신을 제조할 수 있다.")
        if o==1:
            print("충분한 재료가 모였다. 이제 계량만 잘 하면 될 것 같다.")

            t=int(input("T-20을 얼마나 넣으시겠습니까? : "))

            co=int(input("CO-BA를 얼마나 넣으시겠습니까? : "))

            print()
            print ("백신제조를 끝냈다. 이제 이걸 동료에게 먹이도록 하자.")
            print ("백신을 먹은 동료는...")
            time.sleep(3)

            if t==68 and co==20:
                print()
                print("<END 1>")
                print("무사히 치료되었다!")
                time.sleep(2)
                print()
                print("----------엔딩 크레딧----------")
                print()
                print("202111103 권하윤")
                time.sleep(1)
                print("202111114 박예진")
                time.sleep(1)
                print("202111124 진효정")
                time.sleep(1)
                print("202111125 최수빈")
                time.sleep(1)
                print("지도교수 권정인 교수님")
                time.sleep(1)
                print("Team. SMEC")
                print("수고하셨습니다!")
                quit()
                
            else:
                print()
                print("<END 2>")
                print("날 물었다.")
                time.sleep(2)
                print()
                re=(input("다시 시작 하시겠습니까?(y/n): "))

                if re=="y":
                    print("처음으로 돌아갑니다.")
                    o=0
                #계산기 값도 초기화

                elif re=="n":
                    print()
                    print("----------엔딩 크레딧----------")
                    print()
                    print("202111103 권하윤")
                    time.sleep(1)
                    print("202111114 박예진")
                    time.sleep(1)
                    print("202111124 진효정")
                    time.sleep(1)
                    print("202111125 최수빈")
                    time.sleep(1)
                    print("지도교수 권정인 교수님")
                    time.sleep(1)
                    print("Team. SMEC")
                    time.sleep(2)
                    print ("수고하셨습니다.")
                    quit()
                else:
                    print("올바른 값을 입력해 주세요.")
                    
        else:
            print("재료를 먼저 찾아야 할 것 같다.")
            print("재료를 찾으러 가보자.")
        
    else:
        print("올바른 수를 입력해 주세요")
        
#게임시작
o=0
square=0
triangle=0
star=0

print("동료가 좀비에게 물렸다.")
print("완전히 감염되기 전에 백신을 제조하여 동료를 구하자!")
time.sleep(2)


while True:ans()

        
