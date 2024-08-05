lambda = 1;
b = 1/lambda;

x = 0:0.01:2;
y1 = gampdf(x,1,b);
y2 = gampdf(x,2,b);
y3 = gampdf(x,3,b);


plot(x,y1)
hold on
plot(x,y2)
plot(x,y3)
hold off
xlabel('Observation')
ylabel('Probability Density')
legend('a = 1','a = 2','a = 3')
