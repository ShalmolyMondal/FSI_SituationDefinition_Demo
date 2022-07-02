from fuzzy_set import (
    speed_high,
    speed_low,
    speed_normal,
    density_low,
    density_high,
    density_normal,
)

import numpy as np
import skfuzzy as skf


def generateDensity(fuzziness):
    if fuzziness == "low":
        lower_bound = density_low[0]
        upper_bound = density_low[1]
        x = np.random.randint(lower_bound, upper_bound, size=10)
        print(x)
        selected_data_user = int(input("Select a density from the above values: "))

        if selected_data_user in x:
            member_density = skf.trapmf(np.array([selected_data_user]), [0, 0, 15, 20])
        else:
            print("Invalid selection,calculating randomly")
            member_density = skf.trapmf(x, [0, 0, 15, 20])
    elif fuzziness == "normal":
        lower_bound = density_normal[0]
        upper_bound = density_normal[1]
        x = np.random.randint(lower_bound, upper_bound, size=10)
        print(x)
        selected_data_user = int(input("Select a density from the above values: "))

        if selected_data_user in x:
            member_density = skf.trapmf(
                np.array([selected_data_user]), [18, 20, 35, 40]
            )
        else:
            print("Invalid selection,calculating randomly")
            member_density = skf.trapmf(x, [18, 20, 35, 40])
    elif fuzziness == "high":
        lower_bound = density_high[0]
        upper_bound = density_high[1]
        x = np.random.randint(lower_bound, upper_bound, size=10)
        print(x)
        selected_data_user = int(input("Select a density from the above values: "))

        if selected_data_user in x:
            member_density = skf.trapmf(
                np.array([selected_data_user]), [35, 40, 55, 60]
            )
        else:
            print("Invalid selection,calculating randomly")
            member_density = skf.trapmf(x, [35, 40, 55, 60])

    return {
        "density_data": x,
        "input_selected_by_user": selected_data_user,
        "member_data": member_density,
    }


def generateSpeed(fuzziness):
    if fuzziness == "low":
        lower_bound = speed_low[0]
        upper_bound = speed_low[1]
        x = np.random.randint(lower_bound, upper_bound, size=10)
        print(x)
        selected_data_user = int(input("Select a speed from the above values: "))

        if selected_data_user in x:
            member_speed = skf.trapmf(np.array([selected_data_user]), [0, 0, 35, 45])
        else:
            print("Invalid selection,calculating randomly")
            member_speed = skf.trapmf(x, [0, 0, 35, 45])

    elif fuzziness == "normal":
        lower_bound = speed_normal[0]
        upper_bound = speed_normal[1]
        x = np.random.randint(lower_bound, upper_bound, size=10)
        print(x)
        selected_data_user = int(input("Select a speed from the above values: "))

        if selected_data_user in x:
            member_speed = skf.trapmf(np.array([selected_data_user]), [40, 45, 75, 80])
        else:
            print("Invalid selection,calculating randomly")
            member_speed = skf.trapmf(x, [40, 45, 75, 80])
    elif fuzziness == "high":
        lower_bound = speed_high[0]
        upper_bound = speed_high[1]
        x = np.random.randint(lower_bound, upper_bound, size=10)
        print(x)
        selected_data_user = int(input("Select a speed from the above values: "))

        if selected_data_user in x:
            member_speed = skf.trapmf(
                np.array([selected_data_user]), [75, 85, 115, 130]
            )
        else:
            print("Invalid selection,calculating randomly")
            member_speed = skf.trapmf(x, [75, 85, 115, 130])

    return {
        "speed_data": x,
        "input_selected_by_user": selected_data_user,
        "member_data": member_speed,
    }
