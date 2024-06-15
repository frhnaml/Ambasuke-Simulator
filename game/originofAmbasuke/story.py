# story_nodes.py

class Node:
    def __init__(self, id, text, choices=None):
        self.id = id
        self.text = text
        self.choices = choices if choices else []

class Choice:
    def __init__(self, text, target_node_id):
        self.text = text
        self.target_node_id = target_node_id

# Define the nodes
nodes = {
    1: Node(1, "One sunny day, Bob stumbled upon a garage sale. Look at this! A Magic Toaster! What could possibly go wrong?", [
        Choice("Test the Toaster", 2),
        Choice("Ignore it", 3)
    ]),
    2: Node(2, "Bob decides to test the Toaster. Let's see... I wish for money! The Toaster shakes and suddenly, it starts raining counterfeit bills.", [
        Choice("Try another wish", 4),
        Choice("Call Professor Quack", 5)
    ]),
    3: Node(3, "Bob decides to ignore the Toaster.", [
        Choice("Alice convinces Bob to test it", 2),
        Choice("Bob throws it away", 6)
    ]),
    4: Node(4, "Okay, let's try something else... I wish for superpowers! The Toaster glows and Bob suddenly gains the ability to speak to squirrels.", [
        Choice("Talk to squirrels", 7),
        Choice("Undo the wish", 8)
    ]),
    5: Node(5, "Hello, Professor Quack? I need your help with a Magic Toaster. Ah, the Magic Toaster! Follow my instructions carefully.", [
        Choice("Follow Quack’s instructions", 9),
        Choice("Ignore Quack’s advice", 10)
    ]),
    6: Node(6, "Bob throws the Toaster away, but it magically reappears.", [
        Choice("Investigate", 11),
        Choice("Ignore it", 12)
    ]),
    7: Node(7, "Bob talks to squirrels, who give him absurd advice.", [
        Choice("Follow squirrel advice", 13),
        Choice("Ignore the squirrels", 14)
    ]),
    8: Node(8, "Bob tries to undo the wish, but ends up swapping voices with Alice.", [
        Choice("Visit Professor Quack", 15),
        Choice("Accept the new voices", 16)
    ]),
    9: Node(9, "Quack provides a complex solution.", [
        Choice("Perform the ritual", 17),
        Choice("Improvise", 18)
    ]),
    10: Node(10, "Bob ignores Quack, causing more chaos.", [
        Choice("Apologize to Quack", 19),
        Choice("Seek Alice’s help", 20)
    ]),
    11: Node(11, "Bob investigates the Toaster’s origins.", [
        Choice("Visit the garage sale again", 21),
        Choice("Search online", 22)
    ]),
    12: Node(12, "Bob ignores the Toaster, but it keeps causing small pranks.", [
        Choice("Confront the Toaster", 23),
        Choice("Sell it online", 24)
    ]),
    13: Node(13, "Bob follows the squirrel advice and ends up in bizarre situations.", [
        Choice("Keep following advice", 25),
        Choice("Give up", 26)
    ]),
    14: Node(14, "Bob ignores the squirrels and faces their wrath.", [
        Choice("Apologize to squirrels", 27),
        Choice("Fight back", 28)
    ]),
    15: Node(15, "Bob visits Quack to fix the voice swap.", [
        Choice("Follow Quack’s complex plan", 29),
        Choice("Trust Alice’s simple idea", 30)
    ]),
    16: Node(16, "Bob and Alice adapt to their new voices and become famous voice actors."),
    17: Node(17, "The ritual works but Bob turns into a toaster."),
    18: Node(18, "Bob improvises and accidentally turns everyone into bread."),
    19: Node(19, "Quack forgives Bob and fixes everything, but the Toaster stays magical."),
    20: Node(20, "Alice helps Bob and they manage to tame the Toaster.")
}

def get_node(node_id):
    return nodes[node_id]
