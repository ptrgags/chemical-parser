# Chemical Parser

This is a simple chemical formula parser that takes in chemical formulae and displays how many of each element are present
in the formula.

The parser supports nested parentheses and brackets as well as integer quantities.

## Usage

To run Chemical Parser as a REPL:
`./ChemicalParser.py`

To run with sample input:
`./ChemicalParser.py < example_formulae.txt`

Example input -> Example output:
* `H20 -> {'H': 2, 'O': 1}`
* `Al2(CO3)3 -> {'C': 3, 'Al': 2, 'O': 9}`
* `K4[ON(SO3)2]2 -> {'K': 4, 'S': 4, 'O': 14, 'N': 2}`
