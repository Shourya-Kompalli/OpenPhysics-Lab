import math
import matplotlib.pyplot as plt


def calculate_trajectory(speed, angle_degrees, gravity=9.81, steps=200):
    """Calculate the trajectory of a projectile."""

    angle = math.radians(angle_degrees)

    vx = speed * math.cos(angle)
    vy = speed * math.sin(angle)

    flight_time = (2 * vy) / gravity

    times = [
        i * flight_time / steps
        for i in range(steps + 1)
    ]

    x_values = [
        vx * t
        for t in times
    ]

    y_values = [
        vy * t - 0.5 * gravity * t**2
        for t in times
    ]

    return times, x_values, y_values


def main():
    speed = 20.0
    angle = 45.0
    gravity = 9.81

    times, x_values, y_values = calculate_trajectory(
        speed,
        angle,
        gravity
    )

    print(f"Initial speed: {speed} m/s")
    print(f"Launch angle: {angle} degrees")
    print(f"Gravity: {gravity} m/s²")
    print(f"Flight time: {times[-1]:.3f} s")
    print(f"Maximum height: {max(y_values):.3f} m")
    print(f"Range: {x_values[-1]:.3f} m")

    plt.plot(x_values, y_values)

    plt.xlabel("Horizontal distance (m)")
    plt.ylabel("Height (m)")
    plt.title("Projectile Motion")

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()