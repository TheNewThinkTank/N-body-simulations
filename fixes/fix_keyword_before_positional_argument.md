# Fix Python arguments

## Resolve Python keyword argument before positional argument error in VS Code

example erroneous code:<br>
`Plt(datalistA_R32[0], 1, x=0, y=3, 'r-o', 0, -52)`

using the VS Code built-in search-and-replace, in regex mode (`cmd + f`):

regex search:<br>
`(.*)(,\sx=\d{1,},\sy=\d{1,})(.*)\)`

replace-all with:<br>
`$1$3$2)`

after fix:<br>
`Plt(datalistA_R32[0], 1, 'r-o', 0, -52, x=0, y=3)`
