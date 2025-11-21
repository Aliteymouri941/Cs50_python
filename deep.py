result=["42","forty-two","forty two"]
question = input("what is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
if question in result:
    print("yes")
else:
    print("no")