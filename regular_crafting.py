from crafting_functions import reseting, total, c_artifact, c_amethyst, c_elementstone, c_bronze, c_fire, c_firestone, c_gold, c_metal, c_necklace, c_needles, c_orb, c_pendant, c_ribbon, c_silver, c_sparkles, c_string, c_water, c_waterstone, c_wood

items = ""
num = ""

while items != "end":
  items = input("item to craft: ")
  if items == "end":
    continue
  elif items == "total":
    total()
    print("")
    continue
  elif items == "reset":
    reseting()
    print("")
    continue
  else:
    num = int(input("number of item to craft: "))
  match items:
    case str("artifact"): c_artifact(num)
    case str("elementstone"): c_elementstone(num)
    case str("firestone"): c_firestone(num)
    case str("waterstone"): c_waterstone(num)
    case str("fire"): c_fire(num)
    case str("water"): c_water(num)
    case str("orb"): c_orb(num)
    case str("necklace"): c_necklace(num)
    case str("pendant"): c_pendant(num)
    case str("amethyst"): c_amethyst(num)
    case str("gold"): c_gold(num)
    case str("silver"): c_silver(num)
    case str("bronze"): c_bronze(num)
    case str("sparkles"): c_sparkles(num)
    case str("needles"): c_needles(num)
    case str("metal"): c_metal(num)
    case str("ribbon"): c_ribbon(num)
    case str("wood"): c_wood(num)
    case str("string"): c_string(num)
    case default: print("error")

