import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("ex01-20230613/fig/3.png")
    k_img = pg.transform.flip(kk_img,True,False)
    kh_img = pg.transform.rotozoom(k_img, 10, 1.0)
    kl_img = []
    kl_img.append(k_img)  
    kl_img.append(kh_img)
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x,0])
        screen.blit(bg_img2, [1600-x,0])
        screen.blit(bg_img,[3200-x,0])
        screen.blit(kl_img[tmr//100%2],[300,200])
        pg.display.update()
        tmr += 1  
        x += 1
        clock.tick(100)
        if x > 1599:
            x = 0

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()