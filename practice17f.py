import re                               # re -> Regular Expression
# Regular Expression Symbols

quote = "Search the Candle rather than Cursing the Darkness"

result = re.search("Candle", quote)

print(result)
print(type(result))
