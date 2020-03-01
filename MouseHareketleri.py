import pygame,sys#Pygame kütüphanesini çağırıyoruz

pygame.init()#Pygame fonksiyonlarını hazırlar
top=pygame.image.load("top.jpg")

boyut=(800,600)#800 PIXEL yüksekliğinde 600 PIXEL genişliğinde



topunboyutu=top.get_size()
print(topunboyutu)#TOPUN BOYUTUNU ALIRIZ
topunboyutuX=top.get_size()[0]
topunboyutuY=top.get_size()[1]


pencere=pygame.display.set_mode(boyut)

x=0
y=0
clock=pygame.time.Clock()
xYon=1#SOL SAĞ
yYon=1#aşağı yukarı
while True:#EKRAN SÜREKLİ KALSIN DİYE SONSUZ DÖNGÜYE ALIYORUZ
    clock.tick(100)#fps değerini belirliyoruz.
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()
    pencere.fill((255,255,255 ))#ARKA PLAN RENGİ BELİRLEME
    #print(pygame.mouse.get_pos())#Mouse fonksiyonlarını çağırır
    pygame.mouse.set_visible(False)#MOUSE İMLECİNİ GÖRMEK İSTEMEZSEK
    mouseX,mouseY=pygame.mouse.get_pos()
    if mouseX+topunboyutuX>800:
        mouseX=mouseX-topunboyutuX
    if mouseY+topunboyutuY>600:
        mouseY=mouseY-topunboyutuY
    


    pencere.blit(top,(mouseX,mouseY))
    pygame.display.update()









