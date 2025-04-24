# Pig Latin
> "Best way to learn pig latin" 
> (no one)

Ever wanted to flex that you learned pig latin in 3rd grade? Or maybe you just want to stare at a word for a minute trying to determine which rule led to the monstronsity that is "UMPJAYEQUALYAYEROZAY? You're in the right place.

## Keywords

| Keyword | English Transaltion | Action |
| ------ | ------ | ------ |
| USHPAY | Push | Pushes the ascii value of a character onto the stack |
| OPPAY | Pop | Pops the value on the top of the stack and prints it |
| ADDYAY | Add | Pops the top two values on the stack, adds them together, then pushes the sum onto the stack |
| UBSAY | Sub | Pops the top two values on the stack, subtracts them, then pushes the difference onto the stack |
| INTPRAY | Print | Prints the string literal passed in as a parameter |
| UMPJAYEQUALYAYEROZAY | Jump Equal Zero | Jumps to the indicated label if the top of the stack has a decimal value equal to 0 |
| UMPJAYEATERGRAYEROZAY | Jump Greater Zero | Jumps to the indicated label if the top of the stack has a decimal value greater than 0 |
| ULMAY | MAY | Pops then multiplies the top two values on the stack together and pushes the product to the stack |
| UPLICATEDAY | Duplicate | Duplicates the top of the stack and pushes the value onto the stack |
| ALTHAY | Halt | Stops the program from running |
| UILDBAY | Build | Takes the value of the character at the provided location and adds it to a string literal |
| ECHOYAY | Echo | Prints the built string literal |
| OINTERPAY | Pointer | Points the stack pointer to the given location |
| OPTAY | Top | Prints the top of the stack |
| APSWAY | Swap | Swaps top two values on stack |
| ISERAY | Rise | Takes the bottom of the stack and pushes it to the top |
| IZESAY | Size | Takes the current size of the stack and pushes it to the top

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