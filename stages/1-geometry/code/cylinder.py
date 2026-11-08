import numpy as np


def screen_to_view(x,y,R,D):
    """x, y: 화면 중심 기준 좌표(px). 반환 u, v: 시청자 이미지 좌표(px)."""
    theta = x/R
    X = R*np.sin(theta)
    Z = R - R*np.cos(theta)
    u = D*X/(Z+D)
    v = D*y/(Z+D)
    return u, v

def view_to_screen(u,v,R,D):
    a = D*R
    b = u*R
    c = u*(R+D)
    r = np.sqrt(a**2+b**2)
    phi = np.arctan2(b,a)
    theta = np.arcsin(c/r) - phi
    x = R*theta
    Z = R*(1-np.cos(theta))
    y = (v*(Z+D))/D
    return x, y



if __name__ == "__main__":
    tx = np.linspace(-200,200,2000)
    ty = np.linspace(-200,200,2000)
    u,v = screen_to_view(tx,ty,300,1000)
    x,y = view_to_screen(u,v,300,1000)
    error_x = abs(tx-x)
    error_y = abs(ty-y)
    print(error_x.max(), error_y.max())


    # print(screen_to_view(0,0,10,10))
    # print(screen_to_view(1,0,10,10))
    # print(screen_to_view(200,1,300,1000))