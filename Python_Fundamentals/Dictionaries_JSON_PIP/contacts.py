contacts = {
    "number": 4,
    "students": [
        {
            "first_name": "Sarah Holderness",
            "email": "sarah@example.com",
        },
        {
            "first_name": "Harry Potter",
            "email": "harry@example.com",
        },
        {
            "first_name": "Hermonie Granger",
            "email": "hermione@example.com",
        },
        {
            "first_name": "Ron Weasley",
            "email": "ron@example.com",
        },
    ],
}

print("Students emails:")
for student in contacts["students"]:
    print(f"{student['email']}")