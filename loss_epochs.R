#Loss versus epochs



x<- c(0, 1, 2, 3, 4, 5 ,6, 7, 
     26, 30, 32, 43, 46, 48,  56, 58,
     75, 87, 90, 97, 113, 131, 143,
     147 )
y<-c(3.5, 2.6, 2.1, 2.06, 2.00, 1.947, 1.904, 1.86,    
     1.62, 1.59, 1.54, 1.53, 1.52, 1.55,  1.469,1.466,
     1.437, 1.42, 1.418, 1.411, 1.395, 1.385, 1.38,
     1.377  )
plot(x, y, type="l", lwd = 4, xlab="epoch number", ylab="loss", main="Loss versus epochs")



#Entropy versus epochs

xx<- c(1,2,26,30,43,56,75,90,113,138,146,148, 150)
yy<-c(3.694,4.04,3.989,4.057,4.01,3.98,4.06,3.93,3.98,3.93,4.068,4.0485, 4.184)
plot(xx, yy, type="l", lwd = 4, xlab="epoch number", ylab="loss", main="Loss versus epochs")
abline(h = 4.184, lwd="6", col="red")
