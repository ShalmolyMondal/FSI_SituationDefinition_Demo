from membership_functions import generateDensity, generateSpeed
import pandas as pd


def predictTraffic(density, speed=None):

    fuzzyness_density = density["fuzzyness"]
    weight_density = density["weight"]

    fuzzyness_speed = speed["fuzzyness"]
    weight_speed = speed["weight"]

    density_membership_data = generateDensity(fuzzyness_density)
    speed_membership_data = generateSpeed(fuzzyness_speed)

    generated_memberfunctiondata_density = list(density_membership_data["member_data"])
    generated_memberfunctiondata_speed = list(speed_membership_data["member_data"])
    if (
        len(generated_memberfunctiondata_density) == 1
        and len(generated_memberfunctiondata_density) == 1
    ):
        certainity = (
            generated_memberfunctiondata_density[0] * weight_density
            + generated_memberfunctiondata_speed[0] * weight_speed
        )
        if fuzzyness_density == "low" and fuzzyness_speed == "normal":
            print(
                "situation low traffic is occuring with {} certainity".format(
                    certainity
                )
            )
        elif fuzzyness_density == "normal" and fuzzyness_speed == "normal":
            print(
                "situation moderate traffic is occuring with {} certainity".format(
                    certainity
                )
            )
        elif fuzzyness_density == "high" and fuzzyness_speed == "slow":
            print(
                "situation high traffic is occuring with {} certainity".format(
                    certainity
                )
            )
        else:
            print("Situation rule not specified")
    else:
        certainity = None

    pd.DataFrame(
        data={
            "density": density_membership_data["density_data"],
            "speed": speed_membership_data["speed_data"],
        }
    ).to_csv("Data_Export.csv", sep="\t")
