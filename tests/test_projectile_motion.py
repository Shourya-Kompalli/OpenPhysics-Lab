import math

from simulations.projectile_motion.projectile import calculate_trajectory


def test_flight_time():
    speed = 20.0
    angle = 45.0
    gravity = 9.81

    times, _, _ = calculate_trajectory(
        speed,
        angle,
        gravity,
    )

    expected = (2 * speed * math.sin(math.radians(angle))) / gravity

    assert math.isclose(times[-1], expected, rel_tol=1e-6)


def test_maximum_height():
    speed = 20.0
    angle = 45.0
    gravity = 9.81

    _, _, y_values = calculate_trajectory(
        speed,
        angle,
        gravity,
    )

    expected = (
        speed**2
        * math.sin(math.radians(angle))**2
        / (2 * gravity)
    )

    assert math.isclose(max(y_values), expected, rel_tol=1e-3)


def test_range():
    speed = 20.0
    angle = 45.0
    gravity = 9.81

    _, x_values, _ = calculate_trajectory(
        speed,
        angle,
        gravity,
    )

    expected = (
        speed**2
        * math.sin(math.radians(2 * angle))
        / gravity
    )

    assert math.isclose(x_values[-1], expected, rel_tol=1e-6)
