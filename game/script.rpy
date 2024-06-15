# script.rpy

# Define a function to handle nodes in a linked list style
define e = Character("Narrator")

# The game starts here.
label start:
    e "Welcome to the Ambasuke visual novel!"
    e "In this game, you will make choices that lead to different outcomes."

    jump node1

# Node 1
label node1:
    e "You wake up in a mysterious place. You have no idea how you got there."
    e "Do you want to explore or stay where you are?"
    menu:
        "Explore":
            jump node2_explore
        "Stay":
            jump node2_stay

# Node 2 - Explore Path
label node2_explore:
    e "You decide to explore the surroundings."
    e "After walking for a while, you find a strange device on the ground."
    e "Do you pick it up?"
    menu:
        "Yes":
            jump node3_explore_yes
        "No":
            jump node3_explore_no

label node3_explore_yes:
    e "You pick up the device and it starts to glow."
    e "Suddenly, you are transported to a different location."
    jump node4_explore_yes

label node3_explore_no:
    e "You decide to leave the device alone."
    e "As you walk away, you hear a noise behind you."
    jump node4_explore_no

label node4_explore_yes:
    e "In the new location, you find yourself in a futuristic city."
    e "You meet a friendly robot who offers to help you."
    jump node5_explore

label node4_explore_no:
    e "You turn around and see a group of hostile creatures approaching."
    e "You need to find a way to escape."
    jump node5_explore

label node5_explore:
    e "You continue your journey and face various challenges."
    e "After a long day, you find a safe place to rest."
    e "Do you trust the robot to keep watch?"
    menu:
        "Yes":
            jump node6_explore_yes
        "No":
            jump node6_explore_no

label node6_explore_yes:
    e "You trust the robot and fall asleep."
    e "When you wake up, you find the robot has disappeared."
    jump node7_explore

label node6_explore_no:
    e "You decide to keep watch yourself."
    e "You stay awake all night, but nothing happens."
    jump node7_explore

label node7_explore:
    e "The next morning, you continue your journey."
    e "You find a map that shows a way out of this place."
    e "Do you follow the map?"
    menu:
        "Yes":
            jump node8_explore_yes
        "No":
            jump node8_explore_no

label node8_explore_yes:
    e "You follow the map and eventually find an exit."
    jump node9_explore

label node8_explore_no:
    e "You ignore the map and continue wandering aimlessly."
    jump node9_explore

label node9_explore:
    e "After hours of walking, you encounter a group of survivors."
    e "They offer you a place in their community."
    e "Do you join them?"
    menu:
        "Yes":
            jump good_ending
        "No":
            jump bad_ending

# Node 2 - Stay Path
label node2_stay:
    e "You decide to stay where you are."
    e "After a while, you hear footsteps approaching."
    e "Do you hide or call out for help?"
    menu:
        "Hide":
            jump node3_stay_hide
        "Call out":
            jump node3_stay_call

label node3_stay_hide:
    e "You hide behind a nearby structure."
    e "A group of strangers walks by, talking in a language you don't understand."
    jump node4_stay

label node3_stay_call:
    e "You call out for help."
    e "The strangers turn towards you and approach cautiously."
    jump node4_stay

label node4_stay:
    e "The strangers turn out to be friendly and offer to help you."
    e "They take you to their camp and give you food and water."
    jump node5_stay

label node5_stay:
    e "You spend the night at the strangers' camp."
    e "The next day, they offer to help you find a way home."
    e "Do you trust them?"
    menu:
        "Yes":
            jump node6_stay_yes
        "No":
            jump node6_stay_no

label node6_stay_yes:
    e "You decide to trust the strangers."
    e "They lead you through a series of tunnels."
    jump node7_stay

label node6_stay_no:
    e "You don't trust the strangers and decide to leave on your own."
    e "You wander through the wilderness, looking for a way out."
    jump node7_stay

label node7_stay:
    e "After a long journey, you find a hidden door in the side of a mountain."
    e "Do you enter?"
    menu:
        "Yes":
            jump node8_stay_yes
        "No":
            jump node8_stay_no

label node8_stay_yes:
    e "You enter the hidden door and find yourself in a secret laboratory."
    e "Scientists there offer to help you get home."
    jump node9_stay

label node8_stay_no:
    e "You decide not to enter the hidden door."
    e "You continue wandering, hoping to find another way out."
    jump node9_stay

label node9_stay:
    e "After days of wandering, you encounter another group of survivors."
    e "They offer you a place in their community."
    e "Do you join them?"
    menu:
        "Yes":
            jump good_ending
        "No":
            jump bad_ending

# Good Ending
label good_ending:
    e "You decide to join the community of survivors."
    e "They welcome you with open arms and help you rebuild your life."
    e "You have found a new home and a new family."
    e "Congratulations, you have reached the good ending!"
    return

# Bad Ending
label bad_ending:
    e "You decide not to join the community of survivors."
    e "You continue wandering alone, struggling to survive."
    e "Eventually, you succumb to the harsh environment."
    e "You have reached the bad ending."
    return
