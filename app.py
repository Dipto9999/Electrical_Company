import database 

database.create_table()

database.add_record(
    ['Muntakim', 'Mahir Tanzil', 'Merina', 'Tunzilur'],
    ['Rahman','Rahman','Sultana', 'Rahman'],
    ['muntakim.rahman@gmail.com', 'mahir199.tanzil@gmail.com', 'merina_70@yahoo.com', 'tunzilur@gmail.com'])

database.show_records_all()