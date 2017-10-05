%pylab inline

s = [] # visszaverodes tavolsaga
s *= 2 # ketszer jarja be
s += 0.18 # a tanyerban megtett ut ketszerese

d_s = []	# ut hibaja

t = []		# ido
d_t = []	# ido hibaja
t *= 10**(-3) # microsec-ben van megadva
d_t *= 10**(-3)

plot(ido, ut, '+')

# illesztes:
from scipy.optimize import curve_fit

def linear(x, a, b):
	return a*x + b

popt, pcov = curve_fit(linear, t, s)
perr = sqrt(diag(pcovwe))

poptwe, pcovwe = curve_fit(linear, t, s, p0=popt, sigma=d_t)
perrwe = sqrt(diag(pcovwe))

figsize(12,8)

tt = linspace(0.0, 0.045, 1000)

plot(tt, lin(tt, *poptwe)
