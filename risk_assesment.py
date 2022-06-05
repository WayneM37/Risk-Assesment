#Covid-10 Risk Assesment
age = input("Please answer these questions with Yes or No. \
Are you a cigarette addict older then 75 years old?: ").capitalize()
chronic = input("Do you have a severe chronic disease?: ").capitalize()
immune = input("Is your immune system too weak?: ").capitalize()

if age == "Yes" or chronic == "Yes" or immune == "Yes":
  print("You are in risky group")
else:
   print("You are not in risky group")