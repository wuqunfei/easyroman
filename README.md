# easyroman

####A easy Integer into Roman numerals converter library.
===

### Knowledge and Algorithm

1. Roman numerals 
2. Context free grammar
3. The roman numerals logic can be express by Context free grammar.
4. Documents in modual doc and following links as Reference:
	1. [WIKI of Roman Numberls](http://en.wikipedia.org/wiki/Roman_numerals)
	
    2. [WIKI of Context Free Grammer](http://en.wikipedia.org/wiki/Context-free_grammar)
    
    3. [Roman Numbers into Context free grammar](http://www.cs.bath.ac.uk/~occ/comp0029/roman_numerals.shtml)
    
### Install
```
unzip easyroman.zip
cd easyroman
sudo python setup.py install

```


### Usages
```
import easyroman
easyroman.to_roman(12)    ## return 'XII'
easyroman.to_roman(3999)  ## return 'MMMCMXCIX'

```

### Limits

Roman numerals, as used today, are based on seven standard symbols.

| Symbol   |      Value    |
|----------|:-------------:|
|I 	|1|
|V 	|5|
|X 	|10|
|L 	|50|
|C 	|100|
|D 	|500|
|M 	|1,000|


This application is not includes extension.  [Big Roman Number](http://www.legionxxiv.org/numerals/)

| Symbol   |      Value    |
|----------|:-------------:|
|i 	|1,000|
|v 	|5,000|
|x 	|10,000|
|l 	|50,000|
|c 	|100,000|
|d 	|500,000|
|m 	|1,000,000|

So the biggest number of roman is MMMCMXCIX(3999). 1 <= x <= 3999. Because, in a few specific cases,[2] to avoid
four characters being repeated in succession (such as IIII or XXXX) these can be reduced using subtractive notation as follows,
so the biggest MMMM is not allowed in my application. MMMM is 4000.


