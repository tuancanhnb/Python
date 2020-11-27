# tạo thư viện pygame
import pygame

# init - khởi tạo 
pygame.init()

# tạo màn hình hiển thị ra với kích thước
screen = pygame.display.set_mode((500,600))

# khai báo màu
GREY = (150,150,150)

# khai báo biến
running = True

# vòng lặp game (giúp hiển thị trên màn hình ko bị tắt)
while running:

    # thay đổi màu nền của chương trình
    screen.fill(GREY)

    # sét các sự kiện như phím tắt, click chuột,...
    for event in pygame.event.get():

        # phát hiện khi ấn nút Quit thì chạy lệnh trong if
        if event.type == pygame.QUIT:
            running = False
        # nếu bấm chuột thì chạy lệnh trong if
        if event.type == pygame.MOUSEBUTTONDOWN:
            # click chuột trái(= 1) thì chạy lệnh trong if
            if event.button == 1:

                print("HiHi")

    # flip dùng để thay đổi màu hiển thị ra màn hình khi thay đổi code
    pygame.display.flip()

# khi chạy xong rồi xóa toàn bộ dữ liệu đã chạy làm giảm bộ nhớ đi
pygame.quit()