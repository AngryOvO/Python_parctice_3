from tkinter import* ## 표준 윈도 라이브러리
window = Tk() ## 루트 윈도 실행
window.title("애완동물 선택하기") ## 루트 윈도의 타이틀명 설정
## 2018038025 정하용
## function ##
def clickB(): ## 버튼을 클릭했을때 사진을 바꾸는 함수
    if i.get() == 1: ## i의 값이 1일때
        lable2.configure(image=photo1) ## lable2의 내용을 변경 (이미지를 photo1로)
    elif i.get() == 2:
        lable2.configure(image=photo2) ## lable2의 내용을 변경 (이미지를 photo2로)
    else:
        lable2.configure(image=photo3) ## lable2의 내용을 변경 (이미지를 photo3로)

## MAIN ##

i = IntVar() ## 정수형 변수 i 선언
## 이미지 파일을 넣을 변수 생성
photo1 = PhotoImage(file= "dog5.gif")
photo2 = PhotoImage(file = "cat2.gif")
photo3 = PhotoImage(file = "rabbit2.gif")
## 레이블 ##
lable1 = Label(window, text = "좋아하는 동물 투표", font = ("궁서체", 15) , fg = "blue")
lable2 = Label(window, text="") ## 처음엔 빈 레이블 이지만 후에 사진이 들어갈 레이블
## 라디오 버튼 ##
rb1 = Radiobutton(window, text = "강아지", variable= i, value = 1) ## 변수 i의 값을 1로 변경
rb2 = Radiobutton(window, text = "고양이", variable= i, value = 2) ## 변수 i의 값을 2로 변경
rb3 = Radiobutton(window, text = "토끼", variable= i, value = 3) ## 변수 i의 값을 3으로 변경
## 버튼 ##
button1 = Button(window, text = "사진 보기", command = clickB) ## 버튼을 클릭시 clickB함수 실행



## 각 기능 루트 윈도우에 추가 ##
lable1.pack()
rb1.pack()
rb2.pack()
rb3.pack()
button1.pack()
lable2.pack()
window.mainloop()