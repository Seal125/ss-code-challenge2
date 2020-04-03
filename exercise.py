# ```
# p - return the sub string that all the words have in common
# e- Input: ["flower","flow","flight"]
# Output: "fl"
# d - string in an array
# a - have one loop
# check same indexes of each string
# when an index doesnt match for all three stop the loop
# if indexes match for all three append that matching index into an array
#
# ```

def prefix(array):
    output = []
    for i in range(len(array[0])):
        output.append(array[0][i])
        if array[i][i] == output[i]:
            continue
        else:
            output.pop()
            return ''.join(output)
    output.pop()
    return ''.join(output)

print(prefix(["flower","flow","flight"]));
