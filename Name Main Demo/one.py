print("hello")


# if __name__ == "main": means that the code here is being run direct


def func():
	print("FUNC() in ONE.PY")

print("Top level in one.py")


if __name__ == "__main__":
	print("one.py is being run directly")
else:
	print("one.py is being imported")