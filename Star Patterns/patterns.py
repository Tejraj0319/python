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
    for j in range(i+1):
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
    for j in range(i+1):
        pattern += "  "
    for k in range(i,n):
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
    for k in range(i+1):
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
    for k in range(i+1):
        pattern += "* "
    for l in range(i):
        pattern += "* "
    print(pattern)
