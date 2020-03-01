import pygame,sys#Pygame kütüphanesini çağırıyoruz

pygame.init()#Pygame fonksiyonlarını hazırlar
top=pygame.image.load("top.jpg")

boyut=(800,600)#800 PIXEL yüksekliğinde 600 PIXEL genişliğinde



topunboyutu=top.get_size()
print(topunboyutu)
topunboyutuX=top.get_size()[0]


pencere=pygame.display.set_mode(boyut)

x=0
y=0
clock=pygame.time.Clock()
xYon=1
while True:#EKRAN SÜREKLİ KALSIN DİYE SONSUZ DÖNGÜYE ALIYORUZ
    clock.tick(400)#fps değerini belirliyoruz.
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()
    pencere.fill((255,255,255))
    pencere.blit(top,(x,y))#Yazımızı ekrana bastırma. 1.parametre değişkenimiz. 2. parametremiz x-y koordinatı
    
    if x>800-topunboyutuX or x<0:
        xYon*=-1
    x+=1*xYon 
    pygame.display.update()









