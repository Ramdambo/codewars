lit2num = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
num2lit = { y: x for x, y in lit2num.items()}

def decode(roman):
  """complete the solution by transforming the roman numeral into an integer"""
  nums = [literals[x] for x in roman]
  result = 0
  print nums
  for i, n in enumerate(nums):
      if i >= len(nums) - 1:
          result += n
      elif n >= nums[i + 1]:
          result += n
      else:
          result -= n
  return result


def encode(number):
    nstr = reversed(str(number))
    lit = []
    for e, n in enumerate(nstr):
        l, n = "", int(n)
        if n < 5:
            if n < 4:
                l = num2lit[10 ** e] * n
            else:
                l = num2lit[10 ** e] + num2lit[5 * 10 ** e]
        else:
            r = n % 5
            if r < 4:
                l = num2lit[5 * 10 ** e] + num2lit[10 ** e] * r
            else:
                l = num2lit[10 ** e] + num2lit[10 ** (e + 1)]
        lit.append(l)
    return "".join(reversed(lit))
