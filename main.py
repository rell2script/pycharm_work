name,major,hometown,age,gpa="   Jarell noble".title().lstrip(),"Cybersecurity".title(),"Brockton".title(),18,2.9
fall_credits,spring_credits=9,12
total_credits=fall_credits+spring_credits
TUITION_PER_CREDIT=10_000.
SCHOLARSHIP=25_723.0
DREAM_TUITON=40_000.0
fall_cost=fall_credits*TUITION_PER_CREDIT
fall_final=fall_cost-SCHOLARSHIP
remaining_dream=fall_final-DREAM_TUITON
college_name="College:Harvard".removeprefix("College:")

print("my dream college profile".upper())
print(f"name:{name} \n major:{major} \n hometown:{hometown} \n age:{age} \n gpa:{gpa}".title().lstrip())
print(f"total credits:{total_credits}".title())
print(f"dream college:{college_name}".title())
print(f"dream tuiton:${DREAM_TUITON}".title())
print(f"cost:${fall_cost}".title())
print(f"scholarship:${SCHOLARSHIP}".title())
print(f"final cost:${fall_final}".title())
print(f"remaining dream:${remaining_dream}".title())
concatenated=str(college_name) + " is my dream college "
print(concatenated)