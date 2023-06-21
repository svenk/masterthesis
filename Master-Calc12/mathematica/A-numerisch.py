#!/usr/bin/python

# Enstanden nach "Symmetrie und Polstellen.nb"
from pylab import *
ion() 


# lattice extend (unitless)
L = 5.

# points to work on in the lattice
N = 10

# Funktion und analytisch bestimmt - mit z.
#h = lambda z: 1. / (1. + 1. / z**2.)
#dh = lambda z: 2. / ((1. + 1. / z**2.)**2. * z**3.)

h = lambda x: x**2. / (x**2. + 1.)
dh = lambda x: 2.*x / (1. + x**2.)**2.

# radial lattice maximum
Lr = sqrt(3 * L**2)

# testfunktion, symmetrisch
dh = lambda x: x**2. / (x**2. + 1) + (x-Lr)**2. / ((x-Lr)**2. + 1)

# Radius where dh(R) is evaluated:
# norm() ist hier seltsam
r = vectorize(lambda x,y,z: sqrt(x*x+y*y+z*z))

dh3 = vectorize(lambda *coords: dh(r(*coords)))



axis = linspace(0, L, N)
X,Y,Z = meshgrid(axis, axis, axis)

# a list of radii
radii = r(X,Y,Z)  # shape: (N,N,N)
unique_radii, indices = unique(radii, return_index=True)

# unique_radii ist nun eine geordnete Liste aller moeglichen Radii [0,1,sqrt(2),sqrt(3),...]
# indices ist deren Position im flatten(radii)
indices3d = [unravel_index(n, radii.shape) for n in indices]
radii_values =  lambda data: array([data[t] for t in indices3d])

# the 3d evaluated data
ortsraum = dh3(X,Y,Z)

# display a cut
def plot_ortsraum():
	figure()
	x=linspace(0,Lr,100)
	plot(x, dh(x), label="$h'(r)$ Holo")
	plot(radii[0,0], ortsraum[0,0], "gs", markersize=12, label="Naive X axis")
	plot(unique_radii, dh(unique_radii), "ro", label="All roots in lattice (Antje)")
	title("Ortsraum mit Diskretisierungs-Cuts (Naiv und Antje)")
	legend()
	xlabel("$r / \ell$")
plot_ortsraum()

# make a fourier transformation
impulsraum = fftn(ortsraum)

def plot_impulsraum():
	figure()
	subplot(2,1,1); ylabel("Realteil")
	title("Impulsraum")
	plot(radii[0,0], real(impulsraum[0,0]), "gs-", markersize=12, label="Real X axis")
	plot(unique_radii, real(radii_values(impulsraum)), "ro-", label="All Real X axis")
	legend()
	subplot(2,1,2); ylabel("Imaginaerteil")
	plot(radii[0,0], imag(impulsraum[0,0]), "gs-", markersize=12, label="Imaginary X axis")
	plot(unique_radii, imag(radii_values(impulsraum)), "ro-", label="All Imag X axis")
	legend()
plot_impulsraum()

