import re                               # re -> Regular Expression
# Regular Expression Symbols

quote = "Search the Candle rather than Cursing the Darkness"

result = re.match("Candle", quote)        # Match from starting

print(result)
print(type(result))
