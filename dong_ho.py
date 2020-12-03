# tạo thư viện pygame
import pygame

# init - khởi tạo 
pygame.init()

# tạo màn hình hiển thị ra với kích thước
screen = pygame.display.set_mode((500,600))

# khai báo màu
GREEN = (58, 191, 55)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

# khai báo biến
running = True

# khai báo tạo font chữ và các nút +, -, Start, Reset
font = pygame.font.SysFont('sans', 50)
text_1 = font.render('+', True, RED)
text_2 = font.render('+', True, RED)
text_3 = font.render('Start', True, RED)
text_4 = font.render('-', False, RED)
text_5 = font.render('-', False, RED)
text_6 = font.render('Reset', False, RED)

# vòng lặp game (giúp hiển thị trên màn hình ko bị tắt)
while running:

    # thay đổi màu nền của chương trình
    screen.fill(GREEN)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x)

    # vẽ lên 1 hình chữ
    pygame.draw.rect(screen, WHITE, (100,50,50,50))
    pygame.draw.rect(screen, WHITE, (200,50,50,50))
    pygame.draw.rect(screen, WHITE, (300,50,150,50))
    pygame.draw.rect(screen, WHITE, (100,200,50,50))
    pygame.draw.rect(screen, WHITE, (200,200,50,50))
    pygame.draw.rect(screen, WHITE, (300,150,150,50))

    # vẽ các kí tự vào các ô
    screen.blit(text_1, (113,45))
    screen.blit(text_2, (213,45))
    screen.blit(text_3, (313,45))
    screen.blit(text_4, (117,193))
    screen.blit(text_5, (219,193))
    screen.blit(text_6, (313,145))
    
    # # vẽ phần số chạy
    # text_time = font.render(time, True, BLACK)
    # screen.blit(text_time, (120,120))

    # vẽ hình chữ nhật dài cuối
    pygame.draw.rect(screen, BLACK, (50,520,400,50))
    pygame.draw.rect(screen, WHITE, (60,530,380,30))

    # vẽ hình tròn
    pygame.draw.circle(screen, BLACK, (250,400),100)
    pygame.draw.circle(screen, WHITE, (250,400),95)
    pygame.draw.circle(screen, BLACK, (250,400),5)

    # vẽ đường thẳng ở tâm hình tròn
    pygame.draw.line(screen, BLACK, (250,400),(250,310))


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