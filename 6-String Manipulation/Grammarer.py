#Turn list into gramatically correct string. Challenge 5

start = ["The", "fox", "jumped", "over", "the", "fence", "."]

end = " ".join(start)
end = end[:-2]+"."

print(end)