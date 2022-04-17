#확대 축소 가능한 이미지
from tkinter import *
from tkinter.filedialog import *
#2018038025 정하용
def func_open() :
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() : #프로그램 종료
    window.quit()
    window.destroy()

def func_zoom(event) : #이미지 확대 함수
    photo = PhotoImage(file = filename)
    photo = photo.zoom(3, 3)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_subsample(event) : #이미지 축소
    photo = PhotoImage(file = filename)
    photo = photo.subsample(3, 3)
    pLabel.configure(image = photo)
    pLabel.image = photo

window = Tk() ## 루트 윈도우 생성
window.geometry("500x500")
window.title("확대 축소 가능") ## 타이틀명 설정

## 이미지 변수 생성 및 레이블에 삽입
photo = PhotoImage(file= "cat9.gif")
pLabel = Label(window, image = photo)
#방향키 위, 아래 사용 시 확대 축소
window.bind("<Down>", func_subsample)
window.bind("<Up>", func_zoom)

pLabel.pack(expand=1, anchor = CENTER)
#파일 메뉴 부분
mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()