# Fix f-string with empty expression

example erroneous code:<br>
```Python
hist_to_txt(x, f'{getRmiddleState(State)}_VR_sigmaR_gamma_{}.txt')
```

using the VS Code built-in search-and-replace, in regex mode (`cmd + f`):

regex search:<br>
`(.*)(f'\{getRmiddleState\(State\)\})(.*)\{\}\.txt'\)`

replace-all with:<br>
`$1"{{r}}$3{{}}.txt".format(**{'r': getRmiddleState(State)}))`

after fix:<br>
```Python
hist_to_txt(x, "{{r}}_VR_sigmaR_gamma_{{}}.txt".format(**{'r': getRmiddleState(State)}))
```
