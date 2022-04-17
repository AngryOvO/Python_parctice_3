## 모듈 삽입
from tkinter import*
from tkinter.colorchooser import*
from tkinter.simpledialog import*
## 2018038025 정하용
## Function ##
def mouseClick(event): ## 마우스 클릭을 입력받아 클릭을 했을때의 좌표를 변수에 저장
    global x1, x2, y1, y2
    x1 = event.x
    y1 = event.y

def mouseDrop(event) : ## 마우스를 드롭하는 순간을 입력받아 그때의 좌표를 변수에 저장
    global x1, x2, y1, y2, penwidth, pencolor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1,y1,x2,y2,width = penwidth, fill = pencolor) ## 변수에 저장된 두 좌표를 바탕으로 선을 그음

def getColor(): ## 선의 색깔을 정하는 함수
    global  pencolor
    color = askcolor()
    pencolor = color[1]

def getwidth(): ## 선의 굵기를 정하는 함수
    global penwidth
    penwidth = askinteger("선 두께", "선 두께(1~10)를 입력하세요", minvalue = 1, maxvalue = 10)

## Variable ##
window = None
canvas = None
x1,x2,y1,y2 = None,None,None,None
pencolor = 'black' ## 시작 색상 검정색으로 설정
penwidth = 5 ## 시작 굵기 5로 설정

## MAIN ##

window = Tk() ## 루트 윈도우 Tk 생성
window.title("그림판 비슷한 프로그램") ## 타이틀명 설정
canvas = Canvas(window, height=300, width= 300) ## 캔버스 선언 및 크기설정
canvas.bind("<Button-1>",mouseClick)
canvas.bind("<ButtonRelease-1>",mouseDrop)
canvas.pack() ## 캔버스 루트 윈도우에 삽입

mainMenu = Menu(window) ## 부모 메뉴 생성
window.config(menu= mainMenu) ## 부모 메뉴
fileMenu = Menu(mainMenu) ## 자식 메뉴 생성
mainMenu.add_cascade(label = "설정", menu = fileMenu) ## 메인 메뉴의 이름설정하고 자식 메뉴 삽입
fileMenu.add_command(label = "선 색상 선택", command= getColor) ## 자식 메뉴의 이름 설정 후 클릭 시 함수 실행
fileMenu.add_separator()
fileMenu.add_command(label= "선 두께 설정", command= getwidth) ## 자식 메뉴의 이름 설정 후 클릭시 함수 실행

window.mainloop()