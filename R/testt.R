# Library
library(streamgraph)

MyData <- read.csv(file="./TopicOccurencesPerBook.csv", header=TRUE, sep=",")
print(MyData)

# Stream graph with a legend
streamgraph(MyData, key="topic", value="value", date="year" )%>%
  sg_legend(show=TRUE, label="names: ")