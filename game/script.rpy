# script.rpy

define e = Character('Epstein', color="E2BBE9", image='Epstein')

image Epstein faggot = "Epstein faggot.png"

init python:
    # Initialize the linked list and add nodes
    from Cerita import LinkedList

    story = LinkedList()
    story.add("node1")
    story.add("node2_explore")
    story.add("node2_stay")
    story.add("node3_explore_yes")
    story.add("node3_explore_no")
    story.add("node4_explore_yes")
    story.add("node4_explore_no")
    story.add("node5_explore")
    story.add("node6_explore_yes")
    story.add("node6_explore_no")
    story.add("node7_explore")
    story.add("node8_explore_yes")
    story.add("node8_explore_no")
    story.add("node9_explore")
    story.add("node3_stay_hide")
    story.add("node3_stay_call")
    story.add("node4_stay")
    story.add("node5_stay")
    story.add("node6_stay_yes")
    story.add("node6_stay_no")
    story.add("node7_stay")
    story.add("node8_stay_yes")
    story.add("node8_stay_no")
    story.add("node9_stay")
    story.add("good_ending")
    story.add("bad_ending")

# The game starts here.
label start:

    show Epstein faggot
    e "Welcome to the Ambasuke visual novel!"
    e "In this game, you will make choices that lead to different outcomes."

    $ current_node = 0
    jump expression story.get(current_node)

label node1:
    show Epstein faggot
    e "You wake up in a mysterious place. You have no idea how you got there."
    e "Do you want to explore or stay where you are?"
    menu:
        "Explore":
            $ current_node = 1
            jump expression story.get(current_node)
        "Stay":
            $ current_node = 2
            jump expression story.get(current_node)

label node2_explore:
    e "You decide to explore the surroundings."
    e "After walking for a while, you find a strange device on the ground."
    e "Do you pick it up?"
    menu:
        "Yes":
            $ current_node = 3
            jump expression story.get(current_node)
        "No":
            $ current_node = 4
            jump expression story.get(current_node)

label node3_explore_yes:
    e "You pick up the device and it starts to glow."
    e "Suddenly, you are transported to a different location."
    $ current_node = 5
    jump expression story.get(current_node)

label node3_explore_no:
    e "You decide to leave the device alone."
    e "As you walk away, you hear a noise behind you."
    $ current_node = 6
    jump expression story.get(current_node)

label node4_explore_yes:
    e "In the new location, you find yourself in a futuristic city."
    e "You meet a friendly robot who offers to help you."
    $ current_node = 7
    jump expression story.get(current_node)

label node4_explore_no:
    e "You turn around and see a group of hostile creatures approaching."
    e "You need to find a way to escape."
    $ current_node = 7
    jump expression story.get(current_node)

label node5_explore:
    e "You continue your journey and face various challenges."
    e "After a long day, you find a safe place to rest."
    e "Do you trust the robot to keep watch?"
    menu:
        "Yes":
            $ current_node = 8
            jump expression story.get(current_node)
        "No":
            $ current_node = 9
            jump expression story.get(current_node)

label node6_explore_yes:
    e "You trust the robot and fall asleep."
    e "When you wake up, you find the robot has disappeared."
    $ current_node = 10
    jump expression story.get(current_node)

label node6_explore_no:
    e "You decide to keep watch yourself."
    e "You stay awake all night, but nothing happens."
    $ current_node = 10
    jump expression story.get(current_node)

label node7_explore:
    e "The next morning, you continue your journey."
    e "You find a map that shows a way out of this place."
    e "Do you follow the map?"
    menu:
        "Yes":
            $ current_node = 11
            jump expression story.get(current_node)
        "No":
            $ current_node = 12
            jump expression story.get(current_node)

label node8_explore_yes:
    e "You follow the map and eventually find an exit."
    $ current_node = 13
    jump expression story.get(current_node)

label node8_explore_no:
    e "You ignore the map and continue wandering aimlessly."
    $ current_node = 13
    jump expression story.get(current_node)

label node9_explore:
    e "After hours of walking, you encounter a group of survivors."
    e "They offer you a place in their community."
    e "Do you join them?"
    menu:
        "Yes":
            $ current_node = 23
            jump expression story.get(current_node)
        "No":
            $ current_node = 24
            jump expression story.get(current_node)

label node2_stay:
    e "You decide to stay where you are."
    e "After a while, you hear footsteps approaching."
    e "Do you hide or call out for help?"
    menu:
        "Hide":
            $ current_node = 14
            jump expression story.get(current_node)
        "Call out":
            $ current_node = 15
            jump expression story.get(current_node)

label node3_stay_hide:
    e "You hide behind a nearby structure."
    e "A group of strangers walks by, talking in a language you don't understand."
    $ current_node = 16
    jump expression story.get(current_node)

label node3_stay_call:
    e "You call out for help."
    e "The strangers turn towards you and approach cautiously."
    $ current_node = 16
    jump expression story.get(current_node)

label node4_stay:
    e "The strangers turn out to be friendly and offer to help you."
    e "They take you to their camp and give you food and water."
    $ current_node = 17
    jump expression story.get(current_node)

label node5_stay:
    e "You spend the night at the strangers' camp."
    e "The next day, they offer to help you find a way home."
    e "Do you trust them?"
    menu:
        "Yes":
            $ current_node = 18
            jump expression story.get(current_node)
        "No":
            $ current_node = 19
            jump expression story.get(current_node)

label node6_stay_yes:
    e "You decide to trust the strangers."
    e "They lead you through a series of tunnels."
    $ current_node = 20
    jump expression story.get(current_node)

label node6_stay_no:
    e "You don't trust the strangers and decide to leave on your own."
    e "You wander through the wilderness, looking for a way out."
    $ current_node = 20
    jump expression story.get(current_node)

label node7_stay:
    e "After a long journey, you find a hidden door in the side of a mountain."
    e "Do you enter?"
    menu:
        "Yes":
            $ current_node = 21
            jump expression story.get(current_node)
        "No":
            $ current_node = 22
            jump expression story.get(current_node)

label node8_stay_yes:
    e "You enter the hidden door and find yourself in a secret laboratory."
   
