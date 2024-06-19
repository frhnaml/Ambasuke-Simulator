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

label scene1B2:
    kucing "Salah! Tapi tidak apa-apa, kamu masih punya satu kesempatan lagi. Apa yang selalu di depanmu tetapi tidak pernah bisa kamu lihat?"
    menu:
        "Masa depan":
            $ current_node = 21
            jump expression story.get(current_node)
        
        "Bayangan":
            $ current_node = 22
            jump expression story.get(current_node)

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
