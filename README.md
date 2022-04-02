<h1>hangman.py</h1>

<p style="text-align:right">Revision for 0.0.1</p>

### List of contents:
1. Brief Introduction
2. Console Example
3. Legal (MIT license)

<b><h2 style="text-align:center">Brief Introduction</h3></b>

---

A <i>hangman</i> game application written in Python, with a customisable TOML file to filter for random <i>word</i> and <i>defenition</i> keys from an API response (as specified by a URL).

<b><h2 style="text-align:center">Console Example</h3></b>

---

```
{hangman.py}
Word: _ e v e s _
~ Reinstate; reinvest  

- lives remaining: 2
- letters guessed: p a e v o s
Guess (a letter or the word): r
```

```
{hangman.py}
Word: r e v e s _
~ Reinstate; reinvest  

- lives remaining: 1
- letters guessed: p a e v o s r
Guess (a letter or the word): revest

Word: revest
YOU WIN | lives remaining: 1
```

<b><h2 style="text-align:center">License (MIT)</h3></b>

---
<br>

|Permissions|Conditions|Limitations|
|---|---|---|
|Commercial use|License and copyright notice|Liability|
|Distribution||Warranty|
|Modification|||
|Private use|||

```
MIT License

Copyright (c) 2022 Ivan (GitHub: ivanl-exe, E-Mail: ivan.exe@pm.me)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```