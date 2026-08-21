#3-4. guest list
guests = ['Albert Einstein', 'Marie Curie', 'Isaac Newton']
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

#3-5. changing guest list
guests = ['Albert Einstein', 'Marie Curie', 'Isaac Newton']    
print(f"Unfortunately, {guests[1]} cannot make it to dinner.")
guests[1] = 'Nikola Tesla'
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

#3-6. more guests
print("We found a bigger dinner table!")

guests.insert(0, 'mike')
guests.insert(2, 'Charles')
guests.append('Elon Musk')

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

#3-7. shrinking guest list
print("Unfortunately, we can only invite two people for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, we can't invite you to dinner.")

for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

    del guests[0]  
    del guests[0]  

print(guests)