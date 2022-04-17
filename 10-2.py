## tkinter모듈과 ttk 모듈을 삽입
from tkinter import*
from tkinter import ttk
## 2018038025 정하용
## 루트 윈도우 생성 및 타이틀명 ttk
window = Tk()
window.title("ttk")

## 베이스 탭 생성
baseTab = ttk.Notebook(window)
## 베이스 탭에 들어갈 각각의 프레임을 생성 후 텍스트명은 강아지와 고양이로 설정
ttkDog = ttk.Frame(baseTab)
baseTab.add(ttkDog,text='강아지')
ttkCat = ttk.Frame(baseTab)
baseTab.add(ttkCat,text='고양이')

## 베이스탭 윈도우에 삽입
baseTab.pack(expand=1, fill="both")

## 베이스 탭에 맞는 이미지와 레이블을 준비
Dogphoto = PhotoImage(file= "dog3.gif")
## 레이블에 이미지 삽입
Doglabel = Label(ttkDog, image= Dogphoto)
## 레이블 윈도우에 삽입
Doglabel.pack()

Catphoto = PhotoImage(file= "cat7.gif")
Catlabel = Label(ttkCat, image= Catphoto)
## 레이블 윈도우에 삽입
Catlabel.pack()

window.mainloop()

