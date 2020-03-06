print("This line will be printed.")

msg = "Hello Dear"

print(msg)




def sayblah6times():
  for x in range(6):
    if x > 2:
        print("Number greater than 2")
    else:
        print("Number is less than 2")

sayblah6times()

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["milage"] = 90000
print(thisdict.get("brand"))
print(thisdict)
print("brand" in thisdict)
print (thisdict.keys())
print (thisdict.values())

for (key, value) in thisdict.items():
    print('<option value="{0}">{1}</option>'.format(key, value))
my_data = None

if my_data is None:
    print("No Value")

