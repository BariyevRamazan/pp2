string_of_war = str(input())
if( list(map(str.upper, string_of_war)) == list(map(str.upper, reversed( string_of_war)))):
    print(f"The string {string_of_war} is polindrome")
else :
    print(f"The string {string_of_war} is NOT polindrome")