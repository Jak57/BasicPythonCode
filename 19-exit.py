import sys

if len(sys.argv) != 2:
    print("missing command-line argument")
    # as we're not in main so cann't return 1
    sys.exit(1)
else:
    print("Hello, " + sys.argv[1])

sys.exit(0)