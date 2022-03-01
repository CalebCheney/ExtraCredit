import CustomerClass as cc
import CarClass as ca
import ServiceQuote as sq

def main():

    TAX = .0625
    pcharge = float(input('What was the parts cost? '))
    lcharge = float(input('What was the labor cost? '))
    total = (pcharge + lcharge) + ((pcharge + lcharge) * TAX)

    cust = cc.Customer('Caleb','1001 Speight Ave','713-499-9094')
    rx7 = ca.Car('Mazda','RX-7',1999)
    quote = sq.ServiceQuote(pcharge,lcharge,TAX,total)


    print('\n\t-Customer-\n',
    'Name: ', cust.get_name(), '\n',
    'Address: ', cust.get_address(), '\n',
    'Phone: ', cust.get_phone(), '\n\n',
    '\t-Car-\n', 
    'Make: ', rx7.get_make(), '\n',
    'Model: ', rx7.get_model(), '\n',
    'Year: ', rx7.get_year(), '\n\n',
    '\t-Service Quote-\n',
    'Parts: $', format(quote.get_parts_charges(), ',.2f'), '\n',
    'Labor: $', format(quote.get_labor_charges(), ',.2f'), '\n', sep = '')
    print('Total: $', format(quote.get_total_charges(), ',.2f'), sep = '')

    


main()