# regex-notes

### Character class
```
\d                      Digit characters (numbers)
\w                      Word characters (letters and numbers)
\s                      Space characters (space, tab, \n)

\D                      Non-digit
\W                      Non-word
\S                      Non-space
```

### Put characters inside []
```
[aeiouAEIOU]            Matches vowels
[^aeiouAEIOU]           Matches non-vowels
[0-9a-zA-Z]             Matches all numbers and letters (same as \w)
[\(\)]                  Matches ( or )
```

### Punctuation characters need an escape character
```
.                       \.
*                       \*
( or )                  \( or \)
^                       \^
$                       \$
|                       \|
?                       \?
\                       \\
[ or ]                  \[ or \]
+                       \+
{ or }                  \{ or \}
```

### Specifing quantity
```
\d                      One digit
\d?                     Zero or one digits
\d*                     Zero or more digits
\d+                     One or more digits
\d{3}                   Exactly 3 digits
\d{3,5}                 Between 3 and 5 digits
\d{3,}                  3 or more digits

\d{3}-\d{3}-d{4}        Matches 421-231-0030 for example
```

### Grouping
```
[^aeiou][aeiou]+        Matches something like "taaaaaaaaaaaa"
([^aeiou][aeiou])+      Matches something like "tatatatata"
```

### Comma-formated numbers example
```
Example: 1,231,435,202
One or three digits, followed by zero or more groups of comma-digit-digit-digit

\d{1,3}(,\d{3})*
```

### Online tools
- [regexr.com](https://regexr.com)
- [regex101.com](https://regex101.com)
- [regextester.com](https://www.regextester.com)
- [pyregex.com](http://www.pyregex.com)