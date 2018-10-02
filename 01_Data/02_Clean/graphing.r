data = read.csv("appended.csv")

bldata = data[ which(data$Time=='1'), ]
aggdata <-aggregate(bldata, by=list(bldata$Treat), FUN=mean, na.rm=TRUE)
jpeg("../../02_output/balance.jpg", width = 500, height = 500)
barplot(with(aggdata, setNames(Income, Treat)), main = "Income Balance", xlab = "Treatment", ylab = "Income")
dev.off()