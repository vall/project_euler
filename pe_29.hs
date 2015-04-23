#!/usr/bin/env runhaskell

import Data.Set

numbers = Data.Set.fromList [x^y | x <- [2..100], y <- [2..100]]
main = print(Data.Set.size numbers)
