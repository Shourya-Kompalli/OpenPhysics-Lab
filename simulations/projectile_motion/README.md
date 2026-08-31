# Projectile Motion

This simulation models the motion of a projectile launched at an initial speed and angle under constant gravitational acceleration.

Air resistance is not included.

## Mathematical Model

The initial velocity is separated into horizontal and vertical components:

$$
v_x = v_0 \cos(\theta)
$$

$$
v_y = v_0 \sin(\theta)
$$

The position of the projectile at time \(t\) is:

$$
x(t) = v_x t
$$

$$
y(t) = v_y t - \frac{1}{2}gt^2
$$

where:

* \(v_0\) is the initial speed
* \(\theta\) is the launch angle
* \(g\) is gravitational acceleration
* \(t\) is time

The simulation uses:

$$
g = 9.81\text{ m/s}^2
$$

## Parameters

The default simulation uses:

| Parameter     | Value | Unit    |
| ------------- | ----: | ------- |
| Initial speed |  20.0 | m/s     |
| Launch angle  |  45.0 | degrees |
| Gravity       |  9.81 | m/s²    |

## Expected Results

For the default parameters, the theoretical values are approximately:

* Flight time: 2.884 s
* Maximum height: 10.194 m
* Horizontal range: 40.775 m

The trajectory should form a parabola.

## Running the Simulation

From the root of the repository, run:

```text
python simulations/projectile_motion/projectile.py
```

The program prints the calculated flight time, maximum height, and range and displays the trajectory.

## Assumptions

The model assumes:

* Constant gravitational acceleration
* No air resistance
* Flat ground
* A point-like projectile
* No wind
* Newtonian mechanics

## Validation

The simulation uses the analytical equations of projectile motion directly.

The calculated flight time can be checked using:

$$
T = \frac{2v_0\sin(\theta)}{g}
$$

The maximum height can be checked using:

$$
H = \frac{v_0^2\sin^2(\theta)}{2g}
$$

The horizontal range can be checked using:

$$
R = \frac{v_0^2\sin(2\theta)}{g}
$$

These equations provide a reference for validating the implementation.

## Limitations

This is an idealized model.

Real projectiles are affected by factors such as air resistance, wind, changing atmospheric conditions, and variations in gravitational acceleration.

## Possible Extensions

Future contributions could add:

* Air resistance
* Different gravitational fields
* Interactive parameters
* Numerical integration
* Analytical-versus-numerical error analysis
* Additional visualization
