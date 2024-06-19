# script.rpy

define e = Character("Narrator")
define characterSampingan = Character("Jaka")
define kucing = Character("Tom")
define pohon = Character("Groot")


init python:
    # Initialize the linked list and add nodes
    from Cerita import LinkedList

    # Urutan Node
    story = LinkedList()
    story.add("start")    # 0
    story.add("scene1")    # 1
    story.add("scene2")    # 2
    story.add("scene1A")   # 3
    story.add("scene1B")   # 4
    story.add("scene2A")   # 5
    story.add("scene2B")   # 6
    story.add("scene1A1")  # 7
    story.add("scene1A2")  # 8
    story.add("scene1B1")  # 9
    story.add("scene1B2")  # 10
    story.add("scene2A1")  # 11
    story.add("scene2A2")  # 12
    story.add("scene2B1")  # 13
    story.add("scene2B2")  # 14
    story.add("scene1A1A") # 15
    story.add("scene1A1B") # 16
    story.add("scene1A2A") # 17
    story.add("scene1A2B") # 18
    story.add("scene1B1A") # 19
    story.add("scene1B1B") # 20
    story.add("scene1B2A") # 21
    story.add("scene1B2B") # 22
    story.add("scene2A1A") # 23
    story.add("scene2A1B") # 24
    story.add("scene2A2A") # 25
    story.add("scene2A2B") # 26
    story.add("scene2B1A") # 27
    story.add("scene2B1B") # 28
    story.add("scene2B2A") # 29
    story.add("scene2B2B") # 30
 
# The game starts here.
label start:
    scene bg class

    e "Jaka, seorang pemuda yang suka petualangan, suatu hari menemukan pintu misterius di dalam lemari tuanya. Karena penasaran, dia memutuskan untuk masuk ke dalam pintu tersebut."
    e "Tiba-tiba, dia menemukan dirinya di dunia lain yang penuh dengan makhluk aneh dan lucu."

    $ current_node = 0
    menu:
        "Jaka melihat seekor kucing yang bisa berbicara.":
            $ current_node = 1
            jump expression story.get(current_node)
        "Jaka melihat pohon yang sedang menari.":
            $ current_node = 2
            jump expression story.get(current_node)

#Definisikan isi Node 
label scene1:
    e "Jaka terkejut melihat seekor kucing yang sedang membaca buku dan bisa berbicara."
    e "Kucing itu menyapa Jaka dengan ramah."

    kucing "Halo, manusia! Namaku Tom. Apa yang membawamu ke sini?"
    menu:
        "Jaka bertanya kepada kucing tentang dunia ini.":
            $ current_node = 3
            jump expression story.get(current_node)
        "Jaka meminta kucing menunjukkan jalan keluar.":
            $ current_node = 4
            jump expression story.get(current_node)

label scene2:
    e "Jaka terpukau melihat pohon yang menari mengikuti irama musik yang entah berasal dari mana."
    e "Tiba-tiba, pohon itu berhenti dan menyapanya."
    pohon "Halo, manusia! Namaku Groot. Apa yang membawamu ke sini?"
    e ""
    menu:
        "Jaka bertanya kepada pohon tentang dunia ini.":
            $ current_node = 5
            jump expression story.get(current_node)
        "Jaka meminta pohon menunjukkan jalan keluar.":
            $ current_node = 6
            jump expression story.get(current_node)

label scene1A:
    characterSampingan "Tom, bisa ceritakan tentang dunia ini?"
    kucing "Ini adalah Dunia Lucu, tempat di mana segala sesuatu bisa terjadi. Kamu ingin mencoba sesuatu yang menarik?"
    menu:
        "Aku ingin mencoba makanan ajaib.":
            $ current_node = 7
            jump expression story.get(current_node)
        
        "Aku ingin mencoba terbang dengan sayap kucing.":
            $ current_node = 8
            jump expression story.get(current_node)

label scene1B:
    characterSampingan "Tom, bisa tunjukkan jalan keluar dari sini?"
    kucing "Tentu, tapi kamu harus menjawab teka-teki dulu. Apa yang memiliki ekor tapi bukan hewan?"
    menu:
        "layang-layang":
            $ current_node = 9
            jump expression story.get(current_node)
        
        "cacing":
            $ current_node = 10
            jump expression story.get(current_node)

