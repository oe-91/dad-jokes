from src.functions import get_me_a_joke

print("\n-------------------------------------------")
print("-   Random joke from icanhazdadjoke.com   -")
print("-------------------------------------------\n")
answer = "y"
while answer == "y":
    print ("\t>>" , get_me_a_joke())
    answer = input("\nPrint another joke? (y/n)\n")