import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 11)

X, Y = np.meshgrid(x,x)

X = X.ravel()
Y = Y.ravel()
W = np.ones(121)

pts = np.vstack([X, Y, W])

tx, ty = 0,0
# T_to_origin = np.array([[1,0,-tx],
#                         [0,1,-ty],
#                         [0,0,1]])

# T_back =  np.array([[1,0,tx],
#                     [0,1,ty],
#                     [0,0,1]])

# cos = np.cos(np.pi/6)
# sin = np.sin(np.pi/6)

# R = np.array([[cos,-sin,0],
#               [sin,cos,0],
#               [0,0,1]])

# a,b,c,d = 1, 0.5, 0, 1
# A = np.array([[a,b,tx],
#               [c,d,ty],
#               [0,0,1]])

P =  T_back =  np.array([[1,0,0],
                         [0,1,0],
                         [0.05,0,1]])

H = P


new = H@pts

new = new/new[2]


plt.scatter(pts[0,:], pts[1, :], s= 5, label= 'original')
plt.scatter(new[0,:], new[1, :], s= 5, label= 'projective')
plt.legend()
plt.axis('equal')
plt.savefig('stages/1-geometry/results/projective.png')
plt.show()