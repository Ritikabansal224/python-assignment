def c(show):
    count = 0
    for name in show:
        if name == "Emma":
            count = count + 1
        return count

count = c("Emma is a good developer. Emma is also a writer")
print(count)