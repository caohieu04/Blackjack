# Blackjack

## About
My free-time project

### Motivation:
In Vietnam we play Blackjack on Tet Holiday, because of everlong losing streak, I come up with the idea: Given initial set of 2 cards, what is expected value of money ratio if I pull 1 more card. 

Labels: 
  * Win: `1.0`
  * Lose: `-1.0`

### Result

`EV: Predicted expected value of neural net`
```
|Cards|EV|
|---|--|
| ['5♠' '7♦']  | -0.5190| 
| ['7♥' '8♦']  | -0.5109| 
| ['J♥' 'K♥']  | -0.8039| 
| ['J♦' 'Q♦']  | -0.7920| 
| ['9♣' '10♥'] | -0.6917| 
| ['4♠' 'Q♠']  | -0.5038| 
| ['2♦' 'Q♣']  | -0.5006| 
| ['2♥' '8♥']  | -0.1896| 
| ['J♣' 'Q♦']  | -0.8004| 
| ['3♣' '7♥']  | -0.1609| 
| ['J♦' 'J♥']  | -0.7875| 
| ['6♠' '9♥']  | -0.5172| 
| ['8♥' '10♣'] | -0.5855| 
| ['A♦' 'Q♦']  | 0.0805 | 
| ['4♦' '6♥']  | -0.2182| 
| ['7♥' '8♠']  | -0.5019| 
| ['4♣' 'Q♥']  | -0.4958| 
| ['3♥' 'K♥']  | -0.5048| 
```
