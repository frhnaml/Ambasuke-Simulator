# script.rpy

define e = Character("Epstein")
define characterSampingan = Character("Jaka")
define kucing = Character("Tom")
define pohon = Character("Groot")


init python:
    # Initialize the linked list and add nodes
    from Cerita import LinkedList

    # Urutan Node
    story = LinkedList()
    story.add("scene0")    # 0
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
    
    show jaka shocked
    characterSampingan "Jaka, seorang pemuda yang suka petualangan, suatu hari menemukan pintu misterius di dalam lemari tuanya. Karena penasaran, dia memutuskan untuk masuk ke dalam pintu tersebut."
    characterSampingan "Tiba-tiba, dia menemukan dirinya di dunia lain yang penuh dengan makhluk aneh dan lucu."
    
    hide jaka

    $ current_node = 0
    jump expression story.get(current_node)


#Definisikan isi Node 
label scene1:
    menu:
        "Jaka melihat seekor kucing yang bisa berbicara.":
            $ current_node = 1
            jump expression story.get(current_node)
        "Jaka melihat pohon yang sedang menari.":
            $ current_node = 2
            jump expression story.get(current_node)

label scene2A:
    e "Jaka terkejut melihat seekor kucing yang sedang membaca buku dan bisa berbicara. Kucing itu menyapa Jaka dengan ramah."
    kucing "Halo, manusia! Namaku Tom. Apa yang membawamu ke sini?"
    menu:
        "Jaka bertanya kepada kucing tentang dunia ini.":
            $ current_node = 3
            jump expression story.get(current_node)
        "Jaka meminta kucing menunjukkan jalan keluar.":
            $ current_node = 4
            jump expression story.get(current_node)

label scene2B:
    e "Jaka terpukau melihat pohon yang menari mengikuti irama musik yang entah berasal dari mana. Tiba-tiba, pohon itu berhenti dan menyapanya."
    pohon "Halo, manusia! Namaku Groot. Apa yang membawamu ke sini?"
    menu:
        "Jaka bertanya kepada pohon tentang dunia ini.":
            $ current_node = 
            jump expression story.get(current_node)
        "Jaka meminta pohon menunjukkan jalan keluar.":
            $ current_node = 
            jump expression story.get(current_node)

label scene3A:
    characterSampingan "Tom, bisa ceritakan tentang dunia ini?"
    kucing "Ini adalah Dunia Lucu, tempat di mana segala sesuatu bisa terjadi. Kamu ingin mencoba sesuatu yang menarik?"
    menu:
        "Jaka ingin mencoba makanan ajaib.":
            $ current_node = 5
            jump expression story.get(current_node)
        
        "Jaka ingin mencoba terbang dengan sayap kucing.":
            $ current_node = 6
            jump expression story.get(current_node)

label scene3Av2:
    characterSampingan "Tom, bisa ceritakan tentang dunia ini?"
    kucing "Ini adalah Dunia Lucu, tempat di mana segala sesuatu bisa terjadi. Kamu ingin mencoba sesuatu yang menarik?"
    menu:
        "Jaka ingin mencoba makanan ajaib.":
            $ current_node = 5
            jump expression story.get(current_node)
        
        "Jaka ingin mencoba terbang dengan sayap kucing.":
            $ current_node = 6
            jump expression story.get(current_node)



