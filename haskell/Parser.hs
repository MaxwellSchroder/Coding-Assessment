module PolyParser (Polynom(..), polynom, parse, Parser) where
import Control.Applicative

{--
Do not import anything.

====
TASK 1
====
Write an instance of show for the Polynom data type that produces *exactly* the 
behaviour in the example.

In particular, only print brackets when necessary.

Note that we're allowing zero coefficients on monos to simplify the parser.

=======
EXAMPLE
=======
> Mono 1 1
x

> Mono 1 0
1

> (m,n,j,k) = (Mono 1 2, Mono 3 4, Mono 5 6, Mono 7 8)
(x^2,3x^4,5x^6,7x^8)

> Add (m) (Add (n) (j))
x^2 + 3x^4 + 5x^6

> Add (Add (m) (n)) (j)
x^2 + 3x^4 + 5x^6

> Mul (Add (m) (n)) (Add (j) (k))
(x^2 + 3x^4)(5x^6 + 7x^8)

> Mul m n
(x^2)(3x^4)

> Mul (Mul m n) j
(x^2)(3x^4)(5x^6)

> Mul m (Mul n j)
(x^2)(3x^4)(5x^6)

====
TASK 2
====

Write a parser
    polynom :: Parser Polynom
for reading the string representation of a polynomial back into the Polynom 
data type.

Use polynom to define an instance of read for the Polynom data type.

=======
EXAMPLE
=======
> (parse polynom) ")("
Nothing

> (parse polynom) "2x^3"

> (parse polynom) "(2x^3)"
Just (Mono 2 3,"")

> (parse polynom) ("0x^2")  -- It's okay to do this
Just (Mono 0 2,"")

> (parse polynom) ("3x^24x^3")
Just (Mul (Mono 3 24) (Mono 1 3),"")

> (parse polynom) "(2x^2+3)(x^3)"
Just (Mul (Add (Mono 2 2) (Mono 3 0)) (Mono 1 3),"")

> (parse polynom) "(1+x^2)+x^3"
Just (Add (Add (Mono 1 0) (Mono 1 2)) (Mono 1 3),"")

> (parse polynom) "1+(x^2+x^3)"
Just (Add (Mono 1 0) (Add (Mono 1 2) (Mono 1 3)),"")

> (parse polynom) "(x)(x^2)+x^3"
Just (Add (Mul (Mono 1 1) (Mono 1 2)) (Mono 1 3),"")

> (parse polynom) "(x)(x)(x)"
Just (Mul (Mono 1 1) (Mul (Mono 1 1) (Mono 1 1)),"")

> (parse polynom) "(((x)))"
Just (Mono 1 1,"")
--}

--  start: DO NOT MODIFY --

type Deg = Integer   -- precondition: always nonnegative.
type Coeff = Integer -- precondition: always nonnegative.

data Polynom = Mono Coeff Deg | Add Polynom Polynom | Mul Polynom Polynom deriving (Eq)

newtype Parser a = P (String -> Maybe (a, String))

instance Functor Parser where
    -- fmap : (a -> b) -> Parser a -> Parser b
    fmap g pa = do
      a <- pa
      return $ g a

instance Applicative Parser where
    -- pure :: a -> Parser a
    pure a = P (\cs -> Just (a,cs))

    -- (<*>) :: Parser (a -> b) -> Parser a -> Parser b
    pg <*> pa = do
      g <- pg
      g <$> pa

instance Monad Parser where
    -- pure :: a -> Parser a
    return v = P (\inp -> Just (v,inp))
    
    -- (>>=) :: Parser a -> (a -> Parser b) -> Parser b
    p >>= f = P $ \cs -> 
        case parse p cs of
          Nothing      -> Nothing
          Just (a, str') -> parse (f a) str'

instance Alternative Parser where
    -- empty :: Parser
    empty = P $ \str -> Nothing

    -- (<|>) :: Parse a -> Parser a -> Parser a
    p <|> q = P $ \cs ->
        case parse p cs of
          Nothing -> parse q cs
          mx -> mx

-- aux function for removing decorator
parse :: Parser a -> String -> Maybe (a, String)
parse (P p) cs = p cs

-- parase one character
item :: Parser Char
item = P $ foo
  where
    foo (c:cs) = Just $ (c, cs)
    foo _ = Nothing

-- parse a char c when P c.
sat :: (Char -> Bool) -> Parser Char
sat p = do
    x <- item
    if p x then return x else empty

-- parse a digit
digit :: Parser Char
digit = sat (\x -> elem x ['0'..'9'])

-- parse the character x
char :: Char -> Parser Char
char x = sat (== x)

-- parse the string xs
string :: String -> Parser String
string [] = return []
string (x:xs) = (\x xs -> x:xs) <$> (char x) <*> (string xs)

-- parse a natural number
nat :: Parser Integer
nat = read <$> (some digit)

-- throw away space
space :: Parser ()
space = (\x -> ()) <$> (many $ char ' ')

-- ignore surrounding whitespace
token :: Parser a -> Parser a
token pa = do
    space
    a <- pa
    space
    return a

-- parse a symbol, ignoring whitespace
symbol :: String -> Parser String
symbol xs = token $ string xs

-- end DO NOT MODIFY --

--data Polynom = Mono Coeff Deg | Add Polynom Polynom | Mul Polynom Polynom deriving (Eq)

instance Show Polynom where
    show (Mono coeff deg)
        | coeff == 0 = ""
        | deg == 0 = show coeff
        | coeff == 1 && deg == 1 = "x"
        | coeff == 1 && deg /= 1 = "x^" ++ show deg
        | deg == 1 && coeff /= 1 = show coeff ++ "x"
        | otherwise = show coeff ++ "x^" ++ show deg
    show (Add p1 p2) = show p1 ++ " + " ++ show p2
    show (Mul p1 p2)
        | isMull p1 && isMull p2 = show p1 ++ show p2
        | isMull p1 = show p1 ++ "(" ++ show p2 ++ ")"
        | isMull p2 = "(" ++ show p1 ++ ")" ++ show p2
        | otherwise = "(" ++ show p1 ++ ")(" ++ show p2 ++ ")"

isMull :: Polynom -> Bool
isMull (Mul _ _) = True
isMull _ = False


polynom :: Parser Polynom
polynom = undefined