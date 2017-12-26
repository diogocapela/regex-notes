# regex-notes

### Character class
```
\d                     	Digit characters (numbers)
\w                     	Word characters (letters and numbers)
\s                     	Space characters (space, tab, \n)

\D                     	Non-digit
\W                     	Non-word
\S                     	Non-space
```

### Put characters inside []
```
[aeiouAEIOU]           	Matches vowels
[^aeiouAEIOU]          	Matches non-vowels
[0-9a-zA-Z]            	Matches all numbers and letters (same as \w)
```

### Punctuation characters need an escape character
```
.						\.
*						\*
( or )					\( or \)
^						\^
$						\$
|						\|
?						\?
\						\\
[ or ]					\[ or \]
+						\+
{ or }					\{ or \}
```