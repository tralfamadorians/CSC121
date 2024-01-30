"""6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output."""

glossary = {
    'Key value pairs':'set of values associated with one another.',
    'Conditional test':'expression that can be valued true or false.',
    'Dictionary': 'collection of key-value pairs.',
    'PEP 8': 'one of the Python Enhancement Proposals that instructs Python programmers on how to style their code.',
    'Tuple': 'an immutable list.'
}

print(f"Key value pairs: {glossary['Key value pairs']}")
print(f"Conditional test: {glossary['Conditional test']}")
print(f"Dictionary: {glossary['Dictionary']}")
print(f"PEP 8: {glossary['PEP 8']}")
print(f"Tuple: {glossary['Tuple']}")