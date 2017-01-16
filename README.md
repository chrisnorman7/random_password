# random_password
Create a random password.

## Usage
```
>>> from random_password import random_password
>>> random_password()
'Vs6ieNxR'
>>> random_password(length=16)
'BdeBxlOdSboH59zI'
>>> random_password(characters='hello world')
'rrelhodd'
>>> random_password(length=4, characters=['hello', 'there', 'my', 'world'])
'hellomytherethere'
```
