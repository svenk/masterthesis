#!/usr/bin/python

# Enstanden nach "Symmetrie und Polstellen.nb"
# Enstanden nach "A-numerisch.py", als simpler Test nur 1d.
from pylab import *
ion() 


# lattice extend (unitless)
# from -L..L
L = 5.

# points to work on in the lattice
N = 12*2


h = lambda x: x**2. / (x**2. + 1.)
dh = lambda x: 2.*x / (1. + x**2.)**2.

# testfunktion, symmetrisch
fun = lambda x: h(x+L) + h(L-x) - 1
dh = vectorize(fun)

X = linspace(-L, L, N, endpoint=False)

ortsraum = dh(X)
ortsraum[0] = 0 # oder so, mit der Hand

# display a cut
def plot_ortsraum():
	figure()
	x=linspace(-L,L,100)
	plot(x, dh(x), label="$h'(r)$ Holo")
	plot(X, ortsraum, "gs", markersize=12, label="Lattice")
	title("Ortsraum 1D (also radial)")
	legend()
	xlabel("$r / \ell$")
plot_ortsraum()

# make a fourier transformation
impulsraum = fft(ortsraum)

def plot_impulsraum():
	figure()
	subplot(2,1,1); ylabel("Realteil")
	title("Impulsraum")
	plot(X, real(impulsraum), "gs-", markersize=12, label="Real X axis")
	#plot(unique_radii, real(radii_values(impulsraum)), "ro-", label="All Real X axis")
	legend()
	subplot(2,1,2); ylabel("Imaginaerteil")
	plot(X, imag(impulsraum), "gs-", markersize=12, label="Imaginary X axis")
	#plot(unique_radii, imag(radii_values(impulsraum)), "ro-", label="All Imag X axis")
	legend()
plot_impulsraum()

