# Library
library(streamgraph)

# Create data:
year=rep(seq(1990,2016) , each=10)
name=rep(letters[1:10] , 27)
value=sample( seq(0,1,0.0001) , length(year))
data=data.frame(year, name, value)

# Stream graph with a legend
streamgraph(data, key="name", value="value", date="year" )%>%
  sg_legend(show=TRUE, label="names: ")