label scene2A:
    characterSampingan "Groot, bisa ceritakan tentang dunia ini?"
    kucing "Ini adalah Dunia Lucu, tempat di mana pohon bisa menari dan manusia bisa berbicara dengan pohon. Kamu ingin mencoba sesuatu yang menarik?"
    menu:
        "Aku ingin menari dengan pohon.":
            $ current_node = 11
            jump expression story.get(current_node)
        
        "Aku ingin memetik buah ajaib dari pohon.":
            $ current_node = 12
            jump expression story.get(current_node)

label scene2B:
    characterSampingan "Groot, bisa tunjukkan jalan keluar dari sini?"
    kucing "Tentu, tapi kamu harus menjawab teka-teki dulu. Apa yang selalu di depanmu tetapi tidak pernah bisa kamu lihat?"
    menu:
        "Masa depan.":
            $ current_node = 13
            jump expression story.get(current_node)
        
        "Bayangan.":
            $ current_node = 14
            jump expression story.get(current_node)

label scene1A1:
    kucing "Baiklah, cobalah kue ini. Setiap gigitan akan membuatmu merasa seperti tokoh kartun!"
    e "Jaka mencoba kue itu dan tiba-tiba badannya mulai berubah menjadi kartun, tangannya bisa melar seperti karet dan kepalanya bisa berputar."
    menu:
        "Jaka senang dan ingin mencoba lebih banyak makanan ajaib.":
            $ current_node = 15
            jump expression story.get(current_node)
        
        "Jaka panik dan meminta bantuan Tom.":
            $ current_node = 16
            jump expression story.get(current_node)

label scene1A1A:
    characterSampingan "Wah, ini luar biasa! Aku ingin mencoba lebih banyak makanan ajaib!"
    kucing "Bagus! Aku punya banyak makanan lain yang bisa kamu coba."
    e "Kucing itu memberikan Jaka berbagai macam makanan ajaib. Setiap makanan memberikan kekuatan kartun yang berbeda. Jaka sangat senang dan menghabiskan waktu seharian bermain dengan kekuatan barunya."
    e "Akhirnya, Jaka menemukan makanan yang bisa mengembalikannya ke wujud normal. Ia menyimpan makanan ajaib lainnya untuk digunakan di kemudian hari."
    e "Jaka pulang ke rumah dengan hati gembira, siap untuk petualangan baru di masa depan dengan kekuatan barunya."
    return

label scene1A1B:
    characterSampingan "Oh tidak, apa yang terjadi padaku? Tom! Tolong aku!"
    e "Jaka panik dan berlari mencari Tom. Ketika menemukan Tom, ia menjelaskan apa yang terjadi."
    kucing "Tenang Jaka, aku akan membantumu."
    e "Tom mencoba berbagai cara untuk mengembalikan Jaka ke wujud normal, tetapi tidak ada yang berhasil. Jaka mulai putus asa."
    e "Hari demi hari berlalu, dan Jaka harus belajar hidup dengan tubuh kartunnya. Meski pada awalnya sulit, lambat laun Jaka mulai menerima kenyataan dan menemukan cara untuk menggunakan kekuatannya untuk membantu orang lain."
    e "Walau Jaka tidak pernah bisa kembali sepenuhnya seperti semula, ia menemukan makna baru dalam hidupnya dengan membantu orang lain dengan kekuatan kartunnya."
    return

label scene1A2:
    kucing "Baiklah, pegang ini!"
    e "Tom memberikan sayap ajaib kepada Jaka."
    e "Jaka memasang sayap tersebut dan tiba-tiba dia bisa terbang seperti burung."
    menu:
        "Jaka terbang tinggi dan menjelajahi dunia dari atas":
            $ current_node = 17
            jump expression story.get(current_node)
        
        "Jaka terbang rendah dan mencoba mendarat di tempat aman.":
            $ current_node = 18
            jump expression story.get(current_node)

