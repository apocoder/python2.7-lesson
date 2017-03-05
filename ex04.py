# -*- coding: utf-8 -*-
x = "%d cesit insan var" % 10
ikili ='ikili'
olmayan = 'olmayan'

y = "%s olan ve %s" %(ikili,olmayan)

print x
print y

print "Benim bildigim %r" %x

neseli = False
saka_sonucu= "Bu saka okadar komik degil miydi? %r"

print saka_sonucu % neseli

w = "Bu bolum sol taraf"

e = "Bu bolum sag taraf"

print w + e

# %r ile %s arasındaki fark r raw data olarak sonuc verir s ise vermez
