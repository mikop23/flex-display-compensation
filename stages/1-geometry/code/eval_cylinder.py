import numpy as np
from cylinder import view_to_screen
from cylinder import screen_to_view

W, H = 400, 300
R = 300
D = 1000

c = np.arange(W)
r = np.arange(H)

cols, rows = np.meshgrid(c,r)

u = cols - (W-1)/2
v = rows - (H-1)/2

x, y = view_to_screen(u,v,R,D)

cx, cy = screen_to_view(x,y,R,D)

map_x = x + (W-1)/2
map_y = y + (H-1)/2

mask = ~np.isnan(map_x) & (map_x>=0) & (map_x<W-1) & (map_y>=0) & (map_y<H-1)

error_distance = np.sqrt((cx-u)**2+(cy-v)**2)

error_distance_mask = error_distance[mask]

print(error_distance_mask.max(), error_distance_mask.mean())