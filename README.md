# Görüntü İşleme ile Captcha Algılama

Bu kodları oynadığım bir masaüstü oyununda tekrar eden işlemleri otomize etmek için yazdım. Bu eğlence amaçlı projem aynı zamanda oyunun güvenlik sistemi tarafından oluşturulan **CAPTCHA** kodlarını aşabilen bir görüntü işleme projesidir. Projenin ana modülleri aşağıdaki gibi açıklanmıştır.

## toBinary:
Bu fonksiyon, oyun ekranından aldığım captcha görüntülerini ikili formata dönüştürmek için kullanılır. İkili format, görüntüdeki piksellerin siyah veya beyaz olduğu bir formattır. Bu format, captcha görüntülerini tanımak için daha uygun olduğu için kullanılır. Fonksiyon, görüntüyü gri tonlamaya çevirir, ardından belirli bir eşik değerine göre siyah veya beyaz yapar. Ayrıca, görüntüdeki küçük parazitleri temizlemek için bağlı bileşenler analizi yapar.

## OCR:
Bu fonksiyon, ikili formata dönüştürülen captcha görüntülerini okumak için kullanılır. OCR (Optical Character Recognition), optik karakter tanıma anlamına gelir. Fonksiyon, captcha görüntülerini önceden hazırladığım rakam görüntüleriyle karşılaştırır ve en yüksek doğruluk puanına sahip olanları seçer. Böylece, captcha görüntülerindeki rakamları tahmin etmiş olur.

## Balik_Bot:
Bu fonksiyon, oyun ekranında belirli noktalara tıklamak için kullanılır. Fonksiyon, pyautogui modülünü kullanarak fare hareketlerini ve tıklamalarını simüle eder. Fonksiyon, oyun ekranında balık tutma tuşunu, captcha giriş kutusunu ve captcha onay tuşunu bulmak için imagesearch modülünü kullanır. Fonksiyon, captcha görüntülerini almak ve OCR fonksiyonuna göndermek için pyautogui.screenshot fonksiyonunu kullanır.

## attempt:

Bu fonksiyon, balık tutma işlemini tekrarlamak için kullanılır. Fonksiyon, while döngüsünü kullanarak Balik_Bot fonksiyonunu sürekli çağırır. Fonksiyon, oyun ekranında balık tutma durumunu kontrol etmek için win32api modülünü kullanır. Fonksiyon, oyun ekranında belirli bir renk kodu bulunursa balık tutma işlemini durdurur.