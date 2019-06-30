import re

# https://www.vogella.com/tutorials/JavaRegularExpressions/article.html
quote = "Search the Candle Rather than cursing the Darkness"

result = re.findall("the", quote)
print(result)
print(type(result))

print()



data = re.sub("the", "a", quote)
print(quote)
print(data)
