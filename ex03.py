# -*- coding: utf-8 -*-
arabalar = 200
araba_yolcu_kapasitesi = 4.0
suruculer = 30
yolcular = 150

surucusuz_arabalar = arabalar - suruculer
surulebilen_arabalar = suruculer
toplam_yolcu_kapasitesi = surulebilen_arabalar * araba_yolcu_kapasitesi
araba_basina_dusen_ortalama_yolcu = yolcular / surulebilen_arabalar

print "Toplam ",arabalar," araba uygun."
print "Toplam ",suruculer," sürücü uygun."
print "Toplam sürülemeyen arabalar ",surucusuz_arabalar
print "Toplam yolcu kapasitesi ", toplam_yolcu_kapasitesi
print "Şuanda toplam ",yolcular," yolcumuz var."
print "Bizim her arabaya ortalama ",araba_basina_dusen_ortalama_yolcu ," yolcu yerleştirmemiz gerekiyor"
print "----------------------------------------------------------------"
#print içersinde "format string" kullanmak
ismim = 'python'
yasim = 46
agirligim = 74 #kg
boyum = 180 #cm
goz_rengim = 'Siyah'
saclarim = 'Kahverengi'

print "Merhaba benim adım %s." % ismim
print "Ağırlığım %d" % agirligim
print "Boyum %d" % boyum
print "Saçlarım %s , gözlerim %s" % (goz_rengim,saclarim)

print "Ağırlığımı %d , Boyumu %d , Yaşımı %d toplarsak,%d elde ederiz" % (
    agirligim,boyum,yasim,agirligim+boyum+yasim)
