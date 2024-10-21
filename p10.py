#Dictionary in python
power = {
    "halfling vampire":200,
    "vampire":400,
    "Nobal vapire": 600,
    "loard of vampire":1000,
    "King of vampire":1500,
    "Original":3000,
}
#It is mutable
print(power,"\n",type(power))

print("Power of vampire:",power["vampire"])

#Method of dictionary
print(power.items(),"\n")
print(power.keys(),"\n")
print(power.values(),"\n")

power.update({"Original":4000,"King of vampire":2000})
print(power)

print(power.get("Monster"))
# print(power.get["Monster"])
# #[] shows the error in dictionary while () gives none when value does not exit in dictionary
print(power.get("loard of vampire"))