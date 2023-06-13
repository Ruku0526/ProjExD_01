import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01-20230613/fig/3.png")
    k_img = pg.transform.flip(kk_img,True,False)
    kh_img = pg.transform.rotozoom(k_img, 10, 1.0)
    kl_img = []
    kl_img.append(k_img)  
    kl_img.append(kh_img)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(kl_img[tmr%2],[300,200])
        pg.display.update()
        tmr += 1  
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()