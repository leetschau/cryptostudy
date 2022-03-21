# Exercise 1.1

from functools import partial
import string
from rich import print


# Implementation 1: define 'encode' and 'decode' respectively:

def encode_char(char: str, shft: int, vocab: str) -> str:
    if char not in vocab:
        return char
    target = (vocab.index(char) + shft) % len(vocab)
    return vocab[target]

def decode_char(char: str, shft: int, vocab: str) -> str:
    if char not in vocab:
        return char
    return vocab[vocab.index(char) - shft]

def encode(inp: str, shift: int) -> str:
    return ''.join(map(partial(encode_char,
                               shft=shift,
                               vocab=string.ascii_uppercase),
                       inp))

def decode(inp: str, shift: int) -> str:
    return ''.join(map(partial(decode_char,
                               shft=shift,
                               vocab=string.ascii_uppercase),
                       inp))


# Implementation 2: combine 'encode' and 'decode' in one function:

def convert_char(char: str, shft: int, method: str, vocab: str) -> str:
    if char not in vocab:
        return char
    target = (vocab.index(char) + shft) % len(vocab) if method == 'encode' else vocab.index(char) - shft
    return vocab[target]

def convert(inp: str, shift: int, method: str, vocab: str) -> str:
    return ''.join(map(partial(convert_char, shft=shift, method=method, vocab=vocab), inp))


# Test cases:

sample = 'HELLO AZ, hello az'
shift = 2

## Test implementaion 1:

crypto1 = encode(sample, shift)
print(f'Cryptotextx of [bold green]{sample}[/bold green] are: [bold cyan]{crypto1}[/bold cyan]')
print(f'Original text: [bold green]{decode(crypto1, shift)}[/bold green]\n')

## Test implementaion 2:

crypto2 = convert(sample, shift, 'encode', string.ascii_uppercase)
print(f'Cryptotexts of [bold green]{sample}[/bold green] (in CAPiTAL CASE) are: '
      f'[bold cyan]{crypto2}[/bold cyan]')
print('Original text: [bold green]'
      f'{convert(crypto2, shift, "decode", string.ascii_uppercase)}[/bold green]\n')

crypto3 = convert(sample, shift, 'encode', string.ascii_lowercase)
print(f'Cryptotexts of [bold green]{sample}[/bold green] (in lower case) are: '
      f'[bold magenta]{crypto3}[/bold magenta]')
print('Original text: [bold green]'
      f'{convert(crypto3, shift, "decode", string.ascii_lowercase)}[/bold green]\n')
