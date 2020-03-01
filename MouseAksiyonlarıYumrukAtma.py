import pygame,sys#Pygame kütüphanesini çağırıyoruz

pygame.init()#Pygame fonksiyonlarını hazırlar
foto=pygame.image.load("dark.jpg")

boyut=(800,600)#800 PIXEL yüksekliğinde 600 PIXEL genişliğinde

pygame.mixer.music.load("starwars.mp3")#Hangi müziği seçeceğimizi belirleriz
pygame.mixer.music.load("yumruksesi.mp3")
pygame.mixer.music.play()#Oyun başladığında direkt müzik başlar
#pygame.mixer.music.set_volume()#Ondalıklı değer alır


fotonunboyutu=foto.get_size()
print(fotonunboyutu)#TOPUN BOYUTUNU ALIRIZ
fotonunboyutuX=foto.get_size()[0]
fotonunboyutuY=foto.get_size()[1]


pencere=pygame.display.set_mode(boyut)

x=0
y=0

clock=pygame.time.Clock()
pygame.mouse.get_rel()#Mouse hızını gösterir ve belirler


xYon=1#SOL SAĞ
yYon=1#aşağı yukarı
while True:#EKRAN SÜREKLİ KALSIN DİYE SONSUZ DÖNGÜYE ALIYORUZ
    clock.tick(100)#fps değerini belirliyoruz.
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()
    pencere.fill((255,255,255 ))#ARKA PLAN RENGİ BELİRLEME
    #(pygame.mouse.get_pos())#Mouse fonksiyonlarını çağırır
    
    sol,orta,sag=pygame.mouse.get_pressed()#SOL ORTA SAĞ MOUSE
    mousex,mousey=pygame.mouse.get_pos()

    Xhareket,Yhareket=pygame.mouse.get_rel()#MOUSE HIZINI GÖSTERİR EKRANDA
    if Xhareket>50 or Yhareket>50 or Xhareket<-100 or Yhareket<-100:
        pygame.mixer.music.play()

        
    

    if mousex+fotonunboyutuX>800:
        mousex=mousex-fotonunboyutuX
    if mousey+fotonunboyutuY>600:
        mousey=mousey-fotonunboyutuY   


    




    if sol==1:
        pygame.mixer.music.set_volume(0.0)#pygame.mixer.music.pause
    if sag==1:
        pygame.mixer.music.set_volume(1.0)#pygame.mixer.music.unpause

    

    
    pygame.display.update()









