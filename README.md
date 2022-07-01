This has been designed to go through Invoicely invoices and extract the total from each invoice, save them in a text file in the directory and then provides a sum total of all invoices.

This can be called in terminal with command line arguments. just calling tax.py will default to looping through current directory. Alternatively it will take command line arguments for another folder. It will auto extract your home dir and add it to arguments so just put in as seperate texts the route in order seperaetd by spaces eg tax.py Documents Inovices
will send the program to loop through each of the pdf files in the invoices folder. NB these need exact speling and are case sensitive.

After running check the save.txt in specified folder.
