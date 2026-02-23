Title: Veri Analisti Yolculuğum Başlıyor
Date: 2026-02-24
Category: Blog
Summary: Jeoloji mühendisliğinden veri analitiğine geçiş sürecimdeki ilk adımlar ve hedeflerim.

"Bir mühendis nasıl düşünür?"

Bu sorunun cevabını, üniversite hayatımın ilk günlerinde öğrendim. Hocamız duvara monte edilmiş basit bir kıyafet askısını göstererek "Ne görüyorsunuz?" diye sormuştu. Ardından söylediği o sözler bugün bile kulağımdadır: "Bir mühendis sadece herkesin gördüğü o askıyı görmez. O metali, o ürünü, o taşı... Baktığı her şeyde, oluşumundan yok oluşuna kadar geçen o devasa süreci görebilmeli. Ancak bu süreci zihninde canlandırabildiğinde gerçekten bir mühendis gibi düşünmüş olursun."

O günden bu yana, dünyayı hep bu mercekten anlamlandırmaya çalıştım. Jeoloji alanında geçen 10 yıllık mühendislik ve 3 yıllık yüksek lisans serüvenimde, doğanın ve süreçlerin aslında devasa bir "veri" yığını olduğunu fark ettim. Eğitim ve saha çalışmalarım boyunca; analitik düşünmenin, doğru soruları sormanın ve var olanı sorgulamanın sonuçları ne kadar dramatik şekilde değiştirebileceğini bizzat yaşayarak öğrendim.

İşte bu keşif, bana kariyerimde yepyeni bir rota çizmem gerektiğini fısıldadı. Süreçleri anlamlandırma tutkum, yolumu doğal olarak veri analitiği ve veri bilimiyle kesiştirdi.

<br/>

![Mühendislik bakış açısını simgeleyen teknik bir çizim]({static}/images/muhendislik-askisi.jpg)


<h2 class="text-2xl font-bold mt-8 mb-4">Veri ile İlk Temas ve Yeni Silahlarım</h2>

Verinin ne olduğunu bir mühendis gibi düşünerek keşfetmek işin sadece başlangıcıydı. Bu verileri bulmak, işlemek ve nihayetinde o verinin hikayesini yazmak gerekiyordu. Tam bu noktada karşıma dört temel aşama çıktı: Veriyi toplamak, depolamak, analiz etmek ve görselleştirmek.

Her bir aşama için en doğru teknolojiyi seçmem gerekiyordu. Yüksek lisans dönemimden gelen akademik araştırma ve "veri toplama" (data scraping) refleksimi, ilk olarak hangi araçları öğrenmem gerektiğini bulmak için kullandım. Sektörün standartlarını incelediğimde karşıma o muhteşem üçlü çıktı: Depolamak için SQL, analiz için Python ve görselleştirmek için Power BI.

İşe verinin temelinden başladım ve PostgreSQL dünyasına adım attım. Verileri sağlam bir ilişkisel veri tabanında toplamak, hem verilere yapısal bir düzen getiriyor hem de verinin hacmi ne kadar büyürse büyüsün sistemin ayakta kalmasını sağlıyordu. Ardından, bu ham veriyi işleyip anlamlandırmak için Python ve onun güçlü kütüphaneleriyle (Pandas, NumPy, Matplotlib) tanıştım.

Artık elimde hem sağlam veriler hem de derinlemesine analizler vardı. Fakat geriye en kritik adım kalmıştı: Bulduğum bu sonuçları başkalarına nasıl anlatacaktım? İşte tam o noktada Power BI imdadıma yetişti. Karmaşık sayı yığınlarını ve analiz çıktılarını; herkesin anlayabileceği, interaktif ve karar alma süreçlerini hızlandıran görsel şölenlere dönüştürmenin o büyüleyici yollarını keşfettim.

<br/>

![Veri depola, analiz et ve görselleştir]({static}/images/aletcantasi.jpg)


<h2 class="text-2xl font-bold mt-8 mb-4">Mühendislik Disiplinini Dijitale Taşımak</h2>

Jeoloji mühendisliğinde, sahadan ofise uzanan süreçte hangi numunenin veya fiziksel verinin nereye ait olduğunu tam olarak bilmek ve parçalar arasındaki o yapısal bağı kurmak işin temelidir. Veri analitiği yolculuğumda gördüm ki; ilişkisel bir veri tabanındaki tabloları birbirine bağlamak da aslında tamamen aynı mühendislik mantığına dayanıyor.

Fiziksel dünyadaki o mekansal disiplini dijitale aktarmak, sağlam bir SQL mimarisi kurmanın kalbini oluşturuyor. Bu mimariyi kurgulamanın neden bir mühendis titizliği gerektirdiğini ise "kirli veri" (dirty data) ile yüzleştiğinizde çok daha iyi anlıyorsunuz. Gerçek dünyada, internette "temiz" ve hazır veri bulmak neredeyse imkansızdır.

Tıpkı araziden çıkarılan toprakla karışık bir maden cevherini laboratuvarda yıkayıp saf hale getirmek gibi; ham veriyi bulmak, onu satır satır titizlikle temizlemek ve analize uygun formata sokmak işin neredeyse %70'ini oluşturuyor. İşte yeraltının o zorlu şartlarında yıllarca edindiğim mühendislik sabrımın ve hata kabul etmeyen yaklaşımımın, dijital dünyada bana en büyük avantajı sağladığı yer de tam olarak bu oldu.

<br/>

![Mühendislik disiplinini dijitale taşımak]({static}/images/sahadan-dijitale.jpg)


<h2 class="text-2xl font-bold mt-8 mb-4">Bu Blogda Sizi Neler Bekliyor?</h2>

"Bir mühendis nasıl düşünür?" sorusuyla başladığım bu yolda; verinin oluşumundan, depolanmasına ve nihayetinde görselleştirilmesine kadar geçen o devasa süreci bizzat inşa etmenin mutluluğunu yaşıyorum. Bu dönüşüm benim için sadece yeni araçlar öğrendiğim bir serüven değil, aynı zamanda mühendislik temellerimin üzerine gururla koyduğum yeni bir inşa süreci oldu.

Tabii ki öğrendiklerimi sadece teoride bırakmadım. Gerçek dünya verilerini kullanarak hazırladığım "Türkiye Deprem Aktivite Analizi" ve "Maden Piyasası Analizleri" gibi projeleri hayata geçirdim. Bu projelerin çıktılarını ve veri hikayelerini LinkedIn hesabımdan <a href="https://www.linkedin.com/in/ozanbrn/" target="_blank" class="text-blue-400 hover:text-blue-300">(Ozan Baran)</a>, işin mutfağını ve kaynak kodlarını ise GitHub hesabımdan <a href="https://github.com/ozanbrn" target="_blank" class="text-blue-400 hover:text-blue-300">(Ozan Baran)</a> paylaşmaya devam ediyorum.

Peki sırada ne var? Sadece geçmiş verileri analiz edip "ne olduğunu" raporlamakla yetinmeye niyetim yok. Geçmişin izlerinden geleceğin haritasını çıkaracağım o heyecan verici Veri Bilimi (Data Science) ve tahminleyici analitik yolculuğuna adım atmak için şimdiden sabırsızlanıyorum. Bu yolculukta karşılaştığım zorlukları, çözdüğüm hataları ve yeni projelerimi bu blogda paylaşmaya devam edeceğim.

<br/>
Veriyle kalın!

Diğer yazılarımı okumak için <a href="https://ozanbaran.com.tr/category/blog.html" class="text-blue-400 hover:text-blue-300">Tıklayın..!</a>

