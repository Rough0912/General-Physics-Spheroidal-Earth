import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

A_EQ = 6_378_137.0
OMEGA = 7.292e-5
E_EARTH = 0.08182

def rho_of_theta(theta, a, e):
    return a * np.cos(theta) / np.sqrt(1.0 - e**2 * np.sin(theta)**2)

def merid_radius(theta, a, e):
    return a * (1.0 - e**2) / (1.0 - e**2 * np.sin(theta)**2)**1.5

def equations_of_motion(t, y, a, e):
    theta, phi, v_theta, v_phi = y
    a_cor_theta = +2.0 * OMEGA * np.sin(theta) * v_phi
    a_cor_phi = -2.0 * OMEGA * np.sin(theta) * v_theta
    rho = rho_of_theta(theta, a, e)
    if e == 0.0:
        a_grav_theta = -(OMEGA**2) * rho * np.sin(theta)
    else:
        a_grav_theta = 0.0
    R = merid_radius(theta, a, e)
    return [v_theta / R, v_phi / rho, a_cor_theta + a_grav_theta, a_cor_phi]

def simulate(e, theta0_deg, phi0_deg, v_north, v_east, hours, n=6000):
    y0 = [np.radians(theta0_deg), np.radians(phi0_deg), v_north, v_east]
    t_end = hours * 3600.0
    t_eval = np.linspace(0, t_end, n)
    sol = solve_ivp(equations_of_motion, [0, t_end], y0, t_eval=t_eval,
                    args=(A_EQ, e), rtol=1e-9, atol=1e-9, method="RK45")
    return sol.t, np.degrees(sol.y[0]), np.degrees(sol.y[1]), np.sqrt(sol.y[2]**2 + sol.y[3]**2)

def main():
    launch = dict(theta0_deg=40.0, phi0_deg=0.0, v_north=50.0, v_east=0.0, hours=24)

    t_sph, lat_sph, lon_sph, spd_sph = simulate(e=0.0, **launch)
    t_spd, lat_spd, lon_spd, spd_spd = simulate(e=E_EARTH, **launch)

    print("SPHERE   latitude range:  %.1f to %.1f deg, speed %.0f-%.0f m/s"
          % (lat_sph.min(), lat_sph.max(), spd_sph.min(), spd_sph.max()))
    print("SPHEROID latitude range:  %.1f to %.1f deg, speed %.0f-%.0f m/s"
          % (lat_spd.min(), lat_spd.max(), spd_spd.min(), spd_spd.max()))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
    ax1.plot(lon_sph, lat_sph, color="#E24B4A", lw=1.5)
    ax1.plot(lon_sph[0], lat_sph[0], "ko", ms=6)
    ax1.set_title("SPHERE  (e = 0)\nzig-zag, drifts to equator")
    ax1.set_xlabel("longitude [deg]")
    ax1.set_ylabel("latitude [deg]")
    ax1.grid(alpha=0.3)
    ax2.plot(lon_spd, lat_spd, color="#065A82", lw=1.5)
    ax2.plot(lon_spd[0], lat_spd[0], "ko", ms=6)
    ax2.set_title("SPHEROID  (e = 0.082)\ntight inertial loops")
    ax2.set_xlabel("longitude [deg]")
    ax2.set_ylabel("latitude [deg]")
    ax2.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("trajectories.png", dpi=150)
    print("saved trajectories.png")

    m = 0.16
    ke_sph = 0.5 * m * spd_sph**2
    ke_spd = 0.5 * m * spd_spd**2
    fig2, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(t_sph / 3600, ke_sph, color="#E24B4A", lw=1.8,
            label="SPHERE  (varies -> KE not conserved in rotating frame)")
    ax.plot(t_spd / 3600, ke_spd, color="#065A82", lw=2.0,
            label="SPHEROID  (flat -> KE conserved in rotating frame)")
    ax.set_xlabel("time [hours]")
    ax.set_ylabel("rotating-frame kinetic energy [J]")
    ax.set_title("Verification of Eq. 52: which frame conserves kinetic energy")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("energy_check.png", dpi=150)
    print("saved energy_check.png")

    plt.show()

if __name__ == "__main__":
    main()
