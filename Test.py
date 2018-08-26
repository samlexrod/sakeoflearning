def bacon(bake_beans):
    bake_beans.append("I don't like Spam")

spam = [1, 2, 3]
bacon(spam[:])
print(spam)