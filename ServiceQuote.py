from functools import total_ordering


class ServiceQuote:
    def __init__(self,pcharge,lcharge,tax,total):
        self.__pcharge = pcharge
        self.__lcharge = lcharge
        self.__sales_tax = tax
        self.__total_charges = total
        
    
    def set_parts_charges(self,pcharge):
        self.__pcharge = abs(pcharge)

    def set_labor_charges(self,lcharge):
        self.__lcharge = abs(lcharge)
        
    def set_sales_tax(self,rate):
        self.__sales_tax += rate
        
    def set_total_charges(self,pcharge,lcharge,rate):
        self.__total_charges = (pcharge + lcharge) + ((pcharge + lcharge) * rate)
        
    def get_parts_charges(self):
        return self.__pcharge

    def get_labor_charges(self):
        return self.__lcharge

    def get_sales_tax(self):
        return self.get_sales_tax

    def get_total_charges(self):
        return self.__total_charges

