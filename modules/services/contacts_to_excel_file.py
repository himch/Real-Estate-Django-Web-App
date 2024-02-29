from contacts.views import contacts_to_excel_view


def contacts_to_excel_file():
    response = contacts_to_excel_view(None)
    if response.headers.get('Content-Disposition'):
        print("Got file in response")
        print("Writing file to filename.bin")
        with open("excel.xlsx", 'wb') as f:
            f.write(response.content)
    print('Ready to save Contacts to excel file')