label scene1A2A:
    e "Jaka terbang tinggi ke langit, menjelajahi dunia dari atas. Pemandangan yang ia lihat sangat menakjubkan; gunung, lautan, dan kota-kota terlihat begitu kecil dari ketinggian."
    e "Jaka merasa sangat bebas dan bahagia, melayang di udara seperti burung."
    jaka "Ini luar biasa! Aku bisa melihat seluruh dunia dari sini!"
    e "Setelah beberapa jam menikmati pemandangan, Jaka memutuskan untuk kembali ke tanah. Dia menemukan tempat yang aman untuk mendarat."
    e "Ketika mendarat, sayap ajaibnya menghilang dengan perlahan."
    kucing "Bagaimana rasanya terbang, Jaka?"
    jaka "Itu pengalaman yang tak terlupakan. Terima kasih!"
    e "Jaka pulang dengan hati yang penuh kebahagiaan dan kenangan indah dari petualangannya di langit. Dia tahu bahwa dia selalu bisa mengandalkan kucing untuk petualangan ajaib di masa depan."
    return

label scene1A2B:
    e "Jaka terbang rendah, menikmati sensasi terbang di dekat tanah. Ia merasakan angin di wajahnya dan melihat detail pemandangan dengan lebih jelas."
    jaka "Aku harus mendarat dengan hati-hati."
    e "Jaka mencari tempat yang aman untuk mendarat. Setelah menemukan lapangan terbuka, dia mendarat dengan lembut."
    e "Sayap ajaibnya menghilang dengan perlahan, dan Jaka merasa sangat puas dengan petualangan terbangnya."
    kucing "Apakah kamu menikmati terbang, Jaka?"
    jaka "Sangat! Itu pengalaman yang luar biasa. Terima kasih banyak!"
    e "Jaka pulang dengan hati yang penuh kebahagiaan. Dia tahu bahwa dia bisa menghadapi apa saja dengan keajaiban yang telah ia alami."
    e "Jaka tersenyum dan berpikir tentang petualangan-petualangan seru lainnya yang mungkin akan ia hadapi di masa depan."
    return

label scene1B1:
    kucing "Betul! Layang-layang punya ekor tapi bukan hewan. Ayo, ikut aku!"
    e "Tom membawa Jaka ke sebuah pintu yang bisa membawanya pulang ke rumah."
    e " meJaka memasang sayap tersebut dan tiba-tiba dia bisa terbang seperti burung."
    menu:
        "Jaka pulang ke rumah dan membawa pulang Miau sebagai teman.":
            $ current_node = 19
            jump expression story.get(current_node)
        
        "Jaka memutuskan untuk tinggal lebih lama di Dunia Lucu.":
            $ current_node = 20
            jump expression story.get(current_node)

label scene1B1A:
    e "Jaka memutuskan untuk pulang ke rumah. Sebelum pergi, kucing itu memberikan Miau, seekor kucing kecil yang lucu, sebagai teman."
    jaka "Terima kasih atas semuanya! Aku akan merindukan tempat ini, tapi aku senang bisa membawa Miau bersamaku."
    kucing "Jangan khawatir, Jaka. Kamu selalu bisa kembali ke Dunia Lucu kapan saja."
    e "Jaka berjalan melalui pintu dan tiba-tiba dia berada di kamarnya sendiri. Miau mengikuti di belakangnya."
    e "Dengan Miau di sisinya, Jaka merasa lebih bahagia dan tidak pernah merasa kesepian lagi. Mereka berdua menjadi sahabat yang tak terpisahkan."
    e "Setiap kali Jaka ingin petualangan baru, ia tahu bahwa Dunia Lucu selalu menunggunya."
    e "Jaka menjalani hidupnya dengan penuh keceriaan dan kenangan indah dari Dunia Lucu."
    return

label scene1B1B:
    e "Jaka memutuskan untuk tinggal lebih lama di Dunia Lucu. Tempat itu penuh dengan keajaiban dan petualangan yang tak ada habisnya."
    jaka "Aku ingin menjelajahi lebih banyak tempat di Dunia Lucu. Terlalu banyak yang belum aku lihat."
    kucing "Bagus sekali, Jaka! Mari kita mulai petualangan baru!"
    e "Kucing itu membawa Jaka ke berbagai tempat yang menakjubkan. Mereka bertemu makhluk-makhluk aneh dan menikmati petualangan yang luar biasa."
    e "Suatu hari, Jaka menemukan sebuah gua tersembunyi yang belum pernah dilihat oleh siapapun sebelumnya. Di dalamnya, dia menemukan harta karun dan artefak ajaib."
    jaka "Ini luar biasa! Tempat ini penuh dengan misteri dan keajaiban."
    e "Jaka memutuskan untuk menjadikan Dunia Lucu sebagai rumah keduanya. Setiap hari adalah petualangan baru, dan dia belajar banyak hal tentang dunia dan dirinya sendiri."
    e "Dalam hatinya, Jaka tahu bahwa dia telah menemukan tempat yang benar-benar ajaib, di mana impian menjadi kenyataan."
    return

