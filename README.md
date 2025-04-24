# Pig Latin
> "Best way to learn pig latin" 
> (no one)

Ever wanted to flex that you learned pig latin in 3rd grade? Or maybe you just want to stare at a word for a minute trying to determine which rule led to the monstronsity that is "UMPJAYEQUALYAYEROZAY? You're in the right place.

## Keywords

| Keyword | Action |
| ------ | ------ |
| USHPAY | Pushes the ascii value of a character onto the stack |
| OPPAY | Pops the value on the top of the stack and prints it |
| ADDYAY | Pops the top two values on the stack, adds them together, then pushes the sum onto the stack |
| UBSAY | Pops the top two values on the stack, subtracts them, then pushes the difference onto the stack |
| INTPRAY | Prints the string literal passed in as a parameter |
| UMPJAYEQUALYAYEROZAY | Jumps to the indicated label if the top of the stack has a decimal value equal to 0 |
| UMPJAYEATERGRAYEROZAY |  Jumps to the indicated label if the top of the stack has a decimal value greater than 0 |
| MUL | Pops then multiplies the top two values on the stack together and pushes the product to the stack |
| UPLICATEDAY | Duplicates the top of the stack and pushes the value onto the stack |
| ALTHAY | Stops the program from running |
| UILDBAY | Takes the value of the character at the provided location and adds it to a string literal |
| ECHOYAY | Prints the built string literal |
| OINTERPAY | Points the stack pointer to the given location |
| OPTAY | Prints the top of the stack |
| APSWAY | Swaps top two values on stack |
| ISERAY | Takes the bottom of the stack and pushes it to the top |
| IZESAY | Takes the current size of the stack and pushes it to the top

## File Descriptions
File Interpreter - Parses the code
```sh
interpreteryay.py
```
**Hello World - prints "Hello World"**
Input: none
Output: "Hello world"
```sh
python interpreteryay.py helloworld.oink
```

**Cat - echos your input**
Input: phrase
Output: phrase
```sh
python interpreteryay.py cat.oink
```

**Repeater - repeats your input**
Input 1: character to repeat
Input 2: # of times to repeat
Output: your character repeated nth times
```sh
python interpreteryay.py repeater.oink
```
**Multiply - multiplies two single digit numbers**
Input 1: first factor (0-9)
Input 2: second factor (0-9)
Output: the product
```sh
python interpreteryay.py multiply.oink
```
**Reverse String - echos your input**
Input: phrase
Output: esarhp (your reversed phrase)
```sh
python interpreteryay.py reversestring.oink
```