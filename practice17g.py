import re                               # re -> Regular Expression
# Regular Expression Symbols

quote = "Search the Candle rather than Cursing the Darkness"

result = re.search("the", quote)     # shows only the first the ... starts form starting and ends where the word is found

print(result)
print(type(result))
