from urllib.request import urlopen

# Defining variables to correctly combine multiple JSON files together.
startingBracket = "["
comma = ","
endingBracket = "]"

# Converting Strings to Bytes.
startingBracket = str.encode(startingBracket)
comma = str.encode(comma)
endingBracket = str.encode(endingBracket)

# Reading in the JSON generated by Trello's API (generates bytes). Needs to be converted into an array.
stu1Data = urlopen("https://trello.com/b/uaCT48b5/chronospatial.json").read()
stu2Data = urlopen("https://trello.com/b/rq2mYJNn/public-trello-boards.json").read()

# Combining Byte arrays.
combinedData = startingBracket + stu1Data + comma + stu2Data + endingBracket

# Writing combined Byte array to a file which can be used for analysis.
with open('combinedData.json', 'wb') as f:
    f.write(combinedData)
