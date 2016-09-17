# -*- coding: utf-8 -*-
arabalar = 200
type(arabalar) #type değimi değişkenin ait oldugu tipi verir
araba_yolcu_kapasitesi = 4.0
suruculer = 30
yolcular = 150

surucusuz_arabalar = arabalar - suruculer
surulebilen_arabalar = suruculer
toplam_yolcu_kapasitesi = surulebilen_arabalar * araba_yolcu_kapasitesi
araba_basina_dusen_ortalama_yolcu = yolcular / surulebilen_arabalar

print "Toplam ",arabalar," araba uygun." , type(arabalar)
print "Toplam ",suruculer," sürücü uygun." , type(suruculer)
print "Toplam sürülemeyen arabalar ",surucusuz_arabalar , type(surucusuz_arabalar)
print "Toplam yolcu kapasitesi ", toplam_yolcu_kapasitesi , type(toplam_yolcu_kapasitesi)
print "Şuanda toplam ",yolcular," yolcumuz var." , type(yolcular)
print "Bizim her arabaya ortalama ",araba_basina_dusen_ortalama_yolcu ," yolcu yerleştirmemiz gerekiyor"
print "----------------------------------------------------------------"
#print içersinde "format string" kullanmak
ismim = 'python'
yasim = 46
agirligim = 74 #kg
boyum = 1.80 #m
goz_rengim = 'Siyah'
saclarim = 'Kahverengi'

print "Merhaba benim adım %s." % ismim ,type(ismim)
print "Ağırlığım %d" % agirligim  ,type(agirligim)
print "Boyum %6.2f" % boyum , type(boyum) #string float format
print "Saçlarım %s , gözlerim %s" % (goz_rengim,saclarim)

print "Ağırlığımı %d , Boyumu %d , Yaşımı %d toplarsak,%6.2f elde ederiz" % (
    agirligim,boyum,yasim,agirligim+boyum+yasim)
