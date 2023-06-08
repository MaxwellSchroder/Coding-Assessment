data Expr a = Var a | Add (Expr a) (Expr a) deriving Show

instance Functor Expr where
    -- fmap :: (a->b) -> Expr a -> Exp b
    fmap f (Var a) = Var $ f a
    fmap f (Add x y) = Add (f <$> x) (f <$> y)

instance Applicative Expr where
    -- pure :: a -> Expr a
    pure a = Var a
    -- <*> :: Expr (a -> b) -> Expr a -> Expr b
    (<*>) (Var f) ea = f <$> ea
    (<*>) (Add ef eg) ea = Add (ef <*> ea) (eg <*> ea)

instance Monad Expr where
    -- return :: a -> Expr a
    return = pure
    -- >>= :: Expr a -> (a -> Expr b) -> Expr b
    (>>=) (Var ex) foo = foo ex
    (>>=) (Add ex ey) foo = Add (ex >>= foo) (ey >>= foo)


convert :: Expr (Maybe a) -> Maybe (Expr a)
    --that returns Nothing when an expression contains Nothing. 
    --Otherwise, return a new expression replacing each Just a with a
convert (Var a) = a >>= (\x -> Just $ Var x)
convert (Add ma mb) = do
    x <- convert ma
    y <- convert mb
    return $ Add x y


type State = Int
newtype ST a = S (State -> (a, State))

apply :: ST a -> State -> (a, State)
apply (S st) x = st x


instance Functor ST where
  -- fmap :: (a -> b) -> ST a -> ST b
  fmap f st = do
    state <- st
    return (f state)

instance Applicative ST where
  -- pure :: a -> ST a
  pure x = S (\s -> (x,s))
  -- (<*>) :: ST (a -> b) -> ST a -> ST b
  stf <*> stx = do
    f <- stf
    x <- stx
    return (f x)