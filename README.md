# Forces and Conservation Laws on our Spheroidal Earth

This repository contains the simulation code and the final group project report for **General Physics I** at DGIST (June 2026).

The project models and visualizes the motion of a frictionless puck on a rotating Earth, comparing trajectories on a perfect sphere versus an oblate spheroid. It is based on the pedagogical framework presented in Edwards & Edwards (2021).

## Group Members
* [202311102] Myoungjin Song
* [202611139] Seoungmin Yoon
* [202611064] Taeyoon Kim
* [202611234] Yedam Han
* **Instructor:** Dr. Deniz Olgu Devecioğlu

## Key Features
* **Spherical vs. Spheroidal Earth Models:** Simulates how the $f \approx 0.003$ flattening alters surface dynamics.
* **Force Visualization:** Calculates and applies the Coriolis force and apparent gravitational force in geodetic coordinates.
* **Trajectory Plotting:** Replicates the zigzag motion (sphere) and inertial loops (spheroid) for a Northern Hemisphere launch.
* **Conservation Check:** Verifies that kinetic energy is conserved in the rotating frame for the spheroid but not for the sphere (paper Eq. 52).

## Simulation Outputs
When you run the script, it generates and saves these files in the project directory:
* `trajectories.png` — comparison of the puck's path on a sphere vs. a spheroid.
* `energy_check.png` — rotating-frame kinetic energy over time (conservation check).

## Requirements
Python 3.8+ and the following libraries:
* `numpy` (numerical and vector calculations)
* `scipy` (solving the equations of motion)
* `matplotlib` (plotting trajectories and graphs)

Install them with:
```bash
pip install numpy scipy matplotlib
```

## How to Run
1. Clone this repository:
```bash
git clone https://github.com/Rough0912/General-Physics-Spheroidal-Earth.git
```
2. Move into the project folder:
```bash
cd General-Physics-Spheroidal-Earth
```
3. Run the simulation:
```bash
python simulation.py
```

## Reference
Edwards, B. F., & Edwards, J. M. (2021). *Forces and conservation laws for motion on our spheroidal Earth.* American Journal of Physics, 89(9), 830–842. https://doi.org/10.1119/10.0004801
