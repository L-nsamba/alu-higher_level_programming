>>> text_indentation = __import__('5-text_indentation').text_indentation

>>> text_indentation()
Traceback (most recent call last):
TypeError: text_indentation() missing 1 required positional argument: 'text'

>>> text_indentation("Market. Analysis? How are you: Hamid")
Market.
<BLANKLINE>
Analysis?
<BLANKLINE>
How are you:
<BLANKLINE>
Hamid

>>> text_indentation(2)
Traceback (most recent call last):
TypeError: text must be a string

>>> text_indentation("Market. Structure")
Market.
<BLANKLINE>
Structure
