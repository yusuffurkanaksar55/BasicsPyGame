import pygame,sys#Pygame kütüphanesini çağırıyoruz

pygame.init()#Pygame fonksiyonlarını hazırlar

boyut=(800,600)#800 PIXEL yüksekliğinde 600 PIXEL genişliğinde
font=pygame.font.SysFont("Helvecita",45)#YAZIMIZINI FONTUNU BELİRLİYORUZ
yazı=font.render("Merhaba Dünya",1,(0,255,0),(255,255,255))#("Yazımız",1,Yazının Rengi->BGR,arka plan rengi->BGR)

pencere=pygame.display.set_mode(boyut)
x=0
y=0
clock=pygame.time.Clock()
while True:#EKRAN SÜREKLİ KALSIN DİYE SONSUZ DÖNGÜYE ALIYORUZ
    clock.tick(60)#fps değerini belirliyoruz.
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()
    pencere.blit(yazı,(x,y))#Yazımızı ekrana bastırma. 1.parametre değişkenimiz. 2. parametremiz x-y koordinatı
    pencere.fill((255,255,255))#Hızlı bilgisayarlarda yazı gözükmez.Bunu çözmek için sabit fps belirleyeceğiz.

    x+=1
    pygame.display.update()









