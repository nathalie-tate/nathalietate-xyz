import System.Environment

main = do
  args <- getArgs
  putStrLn $ reverse (args !! 0)
