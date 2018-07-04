from functools import partial

def add(a, b, c):
    return a + b + c

def curry_partial(f,*initial_args):
  "Curries and partially applies the initial arguments to the function"

  f = partial(f, *initial_args) if len(initial_args) != 0 else f

  def nfunc(*args):
      if len(args) == 0:
          return f
      return partial(f, *args)
  return nfunc
