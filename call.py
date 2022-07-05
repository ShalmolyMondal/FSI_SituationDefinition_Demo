from situation_inference import predictTraffic


first_context_attr = input("Enter the first context attribute: ")
weight_attr_first = float(
    input("Enter the weight of {}:".format(first_context_attr)))
fuzzyness_first = input(
    "Enter the fuzziness of {}:".format(first_context_attr))

second_context_attr = input("Enter second context attribute: ")
weight_attr_second = float(
    input("Enter the weight of {}:".format(second_context_attr)))
fuzzyness_second = input(
    "Enter the fuzziness of {}:".format(second_context_attr))


predictTraffic(
    density={"fuzzyness": fuzzyness_first.lower(), "weight": weight_attr_first},
    speed={"fuzzyness": fuzzyness_second.lower(), "weight": weight_attr_second},
)
