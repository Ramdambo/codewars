import re

brackets_exp = re.compile(r"[\[\[{](\w+)[\]\]}](\d?)")
matches = re.findall(brackets_exp, "K4[ON(SO3)2]2")

print(matches)
