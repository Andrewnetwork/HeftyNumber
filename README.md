<p align="center">
  <img src="hn_logo.png">
  <img src="https://travis-ci.org/Andrewnetwork/HeftyNumber.svg?branch=master">
</p>

HeftyNumber is a library built upon Numpy for doing arithmetic in arbitrary bases with arbitrary precision. 

I hope that this library will shape up to be a useful tool for anyone studying number theory, combinatorics, or 
numerical optimization. 

**!This repo is under heavy development, please don't take anything as final or refined!**

## Features
* Effortless base conversion. ✅
* Vector representation of large numbers. ❌
* Ability to count in any base. ❌

## Basic Usage
```
k = 930929309293092930929309293092930929829823832898398239238298323832328398329839283982938928398329839829839829389283
a = HeftyNumber(k,base=10)

# Convert a to base 2. 
print(a.bn(2))

Result:
[[1 1 0 0 0 0 0 1 1 0 0 0 1 1 0 0 0 0 1 1 1 1 1 0 1 1 0 0 0 0 1 0 1 1 0 1 1
  0 1 0 0 0 1 0 0 0 0 0 0 1 1 1 1 0 1 0 1 1 0 0 0 0 1 0 1 0 1 1 0 1 1 1 1 1
  0 0 0 1 0 1 1 1 0 0 1 0 1 1 0 1 1 0 0 1 0 1 1 1 1 1 1 1 1 1 0 1 1 0 0 0 1
  1 0 1 0 0 1 0 0 0 1 0 0 0 0 1 0 1 1 0 1 1 1 1 1 0 0 1 1 0 1 1 0 0 1 0 0 0
  0 1 1 0 1 0 1 1 1 1 1 0 0 1 0 0 1 0 1 1 1 1 0 1 1 1 1 1 0 0 1 1 1 1 0 0 1
  1 0 0 0 1 0 0 0 1 1 1 1 0 1 1 0 0 1 1 0 1 0 1 0 0 1 1 1 0 1 1 0 0 0 0 0 1
  0 0 0 1 1 0 1 1 1 1 1 1 1 0 1 0 0 0 0 0 1 0 0 1 0 1 0 1 1 0 0 1 1 1 0 0 1
  1 0 0 1 1 0 1 0 0 1 1 0 0 0 0 0 0 1 0 0 1 1 0 1 1 0 0 1 0 1 0 0 0 1 1 0 1
  1 1 1 0 1 1 1 0 0 0 1 1 1 1 0 1 0 0 0 0 1 0 0 1 0 1 1 1 0 0 0 1 0 1 1 1 0
  0 1 0 1 0 0 0 1 1 0 1 1 0 1 1 0 0 1 0 1 1 1 0 0 0 1 0 0 0 1 1 1 0 0 1 1 1
  1 1 1 1 0 0 0 1 1]]
```

## Install 
```
pip install git+git://github.com/Andrewnetwork/HeftyNumber
```

## Ratonale & History
In college I wrote a botnet that orchestrated the distributed solution of problems. At its core was a counting mechanism. 
The first conception of the system was used to brute force the cracking of passwords-- the simplest use case I thought of 
for a student application of distributed computing and problem solving. In order to do this, we would count in the base 
of the length of the password character lexicon, and every number in that base could be easily translated to a possible 
password in that character set. More importantly, ranges of numbers would represent password combinations. These password 
ranges would be sent to computers in the botnet whereupon the range of passwords would be tried against some locked file 
-- I designed it so that it would send the password range to an executable, making it more robust than I'm making it seem. 

More coming soon. 