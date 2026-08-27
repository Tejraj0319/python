# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

n = 5
for i in range(n):
    pattern = ""
    for j in range(n):
        pattern += "* "
    print(pattern)

# *
# * *
# * * *
# * * * *
# * * * * *

n = 5
for i in range(n):
    pattern = ""
    for j in range(i + 1):
        pattern += "* "
    print(pattern)


# * * * * *
# * * * *
# * * *
# * *
# *

n = 5
for i in range(n):
    pattern = ""
    for j in range(i, n):
        pattern += "* "
    print(pattern)


#   * * * * *
#     * * * *
#       * * *
#         * *
#           *

n = 5
for i in range(5):
    pattern = ""
    for j in range(i + 1):
        pattern += "  "
    for k in range(i, n):
        pattern += "* "
    print(pattern)


#           *
#         * *
#       * * *
#     * * * *
#   * * * * *

n = 5
for i in range(n):
    pattern = ""
    for j in range(i, n):
        pattern += "  "
    for k in range(i + 1):
        pattern += "* "
    print(pattern)
    #      *
    #     * *
    #    * * *
    #   * * * *
    #  * * * * *
    # AND FOR THIS PATTERN JUST REMOVE ONE SPACE FROM ABOVE PATTERN J LOOP

    #           *
    #         * * *
    #       * * * * *
    #     * * * * * * *
    #   * * * * * * * * *

    n = 5
for i in range(n):
    pattern = ""
    for j in range(i, n):
        pattern += "  "
    for k in range(i + 1):
        pattern += "* "
    for l in range(i):
        pattern += "* "
    print(pattern)


# * * * * *
# *       *
# *       *
# *       *
# * * * * *
n = 5
for i in range(n):
    pattern = ""
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            pattern += "* "
        else:
            pattern += "  "
    print(pattern)


# *
# * *
# *   *
# *     *
# * * * * *

n = 5
for i in range(n):
    pattern = ""
    for j in range(n):
        if j == 0 or j == i or i == n - 1:
            pattern += "* "
        else:
            pattern += "  "
    print(pattern)


# * * * * *
# *     *
# *   *
# * *
# *
n = 5
for i in range(n):
    pattern = ""
    for j in range(i, n):
        if j == i or j == n - 1 or i == 0:
            pattern += "* "
        else:
            pattern += "  "
    print(pattern)


#           *
#         * *
#       *   *
#     *     *
#   * * * * *
n = 5
for i in range(n):
    pattern = ""
    for j in range(i, n):
        pattern += "  "
    for k in range(i + 1):
        if k == 0 or i == n - 1 or k == i:
            pattern += "* "
        else:
            pattern += "  "

    print(pattern)
