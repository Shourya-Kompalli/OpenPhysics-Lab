import math

from simulations.projectile_motion.projectile import calculate_trajectory


def main():
    speed = 20.0
    angle = 45.0
    gravity = 9.81

    times, x_values, y_values = calculate_trajectory(
        speed,
        angle,
        gravity,
    )

    simulated_flight_time = times[-1]
    simulated_max_height = max(y_values)
    simulated_range = x_values[-1]

    analytical_flight_time = (
        2 * speed * math.sin(math.radians(angle)) / gravity
    )

    analytical_max_height = (
        speed**2 * math.sin(math.radians(angle)) ** 2 / (2 * gravity)
    )

    analytical_range = (
        speed**2 * math.sin(math.radians(2 * angle)) / gravity
    )

    flight_time_error = abs(
        simulated_flight_time - analytical_flight_time
    )

    max_height_error = abs(
        simulated_max_height - analytical_max_height
    )

    range_error = abs(
        simulated_range - analytical_range
    )

    print("Projectile Motion Validation")
    print("----------------------------")

    print("Flight time:")
    print(f"  Simulation : {simulated_flight_time:.6f} s")
    print(f"  Analytical: {analytical_flight_time:.6f} s")
    print(f"  Absolute error: {flight_time_error:.6e} s")

    print()

    print("Maximum height:")
    print(f"  Simulation : {simulated_max_height:.6f} m")
    print(f"  Analytical: {analytical_max_height:.6f} m")
    print(f"  Absolute error: {max_height_error:.6e} m")

    print()

    print("Range:")
    print(f"  Simulation : {simulated_range:.6f} m")
    print(f"  Analytical: {analytical_range:.6f} m")
    print(f"  Absolute error: {range_error:.6e} m")


if __name__ == "__main__":
    main()
