## Assignment 2 REQ 3 implementation: 

#### Non-Player Characters
Non-Player character is an abstract class that extends the Actor class. 

##### Non-Player Character variants 
Each of the character variants extends the abstract class of the Non-Player character. All of which implement the CanListen interface - this allows the Player to listen to their
random list of dialogues.

They are also all encoded with a WanderBehaviour in their constructors behaviour map. Now we will go into what is unique for each of the classes for each class below: 

**Kale:** Checks the balance of the player using the checkBalance() method to determine
the number of runes that the player has - this adds the specified dialogues into her dialogue list. These are randomly selected. The getInventory() method is also used to add dialogues.  

**Sellen:** Randomly selects a dialogue from her list of dialogues 

**Guts:** An AttackBehaviour is added into its behaviour mapping. This allows Guts to attack
any that thing moves. The way that things are checked if they can move is if they have the capability CAN_MOVE which is added into the capabilities of an Actor if they have a wanderBehaviour. 

All behaviours are executed in the playTurn() function. 

#### Allowable Actions ~ The Player listening

A listenAction is added into the player if they are near the NPCs. This extends the action class. Also it is important to note that the  listen Action takes in an CanListen target. This ensures that all the inputs from the 
can use the getListenDescription() function from the target. 


