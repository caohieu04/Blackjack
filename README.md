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
Cards: ['5♠' '7♦']  | EV: -0.5190 
Cards: ['7♥' '8♦']  | EV: -0.5109 
Cards: ['J♥' 'K♥']  | EV: -0.8039 
Cards: ['J♦' 'Q♦']  | EV: -0.7920 
Cards: ['9♣' '10♥'] | EV: -0.6917 
Cards: ['4♠' 'Q♠']  | EV: -0.5038 
Cards: ['2♦' 'Q♣']  | EV: -0.5006 
Cards: ['2♥' '8♥']  | EV: -0.1896 
Cards: ['J♣' 'Q♦']  | EV: -0.8004 
Cards: ['3♣' '7♥']  | EV: -0.1609 
Cards: ['J♦' 'J♥']  | EV: -0.7875 
Cards: ['6♠' '9♥']  | EV: -0.5172 
Cards: ['8♥' '10♣'] | EV: -0.5855 
Cards: ['A♦' 'Q♦']  | EV: 0.0805  
Cards: ['4♦' '6♥']  | EV: -0.2182 
Cards: ['7♥' '8♠']  | EV: -0.5019 
Cards: ['4♣' 'Q♥']  | EV: -0.4958 
Cards: ['3♥' 'K♥']  | EV: -0.5048 
```
