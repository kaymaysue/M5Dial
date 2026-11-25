## AI verantwoording

- Prompt: working in uiflow2 and using m5dial. Building with blocks. I have a variable 'gok' and as the rotary turns, the value of gok changes with it. I want the limits to be from 1 to 50. how to using if statements?
  Resultaat: Inside your Loop (or wherever your rotary updates gok): In UIFlow2, specifically
1. Find the Variables category and drag in an if block.
2. In the condition, use the comparison block (<) from Logic.
3. Put the gok variable on the left and 1 on the right.
4. Inside the do section, place set gok to 1.
5. Repeat with another if block using gok > 50, and set gok to 50.


