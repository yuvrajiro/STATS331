from pylab import *
rc("font", size=16, family="serif", serif="Computer Sans")
rc("text", usetex=True)

chains1 = loadtxt('../Code/TTest/chains1.txt')
chains2 = loadtxt('../Code/TTest/chains2.txt')
chains3 = loadtxt('../Code/TTest/chains3.txt')

subplot(1,3,1)
plot(chains1[:,0], chains1[:,1], 'b.', markersize=1)
axis('scaled')
xlabel('mu1')
ylabel('mu2')
axis([20, 70, 20, 70])
title('Prior 1')
subplot(1,3,2)
plot(chains2[:,0], chains2[:,1], 'b.', markersize=1)
axis('scaled')
xlabel('mu1')
axis([20, 70, 20, 70])
title('Prior 2')
subplot(1,3,3)
plot(chains3[:,0], chains3[:,1], 'b.', markersize=1)
axis('scaled')
xlabel('mu1')
axis([20, 70, 20, 70])
title('Prior 3')
savefig('ttest.pdf', bbox_inches='tight')
show()