label scene1B2:
    kucing "Salah! Tapi tidak apa-apa, kamu masih punya satu kesempatan lagi. Apa yang selalu di depanmu tetapi tidak pernah bisa kamu lihat?"
    menu:
        "Masa depan":
            $ current_node = 21
            jump expression story.get(current_node)
        
        "Bayangan":
            $ current_node = 22
            jump expression story.get(current_node)

label scene1B2A:
    e "Jaka berpikir keras dan akhirnya menjawab."
    jaka "Masa depan!"
    kucing "Salah lagi, Jaka! Jawabannya bukan itu."
    e "Tiba-tiba, lantai di bawah Jaka terbuka dan dia jatuh ke dalam kegelapan yang dalam."
    jaka "Aaaahhh!"
    e "Jaka terjebak di dunia yang suram dan penuh dengan ketakutan. Dia mencoba mencari jalan keluar, tapi setiap langkah hanya membawanya lebih dalam ke dalam kegelapan."
    e "Meski berusaha keras, Jaka tidak bisa menemukan jalan kembali ke dunia nyata. Dia terjebak selamanya dalam dunia teka-teki yang tak berujung."
    return

label scene1B2B:
    e "Jaka berpikir keras dan akhirnya menjawab."
    jaka "Bayangan!"
    kucing "Betul sekali! Kamu memang pintar, Jaka."
    e "Pintu besar muncul di depan Jaka, memancarkan cahaya terang yang menyilaukan."
    kucing "Lewat pintu ini, kamu bisa kembali ke rumah."
    e "Jaka tersenyum lega dan melangkah melalui pintu. Seketika, dia menemukan dirinya kembali di kamarnya, aman dan sehat."
    jaka "Terima kasih, kucing! Aku tidak akan melupakan petualangan ini."
    e "Dengan kenangan indah dari Dunia Lucu, Jaka menjalani hari-harinya dengan lebih ceria dan penuh semangat. Dia tahu bahwa kapan saja dia merasa bosan atau kesepian, petualangan selalu menunggunya di suatu tempat yang ajaib."
    return

label scene2A1:
    pohon "Ayo, mari kita menari!"
    e "Jaka dan Groot mulai menari bersama dan Jaka merasa sangat senang, ternyata menari dengan pohon sangat menyenangkan."
    menu:
        "Jaka ingin terus menari dengan Groot.":
            $ current_node = 23
            jump expression story.get(current_node)
        
        "Jaka lelah dan ingin mencari petualangan lain.":
            $ current_node = 24
            jump expression story.get(current_node)

label scene2A2:
    pohon "Baiklah, ini dia buah ajaibnya. Satu gigitan akan membuatmu bisa berbicara dengan semua makhluk di sini."
    e "Jaka memetik buah tersebut dan memakannya."
    menu:
        "Jaka mencoba berbicara dengan makhluk lain.":
            $ current_node = 25
            jump expression story.get(current_node)
        
        "Jaka ingin mencoba buah ajaib lainnya.":
            $ current_node = 26
            jump expression story.get(current_node)

label scene2B1:
    pohon "Betul! Masa depan selalu di depanmu tetapi tidak pernah bisa kamu lihat. Ayo, ikut aku!"
    e "Groot membawa Jaka ke sebuah pintu yang bisa membawanya pulang ke rumah."
    menu:
        "Jaka pulang ke rumah dan membawa pulang Groot sebagai teman.":
            $ current_node = 27
            jump expression story.get(current_node)
        
        "Jaka memutuskan untuk tinggal lebih lama di Dunia Lucu.":
            $ current_node = 28
            jump expression story.get(current_node)

label scene2B2:
    pohon "Salah! Tapi tidak apa-apa, kamu masih punya satu kesempatan lagi. Apa yang memiliki ekor tapi bukan hewan?"
    menu:
        "layang-layang":
            $ current_node = 29
            jump expression story.get(current_node)
        
        "cacing":
            $ current_node = 30
            jump expression story.get(current_node)
