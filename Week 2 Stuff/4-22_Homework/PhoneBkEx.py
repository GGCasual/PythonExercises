print("Electronic Phone Book\n=====================")
print("1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit")

contacts = {
    'Ray': '716-343-6528',
    'Gwen': '343-787-1135',
    'Bob': '087-346-9975',
    'Jamie': '174-853-0663'
}

R = contacts.get('Ray')
G = contacts.get('Gwen')
B = contacts.get('Bob')
J = contacts.get('Jamie')

question = int(input("\nChoose a number: "))

# 1. Look up an entry 
if question == 1:
    name = input("What\'s the person\'s name? ")
    if name == 'Ray' or name == 'ray':
        print(f"Found entry for Ray: {R}")
    if name == 'Gwen' or name == 'gwen':
        print(f"Found entry for Gwen: {G}")
    if name == 'Bob' or name == 'bob':
        print(f"Found entry for Bob: {B}")
    if name == 'Jamie' or name == 'jamie':
        print(f"Found entry for Jamie: {J}")


# 2. Set an entry 
if question == 2:
    name = input("What\'s the person\'s name? ")
    num = input("What\'s the phone number? ")
    contacts[name] = num

print(contacts)


# 3. Delete an entry 
if question == 3:
    name = input("What\'s the person\'s name? ")
    if name == 'Ray' or name == 'ray':
        print(f"Deleted entry for {name}")
        del contacts['Ray']
    if name == 'Gwen' or name == 'gwen':
        print(f"Deleted entry for {name}")
        del contacts['Gwen']
    if name == 'Bob' or name == 'bob':
        print(f"Deleted entry for {name}")
        del contacts['Bob']
    if name == 'Jamie' or name == 'jamie':
        print(f"Deleted entry for {name}")
        del contacts['Jamie']

print(contacts)


# 4. List all entries 
if question == 4:
    for key, value in contacts.items():
        print(key)
        print(value + "\n")


# 5. Quit
if question == 5:
    exit()