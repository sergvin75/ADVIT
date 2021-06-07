

def create_record(name, telephone, address):
    """Create Record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record

user1 = create_record("Vasya", "+978967958359087", "Tinusiya")
user2 = create_record("Petya", "+976196234976666", "Mulisya")

print(user1)
print(user2)

def give_award(medal, *persons):
    """Give Medals to persons"""
    for person in persons:
        print("Tovarisch " + person.title() + " nagrazhdaetsya medalyu " + medal)

give_award("Za Berlin", "vasya", "petya")
give_award("Za London", "vetya", "alexander", "valentin")
